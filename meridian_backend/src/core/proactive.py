"""
proactive.py — Meridian-X Proactive Intelligence Engine

Pushes unsolicited nudges to the frontend via the event bus when:
  1. System health anomalies are detected (CPU / RAM / Disk)
  2. The user has been idle for too long
  3. The clipboard contains something interesting (URL, error, code)
  4. A previous conversation warrants a follow-up suggestion
"""

import os
import re
import time
import asyncio
import threading
import psutil
import platform
import subprocess
import socket
from datetime import datetime
from typing import Optional, List, Dict, Any

from src.core.bus import event_bus

# Game Mode settings
game_mode_active = False
auto_game_mode_active = False

# ──────────────────────────────────────────────
# Shared nudge publisher
# ──────────────────────────────────────────────

def _now_str() -> str:
    return datetime.now().strftime("%H:%M:%S")

def publish_nudge_sync(
    nudge_type: str,
    title: str,
    message: str,
    action_hint: Optional[str] = None,
    icon: str = "💡",
    mascot_state: str = "default",
    action: Optional[str] = None,
    patch: Optional[dict] = None
):
    """Thread-safe helper: schedule nudge publish onto the running event loop."""
    # Suppress notifications if Game Mode is active, unless it is a game mode state update
    if game_mode_active and nudge_type != "game_mode_changed":
        print(f"[Proactive] Suppressed nudge '{title}' due to active Game Mode.")
        return

    payload = {
        "type": nudge_type,
        "title": title,
        "message": message,
        "action_hint": action_hint,
        "icon": icon,
        "timestamp": _now_str(),
        "id": f"nudge-{nudge_type}-{int(time.time())}",
        "mascot_state": mascot_state,
        "action": action
    }
    if patch:
        payload["patch"] = patch
    try:
        # get_running_loop() is the correct API in Python 3.10+ (get_event_loop is deprecated)
        loop = asyncio.get_running_loop()
        # We're inside an async context — schedule coroutine thread-safely
        asyncio.run_coroutine_threadsafe(
            event_bus.publish("proactive_nudge", payload), loop
        )
    except RuntimeError:
        # No running loop in this thread (e.g., APScheduler background thread)
        # BUG-30 fix: use isolated new_loop without asyncio.set_event_loop()
        # (set_event_loop in a non-main thread is deprecated in Python 3.10+)
        new_loop = asyncio.new_event_loop()
        try:
            new_loop.run_until_complete(event_bus.publish("proactive_nudge", payload))
        finally:
            new_loop.close()



# ──────────────────────────────────────────────
# 1. SYSTEM HEALTH CHECK
# ──────────────────────────────────────────────

# Thresholds
CPU_WARN_THRESHOLD = 85.0      # %
RAM_WARN_THRESHOLD = 88.0      # %
DISK_WARN_THRESHOLD = 90.0     # % used
DISK_PATH = "C:\\"

# Cooldown: don't repeat the same alert within N seconds
_last_cpu_alert: float = 0.0
_last_ram_alert: float = 0.0
_last_disk_alert: float = 0.0
_health_cooldown = 300  # 5 minutes

def check_system_health():
    """Called every ~5 minutes by the scheduler. Fires nudge only when anomalous."""
    global _last_cpu_alert, _last_ram_alert, _last_disk_alert
    now = time.time()

    try:
        # CPU
        cpu = psutil.cpu_percent(interval=1.0)
        if cpu > CPU_WARN_THRESHOLD and (now - _last_cpu_alert) > _health_cooldown:
            _last_cpu_alert = now
            # Try to identify top CPU process
            top_proc = ""
            try:
                procs = sorted(psutil.process_iter(['name', 'cpu_percent']),
                               key=lambda p: p.info.get('cpu_percent', 0), reverse=True)
                if procs:
                    top_proc = f" — '{procs[0].info['name']}' is the top consumer."
            except Exception:
                pass
            publish_nudge_sync(
                nudge_type="system_health",
                title="⚠️ High CPU Usage",
                message=f"CPU is at {cpu:.0f}%.{top_proc}",
                action_hint="Investigate processes",
                icon="🔥"
            )

        # RAM
        ram = psutil.virtual_memory().percent
        if ram > RAM_WARN_THRESHOLD and (now - _last_ram_alert) > _health_cooldown:
            _last_ram_alert = now
            ram_avail_gb = psutil.virtual_memory().available / (1024 ** 3)
            publish_nudge_sync(
                nudge_type="system_health",
                title="⚠️ Low Memory",
                message=f"RAM usage is at {ram:.0f}% ({ram_avail_gb:.1f} GB free).",
                action_hint="Check running processes",
                icon="🧠"
            )

        # Disk
        try:
            disk = psutil.disk_usage(DISK_PATH)
            disk_pct = disk.percent
            if disk_pct > DISK_WARN_THRESHOLD and (now - _last_disk_alert) > _health_cooldown:
                _last_disk_alert = now
                free_gb = disk.free / (1024 ** 3)
                publish_nudge_sync(
                    nudge_type="system_health",
                    title="💾 Low Disk Space",
                    message=f"C: drive is {disk_pct:.0f}% full — only {free_gb:.1f} GB remaining.",
                    action_hint="Free up disk space",
                    icon="💾"
                )
        except Exception:
            pass

    except Exception as e:
        print(f"[Proactive] Health check error: {e}")


# ──────────────────────────────────────────────
# 2. IDLE TIME NUDGE
# ──────────────────────────────────────────────

# Track last user activity timestamp
_last_activity_time: float = time.time()
_last_idle_nudge: float = 0.0
_last_memory_consolidation: float = 0.0
MEMORY_CONSOLIDATION_COOLDOWN = 12 * 60 * 60  # Don't consolidate more than once per 12 hours of idle time
IDLE_THRESHOLD_MINUTES = 20        # Nudge after 20 min of no messages
IDLE_NUDGE_COOLDOWN = 25 * 60      # Don't re-nudge for 25 min

IDLE_SUGGESTIONS = [
    ("🧹 Clean up old logs?", "I noticed you haven't typed in a while. Want me to scan and summarize workspace activity?"),
    ("🔍 Knowledge Graph Update", "Been quiet for a bit! I can refresh the project knowledge graph if you'd like."),
    ("📊 System health report", "Your system has been running for a while. Want a quick health summary?"),
    ("💡 Anything on your mind?", "I'm standing by — feel free to ask me anything or delegate a task."),
    ("🗂️ Session summary", "Want me to summarize what we've accomplished in this session so far?"),
]

def record_user_activity():
    """Call this every time the user sends a message."""
    global _last_activity_time
    _last_activity_time = time.time()

def check_idle_time():
    """Called every ~5 minutes by the scheduler."""
    global _last_idle_nudge, _last_memory_consolidation
    now = time.time()
    idle_seconds = now - _last_activity_time
    idle_minutes = idle_seconds / 60.0

    # Sleep cycles: active memory consolidation and doc generation when user is idle for >= 30 minutes
    if idle_minutes >= 30.0 and (now - _last_memory_consolidation) > MEMORY_CONSOLIDATION_COOLDOWN:
        _last_memory_consolidation = now
        try:
            # BUG-35 fix: import at top of conditional rather than inside nested function
            # so ImportError surfaces immediately (not silently swallowed by outer except).
            from database import consolidate_memory_sleep_cycle
            from src.core.doc_generator import generate_mermaid_docs
            
            def run_sleep_cycle_tasks():
                consolidate_memory_sleep_cycle()
                try:
                    generate_mermaid_docs()
                except Exception as de:
                    print("[Scheduler] Failed to generate background Mermaid docs:", de)
                    
            import threading
            threading.Thread(target=run_sleep_cycle_tasks, daemon=True).start()
        except ImportError as ie:
            print("[Scheduler] ImportError in sleep cycle tasks — consolidate_memory_sleep_cycle not available:", ie)
        except Exception as ce:
            print("[Scheduler] Failed to trigger background sleep cycle tasks:", ce)

    if idle_minutes >= IDLE_THRESHOLD_MINUTES and (now - _last_idle_nudge) > IDLE_NUDGE_COOLDOWN:
        _last_idle_nudge = now
        # Rotate suggestions based on hour
        idx = int(datetime.now().hour) % len(IDLE_SUGGESTIONS)
        title, message = IDLE_SUGGESTIONS[idx]
        publish_nudge_sync(
            nudge_type="idle_nudge",
            title=title,
            message=message,
            action_hint="Click to dismiss or reply",
            icon="💤"
        )


# ──────────────────────────────────────────────
# 3. CLIPBOARD INTELLIGENCE
# ──────────────────────────────────────────────

# Cooldown so we don't fire on every keystroke-copy
_last_clipboard_nudge: float = 0.0
CLIPBOARD_COOLDOWN = 15  # seconds

# URL pattern
_URL_RE = re.compile(
    r'https?://[^\s/$.?#].[^\s]*',
    re.IGNORECASE
)

# Python traceback signature
_TRACEBACK_RE = re.compile(
    r'Traceback \(most recent call last\)|Error:|Exception:',
    re.IGNORECASE
)

# Code heuristic: 3+ lines with indentation or common code tokens
def _looks_like_code(text: str) -> bool:
    lines = text.strip().splitlines()
    if len(lines) < 3:
        return False
    indented = sum(1 for l in lines if l.startswith(("    ", "\t")))
    code_tokens = sum(1 for l in lines if any(
        tok in l for tok in ["def ", "class ", "import ", "return ", "=>", "function", "const ", "let "]
    ))
    return indented >= 2 or code_tokens >= 2

_clipboard_history_buffer: List[Dict[str, Any]] = []

def on_clipboard_proactive(text: str):
    """Called by ClipboardWatcher whenever clipboard content changes."""
    global _last_clipboard_nudge, _clipboard_history_buffer
    now = time.time()

    if not text or len(text.strip()) < 8:
        return

    # BUG-36 fix: skip append if text is identical to the last buffer entry
    # to avoid false-positive "Fused Clipboard Errors" from repeated copies.
    if not _clipboard_history_buffer or _clipboard_history_buffer[-1]["text"] != text:
        _clipboard_history_buffer.append({"text": text, "timestamp": now})
    _clipboard_history_buffer = [item for item in _clipboard_history_buffer if now - item["timestamp"] <= 300][-5:]

    # Check for Clipboard Fusion:
    errors_copied = [item["text"] for item in _clipboard_history_buffer if _TRACEBACK_RE.search(item["text"])]
    code_copied = [item["text"] for item in _clipboard_history_buffer if _looks_like_code(item["text"])]

    if len(errors_copied) >= 2 and (now - _last_clipboard_nudge) > CLIPBOARD_COOLDOWN:
        _last_clipboard_nudge = now
        publish_nudge_sync(
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
        publish_nudge_sync(
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

    # Detect: URL
    url_match = _URL_RE.search(text)
    if url_match:
        url = url_match.group(0)[:60]
        publish_nudge_sync(
            nudge_type="clipboard_url",
            title="🔗 URL Copied",
            message="Detected a URL. Want me to summarize or open it?",
            action_hint=f"Summarize: {url}",
            icon="🌐",
            mascot_state="diagnostic"
        )
        return

    # Detect: Python traceback / error
    if _TRACEBACK_RE.search(text):
        first_line = text.strip().splitlines()[0][:80]
        
        # Run background generation of the self-healing patch
        def run_patch_gen():
            patch = None
            try:
                # Look for File "path", line line_number
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
                        model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
                        
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
                        
                        # Clean code fence blocks
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
            
            # Publish nudge
            if patch:
                publish_nudge_sync(
                    nudge_type="clipboard_error",
                    title="🐛 Error Detected & Analyzed",
                    message=f"I detected a traceback and auto-generated a fix for {os.path.basename(patch['file_path'])}.",
                    action_hint=f"Review & Apply Fix",
                    icon="🔴",
                    mascot_state="diagnostic",
                    action="show_diff",
                    patch=patch
                )
            else:
                publish_nudge_sync(
                    nudge_type="clipboard_error",
                    title="🐛 Error Detected in Clipboard",
                    message="Looks like you copied an error or traceback. Want me to diagnose it?",
                    action_hint=f"Diagnose: {first_line}",
                    icon="🔴",
                    mascot_state="diagnostic"
                )
                
        threading.Thread(target=run_patch_gen, daemon=True).start()
        return

    # Detect: code snippet
    if _looks_like_code(text):
        publish_nudge_sync(
            nudge_type="clipboard_code",
            title="📋 Code Snippet Copied",
            message="I see you copied a code snippet. Want me to review, explain, or refactor it?",
            action_hint="Review copied code",
            icon="💻",
            mascot_state="diagnostic"
        )
        return


# ──────────────────────────────────────────────
# 4. CONVERSATION FOLLOW-UP
# ──────────────────────────────────────────────

# After ENGINEER-mode turns, schedule a follow-up after a delay
_pending_followups: list = []  # list of (fire_at_timestamp, message)
_followup_lock = threading.Lock()

ENGINEER_FOLLOWUP_DELAY = 30 * 60   # 30 minutes

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
    now = time.time()
    with _followup_lock:
        due = [(ft, m, msg) for ft, m, msg in _pending_followups if now >= ft]
        for item in due:
            _pending_followups.remove(item)

    for fire_at, mode, message in due:
        publish_nudge_sync(
            nudge_type="followup",
            title="🔁 Follow-up Suggestion",
            message=message,
            action_hint="Click to pick up where we left off",
            icon="🔁",
            mascot_state="happy"
        )

# ──────────────────────────────────────────────
# 5. ACTIVE WINDOW & DISTRACTION MONITOR
# ──────────────────────────────────────────────

_last_distraction_alert: float = 0.0
_distraction_start_time: Optional[float] = None
_last_window_title: str = ""

def get_active_process_and_title() -> tuple[str, str]:
    sys_platform = platform.system()
    title = ""
    proc_name = ""
    if sys_platform == "Windows":
        try:
            import ctypes
            from ctypes import wintypes
            hwnd = ctypes.windll.user32.GetForegroundWindow()
            if hwnd:
                # 1. Get Window Title
                length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
                buf = ctypes.create_unicode_buffer(length + 1)
                ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
                title = buf.value
                
                # 2. Get Process Executable Name
                pid = wintypes.DWORD()
                ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
                PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
                handle = ctypes.windll.kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid.value)
                if handle:
                    try:
                        buf_path = ctypes.create_unicode_buffer(1024)
                        size = wintypes.DWORD(1024)
                        if ctypes.windll.kernel32.QueryFullProcessImageNameW(handle, 0, buf_path, ctypes.byref(size)):
                            proc_name = os.path.basename(buf_path.value)
                    finally:
                        ctypes.windll.kernel32.CloseHandle(handle)
                
                # Robust fallback for anti-cheat protected processes (e.g., Valorant under Riot Vanguard)
                if not proc_name and pid.value:
                    try:
                        import psutil
                        proc_name = psutil.Process(pid.value).name()
                    except Exception:
                        pass
        except Exception:
            pass
    elif sys_platform == "Darwin":
        try:
            cmd = "osascript -e 'tell application \"System Events\" to get name of first process whose frontmost is true'"
            title = subprocess.check_output(cmd, shell=True).decode("utf-8", errors="ignore").strip()
            proc_name = title
        except Exception:
            pass
    return proc_name, title

def is_game_process_running(keywords) -> bool:
    try:
        import psutil
        for proc in psutil.process_iter(['name']):
            try:
                name = (proc.info['name'] or "").lower()
                if any(k in name for k in keywords):
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    except Exception:
        pass
    return False

def check_active_window():
    global _last_window_title, _distraction_start_time, _last_distraction_alert, game_mode_active, auto_game_mode_active
    proc_name, title = get_active_process_and_title()
    if not title and not proc_name:
        return
        
    now = time.time()
    title_lower = title.lower()
    proc_lower = proc_name.lower()

    # ── Game Mode Auto-Detection ──────────────────────────────
    game_keywords = [
        "valorant", "cyberpunk", "counter-strike", "csgo", "cs2", 
        "dota 2", "dota2", "league of legends", "leagueoflegends", 
        "gta v", "gta5", "minecraft", "javaw", "fortnite", 
        "genshin impact", "genshinimpact", "genshin", 
        "apex legends", "apexlegends", "r5apex", "hades"
    ]
    is_playing_game = any(gk in title_lower or gk in proc_lower for gk in game_keywords)
    
    if is_playing_game:
        if not game_mode_active:
            print(f"[Proactive] Game detected: '{title or proc_name}'. Automatically entering Game Mode.")
            game_mode_active = True
            auto_game_mode_active = True
            publish_nudge_sync(
                nudge_type="game_mode_changed",
                title="Game Mode Auto-Enabled",
                message="enabled",
                icon="🎮",
                action="game_mode_update"
            )
        return
    elif game_mode_active and auto_game_mode_active:
        # Check if the game process is still running in the background before disabling Game Mode
        if is_game_process_running(game_keywords):
            # Game is still running in background, preserve Game Mode
            return
            
        print(f"[Proactive] Game exited: '{title or proc_name}'. Automatically exiting Game Mode.")
        game_mode_active = False
        auto_game_mode_active = False
        publish_nudge_sync(
            nudge_type="game_mode_changed",
            title="Game Mode Auto-Disabled",
            message="disabled",
            icon="🎮",
            action="game_mode_update"
        )
    
    # Distraction check
    distractions = ["youtube", "facebook", "twitter", "netflix", "reddit", "instagram", "gaming", "steam", "x.com"]
    is_distracted = any(d in title_lower for d in distractions)
    
    if is_distracted:
        if _distraction_start_time is None:
            _distraction_start_time = now
        elif (now - _distraction_start_time) >= 600: # 10 minutes
            if (now - _last_distraction_alert) > 600:
                _last_distraction_alert = now
                publish_nudge_sync(
                    nudge_type="focus_distraction",
                    title="🧠 Smart Focus Guard",
                    message=f"I noticed you've been on '{title[:30]}' for over 10 minutes. Ready to get back to coding?",
                    action_hint="Resume coding session",
                    icon="🧠",
                    mascot_state="disapproving"
                )
    else:
        _distraction_start_time = None
        
    # Active Window Context (App-Aware Focus)
    ides = ["visual studio code", "vscode", "cursor", "pycharm", "sublime text", "notepad++"]
    if any(ide in title_lower for ide in ides) and title != _last_window_title:
        _last_window_title = title
        publish_nudge_sync(
            nudge_type="app_context",
            title="🖥️ IDE Focus Detected",
            message=f"Focused on IDE: '{title[:40]}'. Let me know if you need code generation, reviews, or refactoring.",
            action_hint="Suggest code task",
            icon="💻",
            mascot_state="diagnostic"
        )

# ──────────────────────────────────────────────
# 6. SMART BATTERY & RESOURCE SAVER
# ──────────────────────────────────────────────

_last_battery_alert: float = 0.0

def check_battery_status():
    global _last_battery_alert
    now = time.time()
    
    if (now - _last_battery_alert) < 900: # 15 min cooldown
        return
        
    try:
        battery = psutil.sensors_battery()
        if battery is None:
            return
            
        percent = battery.percent
        power_plugged = battery.power_plugged
        
        if percent < 30 and not power_plugged:
            _last_battery_alert = now
            publish_nudge_sync(
                nudge_type="battery_saver",
                title="🔋 Battery Low - Unplugged",
                message=f"Battery is at {percent}%. Let's switch to the Qwen 1.5B fallback model and pause heavy monitors to save VRAM and power.",
                action_hint="Activate Power-Saving Mode",
                icon="🔋",
                mascot_state="tired"
            )
    except Exception as e:
        print(f"[Proactive] Battery check error: {e}")

# ──────────────────────────────────────────────
# 7. AUTOMATED GIT COPILOT
# ──────────────────────────────────────────────

_last_git_check: float = 0.0

def check_git_status():
    global _last_git_check
    now = time.time()
    
    if (now - _last_git_check) < 600: # 10 min cooldown
        return
    _last_git_check = now
    
    try:
        # BUG-26 fix: resolve repo root from env var instead of CWD,
        # and use shell=False to avoid unnecessary attack surface.
        repo_path = os.environ.get(
            "MERIDIAN_REPO_PATH",
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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
            publish_nudge_sync(
                nudge_type="git_copilot",
                title="🐙 Git Changes Detected",
                message=f"You have {modified} modified and {untracked} untracked files in the workspace. Want me to draft structured commit messages?",
                action_hint="Draft Git Commit Message",
                icon="🐙",
                mascot_state="diagnostic"
            )
    except Exception:
        pass

# ──────────────────────────────────────────────
# 8. CIRCADIAN & MEETING REMINDERS
# ──────────────────────────────────────────────

_last_circadian_alert: float = 0.0

def check_circadian_reminders():
    global _last_circadian_alert
    now = time.time()
    
    if (now - _last_circadian_alert) < 1800: # 30 min cooldown
        return
        
    dt = datetime.now()
    hour = dt.hour
    
    # Late Night Reminder (Past 12:30 AM, i.e., hour == 0 and min >= 30, or 1 <= hour < 5)
    if (hour == 0 and dt.minute >= 30) or (hour >= 1 and hour < 5):
        _last_circadian_alert = now
        publish_nudge_sync(
            nudge_type="circadian_alert",
            title="🌙 Late Night Alert",
            message="It's past midnight! Would you like me to summarize our progress, commit files, and save the session runbook so you can wrap up?",
            action_hint="Summarize and wrap up",
            icon="🌙",
            mascot_state="sleeping"
        )
        return
        
    # Mock status meeting checks
    if (hour == 10 and dt.minute >= 45 and dt.minute <= 55) or (hour == 15 and dt.minute >= 45 and dt.minute <= 55):
        _last_circadian_alert = now
        publish_nudge_sync(
            nudge_type="circadian_alert",
            title="📅 Pre-Meeting Update Draft",
            message="Your status meeting starts in 15 minutes. Want me to draft a quick status update based on today's session?",
            action_hint="Draft status update",
            icon="📅",
            mascot_state="happy"
        )

# ──────────────────────────────────────────────
# 9. SMART OFFLINE-MODE ADAPTER
# ──────────────────────────────────────────────

_last_network_alert: float = 0.0
_is_offline: bool = False

def check_network_status():
    global _is_offline, _last_network_alert  # BUG-28 fix: declare _last_network_alert as global so we can update it
    
    offline_now = False
    try:
        # BUG-7 fix: use create_connection with a scoped timeout instead of
        # socket.setdefaulttimeout() which permanently alters the global socket timeout
        # for the entire process (affecting MongoDB, Ollama, httpx, etc.)
        with socket.create_connection(("1.1.1.1", 53), timeout=2.0):
            pass
    except Exception:
        offline_now = True
        
    if offline_now and not _is_offline:
        _is_offline = True
        _last_network_alert = time.time()  # BUG-28 fix: update timestamp so cooldown works correctly
        publish_nudge_sync(
            nudge_type="network_adapter",
            title="🌐 Offline Mode Activated",
            message="Internet connection lost. Switching to offline mode and local LLM/embedding models.",
            action_hint="Configure local fallback",
            icon="🌐",
            mascot_state="tired"
        )
    elif not offline_now and _is_offline:
        _is_offline = False
        _last_network_alert = time.time()  # BUG-28 fix: update timestamp on restore too
        publish_nudge_sync(
            nudge_type="network_adapter",
            title="🌐 Online Mode Restored",
            message="Internet connection restored. Cloud API models are available.",
            action_hint="Restore cloud settings",
            icon="🌐",
            mascot_state="happy"
        )
