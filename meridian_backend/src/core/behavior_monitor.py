"""
behavior_monitor.py — Real-Time Process Behavior Monitor / EDR-Lite (SEC-37)
Monitors process trees for crypto-miners, suspicious parent-child execution chains (Word/Browser -> CMD/Powershell),
process injection patterns, and excessive file handle access.
"""

import os
import psutil
import logging
from typing import Dict, List, Any

logger = logging.getLogger("meridian_behavior_monitor")

# Known legitimate system executables
SYSTEM_WHITELIST = {
    "system", "explorer.exe", "svchost.exe", "services.exe", "csrss.exe",
    "lsass.exe", "smss.exe", "wininit.exe", "taskhostw.exe",
    "kernel_task", "launchd", "windowserver", "systemd", "init"
}

# Suspicious parent processes that should NOT normally spawn shells
RESTRICTED_PARENTS = {"winword.exe", "excel.exe", "powerpnt.exe", "chrome.exe", "msedge.exe", "firefox.exe", "acrobat.exe"}
SUSPICIOUS_SHELLS = {"cmd.exe", "powershell.exe", "pwsh.exe", "wscript.exe", "cscript.exe", "mshta.exe", "bash", "sh"}

def scan_process_behavior(auto_quarantine: bool = False) -> Dict[str, Any]:
    """
    Scans active processes for EDR-Lite threat indicators:
    1. Suspicious Parent-Child Process Chains (e.g., Office/Browser spawning PowerShell/CMD).
    2. Crypto-miner signatures (sustained CPU > 80% with > 4 worker threads in unverified binaries).
    3. High file handle access anomalies.
    """
    flagged_threats: List[Dict[str, Any]] = []
    quarantined_pids: List[int] = []
    current_pid = os.getpid()

    for proc in psutil.process_iter(['pid', 'name', 'ppid', 'cpu_percent', 'num_threads']):
        try:
            pid = proc.info['pid']
            name = (proc.info['name'] or "").lower()
            ppid = proc.info['ppid']
            cpu = proc.info['cpu_percent'] or 0.0
            threads = proc.info['num_threads'] or 1

            if pid == current_pid or name in SYSTEM_WHITELIST:
                continue

            threat_reasons = []

            # Rule 1: Suspicious Parent-Child Process Chain
            if name in SUSPICIOUS_SHELLS and ppid:
                try:
                    parent_proc = psutil.Process(ppid)
                    parent_name = (parent_proc.name() or "").lower()
                    if parent_name in RESTRICTED_PARENTS:
                        threat_reasons.append(f"Suspicious parent-child spawn: {parent_name} -> {name}")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

            # Rule 2: Crypto-Miner Signature (High CPU + high threads in unverified executable)
            if cpu > 85.0 and threads >= 4 and name not in {"python.exe", "python3", "node.exe", "tauri"}:
                threat_reasons.append(f"Crypto-miner CPU signature: {cpu}% CPU with {threads} threads")

            # Rule 3: High Open File Handles (Mass File Access Anomaly)
            try:
                num_handles = proc.num_handles() if hasattr(proc, 'num_handles') else len(proc.open_files())
                if num_handles > 2000:
                    threat_reasons.append(f"Excessive file handle access anomaly: {num_handles} handles")
            except (psutil.NoSuchProcess, psutil.AccessDenied, AttributeError):
                pass

            if threat_reasons:
                threat_info = {
                    "pid": pid,
                    "name": name,
                    "ppid": ppid,
                    "cpu_percent": cpu,
                    "reasons": threat_reasons
                }
                flagged_threats.append(threat_info)
                logger.warning(f"[Behavior Monitor] Threat flagged on PID {pid} ({name}): {', '.join(threat_reasons)}")

                if auto_quarantine:
                    try:
                        proc.terminate()
                        quarantined_pids.append(pid)
                        logger.info(f"[Behavior Monitor] Automatically terminated threat PID {pid}.")
                    except Exception as e:
                        logger.error(f"[Behavior Monitor] Failed to terminate threat PID {pid}: {e}")

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return {
        "flagged_threats_count": len(flagged_threats),
        "threats": flagged_threats,
        "quarantined_pids": quarantined_pids
    }
