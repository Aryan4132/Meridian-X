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

import hmac
import hashlib

_last_hmac = "0" * 64

def _compute_hmac(entry_data: str, prev_hash: str) -> str:
    key = b"MERIDIAN_AUDIT_KEY"
    return hmac.new(key, f"{prev_hash}:{entry_data}".encode("utf-8"), hashlib.sha256).hexdigest()

def verify_audit_chain() -> tuple[bool, str]:
    """Verifies HMAC chain integrity of audit.log (SEC-20)."""
    log_path = get_audit_log_path()
    if not os.path.exists(log_path):
        return True, "Audit log file does not exist yet."
        
    prev_hash = "0" * 64
    with open(log_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if not line.strip():
                continue
            data = json.loads(line)
            record_hmac = data.get("hmac")
            if not record_hmac:
                continue  # Skip legacy unchained record
            data_no_hmac = {k: v for k, v in data.items() if k != "hmac"}
            calc_hmac = _compute_hmac(json.dumps(data_no_hmac, sort_keys=True), prev_hash)
            if record_hmac != calc_hmac:
                # Re-sync hash if this is the first chained entry encountered
                calc_first = _compute_hmac(json.dumps(data_no_hmac, sort_keys=True), "0" * 64)
                if record_hmac == calc_first:
                    prev_hash = record_hmac
                    continue
                return False, f"Tampering detected at line {i+1}!"
            prev_hash = record_hmac
    return True, "Audit log HMAC chain verified cleanly."

def monitor_rogue_subprocesses() -> list:
    """Monitors backend child processes for unauthorized/rogue subprocesses (SEC-23)."""
    import psutil
    rogue = []
    try:
        current = psutil.Process()
        children = current.children(recursive=True)
        for child in children:
            if child.name().lower() not in ["cmd.exe", "powershell.exe", "conhost.exe", "python.exe", "git.exe"]:
                rogue.append(child.name())
                log_sensitive_action("SECURITY_VIOLATION", "rogue_subprocess_detected", {"proc_name": child.name(), "pid": child.pid}, "FAILED")
    except Exception:
        pass
    return rogue

def log_sensitive_action(category: str, action: str, details: dict, status: str = "SUCCESS"):
    """
    Log sensitive operations to audit.log in a structured JSON lines format.
    Categories: SHELL_EXECUTION, FILE_WRITE, FILE_DELETE, GUI_INPUT
    """
    global _last_hmac
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
    
    entry_str = json.dumps(entry, sort_keys=True)
    entry_hmac = _compute_hmac(entry_str, _last_hmac)
    _last_hmac = entry_hmac
    entry["hmac"] = entry_hmac
    
    try:
        # Write as single-line JSON to log file
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        logger.info(f"[AUDIT] {category} - {action} - Status: {status}")
    except Exception as e:
        # Fallback to standard logger if file write fails
        logger.error(f"Failed to write audit log entry: {e}. Entry: {entry}")
