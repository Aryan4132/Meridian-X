import os
import time
import threading
from typing import List, Dict, Optional
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from src.tools.communication import send_notification
from database import add_to_task_log

class LogFileHandler(FileSystemEventHandler):
    def __init__(self, file_path: str, patterns: List[str], on_match_goal: str):
        super().__init__()
        self.file_path = os.path.abspath(file_path)
        self.patterns = [p.lower() for p in patterns]
        self.on_match_goal = on_match_goal
        self.last_position = os.path.getsize(self.file_path) if os.path.exists(self.file_path) else 0

    def on_modified(self, event):
        if os.path.abspath(event.src_path) == self.file_path:
            self.process_new_lines()

    def process_new_lines(self):
        if not os.path.exists(self.file_path):
            return
            
        try:
            current_size = os.path.getsize(self.file_path)
            if current_size < self.last_position:
                # File was truncated/cleared, reset position
                self.last_position = 0
                
            with open(self.file_path, "r", encoding="utf-8", errors="ignore") as f:
                f.seek(self.last_position)
                lines = f.readlines()
                self.last_position = f.tell()
                
            for line in lines:
                line_lower = line.lower()
                matched = any(p in line_lower for p in self.patterns)
                if matched:
                    self.trigger_match_alarm(line.strip())
        except Exception as e:
            print("[Log Watcher] Error reading logs:", e)

    def trigger_match_alarm(self, matched_line: str):
        print(f"[Log Watcher] Trigger! Matched line: '{matched_line}'")
        send_notification(
            title="🚨 System Log Monitor Spike",
            message=f"Detected error pattern. Diagnosing: {matched_line[:60]}..."
        )
        add_to_task_log("watch_log", 1, "triggered", f"Pattern matched on line: {matched_line}")
        
        # Trigger background analysis thread to avoid blocking filesystem watcher
        threading.Thread(target=self.run_self_healing_diagnosis, args=(matched_line,), daemon=True).start()

    def run_self_healing_diagnosis(self, matched_line: str):
        try:
            from database import get_ollama_client
            
            client = get_ollama_client()
            prompt = (
                f"You are Meridian's log analyzer. A log watcher triggered on this error line:\n"
                f"'{matched_line}'\n\n"
                f"Provide a brief, 1-sentence diagnosis of the root cause and a 1-sentence suggestion to fix it."
            )
            model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
            res = client.generate(model=model, prompt=prompt)
            # GenerateResponse is an object, not a dict
            diagnosis = (res.response if hasattr(res, "response") else res.get("response", "Unknown error condition.")).strip() or "Unknown error condition."

            
            print(f"[Log Watcher Healing Diagnosis]: {diagnosis}")
            send_notification(
                title="🔍 Auto-Healing Diagnosis",
                message=diagnosis[:120]
            )
        except Exception as e:
            print("[Log Watcher Diagnosis] LLM call failed:", e)

# Observers manager
_log_observers: Dict[str, Observer] = {}

def start_watching_log(file_path: str, patterns: List[str], on_match_goal: str) -> str:
    abs_path = os.path.abspath(file_path)
    if abs_path in _log_observers:
        return f"Already watching log file: {abs_path}"
        
    if not os.path.exists(abs_path):
        # Create empty file if not exists to watch it
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write("")
            
    handler = LogFileHandler(abs_path, patterns, on_match_goal)
    observer = Observer()
    observer.schedule(handler, path=os.path.dirname(abs_path), recursive=False)
    observer.start()
    
    _log_observers[abs_path] = observer
    return f"Started real-time log monitoring on: {abs_path}"

def stop_watching_log(file_path: str) -> str:
    abs_path = os.path.abspath(file_path)
    if abs_path in _log_observers:
        observer = _log_observers[abs_path]
        observer.stop()
        observer.join(timeout=2.0)
        del _log_observers[abs_path]
        return f"Stopped watching log: {abs_path}"
    return f"Log file is not currently monitored: {abs_path}"

def list_log_watchers() -> List[str]:
    return list(_log_observers.keys())

# ----------------- FOLDER WATCHER IMPLEMENTATION -----------------

class FolderEventHandler(FileSystemEventHandler):
    def __init__(self, folder_path: str, on_create_goal: Optional[str], on_modify_goal: Optional[str]):
        super().__init__()
        self.folder_path = os.path.abspath(folder_path)
        self.on_create_goal = on_create_goal
        self.on_modify_goal = on_modify_goal

    def on_created(self, event):
        if event.is_directory:
            return
        if self.on_create_goal:
            # Replace placeholder with file path
            goal = self.on_create_goal.replace("{{file_path}}", event.src_path)
            print(f"[Folder Watcher] File created: {event.src_path}. Executing: '{goal}'")
            from src.core.scheduler import execute_scheduled_goal
            threading.Thread(target=execute_scheduled_goal, args=(goal,), daemon=True).start()

    def on_modified(self, event):
        if event.is_directory:
            return
        if self.on_modify_goal:
            # Replace placeholder with file path
            goal = self.on_modify_goal.replace("{{file_path}}", event.src_path)
            print(f"[Folder Watcher] File modified: {event.src_path}. Executing: '{goal}'")
            from src.core.scheduler import execute_scheduled_goal
            threading.Thread(target=execute_scheduled_goal, args=(goal,), daemon=True).start()

_folder_observers: Dict[str, Observer] = {}

def start_watching_folder(folder_path: str, on_create_goal: Optional[str] = None, on_modify_goal: Optional[str] = None) -> str:
    abs_path = os.path.abspath(folder_path)
    if abs_path in _folder_observers:
        return f"Already watching directory: {abs_path}"
        
    if not os.path.exists(abs_path):
        os.makedirs(abs_path, exist_ok=True)
        
    handler = FolderEventHandler(abs_path, on_create_goal, on_modify_goal)
    observer = Observer()
    observer.schedule(handler, path=abs_path, recursive=False)
    observer.start()
    
    _folder_observers[abs_path] = observer
    return f"Started folder monitoring on: {abs_path}"

def stop_watching_folder(folder_path: str) -> str:
    abs_path = os.path.abspath(folder_path)
    if abs_path in _folder_observers:
        observer = _folder_observers[abs_path]
        observer.stop()
        observer.join(timeout=2.0)
        del _folder_observers[abs_path]
        return f"Stopped folder watcher on: {abs_path}"
    return f"Directory is not currently monitored: {abs_path}"

def list_folder_watchers() -> List[str]:
    return list(_folder_observers.keys())

# ----------------- WORKSPACE SECURITY & LINT WATCHER -----------------

import ast
import re

# Regex for common raw secrets (API keys, connection strings, private keys)
SECRET_REGEX = re.compile(
    r'(?i)\b(api_key|client_secret|db_password|aws_secret|token|private_key)\b\s*=\s*[\'"]([a-zA-Z0-9_\-\.\:\/+=]{12,})[\'"]',
    re.IGNORECASE
)

class WorkspaceWatcher(FileSystemEventHandler):
    def __init__(self, workspace_path: str):
        super().__init__()
        self.workspace_path = os.path.abspath(workspace_path)
        self._last_trigger: Dict[str, float] = {}

    def on_modified(self, event):
        if event.is_directory:
            return
            
        file_path = os.path.abspath(event.src_path)
        # Avoid recursive watch on logs, venv, git, node_modules, temp files
        ignore_dirs = [".git", "node_modules", "venv", "__pycache__", ".tauri", "dist", "meridian_memory"]
        if any(d in file_path for d in ignore_dirs):
            return
            
        # Cooldown: 2 seconds per file to avoid multiple events on single save
        now = time.time()
        if file_path in self._last_trigger and (now - self._last_trigger[file_path]) < 2.0:
            return
        self._last_trigger[file_path] = now

        # Run checks in a background thread to prevent blocking file operations
        threading.Thread(target=self.run_checks, args=(file_path,), daemon=True).start()

    def run_checks(self, file_path: str):
        file_name = os.path.basename(file_path)
        ext = os.path.splitext(file_name)[1].lower()
        
        # Only check text files
        if ext not in [".py", ".ts", ".tsx", ".js", ".jsx", ".json", ".env", ".html", ".css"]:
            return
            
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception:
            return
            
        # 1. Secret Leak Shield
        matches = SECRET_REGEX.findall(content)
        if matches:
            # Avoid matching .env files themselves or placeholder values
            is_env_file = file_name.startswith(".env")
            has_placeholder = any("your_" in val or "placeholder" in val or "test_key" in val for key, val in matches)
            if not is_env_file and not has_placeholder:
                from src.core.proactive import publish_nudge_sync
                publish_nudge_sync(
                    nudge_type="secret_leak",
                    title="⚠️ Security Alert: Secret Detected",
                    message=f"I detected a raw credential/key inside '{file_name}'. Let's move it to a safe .env configuration.",
                    action_hint=f"Secure key in .env: {file_path}",
                    icon="🔒",
                    mascot_state="disapproving"
                )
                return

        # 2. Save-to-Heal Linter check (Python only)
        if ext == ".py":
            try:
                # Validate syntax locally using AST compilation
                compile(content, file_path, "exec")
            except SyntaxError as se:
                error_msg = f"Line {se.lineno}: {se.msg}"
                from src.core.proactive import publish_nudge_sync
                publish_nudge_sync(
                    nudge_type="save_to_heal",
                    title="🧹 Syntax Error on Save",
                    message=f"Syntax issue in '{file_name}': {error_msg}. Want me to fix it?",
                    action_hint=f"Fix syntax: {file_path}:{se.lineno}",
                    icon="🧹",
                    mascot_state="diagnostic"
                )
                return

            # 3. Broken Import / Call-Site Audit (Lightweight AST Check)
            try:
                ast.parse(content)
                # CodeGraph can query this, or LSP diagnostics can report it in the background
            except Exception:
                pass

_workspace_observer: Optional[Observer] = None

def start_workspace_watcher(path: str):
    global _workspace_observer
    if _workspace_observer is None:
        abs_path = os.path.abspath(path)
        handler = WorkspaceWatcher(abs_path)
        _workspace_observer = Observer()
        _workspace_observer.schedule(handler, path=abs_path, recursive=True)
        _workspace_observer.start()
        print(f"[Workspace Guard] Listening for file modifications in: {abs_path}")

def stop_workspace_watcher():
    global _workspace_observer
    if _workspace_observer is not None:
        _workspace_observer.stop()
        _workspace_observer.join(timeout=2.0)
        _workspace_observer = None
        print("[Workspace Guard] Watcher stopped.")

def stop_all_watchers():
    """Stops all running folder and log file observers on application shutdown."""
    stop_workspace_watcher()
    for abs_path in list(_log_observers.keys()):
        try:
            stop_watching_log(abs_path)
        except Exception:
            pass
    for abs_path in list(_folder_observers.keys()):
        try:
            stop_watching_folder(abs_path)
        except Exception:
            pass

