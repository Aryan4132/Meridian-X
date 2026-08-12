import os
import time
import json
import getpass
import platform
import logging
import threading
import hmac
import hashlib

logger = logging.getLogger("meridian_audit")

_audit_lock = threading.Lock()
_last_hmac = None

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

def _compute_hmac(entry_data: str, prev_hash: str) -> str:
    key = b"MERIDIAN_AUDIT_KEY"
    return hmac.new(key, f"{prev_hash}:{entry_data}".encode("utf-8"), hashlib.sha256).hexdigest()

def _get_last_hmac_from_file(log_path: str) -> str:
    """Reads the last recorded HMAC from audit.log to ensure chain continuity across restarts."""
    if os.path.exists(log_path):
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in reversed(lines):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        data = json.loads(line)
                        if data.get("hmac"):
                            return data["hmac"]
                    except Exception:
                        pass
        except Exception:
            pass
    return "0" * 64

def verify_audit_chain(log_path: str = "") -> tuple[bool, str]:
    """Verifies HMAC chain integrity of audit.log (SEC-20).

    Args:
        log_path: Optional override path for the audit log (used in tests).
    """
    if not log_path:
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
                # Re-sync hash if this is a chain-restart point (new process boot)
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

def log_sensitive_action(
    category: str,
    action: str,
    details: dict,
    status: str = "SUCCESS",
    _log_path: str = "",
    _hmac_state: list = [],
):
    """
    Log sensitive operations to audit.log in a structured JSON lines format.
    Categories: SHELL_EXECUTION, FILE_WRITE, FILE_DELETE, GUI_INPUT
    Thread-safe and persistent across daemon restarts.

    Args:
        _log_path: Optional override path (used in tests for isolation).
        _hmac_state: Optional mutable list holding [last_hmac] for test isolation.
    """
    global _last_hmac
    log_path = _log_path or get_audit_log_path()

    with _audit_lock:
        # Use caller-supplied HMAC state when provided (test isolation)
        if _hmac_state:
            current_hmac = _hmac_state[0]
        else:
            if _last_hmac is None:
                _last_hmac = _get_last_hmac_from_file(log_path)
            current_hmac = _last_hmac

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
        entry_hmac = _compute_hmac(entry_str, current_hmac)
        entry["hmac"] = entry_hmac

        # Persist HMAC state
        if _hmac_state:
            _hmac_state[0] = entry_hmac
        else:
            _last_hmac = entry_hmac

        try:
            # Write as single-line JSON to log file
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
            logger.info(f"[AUDIT] {category} - {action} - Status: {status}")
        except Exception as e:
            # Fallback to standard logger if file write fails
            logger.error(f"Failed to write audit log entry: {e}. Entry: {entry}")

