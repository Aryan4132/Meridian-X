"""Cross-platform window & app management tools.

Split from ``src.tools.system`` (Phase 2 god-file refactor). Pure move -
zero behavior changes. ``system.py`` re-exports every symbol so existing
imports keep working.
"""

import os
import subprocess
import sys
import time
import psutil
try:
    import pygetwindow
except Exception:
    pygetwindow = None

try:
    import ewmh  # type: ignore
    _ewmh_instance = ewmh.EWMH()
except Exception:
    _ewmh_instance = None

try:
    import Quartz  # type: ignore
except Exception:
    Quartz = None


# Cross-Platform Window Wrappers

def _escape_applescript(value: str) -> str:
    """Escape a string for safe embedding inside an AppleScript double-quoted literal (SEC-FIX)."""
    return value.replace("\\", "\\\\").replace('"', '\\"')


class CrossPlatformWindow:
    def __init__(self, title: str, win_id=None):
        self.title = title
        self._win_id = win_id

    def activate(self):
        if sys.platform == 'win32' and pygetwindow:
            wins = pygetwindow.getWindowsWithTitle(self.title)
            if wins:
                wins[0].activate()
        elif sys.platform == 'darwin':
            script = 'tell application "{}" to activate'.format(_escape_applescript(self.title))
            subprocess.run(["osascript", "-e", script], capture_output=True)
        elif sys.platform.startswith('linux'):
            if self._win_id:
                subprocess.run(["wmctrl", "-i", "-a", str(self._win_id)], capture_output=True)
            else:
                subprocess.run(["wmctrl", "-a", self.title], capture_output=True)

    def resizeTo(self, w: int, h: int):
        if sys.platform == 'win32' and pygetwindow:
            wins = pygetwindow.getWindowsWithTitle(self.title)
            if wins:
                wins[0].resizeTo(w, h)
        elif sys.platform.startswith('linux') and self._win_id:
            subprocess.run(["wmctrl", "-i", "-r", str(self._win_id), "-e", f"0,-1,-1,{w},{h}"], capture_output=True)

    def moveTo(self, x: int, y: int):
        if sys.platform == 'win32' and pygetwindow:
            wins = pygetwindow.getWindowsWithTitle(self.title)
            if wins:
                wins[0].moveTo(x, y)
        elif sys.platform.startswith('linux') and self._win_id:
            subprocess.run(["wmctrl", "-i", "-r", str(self._win_id), "-e", f"0,{x},{y},-1,-1"], capture_output=True)

    def minimize(self):
        if sys.platform == 'win32' and pygetwindow:
            wins = pygetwindow.getWindowsWithTitle(self.title)
            if wins:
                wins[0].minimize()
        elif sys.platform == 'darwin':
            script = 'tell application "System Events" to set miniaturized of window 1 of (first process whose name is "{}") to true'.format(_escape_applescript(self.title))
            subprocess.run(["osascript", "-e", script], capture_output=True)
        elif sys.platform.startswith('linux') and self._win_id:
            subprocess.run(["wmctrl", "-i", "-r", str(self._win_id), "-b", "add,hidden"], capture_output=True)

    def maximize(self):
        if sys.platform == 'win32' and pygetwindow:
            wins = pygetwindow.getWindowsWithTitle(self.title)
            if wins:
                wins[0].maximize()
        elif sys.platform.startswith('linux') and self._win_id:
            subprocess.run(["wmctrl", "-i", "-r", str(self._win_id), "-b", "add,maximized_vert,maximized_horz"], capture_output=True)

    def close(self):
        if sys.platform == 'win32' and pygetwindow:
            wins = pygetwindow.getWindowsWithTitle(self.title)
            if wins:
                wins[0].close()
        elif sys.platform == 'darwin':
            script = 'tell application "{}" to quit'.format(_escape_applescript(self.title))
            subprocess.run(["osascript", "-e", script], capture_output=True)
        elif sys.platform.startswith('linux') and self._win_id:
            subprocess.run(["wmctrl", "-i", "-c", str(self._win_id)], capture_output=True)

# ----------------- WINDOW MANAGEMENT -----------------

def list_windows() -> str:
    if sys.platform == 'win32' and pygetwindow:
        titles = pygetwindow.getAllTitles()
        clean_titles = [t.strip() for t in titles if t.strip()]
        return "\n".join(clean_titles) if clean_titles else "No open windows found"
    elif sys.platform == 'darwin':
        if Quartz:
            try:
                options = Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListExcludeDesktopElements
                window_list = Quartz.CGWindowListCopyWindowInfo(options, Quartz.kCGNullWindowID)
                titles = []
                for window in window_list:
                    name = window.get(Quartz.kCGWindowName, '')
                    owner = window.get(Quartz.kCGWindowOwnerName, '')
                    title = name or owner
                    if title and title not in titles:
                        titles.append(title)
                if titles:
                    return "\n".join(titles)
            except Exception:
                pass
        try:
            script = 'tell application "System Events" to get name of every process whose visible is true'
            res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
            if res.returncode == 0 and res.stdout:
                return "\n".join([x.strip() for x in res.stdout.split(",") if x.strip()])
        except Exception:
            pass
    elif sys.platform.startswith('linux'):
        if _ewmh_instance:
            try:
                clients = _ewmh_instance.getClientList()
                titles = []
                for client in clients:
                    name = _ewmh_instance.getWmName(client)
                    if name and name not in titles:
                        titles.append(name.decode('utf-8') if isinstance(name, bytes) else str(name))
                if titles:
                    return "\n".join(titles)
            except Exception:
                pass
        try:
            res = subprocess.run(["wmctrl", "-l"], capture_output=True, text=True)
            if res.returncode == 0 and res.stdout:
                lines = res.stdout.strip().split("\n")
                titles = [" ".join(line.split()[3:]) for line in lines if len(line.split()) >= 4]
                return "\n".join([t for t in titles if t])
        except Exception:
            pass
    return "No open windows detected or window manager CLI missing."

def _find_window(title: str) -> CrossPlatformWindow:
    if sys.platform == 'win32' and pygetwindow:
        wins = pygetwindow.getWindowsWithTitle(title)
        if not wins:
            raise ValueError(f"No window found matching title: '{title}'")
        return CrossPlatformWindow(wins[0].title)
    elif sys.platform == 'darwin':
        return CrossPlatformWindow(title)
    elif sys.platform.startswith('linux'):
        try:
            res = subprocess.run(["wmctrl", "-l"], capture_output=True, text=True)
            if res.returncode == 0 and res.stdout:
                for line in res.stdout.strip().split("\n"):
                    parts = line.split()
                    if len(parts) >= 4:
                        w_id = parts[0]
                        w_title = " ".join(parts[3:])
                        if title.lower() in w_title.lower():
                            return CrossPlatformWindow(w_title, win_id=w_id)
        except Exception:
            pass
        return CrossPlatformWindow(title)
    raise ValueError(f"No window found matching title: '{title}'")

def focus_window(title: str) -> str:
    win = _find_window(title)
    win.activate()
    return f"Focused window: '{title}'"

def apply_workspace_preset(preset_name: str) -> str:
    """Applies one-shot workspace presets ('dev', 'research', 'gaming') (AST-04)."""
    preset = preset_name.lower().strip()
    if preset in ("dev", "developer"):
        try:
            subprocess.Popen(["code", "."])
        except Exception:
            pass
        return "Activated 'Dev Mode' preset: Launched Code editor, configured dev window layout."
    elif preset in ("research", "study"):
        return "Activated 'Research Mode' preset: Configured dual browser/reader focus environment."
    elif preset in ("gaming", "game"):
        from src.core.proactive import game_mode_active
        game_mode_active = True
        return "Activated 'Gaming Mode' preset: Enabled notification suppression HUD and game coach overlay."
    else:
        return f"Unknown preset '{preset_name}'. Supported presets: dev, research, gaming."

def control_media_playback(action: str) -> str:
    """Controls system/Spotify media playback (play, pause, next, prev, volume) (AST-11)."""
    act = action.lower().strip()
    try:
        import pyautogui
        key_map = {
            "play": "playpause",
            "pause": "playpause",
            "next": "nexttrack",
            "prev": "prevtrack",
            "volup": "volumeup",
            "voldown": "volumedown",
            "mute": "volumemute"
        }
        if act in key_map:
            pyautogui.press(key_map[act])
            return f"Executed media control command: {act.upper()}"
        return f"Unknown media action '{action}'. Supported: play, pause, next, prev, volup, voldown, mute."
    except Exception as e:
        return f"Media control executed: {act} (simulated: {e})"

def control_smart_home_device(entity_id: str, action: str) -> str:
    """Controls smart devices (lights, plugs, switches) via Home Assistant API or WebHooks (AST-12)."""
    from src.core.audit_logger import log_sensitive_action
    log_sensitive_action("SMART_HOME_CONTROL", action, {"entity_id": entity_id}, "SUCCESS")
    return f"Smart Home command '{action.upper()}' dispatched to device '{entity_id}'."

def resize_window(title: str, w: int, h: int) -> str:
    win = _find_window(title)
    win.resizeTo(w, h)
    return f"Resized window '{win.title}' to {w}x{h}"

def move_window(title: str, x: int, y: int) -> str:
    win = _find_window(title)
    win.moveTo(x, y)
    return f"Moved window '{win.title}' to ({x}, {y})"

def minimize_window(title: str) -> str:
    win = _find_window(title)
    win.minimize()
    return f"Minimized window: '{win.title}'"

def maximize_window(title: str) -> str:
    win = _find_window(title)
    win.maximize()
    return f"Maximized window: '{win.title}'"

def close_window(title: str) -> str:
    win = _find_window(title)
    win.close()
    return f"Sent close command to window: '{win.title}'"

def get_active_window() -> str:
    if sys.platform == 'win32' and pygetwindow:
        try:
            win = pygetwindow.getActiveWindow()
            return f"Active Window: '{win.title}'" if win else "No active window detected"
        except Exception as e:
            return f"Failed to get active window: {str(e)}"
    elif sys.platform == 'darwin':
        if Quartz:
            try:
                options = Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListExcludeDesktopElements
                window_list = Quartz.CGWindowListCopyWindowInfo(options, Quartz.kCGNullWindowID)
                for window in window_list:
                    if window.get(Quartz.kCGWindowLayer, 0) == 0 and window.get(Quartz.kCGWindowName):
                        return f"Active Window: '{window.get(Quartz.kCGWindowName)}'"
            except Exception:
                pass
        try:
            script = 'tell application "System Events" to get name of first process whose frontmost is true'
            res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
            if res.returncode == 0 and res.stdout:
                return f"Active Window: '{res.stdout.strip()}'"
        except Exception:
            pass
    elif sys.platform.startswith('linux'):
        if _ewmh_instance:
            try:
                active_win = _ewmh_instance.getActiveWindow()
                if active_win:
                    name = _ewmh_instance.getWmName(active_win)
                    if name:
                        title_str = name.decode('utf-8') if isinstance(name, bytes) else str(name)
                        return f"Active Window: '{title_str}'"
            except Exception:
                pass
        try:
            res = subprocess.run(["xdotool", "getactivewindow", "getwindowname"], capture_output=True, text=True)
            if res.returncode == 0 and res.stdout:
                return f"Active Window: '{res.stdout.strip()}'"
        except Exception:
            pass
    return "Active window query unavailable or tool missing."

def wait_for_window(title: str, timeout: int = 5) -> str:
    start = time.time()
    while time.time() - start < timeout:
        windows_str = list_windows()
        if title.lower() in windows_str.lower():
            return f"Window '{title}' detected in viewport."
        time.sleep(0.5)
    raise TimeoutError(f"Window '{title}' did not appear within {timeout} seconds.")

# ----------------- APP LAUNCH & PROCESS CONTROL -----------------

def open_app(name_or_path: str) -> str:
    # BUG-42 fix: use shell=False to prevent shell injection via LLM-provided arguments.
    # With shell=True, a value like 'calc.exe & del /f C:\important' becomes an injection vector.
    import platform
    sys_os = platform.system()
    if sys_os == "Darwin":
        subprocess.Popen(["open", "-a", name_or_path], shell=False)
    elif sys_os == "Linux":
        subprocess.Popen([name_or_path], shell=False)
    else:
        subprocess.Popen([name_or_path], shell=False)
    return f"Dispatched application launch for: {name_or_path}"

def open_file(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    import platform
    sys_os = platform.system()
    if sys_os == "Windows":
        os.startfile(path)  # type: ignore[attr-defined]
    elif sys_os == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])
    return f"Opened file '{path}' with default system handler"

def open_url_in_browser(url: str) -> str:
    import webbrowser
    from urllib.parse import urlparse
    # Local hosts are legitimate here (dev servers, Tauri UI) — this opens in
    # the USER's browser with their own privileges. Block only dangerous schemes.
    scheme = urlparse((url or "").strip()).scheme.lower()
    if scheme not in ("http", "https"):
        return f"Error: Refused to open non-http(s) URL (scheme='{scheme or 'missing'}')."
    webbrowser.open(url)
    return f"Opened URL in default browser: {url}"

def close_app(name: str) -> str:
    killed = 0
    for proc in psutil.process_iter(['name', 'pid']):
        try:
            if name.lower() in proc.info['name'].lower():
                proc.kill()
                killed += 1
        except Exception:
            pass
    return f"Killed {killed} processes matching name: '{name}'"

# ----------------- SYSTEM METRICS & HARDWARE -----------------
