"""
elevated_runner.py — Hermes / OpenClaw Pattern Elevated Execution Engine
Provides Windows Administrator elevation checks, RunAs subprocess fallback,
and high-privilege scheduled task daemon registration.
"""

import os
import sys
import ctypes
import subprocess
import logging

from typing import Optional

logger = logging.getLogger("meridian_elevated_runner")


def is_admin() -> bool:
    """Check if the current process possesses Windows Administrator privileges."""
    try:
        if sys.platform == "win32":
            return bool(ctypes.windll.shell32.IsUserAnAdmin())
        else:
            return os.geteuid() == 0
    except Exception:
        return False


def run_command_elevated(command: str) -> dict:
    """
    Executes a system shell command with elevated Windows Administrator privileges.
    Uses PowerShell 'Start-Process -Verb RunAs' to bypass PermissionError (Errno 13).
    """
    if sys.platform != "win32":
        try:
            res = subprocess.run(["sudo", "sh", "-c", command], capture_output=True, text=True, timeout=60)
            return {"success": res.returncode == 0, "stdout": res.stdout, "stderr": res.stderr}
        except Exception as e:
            return {"success": False, "error": str(e)}

    # Windows PowerShell RunAs Invocation
    try:
        encoded_cmd = command.replace('"', '`"')
        ps_cmd = f"Start-Process powershell -ArgumentList '-NoProfile -Command \"{encoded_cmd}\"' -Verb RunAs -Wait"
        res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], capture_output=True, text=True, timeout=60)
        return {
            "success": res.returncode == 0,
            "stdout": res.stdout or "Elevated execution finished.",
            "stderr": res.stderr
        }
    except Exception as e:
        logger.error(f"Elevated command execution error: {e}")
        return {"success": False, "error": str(e)}


def register_elevated_scheduled_task(python_exe: Optional[str] = None, script_path: Optional[str] = None) -> dict:
    """
    Registers a Windows Scheduled Task with HIGHEST privilege level (RL HIGHEST)
    so Meridian-X backend runs as Administrator on boot without UAC popups (Hermes/OpenClaw pattern).
    """
    if sys.platform != "win32":
        return {"status": "unsupported_os"}

    if not python_exe:
        python_exe = sys.executable
    if not script_path:
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "api.py"))

    task_name = "MeridianXDaemon"
    task_cmd = f'"{python_exe}" "{script_path}"'
    cmd_args = ["schtasks", "/Create", "/TN", task_name, "/TR", task_cmd, "/SC", "ONLOGON", "/RL", "HIGHEST", "/F"]
    try:
        res = subprocess.run(cmd_args, capture_output=True, text=True)
        if res.returncode == 0:
            logger.info(f"Registered high-privilege scheduled task '{task_name}' successfully.")
            return {"status": "success", "task_name": task_name, "privilege": "HIGHEST"}
        else:
            return {"status": "failed", "error": res.stderr}
    except Exception as e:
        return {"status": "error", "error": str(e)}
