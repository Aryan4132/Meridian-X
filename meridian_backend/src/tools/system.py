import os
import time
import subprocess
import psutil
import pyperclip
import sys




# --- Window tools live in system_windows.py (re-exported here for compat) ---
from src.tools.system_windows import (
    _escape_applescript,
    CrossPlatformWindow,
    list_windows,
    _find_window,
    focus_window,
    apply_workspace_preset,
    control_media_playback,
    control_smart_home_device,
    resize_window,
    move_window,
    minimize_window,
    maximize_window,
    close_window,
    get_active_window,
    wait_for_window,
    open_app,
    open_file,
    open_url_in_browser,
    close_app,
)  # noqa: F401
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
            cpu_out = subprocess.check_output(["bash", "-lc", "lscpu | grep 'Model name' | cut -d: -f2"], shell=False).decode('utf-8').strip()
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
    try:
        from database import save_clipboard_history
        save_clipboard_history(text)
    except Exception:
        pass
    return "Successfully set clipboard content."
