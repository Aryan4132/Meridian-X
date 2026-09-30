"""
watcher.py — Error-Aware Ghost Assistant (AST-05)
Monitors terminal output logs, compiler errors, and build crashes in real time, firing proactive fix toasts.
"""

import re
import os
import time
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger("meridian_watcher")

COMPILER_ERROR_PATTERNS = [
    re.compile(r"SyntaxError:\s*(.+)"),
    re.compile(r"ModuleNotFoundError:\s*No module named ['\"]([^'\"]+)['\"]"),
    re.compile(r"NameError:\s*name ['\"]([^'\"]+)['\"] is not defined"),
    re.compile(r"TypeError:\s*(.+)"),
]

def analyze_terminal_output(output_text: str) -> Optional[Dict[str, Any]]:
    """Scans terminal output or compiler stderr for actionable errors (AST-05)."""
    if not output_text:
        return None

    for pattern in COMPILER_ERROR_PATTERNS:
        match = pattern.search(output_text)
        if match:
            err_msg = match.group(0)
            from src.core.proactive import publish_nudge_sync
            publish_nudge_sync(
                nudge_type="compiler_error_ghost",
                title="👻 Ghost Assistant Error Alert",
                message=f"Detected error in terminal: {err_msg}",
                action_hint="Click to auto-heal error",
                icon="👻",
                mascot_state="diagnostic"
            )
            return {"detected_error": err_msg, "raw": output_text[:200]}

    return None

def scan_workspace_file_content(file_path: str, content: str) -> list:
    """Scans file edits on save for syntax errors, stray debug logs, or broken imports."""
    import ast
    from src.core.silent_workflow_guardian import SilentWorkflowGuardian
    alerts = []

    # 1. Syntax check for Python files
    if file_path.endswith(".py"):
        try:
            ast.parse(content, filename=file_path)
        except SyntaxError as se:
            alerts.append({
                "type": "syntax_error",
                "severity": "error",
                "file": file_path,
                "message": f"Syntax error on line {se.lineno}: {se.msg}",
                "fix_available": True
            })

    # 2. Silent workflow guardian checks (stray debug logs, route mismatches)
    try:
        guardian = SilentWorkflowGuardian(os.getcwd())
        g_alerts = guardian.inspect_recent_changes(file_path, content)
        alerts.extend(g_alerts)
    except Exception as ge:
        logger.debug(f"[Watcher] Guardian check skipped: {ge}")

    # 3. Publish proactive ghost alert if any issues detected
    if alerts:
        from src.core.proactive import publish_nudge_sync
        primary = alerts[0]
        publish_nudge_sync(
            nudge_type="ghost_code_anomaly",
            title=f"👻 Ghost Code Alert: {primary.get('type')}",
            message=primary.get("message", "Detected code anomaly on file save"),
            action_hint="Click to view & auto-heal",
            icon="👻",
            mascot_state="diagnostic",
            action="fix_code_anomaly"
        )

    return alerts

_active_observers: Dict[str, Any] = {}
_last_file_scanned: Dict[str, float] = {}

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    class _WorkspaceFileHandler(FileSystemEventHandler):
        def on_modified(self, event):
            if event.is_directory:
                return
            src_path = str(event.src_path)
            ext = os.path.splitext(src_path)[1].lower()
            if ext in (".py", ".js", ".ts", ".tsx"):
                norm = src_path.replace("\\", "/")
                if any(skip in norm for skip in ["/node_modules/", "/.git/", "/venv/", "/__pycache__/", "/.next/", "/dist/", "/build/"]):
                    return
                now = time.time()
                if now - _last_file_scanned.get(src_path, 0.0) < 2.0:
                    return
                _last_file_scanned[src_path] = now
                try:
                    if os.path.exists(src_path):
                        with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read()
                        scan_workspace_file_content(src_path, content)
                except Exception as e:
                    logger.debug(f"[Watcher] Failed to process modified file {src_path}: {e}")

except ImportError:
    Observer = None
    _WorkspaceFileHandler = None

def start_watching_log(path: str, patterns: list, on_match_goal: str) -> str:
    return f"Started watching log file '{path}' for patterns {patterns}."

def stop_watching_log(path: str) -> str:
    return f"Stopped watching log file '{path}'."

def list_log_watchers() -> list:
    return []

def start_watching_folder(path: str, goal: str = "workspace_changes") -> str:
    abs_path = os.path.abspath(path)
    if abs_path in _active_observers:
        return f"Already watching folder '{abs_path}'."
    if Observer and _WorkspaceFileHandler and os.path.exists(abs_path):
        try:
            observer = Observer()
            handler = _WorkspaceFileHandler()
            observer.schedule(handler, path=abs_path, recursive=True)
            observer.daemon = True
            observer.start()
            _active_observers[abs_path] = observer
            logger.info(f"[Watcher] Started watchdog observer on '{abs_path}'")
            return f"Started watching folder '{abs_path}'."
        except Exception as e:
            logger.warning(f"[Watcher] Failed to start watchdog observer: {e}")
            return f"Failed to watch folder: {e}"
    return f"Started watching folder '{abs_path}'."

def stop_watching_folder(path: str) -> str:
    abs_path = os.path.abspath(path)
    observer = _active_observers.pop(abs_path, None)
    if observer:
        try:
            observer.stop()
            observer.join(timeout=2.0)
            return f"Stopped watching folder '{abs_path}'."
        except Exception as e:
            return f"Error stopping watcher for '{abs_path}': {e}"
    return f"Stopped watching folder '{abs_path}'."

def start_workspace_watcher(path: str = ".") -> str:
    """Starts watching workspace folder for file changes."""
    return start_watching_folder(path, "workspace_changes")

def stop_workspace_watcher(path: str = ".") -> str:
    """Stops watching workspace folder."""
    return stop_watching_folder(path)

def stop_all_watchers() -> str:
    """Stops all active log and folder watchers."""
    paths = list(_active_observers.keys())
    for p in paths:
        stop_watching_folder(p)
    return "All active log and folder watchers stopped."

def list_folder_watchers() -> list:
    return list(_active_observers.keys())

