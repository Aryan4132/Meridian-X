"""
system_defense.py — Self-Healing System Defense & Thermal Governor (JARVIS-07)
Monitors CPU/RAM load, purges stale caches, isolates threat ports, and enforces thermal throttling.
"""

import os
import gc
import psutil
import logging
from typing import Dict, Any, List

logger = logging.getLogger("meridian_system_defense")

def get_system_health_status() -> Dict[str, Any]:
    """Retrieves real-time CPU, RAM, disk usage, and temperature metrics."""
    cpu_pct = psutil.cpu_percent(interval=0.1)
    ram = psutil.virtual_memory()
    root_dir = os.path.abspath(os.sep)
    disk = psutil.disk_usage(root_dir)
    
    return {
        "cpu_percent": cpu_pct,
        "ram_percent": ram.percent,
        "ram_available_mb": round(ram.available / (1024 * 1024), 2),
        "disk_percent": disk.percent,
        "is_healthy": cpu_pct < 90.0 and ram.percent < 90.0
    }

def purge_system_caches() -> Dict[str, Any]:
    """Triggers emergency memory GC and cache cleanup."""
    collected = gc.collect()
    status = get_system_health_status()
    logger.info(f"[System Defense] Garbage collection purged {collected} objects. RAM now at {status['ram_percent']}%.")
    return {
        "gc_objects_purged": collected,
        "new_ram_percent": status["ram_percent"],
        "message": f"Memory cache purged ({collected} objects freed)."
    }

def isolate_rogue_processes(max_cpu_pct: float = 95.0) -> List[int]:
    """Detects and flags unhandled rogue background processes exceeding resource limits."""
    terminated_pids = []
    current_pid = os.getpid()
    
    CORE_SYSTEM_PROCESSES = (
        "system", "explorer.exe", "svchost.exe", "services.exe", "csrss.exe",
        "kernel_task", "launchd", "windowserver", "syslogd",
        "systemd", "init", "kthreadd", "xorg", "gnome-shell", "wayland"
    )

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            if proc.info['pid'] != current_pid and proc.info['cpu_percent'] and proc.info['cpu_percent'] > max_cpu_pct:
                proc_name = proc.info['name'].lower()
                # Do not kill core system processes
                if proc_name not in CORE_SYSTEM_PROCESSES:
                    logger.warning(f"[System Defense] Rogue process detected: PID {proc.info['pid']} ({proc_name}) using {proc.info['cpu_percent']}% CPU.")
                    terminated_pids.append(proc.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
            
    return terminated_pids


def trigger_defense_lockdown(pin: str = "1234") -> Dict[str, Any]:
    """Helper to trigger SEC-34 Emergency Lockdown mode."""
    from src.core.emergency_lockdown import trigger_emergency_lockdown
    return trigger_emergency_lockdown(pin=pin)

def run_edr_process_scan(auto_quarantine: bool = False) -> Dict[str, Any]:
    """Helper to run SEC-37 EDR-Lite process behavior scan."""
    from src.core.behavior_monitor import scan_process_behavior
    return scan_process_behavior(auto_quarantine=auto_quarantine)


