"""
commits.py — Git commit whisperer, workspace change tracker, presence arrival, clipboard intelligence, and follow-ups.
"""

import os
import re
import time
import threading
import subprocess
from datetime import datetime
from typing import Optional, List, Dict, Any

_last_activity_time: float = time.time()
_last_idle_nudge: float = 0.0
_last_memory_consolidation: float = 0.0
MEMORY_CONSOLIDATION_COOLDOWN: float = 12 * 60 * 60
IDLE_THRESHOLD_MINUTES: int = 20
IDLE_NUDGE_COOLDOWN: int = 25 * 60

IDLE_SUGGESTIONS = [
    ("🧹 Clean up old logs?", "I noticed you haven't typed in a while. Want me to scan and summarize workspace activity?"),
    ("🔍 Knowledge Graph Update", "Been quiet for a bit! I can refresh the project knowledge graph if you'd like."),
    ("📊 System health report", "Your system has been running for a while. Want a quick health summary?"),
    ("💡 Anything on your mind?", "I'm standing by — feel free to ask me anything or delegate a task."),
    ("🗂️ Session summary", "Want me to summarize what we've accomplished in this session so far?"),
]

_last_arrival_briefing: float = 0.0
ARRIVAL_BRIEFING_COOLDOWN: float = 300.0

_last_commit_whisper_time: float = 0.0
COMMIT_WHISPER_COOLDOWN: float = 300.0

_last_clipboard_nudge: float = 0.0
CLIPBOARD_COOLDOWN: int = 15

_URL_RE = re.compile(
    r'https?://[^\s/$.?#].[^\s]*',
    re.IGNORECASE
)

_TRACEBACK_RE = re.compile(
    r'Traceback \(most recent call last\)|'
    r'thread \'.*\' panicked at|'
    r'Error:|'
    r'Exception:|'
    r'at\s+.*:\d+:\d+',
    re.IGNORECASE
)

_clipboard_history_buffer: List[Dict[str, Any]] = []

_pending_followups: list = []
_followup_lock = threading.Lock()
ENGINEER_FOLLOWUP_DELAY: int = 30 * 60

FOLLOWUP_TEMPLATES = {
    "ENGINEER": [
        "Earlier you worked on some code. Want me to write unit tests for it?",
        "Did your last code change work as expected? I can run a review.",
        "Want me to commit and document what we built earlier?",
    ],
    "ANALYST": [
        "The system metrics looked interesting earlier. Want a recurring health digest?",
        "Want me to graph the CPU/RAM trends from this session?",
    ],
    "RESEARCHER": [
        "Did you find what you were researching? I can save a summary to the knowledge base.",
        "Want me to compile that research into a report?",
    ],
}

_last_git_check: float = 0.0


def check_presence_arrival(user_name: Optional[str] = "User") -> bool:
    """Checks if user has returned after being away (>= 300s) and triggers executive briefing."""
    import src.core.proactive as proactive
    now = time.time()
    last_act = getattr(proactive, "_last_activity_time", _last_activity_time)
    last_arr = getattr(proactive, "_last_arrival_briefing", _last_arrival_briefing)
    idle_seconds = now - last_act
    if idle_seconds >= 300.0 and (now - last_arr) >= ARRIVAL_BRIEFING_COOLDOWN:
        proactive._last_arrival_briefing = now
        proactive._last_activity_time = now
        try:
            from src.core.presence_briefing import PresenceBriefingEngine
            engine = PresenceBriefingEngine()
            briefing = engine.generate_presence_briefing(user_name=user_name)
            proactive.publish_nudge_sync(
                nudge_type="room_arrival_briefing",
                title="👋 Executive Room Arrival",
                message=briefing.get("text", briefing.get("briefing", "")),
                icon="🎙️",
                action="play_voice_briefing"
            )
            return True
        except Exception as e:
            print(f"[Proactive] Room arrival briefing error: {e}")
    return False


def check_proactive_commits(workspace_root: Optional[str] = None) -> bool:
    """Proactively inspects staged changes and suggests semantic commit messages."""
    import src.core.proactive as proactive
    now = time.time()
    last_commit_time = getattr(proactive, "_last_commit_whisper_time", _last_commit_whisper_time)
    if (now - last_commit_time) < COMMIT_WHISPER_COOLDOWN:
        return False

    try:
        from src.core.commit_whisperer import CommitWhisperer
        ws = workspace_root or os.getcwd()
        whisperer = CommitWhisperer(ws)
        res = whisperer.inspect_staged_commit()
        if res.get("has_staged"):
            proactive._last_commit_whisper_time = now
            msg = res.get("suggested_message", "commit staged changes")
            proactive.publish_nudge_sync(
                nudge_type="commit_suggestion",
                title="📜 Proactive Git Commit",
                message=f"Changes ready to commit: '{msg}'",
                action_hint=f"git commit -m \"{msg}\"",
                icon="🌿",
                action="git_commit"
            )
            return True
    except Exception as e:
        print(f"[Proactive] Commit whisper check error: {e}")
    return False


def trigger_what_broke_auto_fix(error_text: str = "", workspace_root: Optional[str] = None) -> bool:
    """Proactively analyzes recent breakage/error and dispatches actionable patch suggestions."""
    import src.core.proactive as proactive
    try:
        from src.core.what_broke_detective import WhatBrokeDetective
        ws = workspace_root or os.getcwd()
        detective = WhatBrokeDetective(ws)
        diag = detective.diagnose_failures(error_text=error_text)
        if diag.get("breakage_detected"):
            patch_data = diag.get("recommended_patch")
            proactive.publish_nudge_sync(
                nudge_type="what_broke_patch",
                title="🕵️‍♂️ Breakage Auto-Fix Suggestion",
                message=diag.get("error_summary", "Detected code issue"),
                action_hint="Apply Fix Patch",
                icon="🔧",
                patch=patch_data,
                action="apply_auto_fix_patch"
            )
            return True
    except Exception as e:
        print(f"[Proactive] What broke auto-fix error: {e}")
    return False


def record_user_activity():
    """Call this every time the user sends a message or returns."""
    import src.core.proactive as proactive
    proactive.check_presence_arrival()
    proactive._last_activity_time = time.time()


def check_idle_time():
    """Called every ~5 minutes by the scheduler."""
    import src.core.proactive as proactive
    now = time.time()
    last_act = getattr(proactive, "_last_activity_time", _last_activity_time)
    last_idle = getattr(proactive, "_last_idle_nudge", _last_idle_nudge)
    last_mem = getattr(proactive, "_last_memory_consolidation", _last_memory_consolidation)

    idle_seconds = now - last_act
    idle_minutes = idle_seconds / 60.0

    proactive.check_continuous_work_ergonomics()

    if idle_minutes >= 30.0 and (now - last_mem) > MEMORY_CONSOLIDATION_COOLDOWN:
        proactive._last_memory_consolidation = now
        try:
            from database import consolidate_memory_sleep_cycle
            from src.core.doc_generator import generate_mermaid_docs
            
            def run_sleep_cycle_tasks():
                consolidate_memory_sleep_cycle()
                try:
                    generate_mermaid_docs()
                except Exception as de:
                    print("[Scheduler] Failed to generate background Mermaid docs:", de)
                    
            threading.Thread(target=run_sleep_cycle_tasks, daemon=True).start()
        except ImportError as ie:
            print("[Scheduler] ImportError in sleep cycle tasks — consolidate_memory_sleep_cycle not available:", ie)
        except Exception as ce:
            print("[Scheduler] Failed to trigger background sleep cycle tasks:", ce)

    if idle_minutes >= IDLE_THRESHOLD_MINUTES and (now - last_idle) > IDLE_NUDGE_COOLDOWN:
        proactive._last_idle_nudge = now
        idx = datetime.now().hour % len(IDLE_SUGGESTIONS)
        title, message = IDLE_SUGGESTIONS[idx]
        proactive.publish_nudge_sync(
            nudge_type="idle_nudge",
            title=title,
            message=message,
            action_hint="Click to dismiss or reply",
            icon="💤"
        )


def _looks_like_code(text: str) -> bool:
    lines = text.strip().splitlines()
    if len(lines) < 3:
        return False
    indented = sum(1 for l in lines if l.startswith(("    ", "\t")))
    code_tokens = sum(1 for l in lines if any(
        tok in l for tok in ["def ", "class ", "import ", "return ", "=>", "function", "const ", "let "]
    ))
    return indented >= 2 or code_tokens >= 2


def on_clipboard_proactive(text: str):
    """Called by ClipboardWatcher whenever clipboard content changes."""
    global _last_clipboard_nudge, _clipboard_history_buffer
    import src.core.proactive as proactive
    now = time.time()

    if not text or len(text.strip()) < 8:
        return

    if not _clipboard_history_buffer or _clipboard_history_buffer[-1]["text"] != text:
        _clipboard_history_buffer.append({"text": text, "timestamp": now})
    _clipboard_history_buffer = [item for item in _clipboard_history_buffer if now - item["timestamp"] <= 300][-5:]

    errors_copied = [item["text"] for item in _clipboard_history_buffer if _TRACEBACK_RE.search(item["text"])]
    code_copied = [item["text"] for item in _clipboard_history_buffer if _looks_like_code(item["text"])]

    if len(errors_copied) >= 2 and (now - _last_clipboard_nudge) > CLIPBOARD_COOLDOWN:
        _last_clipboard_nudge = now
        proactive.publish_nudge_sync(
            nudge_type="clipboard_fusion_error",
            title="📋 Fused Clipboard Errors",
            message=f"I noticed you copied {len(errors_copied)} tracebacks recently. Want me to compile them into a unified diagnostic plan?",
            action_hint="Diagnose compiled errors",
            icon="🔴",
            mascot_state="diagnostic"
        )
        return
    elif len(code_copied) >= 2 and (now - _last_clipboard_nudge) > CLIPBOARD_COOLDOWN:
        _last_clipboard_nudge = now
        proactive.publish_nudge_sync(
            nudge_type="clipboard_fusion_code",
            title="📋 Fused Clipboard Snippets",
            message=f"I noticed you copied {len(code_copied)} separate code snippets. Want me to draft a helper module to integrate them?",
            action_hint="Combine copied code",
            icon="💻",
            mascot_state="diagnostic"
        )
        return

    if (now - _last_clipboard_nudge) < CLIPBOARD_COOLDOWN:
        return

    _last_clipboard_nudge = now

    url_match = _URL_RE.search(text)
    if url_match:
        url = url_match.group(0)[:60]
        proactive.publish_nudge_sync(
            nudge_type="clipboard_url",
            title="🔗 URL Copied",
            message="Detected a URL. Want me to summarize or open it?",
            action_hint=f"Summarize: {url}",
            icon="🌐",
            mascot_state="diagnostic"
        )
        return

    if _TRACEBACK_RE.search(text):
        first_line = text.strip().splitlines()[0][:80]
        
        def run_patch_gen():
            patch = None
            try:
                match = re.search(r'File "([^"]+)", line (\d+)', text)
                if not match:
                    match = re.search(r'File \'([^\']+)\', line (\d+)', text)
                if match:
                    file_path = match.group(1)
                    line_num = int(match.group(2))
                    if os.path.exists(file_path):
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                            original_code = f.read()
                        
                        import ollama
                        try:
                            from api import get_ollama_client_host
                            ollama_host = get_ollama_client_host()
                        except Exception:
                            ollama_host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
                            
                        client = ollama.Client(host=ollama_host)
                        from database import get_brain_model
                        model = get_brain_model()
                        
                        prompt = (
                            f"You are a self-healing compiler assistant. The user copied a traceback highlighting an error in this file:\n"
                            f"File: {file_path}\n"
                            f"Line with error: {line_num}\n"
                            f"Traceback/Error message:\n{text}\n\n"
                            f"Original Code:\n"
                            f"```\n{original_code}\n```\n\n"
                            f"Rewrite this file to fix the issue highlighted by the traceback/error. Output ONLY the raw corrected file contents. Do NOT include markdown code blocks, explanation, or notes. Just the raw, compile-ready code."
                        )
                        
                        res = client.generate(model=model, prompt=prompt)
                        proposed = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
                        
                        if proposed.startswith("```"):
                            lines = proposed.splitlines()
                            if lines[0].startswith("```"):
                                lines = lines[1:]
                            if lines and lines[-1].startswith("```"):
                                lines = lines[:-1]
                            proposed = "\n".join(lines).strip()
                        
                        patch = {
                            "file_path": file_path,
                            "original": original_code,
                            "proposed": proposed,
                            "error_message": text
                        }
            except Exception as e:
                print(f"[Proactive Patch Generator] Failed to auto-generate fix: {e}")
            
            if patch:
                proactive.publish_nudge_sync(
                    nudge_type="clipboard_error",
                    title="🐛 Error Detected & Analyzed",
                    message=f"I detected a traceback and auto-generated a fix for {os.path.basename(patch['file_path'])}.",
                    action_hint="Review & Apply Fix",
                    icon="🔴",
                    mascot_state="diagnostic",
                    action="show_diff",
                    patch=patch
                )
            else:
                proactive.publish_nudge_sync(
                    nudge_type="clipboard_error",
                    title="🐛 Error Detected in Clipboard",
                    message="Looks like you copied an error or traceback. Want me to diagnose it?",
                    action_hint=f"Diagnose: {first_line}",
                    icon="🔴",
                    mascot_state="diagnostic"
                )
                
        threading.Thread(target=run_patch_gen, daemon=True).start()
        return

    if _looks_like_code(text):
        proactive.publish_nudge_sync(
            nudge_type="clipboard_code",
            title="📋 Code Snippet Copied",
            message="I see you copied a code snippet. Want me to review, explain, or refactor it?",
            action_hint="Review copied code",
            icon="💻",
            mascot_state="diagnostic"
        )
        return


def schedule_followup(mode: str):
    """Called at the end of a significant agent loop to queue a follow-up nudge."""
    if mode not in FOLLOWUP_TEMPLATES:
        return
    import random
    message = random.choice(FOLLOWUP_TEMPLATES[mode])
    fire_at = time.time() + ENGINEER_FOLLOWUP_DELAY
    with _followup_lock:
        _pending_followups.append((fire_at, mode, message))
    print(f"[Proactive] Scheduled {mode} follow-up for {ENGINEER_FOLLOWUP_DELAY/60:.0f} min from now.")


def check_followups():
    """Called every ~5 minutes by the scheduler. Fires any due follow-ups."""
    import src.core.proactive as proactive
    now = time.time()
    with _followup_lock:
        due = [(ft, m, msg) for ft, m, msg in _pending_followups if now >= ft]
        for item in due:
            _pending_followups.remove(item)

    for fire_at, mode, message in due:
        proactive.publish_nudge_sync(
            nudge_type="followup",
            title="🔁 Follow-up Suggestion",
            message=message,
            action_hint="Click to pick up where we left off",
            icon="🔁",
            mascot_state="happy"
        )


def check_git_status():
    global _last_git_check
    import src.core.proactive as proactive
    now = time.time()
    
    if (now - _last_git_check) < 600:
        return
    _last_git_check = now
    
    try:
        repo_path = os.environ.get(
            "MERIDIAN_REPO_PATH",
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        )
        if not os.path.exists(os.path.join(repo_path, ".git")):
            return
            
        status = subprocess.check_output(
            ["git", "status", "--porcelain"],
            cwd=repo_path
        ).decode("utf-8", errors="ignore").strip()
        if not status:
            return
            
        lines = status.split("\n")
        modified = sum(1 for l in lines if l.startswith((" M", "M ", "MM")))
        untracked = sum(1 for l in lines if l.startswith("??"))
        
        if modified > 0 or untracked > 0:
            proactive.publish_nudge_sync(
                nudge_type="git_copilot",
                title="🐙 Git Changes Detected",
                message=f"You have {modified} modified and {untracked} untracked files in the workspace. Want me to draft structured commit messages?",
                action_hint="Draft Git Commit Message",
                icon="🐙",
                mascot_state="diagnostic"
            )
    except Exception:
        pass
