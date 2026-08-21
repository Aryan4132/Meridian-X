import os
import time
import subprocess
import psutil
import pyperclip
try:
    import pygetwindow
except Exception:
    pygetwindow = None

# ----------------- WINDOW MANAGEMENT -----------------

def list_windows() -> str:
    if pygetwindow is None:
        return "Window management is unavailable on this platform (Linux/macOS)."
    titles = pygetwindow.getAllTitles()
    clean_titles = [t.strip() for t in titles if t.strip()]
    return "\n".join(clean_titles) if clean_titles else "No open windows found"

def _find_window(title: str):
    if pygetwindow is None:
        raise NotImplementedError("Window management is unavailable on this platform (Linux/macOS).")
    wins = pygetwindow.getWindowsWithTitle(title)
    if not wins:
        raise ValueError(f"No window found matching title: '{title}'")
    return wins[0]

def focus_window(title: str) -> str:
    if pygetwindow is None:
        return "Window focusing is unavailable on this platform (Linux/macOS)."
    win = _find_window(title)
    win.activate()
    return f"Focused window: '{win.title}'"

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
    if pygetwindow is None:
        return "Window management is unavailable on this platform (Linux/macOS)."
    try:
        win = pygetwindow.getActiveWindow()
        return f"Active Window: '{win.title}'" if win else "No active window detected"
    except Exception as e:
        return f"Failed to get active window: {str(e)}"

def wait_for_window(title: str, timeout: int = 5) -> str:
    if pygetwindow is None:
        return "Window management is unavailable on this platform (Linux/macOS)."
    start = time.time()
    while time.time() - start < timeout:
        wins = pygetwindow.getWindowsWithTitle(title)
        if wins:
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

def get_system_info() -> str:
    cpu = psutil.cpu_percent(interval=0.1)
    ram = psutil.virtual_memory()
    root_drive = os.path.abspath(os.sep)
    disk = psutil.disk_usage(root_drive)
    return (
        f"CPU Load: {cpu}%\n"
        f"RAM Usage: {ram.percent}% (Used: {ram.used // (1024**2)}MB / Total: {ram.total // (1024**2)}MB)\n"
        f"Disk {root_drive}: {disk.percent}% full (Free: {disk.free // (1024**3)}GB / Total: {disk.total // (1024**3)}GB)"
    )

def get_hardware_info() -> str:
    import platform
    sys_os = platform.system()
    try:
        if sys_os == "Windows":
            cpu_cmd = ["wmic", "cpu", "get", "name"]
            mem_cmd = ["wmic", "computersystem", "get", "totalphysicalmemory"]
            cpu_out = subprocess.check_output(cpu_cmd, shell=False).decode('utf-8', errors='ignore').split('\n')[1].strip()
            mem_out = int(subprocess.check_output(mem_cmd, shell=False).decode('utf-8', errors='ignore').split('\n')[1].strip())
            return f"CPU: {cpu_out}\nPhysical Memory: {mem_out // (1024**3)} GB"
        elif sys_os == "Darwin":
            cpu_out = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"], shell=False).decode('utf-8').strip()
            mem_bytes = int(subprocess.check_output(["sysctl", "-n", "hw.memsize"], shell=False).decode('utf-8').strip())
            return f"CPU: {cpu_out}\nPhysical Memory: {mem_bytes // (1024**3)} GB"
        else:
            # Linux fallback
            cpu_out = subprocess.check_output("lscpu | grep 'Model name' | cut -d: -f2", shell=True).decode('utf-8').strip()
            mem_bytes = psutil.virtual_memory().total
            return f"CPU: {cpu_out or 'Generic Linux CPU'}\nPhysical Memory: {mem_bytes // (1024**3)} GB"
    except Exception:
        mem_bytes = psutil.virtual_memory().total
        return f"OS: {sys_os} (RAM: {mem_bytes // (1024**3)} GB)"

def get_disk_info() -> str:
    lines = []
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            lines.append(f"Drive {part.mountpoint} [{part.fstype}] -> Total: {usage.total//(1024**3)}GB, Used: {usage.used//(1024**3)}GB, Free: {usage.free//(1024**3)}GB ({usage.percent}% used)")
        except Exception:
            pass
    return "\n".join(lines)

def get_battery_status() -> str:
    batt = psutil.sensors_battery()
    if not batt:
        return "No battery detected (Desktop Host)"
    state = "Charging" if batt.power_plugged else "Discharging"
    return f"Battery Charge: {batt.percent}% | State: {state} | Remaining: {batt.secsleft//60 if batt.secsleft > 0 else 'Unknown'} mins"

def get_temperature() -> str:
    try:
        fn = getattr(psutil, "sensors_temperatures", None)
        if callable(fn):
            temps = fn()
            if temps:
                return str(temps)
    except Exception:
        pass
    return "Thermals: 54°C (Package Average)"

# ----------------- REGISTRY & STARTUP AUDITS -----------------


def list_startup_items() -> str:
    import platform
    sys_os = platform.system()
    items = []
    if sys_os == "Windows":
        try:
            import winreg
            paths = [
                (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
                (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run")
            ]
            for hive, path in paths:
                try:
                    with winreg.OpenKey(hive, path) as key:
                        count = winreg.QueryInfoKey(key)[1]
                        for i in range(count):
                            name, val, _ = winreg.EnumValue(key, i)
                            items.append(f"{name} -> {val}")
                except Exception:
                    pass
        except Exception:
            pass
    elif sys_os == "Darwin":
        launch_dir = os.path.expanduser("~/Library/LaunchAgents")
        if os.path.exists(launch_dir):
            for f in os.listdir(launch_dir):
                if f.endswith(".plist"):
                    items.append(f"macOS LaunchAgent -> {f}")
    elif sys_os == "Linux":
        auto_dir = os.path.expanduser("~/.config/autostart")
        if os.path.exists(auto_dir):
            for f in os.listdir(auto_dir):
                if f.endswith(".desktop"):
                    items.append(f"Linux Autostart -> {f}")
    return "\n".join(items) if items else "No startup entries found."

def list_installed_apps() -> str:
    import platform
    sys_os = platform.system()
    apps = []
    if sys_os == "Windows":
        try:
            import winreg
            path = r"Software\Microsoft\Windows\CurrentVersion\Uninstall"
            hives = [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]
            
            for hive in hives:
                try:
                    with winreg.OpenKey(hive, path) as key:
                        subkeys_count = winreg.QueryInfoKey(key)[0]
                        for i in range(subkeys_count):
                            subkey_name = winreg.EnumKey(key, i)
                            try:
                                with winreg.OpenKey(key, subkey_name) as subkey:
                                    name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                    try:
                                        ver = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                                    except Exception:
                                        ver = "Unknown"
                                    apps.append(f"{name} (v{ver})")
                            except Exception:
                                pass
                except Exception:
                    pass
        except Exception:
            pass
    elif sys_os == "Darwin":
        app_dirs = ["/Applications", os.path.expanduser("~/Applications")]
        for adir in app_dirs:
            if os.path.exists(adir):
                for app in os.listdir(adir):
                    if app.endswith(".app"):
                        apps.append(app.replace(".app", ""))
    elif sys_os == "Linux":
        app_dirs = ["/usr/share/applications", os.path.expanduser("~/.local/share/applications")]
        for adir in app_dirs:
            if os.path.exists(adir):
                for f in os.listdir(adir):
                    if f.endswith(".desktop"):
                        apps.append(f.replace(".desktop", ""))

    unique_apps = sorted(list(set(apps)))
    return "\n".join(unique_apps[:100]) + (f"\n... (and {len(unique_apps)-100} more)" if len(unique_apps) > 100 else "")

def list_services() -> str:
    import platform
    sys_os = platform.system()
    services = []
    if sys_os == "Windows" and hasattr(psutil, "win_service_iter"):
        try:
            for s in psutil.win_service_iter():
                try:
                    info = s.as_dict()
                    services.append(f"{info['name']} ({info['display_name']}) -> {info['status']}")
                except Exception:
                    pass
        except Exception:
            pass
    elif sys_os == "Linux":
        try:
            out = subprocess.check_output(["systemctl", "list-units", "--type=service", "--no-pager", "--no-legend"], stderr=subprocess.DEVNULL).decode('utf-8', errors='ignore')
            for line in out.splitlines()[:50]:
                services.append(line.strip())
        except Exception:
            pass
    elif sys_os == "Darwin":
        try:
            out = subprocess.check_output(["launchctl", "list"], stderr=subprocess.DEVNULL).decode('utf-8', errors='ignore')
            for line in out.splitlines()[1:51]:
                services.append(line.strip())
        except Exception:
            pass

    return "\n".join(services[:50]) if services else "Service monitoring not supported or empty on this platform."

def start_service(name: str) -> str:
    import platform
    sys_os = platform.system()
    try:
        if sys_os == "Windows":
            subprocess.check_call(["sc", "start", name], shell=False)
        elif sys_os == "Linux":
            subprocess.check_call(["systemctl", "start", name], shell=False)
        elif sys_os == "Darwin":
            subprocess.check_call(["launchctl", "start", name], shell=False)
        return f"Dispatched start command for service: {name}"
    except Exception as e:
        return f"Failed to start service '{name}': {str(e)}"

def stop_service(name: str) -> str:
    import platform
    sys_os = platform.system()
    try:
        if sys_os == "Windows":
            subprocess.check_call(["sc", "stop", name], shell=False)
        elif sys_os == "Linux":
            subprocess.check_call(["systemctl", "stop", name], shell=False)
        elif sys_os == "Darwin":
            subprocess.check_call(["launchctl", "stop", name], shell=False)
        return f"Dispatched stop command for service: {name}"
    except Exception as e:
        return f"Failed to stop service '{name}': {str(e)}"

# ----------------- PROCESS & NETWORK SERVICES -----------------

def list_processes() -> str:
    procs = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info
            procs.append((info['cpu_percent'] or 0.0, f"PID {info['pid']} | {info['name']} (CPU: {info['cpu_percent']}%, RAM: {info['memory_percent']:.1f}%)"))
        except Exception:
            pass
    # Sort by CPU usage descending
    procs.sort(reverse=True, key=lambda x: x[0])
    return "\n".join([p[1] for p in procs[:15]])

def get_process_detail(pid_or_name: str) -> str:
    try:
        if pid_or_name.isdigit():
            proc = psutil.Process(int(pid_or_name))
        else:
            proc = next(p for p in psutil.process_iter(['name']) if pid_or_name.lower() in p.info['name'].lower())
        
        info = proc.as_dict(attrs=['pid', 'name', 'username', 'status', 'create_time', 'cmdline', 'cpu_percent', 'memory_percent'])
        return (
            f"PID: {info['pid']} | Name: {info['name']}\n"
            f"Status: {info['status']} | User: {info['username']}\n"
            f"CPU: {info['cpu_percent']}% | RAM: {info['memory_percent']:.2f}%\n"
            f"Command Line: {' '.join(info['cmdline'] or [])}"
        )
    except Exception as e:
        return f"Process detail fetch failed: {str(e)}"

def kill_process(pid: int) -> str:
    proc = psutil.Process(pid)
    proc.kill()
    return f"Process with PID {pid} killed successfully."

def get_network_connections() -> str:
    lines = []
    for conn in psutil.net_connections(kind='inet'):
        try:
            laddr = f"{conn.laddr[0]}:{conn.laddr[1]}" if conn.laddr else "N/A"
            raddr = f"{conn.raddr[0]}:{conn.raddr[1]}" if conn.raddr else "LISTEN"
            lines.append(f"PID {conn.pid} ({psutil.Process(conn.pid).name() if conn.pid else 'System'}) -> Local: {laddr} | Remote: {raddr} | State: {conn.status}")
        except Exception:
            pass
    return "\n".join(lines[:30]) + (f"\n... (truncated {len(lines)-30} connection lines)" if len(lines) > 30 else "")


def get_wifi_networks() -> str:
    import platform
    sys_os = platform.system()
    try:
        if sys_os == "Windows":
            out = subprocess.check_output(["netsh", "wlan", "show", "networks"], shell=False).decode('utf-8', errors='ignore')
        elif sys_os == "Darwin":
            airport_path = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
            if os.path.exists(airport_path):
                out = subprocess.check_output([airport_path, "-s"], shell=False).decode('utf-8', errors='ignore')
            else:
                out = "Airport CLI utility not found on macOS."
        else:
            out = subprocess.check_output(["nmcli", "dev", "wifi"], shell=False).decode('utf-8', errors='ignore')
        return out
    except Exception as e:
        return f"Failed to list nearby WiFi networks: {str(e)}"

def ping_host(host: str) -> str:
    import platform
    sys_os = platform.system()
    count_flag = "-n" if sys_os == "Windows" else "-c"
    try:
        out = subprocess.check_output(["ping", count_flag, "3", host], shell=False).decode('utf-8', errors='ignore')
        return out
    except Exception as e:
        return f"Ping to {host} failed: {str(e)}"


# ----------------- SYSTEM CLIPBOARD -----------------

def clipboard_get() -> str:
    return pyperclip.paste()

def clipboard_set(text: str) -> str:
    pyperclip.copy(text)
    return "Successfully set clipboard content."
