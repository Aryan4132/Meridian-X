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
    mascot_state: str = "default"
):
    """Thread-safe helper: schedule nudge publish onto the running event loop."""
    payload = {
        "type": nudge_type,
        "title": title,
        "message": message,
        "action_hint": action_hint,
        "icon": icon,
        "timestamp": _now_str(),
        "id": f"nudge-{nudge_type}-{int(time.time())}",
        "mascot_state": mascot_state
    }
    try:
        # get_running_loop() is the correct API in Python 3.10+ (get_event_loop is deprecated)
        loop = asyncio.get_running_loop()
        # We're inside an async context — schedule coroutine thread-safely
        asyncio.run_coroutine_threadsafe(
            event_bus.publish("proactive_nudge", payload), loop
        )
    except RuntimeError:
        # No running loop in this thread (e.g., APScheduler background thread)
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        try:
            new_loop.run_until_complete(event_bus.publish("proactive_nudge", payload))
        finally:
            new_loop.close()
            asyncio.set_event_loop(None)  # clean up thread-local loop reference



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
    global _last_idle_nudge
    now = time.time()
    idle_seconds = now - _last_activity_time
    idle_minutes = idle_seconds / 60.0

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

    # Append to rolling clipboard history buffer (limit to last 5 entries in 5 min)
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
        publish_nudge_sync(
            nudge_type="clipboard_error",
            title="🐛 Error Detected in Clipboard",
            message="Looks like you copied an error or traceback. Want me to diagnose it?",
            action_hint=f"Diagnose: {first_line}",
            icon="🔴",
            mascot_state="diagnostic"
        )
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

def get_active_window_title() -> str:
    sys_platform = platform.system()
    if sys_platform == "Windows":
        try:
            import ctypes
            hwnd = ctypes.windll.user32.GetForegroundWindow()
            length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
            buf = ctypes.create_unicode_buffer(length + 1)
            ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
            return buf.value
        except Exception:
            pass
    elif sys_platform == "Darwin":
        try:
            cmd = "osascript -e 'tell application \"System Events\" to get name of first process whose frontmost is true'"
            return subprocess.check_output(cmd, shell=True).decode("utf-8", errors="ignore").strip()
        except Exception:
            pass
    return ""

def check_active_window():
    global _last_window_title, _distraction_start_time, _last_distraction_alert
    title = get_active_window_title()
    if not title:
        return
        
    now = time.time()
    title_lower = title.lower()
    
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
        if not os.path.exists(".git"):
            return
            
        status = subprocess.check_output("git status --porcelain", shell=True).decode("utf-8", errors="ignore").strip()
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
    global _is_offline
    
    offline_now = False
    try:
        socket.setdefaulttimeout(2.0)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("1.1.1.1", 53))
        s.close()
    except Exception:
        offline_now = True
        
    if offline_now and not _is_offline:
        _is_offline = True
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
        publish_nudge_sync(
            nudge_type="network_adapter",
            title="🌐 Online Mode Restored",
            message="Internet connection restored. Cloud API models are available.",
            action_hint="Restore cloud settings",
            icon="🌐",
            mascot_state="happy"
        )
