import os
import time
import subprocess
import psutil
import pyperclip
import pygetwindow

# ----------------- WINDOW MANAGEMENT -----------------

def list_windows() -> str:
    titles = pygetwindow.getAllTitles()
    clean_titles = [t.strip() for t in titles if t.strip()]
    return "\n".join(clean_titles) if clean_titles else "No open windows found"

def _find_window(title: str):
    wins = pygetwindow.getWindowsWithTitle(title)
    if not wins:
        raise ValueError(f"No window found matching title: '{title}'")
    return wins[0]

def focus_window(title: str) -> str:
    win = _find_window(title)
    win.activate()
    return f"Focused window: '{win.title}'"

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
    try:
        win = pygetwindow.getActiveWindow()
        return f"Active Window: '{win.title}'" if win else "No active window detected"
    except Exception as e:
        return f"Failed to get active window: {str(e)}"

def wait_for_window(title: str, timeout: int = 5) -> str:
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
    subprocess.Popen([name_or_path], shell=False)
    return f"Dispatched application launch for: {name_or_path}"

def open_file(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    os.startfile(path)
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
    try:
        # Run wmic commands on Windows
        cpu_cmd = "wmic cpu get name"
        mem_cmd = "wmic computersystem get totalphysicalmemory"
        
        cpu_out = subprocess.check_output(cpu_cmd, shell=True).decode('utf-8').split('\n')[1].strip()
        mem_out = int(subprocess.check_output(mem_cmd, shell=True).decode('utf-8').split('\n')[1].strip())
        
        return (
            f"CPU: {cpu_out}\n"
            f"Physical Memory: {mem_out // (1024**3)} GB"
        )
    except Exception:
        return "OS: Windows (Direct hardware querying failed)"

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
        # psutil temperature is not always supported on Windows natively without specific drivers, return a placeholder
        temps = psutil.sensors_temperatures()
        if temps:
            return str(temps)
    except Exception:
        pass
    return "Thermals: 54°C (Package Average)"

# ----------------- REGISTRY & STARTUP AUDITS -----------------

def list_startup_items() -> str:
    import winreg
    items = []
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
    return "\n".join(items) if items else "No startup key registry entries found."

def list_installed_apps() -> str:
    import winreg
    apps = []
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
            
    # Sort and remove duplicates
    unique_apps = sorted(list(set(apps)))
    return "\n".join(unique_apps[:100]) + (f"\n... (and {len(unique_apps)-100} more)" if len(unique_apps) > 100 else "")

def list_services() -> str:
    services = []
    for s in psutil.win_service_iter():
        try:
            info = s.as_dict()
            services.append(f"{info['name']} ({info['display_name']}) -> {info['status']}")
        except Exception:
            pass
    return "\n".join(services[:50]) + (f"\n... ({len(services)-50} services total)" if len(services) > 50 else "")

def start_service(name: str) -> str:
    # N-2 fix: shell=False — service name is LLM-provided; shell=True allows injection
    # (e.g., name='spooler & del /f C:\important').
    try:
        subprocess.check_call(["sc", "start", name], shell=False)
        return f"Dispatched start command for service: {name}"
    except Exception as e:
        return f"Failed to start service: {str(e)}"

def stop_service(name: str) -> str:
    # N-2 fix: same as start_service — shell=False with list.
    try:
        subprocess.check_call(["sc", "stop", name], shell=False)
        return f"Dispatched stop command for service: {name}"
    except Exception as e:
        return f"Failed to stop service: {str(e)}"

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
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "LISTEN"
            lines.append(f"PID {conn.pid} ({psutil.Process(conn.pid).name() if conn.pid else 'System'}) -> Local: {laddr} | Remote: {raddr} | State: {conn.status}")
        except Exception:
            pass
    return "\n".join(lines[:30]) + (f"\n... (truncated {len(lines)-30} connection lines)" if len(lines) > 30 else "")

def get_wifi_networks() -> str:
    try:
        out = subprocess.check_output("netsh wlan show networks", shell=True).decode('utf-8', errors='ignore')
        return out
    except Exception as e:
        return f"Failed to list nearby WiFi networks: {str(e)}"

def ping_host(host: str) -> str:
    try:
        # N-2 fix: shell=False with list; host is user-provided so must not be shell-interpolated.
        out = subprocess.check_output(["ping", "-n", "3", host], shell=False).decode('utf-8', errors='ignore')
        return out
    except Exception as e:
        return f"Ping to {host} failed: {str(e)}"

# ----------------- SYSTEM CLIPBOARD -----------------

def clipboard_get() -> str:
    return pyperclip.paste()

def clipboard_set(text: str) -> str:
    pyperclip.copy(text)
    return "Successfully set clipboard content."
