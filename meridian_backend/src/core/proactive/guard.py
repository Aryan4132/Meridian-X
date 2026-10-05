"""
guard.py — System health, process monitoring, game mode auto-detection, and resource guards.
"""

import os
import time
import socket
import psutil
import platform
import subprocess
from typing import Optional, Tuple, Set

# Game Mode settings
game_mode_active: bool = False
auto_game_mode_active: bool = False

# Thresholds
CPU_WARN_THRESHOLD: float = 85.0      # %
RAM_WARN_THRESHOLD: float = 88.0      # %
DISK_WARN_THRESHOLD: float = 90.0     # % used
DISK_PATH: str = os.path.abspath(os.sep)

# Cooldown: don't repeat the same alert within N seconds
_last_cpu_alert: float = 0.0
_last_ram_alert: float = 0.0
_last_disk_alert: float = 0.0
_health_cooldown: int = 300  # 5 minutes

_auto_detected_game_pid: Optional[int] = None
_auto_detected_game_name: Optional[str] = None

_last_battery_alert: float = 0.0
_last_network_alert: float = 0.0
_is_offline: bool = False

_last_distraction_alert: float = 0.0
_distraction_start_time: Optional[float] = None
_last_window_title: str = ""


def check_system_health():
    """Called every ~5 minutes by the scheduler. Fires nudge only when anomalous."""
    global _last_cpu_alert, _last_ram_alert, _last_disk_alert
    import src.core.proactive as proactive
    now = time.time()

    # Dynamic thresholds and disk path loading
    try:
        from database import get_user_profile
        cpu_warn_threshold = get_user_profile("cpu_warn_threshold") or CPU_WARN_THRESHOLD
        ram_warn_threshold = get_user_profile("ram_warn_threshold") or RAM_WARN_THRESHOLD
        disk_warn_threshold = get_user_profile("disk_warn_threshold") or DISK_WARN_THRESHOLD
    except Exception:
        cpu_warn_threshold = CPU_WARN_THRESHOLD
        ram_warn_threshold = RAM_WARN_THRESHOLD
        disk_warn_threshold = DISK_WARN_THRESHOLD

    try:
        disk_path = os.path.abspath(os.sep)
    except Exception:
        disk_path = DISK_PATH

    try:
        # CPU
        cpu = psutil.cpu_percent(interval=0.1)
        if cpu > cpu_warn_threshold and (now - _last_cpu_alert) > _health_cooldown:
            _last_cpu_alert = now
            top_proc = ""
            try:
                procs = sorted(
                    psutil.process_iter(['name', 'cpu_percent']),
                    key=lambda p: p.info.get('cpu_percent', 0),
                    reverse=True
                )
                if procs:
                    top_proc = f" — '{procs[0].info['name']}' is the top consumer."
            except Exception:
                pass
            proactive.publish_nudge_sync(
                nudge_type="system_health",
                title="⚠️ High CPU Usage",
                message=f"CPU is at {cpu:.0f}%.{top_proc}",
                action_hint="Investigate processes",
                icon="🔥"
            )

        # RAM
        ram = psutil.virtual_memory().percent
        if ram > ram_warn_threshold and (now - _last_ram_alert) > _health_cooldown:
            _last_ram_alert = now
            ram_avail_gb = psutil.virtual_memory().available / (1024 ** 3)
            proactive.publish_nudge_sync(
                nudge_type="system_health",
                title="⚠️ Low Memory",
                message=f"RAM usage is at {ram:.0f}% ({ram_avail_gb:.1f} GB free).",
                action_hint="Check running processes",
                icon="🧠"
            )

        # Disk
        try:
            disk = psutil.disk_usage(disk_path)
            disk_pct = disk.percent
            if disk_pct > disk_warn_threshold and (now - _last_disk_alert) > _health_cooldown:
                _last_disk_alert = now
                free_gb = disk.free / (1024 ** 3)
                proactive.publish_nudge_sync(
                    nudge_type="system_health",
                    title="💾 Low Disk Space",
                    message=f"Drive ({disk_path}) is {disk_pct:.0f}% full — only {free_gb:.1f} GB remaining.",
                    action_hint="Free up disk space",
                    icon="💾"
                )
        except Exception:
            pass

    except Exception as e:
        print(f"[Proactive] Health check error: {e}")


def get_active_process_and_title() -> Tuple[str, str, Optional[int]]:
    sys_platform = platform.system()
    title = ""
    proc_name = ""
    pid_val = None
    if sys_platform == "Windows":
        try:
            import ctypes
            from ctypes import wintypes
            hwnd = ctypes.windll.user32.GetForegroundWindow()
            if hwnd:
                length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
                buf = ctypes.create_unicode_buffer(length + 1)
                ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
                title = buf.value
                
                pid = wintypes.DWORD()
                ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
                pid_val = pid.value
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
                
                if not proc_name and pid.value:
                    try:
                        proc_name = psutil.Process(pid.value).name()
                    except Exception:
                        pass
        except Exception:
            pass
    elif sys_platform == "Darwin":
        try:
            cmd = ["osascript", "-e", 'tell application "System Events" to set frontApp to first application process whose frontmost is true\nget {name, unix id} of frontApp']
            out = subprocess.check_output(cmd, timeout=2.0).decode("utf-8", errors="ignore").strip()
            parts = [p.strip() for p in out.split(",")]
            if parts:
                proc_name = parts[0]
                title = parts[0]
                if len(parts) > 1 and parts[1].isdigit():
                    pid_val = int(parts[1])
        except Exception:
            pass
    elif sys_platform == "Linux":
        try:
            pid_out = subprocess.check_output(["xdotool", "getactivewindow", "getwindowpid"], timeout=1.0, stderr=subprocess.DEVNULL).decode("utf-8").strip()
            if pid_out.isdigit():
                pid_val = int(pid_out)
                proc_name = psutil.Process(pid_val).name()
            title_out = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"], timeout=1.0, stderr=subprocess.DEVNULL).decode("utf-8").strip()
            title = title_out
        except Exception:
            pass

    return proc_name, title, pid_val


def get_active_window_title() -> str:
    """Returns the title of the currently active foreground window."""
    _, title, _ = get_active_process_and_title()
    return title or ""


def is_system_busy_or_fullscreen(hwnd) -> bool:
    sys_platform = platform.system()
    if sys_platform == "Linux":
        try:
            out = subprocess.check_output(["xprop", "-root", "_NET_ACTIVE_WINDOW"], timeout=1.0, stderr=subprocess.DEVNULL).decode("utf-8")
            win_id = out.split()[-1]
            if win_id and win_id != "0x0":
                prop_out = subprocess.check_output(["xprop", "-id", win_id, "_NET_WM_STATE"], timeout=1.0, stderr=subprocess.DEVNULL).decode("utf-8")
                if "_NET_WM_STATE_FULLSCREEN" in prop_out:
                    return True
        except Exception:
            pass
        return False

    if sys_platform != "Windows":
        return False
        
    try:
        import ctypes
        state = ctypes.c_int()
        if ctypes.windll.shell32.SHQueryUserNotificationState(ctypes.byref(state)) == 0:
            if state.value == 3:  # QUNS_RUNNING_DND
                return True
    except Exception:
        pass

    try:
        if hwnd:
            import ctypes
            from ctypes import wintypes
            sw = ctypes.windll.user32.GetSystemMetrics(0)
            sh = ctypes.windll.user32.GetSystemMetrics(1)
            rect = wintypes.RECT()
            if ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect)):
                w = rect.right - rect.left
                h = rect.bottom - rect.top
                if w >= sw and h >= sh:
                    GWL_STYLE = -16
                    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
                    WS_CAPTION = 0x00C00000
                    if (style & WS_CAPTION) != WS_CAPTION:
                        class_buf = ctypes.create_unicode_buffer(256)
                        ctypes.windll.user32.GetClassNameW(hwnd, class_buf, 256)
                        class_name = class_buf.value
                        if class_name not in ["Progman", "WorkerW"]:
                            return True
    except Exception:
        pass
        
    return False


def is_game_process_running(pid: int, expected_name: str) -> bool:
    if not pid or not expected_name:
        return False
    try:
        if psutil.pid_exists(pid):
            p = psutil.Process(pid)
            return p.name().lower() == expected_name.lower()
    except Exception:
        pass
    return False


def get_app_pids() -> Set[int]:
    pids = {os.getpid()}
    try:
        parent = psutil.Process().parent()
        if parent:
            pids.add(parent.pid)
            gparent = parent.parent()
            if gparent:
                pids.add(gparent.pid)
    except Exception:
        pass
    try:
        for child in psutil.Process().children(recursive=True):
            pids.add(child.pid)
    except Exception:
        pass
    return pids


def check_active_window():
    global _last_window_title, _distraction_start_time, _last_distraction_alert
    global game_mode_active, auto_game_mode_active, _auto_detected_game_pid, _auto_detected_game_name
    import src.core.proactive as proactive
    
    proc_name, title, pid = get_active_process_and_title()
    if not title and not proc_name:
        return
        
    now = time.time()
    title_lower = title.lower()
    proc_lower = proc_name.lower()

    hwnd = None
    if platform.system() == "Windows":
        try:
            import ctypes
            hwnd = ctypes.windll.user32.GetForegroundWindow()
        except Exception:
            pass

    SYSTEM_SHELL_PROCESSES = {
        "explorer.exe",
        "searchhost.exe",
        "startmenuexperiencehost.exe",
        "shellexperiencehost.exe",
        "lockapp.exe",
        "taskmgr.exe"
    }

    is_playing_game = False
    try:
        if pid not in get_app_pids() and proc_lower not in SYSTEM_SHELL_PROCESSES:
            is_playing_game = is_system_busy_or_fullscreen(hwnd)
    except Exception:
        if proc_lower not in SYSTEM_SHELL_PROCESSES:
            is_playing_game = is_system_busy_or_fullscreen(hwnd)
    
    if is_playing_game:
        if not getattr(proactive, "game_mode_active", False):
            print(f"[Proactive] Game/Fullscreen detected: '{title or proc_name}' (PID: {pid}). Automatically entering Game Mode.")
            proactive.game_mode_active = True
            proactive.auto_game_mode_active = True
            _auto_detected_game_pid = pid
            _auto_detected_game_name = proc_name or title
            proactive.publish_nudge_sync(
                nudge_type="game_mode_changed",
                title="Game Mode Auto-Enabled",
                message="enabled",
                icon="🎮",
                action="game_mode_update"
            )
        return
    elif getattr(proactive, "game_mode_active", False) and getattr(proactive, "auto_game_mode_active", False):
        if _auto_detected_game_pid and is_game_process_running(_auto_detected_game_pid, _auto_detected_game_name):
            return
            
        print(f"[Proactive] Game/Fullscreen exited. Automatically exiting Game Mode.")
        proactive.game_mode_active = False
        proactive.auto_game_mode_active = False
        _auto_detected_game_pid = None
        _auto_detected_game_name = None
        proactive.publish_nudge_sync(
            nudge_type="game_mode_changed",
            title="Game Mode Auto-Disabled",
            message="disabled",
            icon="🎮",
            action="game_mode_update"
        )
    
    # Distraction check
    try:
        from database import get_user_profile
        distractions = get_user_profile("distraction_sites")
        if not isinstance(distractions, list):
            distractions = ["youtube", "facebook", "twitter", "netflix", "reddit", "instagram", "gaming", "steam", "x.com"]
    except Exception:
        distractions = ["youtube", "facebook", "twitter", "netflix", "reddit", "instagram", "gaming", "steam", "x.com"]

    is_distracted = any(d in title_lower for d in distractions)
    
    if is_distracted:
        if _distraction_start_time is None:
            _distraction_start_time = now
        elif (now - _distraction_start_time) >= 600: # 10 minutes
            if (now - _last_distraction_alert) > 600:
                _last_distraction_alert = now
                proactive.publish_nudge_sync(
                    nudge_type="focus_distraction",
                    title="🧠 Smart Focus Guard",
                    message=f"I noticed you've been on '{title[:30]}' for over 10 minutes. Ready to get back to coding?",
                    action_hint="Resume coding session",
                    icon="🧠",
                    mascot_state="disapproving"
                )
    else:
        _distraction_start_time = None


def check_battery_status():
    global _last_battery_alert
    import src.core.proactive as proactive
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
            proactive.publish_nudge_sync(
                nudge_type="battery_saver",
                title="🔋 Battery Low - Unplugged",
                message=f"Battery is at {percent}%. Let's switch to the Qwen 1.5B fallback model and pause heavy monitors to save VRAM and power.",
                action_hint="Activate Power-Saving Mode",
                icon="🔋",
                mascot_state="tired"
            )
    except Exception as e:
        print(f"[Proactive] Battery check error: {e}")


def check_network_status():
    global _is_offline, _last_network_alert
    import src.core.proactive as proactive
    
    offline_now = False
    try:
        with socket.create_connection(("1.1.1.1", 53), timeout=2.0):
            pass
    except Exception:
        offline_now = True
        
    if offline_now and not _is_offline:
        _is_offline = True
        _last_network_alert = time.time()
        proactive.publish_nudge_sync(
            nudge_type="network_adapter",
            title="🌐 Offline Mode Activated",
            message="Internet connection lost. Switching to offline mode and local LLM/embedding models.",
            action_hint="Configure local fallback",
            icon="🌐",
            mascot_state="tired"
        )
    elif not offline_now and _is_offline:
        _is_offline = False
        _last_network_alert = time.time()
        proactive.publish_nudge_sync(
            nudge_type="network_adapter",
            title="🌐 Online Mode Restored",
            message="Internet connection restored. Cloud API models are available.",
            action_hint="Restore cloud settings",
            icon="🌐",
            mascot_state="happy"
        )
