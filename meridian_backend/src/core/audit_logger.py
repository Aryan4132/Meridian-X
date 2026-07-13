import os
import time
import json
import getpass
import platform
import logging

logger = logging.getLogger("meridian_audit")

def get_audit_log_path() -> str:
    from src.core.config import MERIDIAN_DATA_DIR
    meridian_dir = os.path.join(MERIDIAN_DATA_DIR, ".meridian")
    try:
        os.makedirs(meridian_dir, exist_ok=True)
    except Exception:
        home_dir = os.path.expanduser("~")
        meridian_dir = os.path.join(home_dir, ".meridian")
        os.makedirs(meridian_dir, exist_ok=True)
    return os.path.join(meridian_dir, "audit.log")

def log_sensitive_action(category: str, action: str, details: dict, status: str = "SUCCESS"):
    """
    Log sensitive operations to audit.log in a structured JSON lines format.
    Categories: SHELL_EXECUTION, FILE_WRITE, FILE_DELETE, GUI_INPUT
    """
    log_path = get_audit_log_path()
    entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "epoch": time.time(),
        "category": category.upper(),
        "action": action,
        "details": details,
        "status": status.upper(),
        "system": {
            "user": getpass.getuser(),
            "os": platform.system(),
            "os_release": platform.release(),
            "pid": os.getpid()
        }
    }
    
    try:
        # Write as single-line JSON to log file
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        logger.info(f"[AUDIT] {category} - {action} - Status: {status}")
    except Exception as e:
        # Fallback to standard logger if file write fails
        logger.error(f"Failed to write audit log entry: {e}. Entry: {entry}")
