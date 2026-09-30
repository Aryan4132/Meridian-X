import os
import time
import psutil
import logging
import threading
from typing import Dict, List, Any, Optional

IMMUNE_PROCESS_NAMES = {
    "system", "system idle process", "registry", "smss.exe", "csrss.exe", 
    "wininit.exe", "services.exe", "lsass.exe", "winlogon.exe", "dwm.exe", 
    "explorer.exe", "svchost.exe", "spoolsv.exe", "taskhostw.exe",
    "runtimebroker.exe", "shellexperiencehost.exe", "searchhost.exe",
    "startmenuexperiencehost.exe", "textinputhost.exe", "code.exe"
}

def is_process_immune(pid: int, name: Optional[str] = None) -> bool:
    """Checks if a process is critical to the OS or Meridian-X runtime."""
    if pid <= 4 or pid == os.getpid():
        return True
    try:
        if hasattr(os, "getppid") and pid == os.getppid():
            return True
    except Exception:
        pass
    
    proc_name = (name or "").lower()
    if not proc_name:
        try:
            proc_name = psutil.Process(pid).name().lower()
        except Exception:
            return False
            
    return proc_name in IMMUNE_PROCESS_NAMES or (proc_name.startswith("python") and pid == os.getpid())

class ProactiveSystemGuard:
    """
    Proactive System Guard (🛡️)
    Monitors system RAM, process memory hogs, and disk space usage in real-time.
    Triggers native OS notifications / alert streams when anomalous usage is detected.
    """
    def __init__(self, memory_threshold_mb: float = 3500.0, disk_threshold_percent: float = 90.0):
        self.memory_threshold_mb = memory_threshold_mb
        self.disk_threshold_percent = disk_threshold_percent
        self.running = False
        self._thread: Optional[threading.Thread] = None
        self.alerts: List[Dict[str, Any]] = []

    def start(self):
        if self.running:
            return
        self.running = True
        self._thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self.running = False

    def check_system_resources(self) -> Dict[str, Any]:
        """Scans current process memory hogs and disk usage."""
        hogs: List[Dict[str, Any]] = []
        try:
            for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
                try:
                    info = proc.info
                    pid = info.get('pid')
                    name = info.get('name') or ""
                    if not pid or is_process_immune(pid, name):
                        continue
                    mem_mb = (info['memory_info'].rss if info.get('memory_info') else 0) / (1024 * 1024)
                    if mem_mb >= self.memory_threshold_mb:
                        hogs.append({
                            "pid": pid,
                            "name": name,
                            "memory_mb": round(mem_mb, 2),
                            "memory_gb": round(mem_mb / 1024, 2),
                            "recommendation": f"Process '{name}' (PID {pid}) is consuming {round(mem_mb/1024, 2)} GB RAM."
                        })
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
        except Exception as err:
            logging.error(f"Error checking process memory: {err}")

        disk_path = (os.path.splitdrive(os.getcwd())[0] + os.sep) if os.name == 'nt' else '/'
        try:
            disk = psutil.disk_usage(disk_path)
        except Exception:
            disk = psutil.disk_usage('/')

        disk_warning = None
        if disk.percent >= self.disk_threshold_percent:
            disk_warning = f"Disk usage is critical at {disk.percent}% ({round(disk.free / (1024**3), 2)} GB free)."

        return {
            "hogs": hogs,
            "disk_percent": disk.percent,
            "disk_warning": disk_warning,
            "timestamp": time.time()
        }

    def kill_process(self, pid: int) -> Dict[str, Any]:
        """Terminates a process by PID after immunity verification."""
        try:
            proc = psutil.Process(pid)
            proc_name = proc.name()
            if is_process_immune(pid, proc_name):
                return {"success": False, "message": f"Process '{proc_name}' (PID {pid}) is protected by System Immunity Shield."}
            proc.terminate()
            proc.wait(timeout=3)
            return {"success": True, "message": f"Successfully terminated {proc_name} (PID {pid})."}
        except psutil.NoSuchProcess:
            return {"success": False, "message": f"Process PID {pid} not found."}
        except Exception as e:
            try:
                proc = psutil.Process(pid)
                if is_process_immune(pid, proc.name()):
                    return {"success": False, "message": f"Process PID {pid} is protected by System Immunity Shield."}
                proc.kill()
                return {"success": True, "message": f"Killed process PID {pid}."}
            except Exception as kill_err:
                return {"success": False, "message": f"Failed to kill PID {pid}: {kill_err}"}

    def auto_heal_anomalies(self, kill_rogue_processes: bool = False) -> Dict[str, Any]:
        """Proactively identifies resource hogs and executes or proposes remediation."""
        res = self.check_system_resources()
        hogs = res.get("hogs", [])
        remediations = []

        for hog in hogs:
            action_desc = f"Kill runaway process {hog['name']} (PID {hog['pid']})"
            if kill_rogue_processes:
                kill_res = self.kill_process(hog["pid"])
                remediations.append({"action": action_desc, "executed": True, "result": kill_res})
            else:
                remediations.append({"action": action_desc, "executed": False, "recommended_command": f"taskkill /PID {hog['pid']} /F"})

        return {
            "status": "remediated" if kill_rogue_processes else "action_required",
            "memory_hogs_detected": len(hogs),
            "remediation_actions": remediations,
            "disk_warning": res.get("disk_warning")
        }

    def _monitor_loop(self):
        while self.running:
            res = self.check_system_resources()
            if res["hogs"]:
                for hog in res["hogs"]:
                    alert = {
                        "id": f"alert-{hog['pid']}-{int(time.time())}",
                        "title": "High Memory Consumption",
                        "message": f"Hey, {hog['name']} is eating {hog['memory_gb']}GB of RAM for no reason, should I kill it?",
                        "pid": hog["pid"],
                        "name": hog["name"],
                        "timestamp": time.time()
                    }
                    if not any(a["pid"] == hog["pid"] for a in self.alerts[-10:]):
                        self.alerts.append(alert)
            time.sleep(10)

system_guard = ProactiveSystemGuard()
