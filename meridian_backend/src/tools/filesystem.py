import os
import shutil
import glob
import tempfile
from pathlib import Path
from typing import Dict, Any, Optional, List
from src.core.audit_logger import log_sensitive_action

EXCLUDED_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", ".next", "dist", "build", ".idea", ".vscode"}

def safe_path(target_path: str, allowed_roots: Optional[List[str]] = None) -> str:
    """Canonicalize path and verify it stays within allowed root directories (SEC-13)."""
    expanded_target = os.path.expanduser(target_path)
    abs_target = os.path.abspath(expanded_target)
    if allowed_roots is None:
        user_home = os.path.expanduser("~")
        allowed_roots = [os.getcwd(), os.path.dirname(os.getcwd()), tempfile.gettempdir(), user_home]
    
    target_p = Path(abs_target)
    is_safe = False
    for root in allowed_roots:
        root_p = Path(os.path.abspath(os.path.expanduser(root)))
        try:
            target_p.relative_to(root_p)
            is_safe = True
            break
        except ValueError:
            continue
            
    if not is_safe:
        log_sensitive_action(
            category="SECURITY_VIOLATION",
            action="path_traversal_blocked",
            details={"attempted_path": target_path, "canonical_path": abs_target},
            status="FAILED"
        )
        raise PermissionError(f"Access denied: Path '{target_path}' is outside authorized workspace root.")
    return abs_target

import sys
import time
import ctypes
import subprocess

def is_admin_process() -> bool:
    """Checks if current Python process has Windows Administrator / root privileges."""
    try:
        if sys.platform == "win32":
            return bool(ctypes.windll.shell32.IsUserAnAdmin())
        else:
            return os.geteuid() == 0
    except Exception:
        return False

def retry_file_operation(func, *args, retries: int = 3, delay: float = 0.2, **kwargs):
    """Retries file operations to bypass temporary OneDrive sync locks (Errno 13)."""
    last_exc = None
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except (PermissionError, OSError) as e:
            last_exc = e
            time.sleep(delay * (2 ** attempt))
    if last_exc:
        raise last_exc

def read_file(path: str) -> str:
    path = safe_path(path)
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    def _do_read():
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    res = retry_file_operation(_do_read)
    return str(res) if res is not None else ""

def write_file(path: str, content: str) -> str:
    path = safe_path(path)
    try:
        parent = os.path.dirname(os.path.abspath(path))
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        
        # SEC-36: Download / File write malware inspection hook
        try:
            from src.core.malware_scanner import scan_file_and_quarantine
            scan_res = scan_file_and_quarantine(path)
            if scan_res.get("is_threat"):
                return f"WARNING: File {path} was flagged as malicious and moved to quarantine: {scan_res.get('threat_reasons')}"
        except Exception:
            pass

        log_sensitive_action(
            category="FILE_WRITE",
            action="write_file",
            details={"path": path, "content_length": len(content)},
            status="SUCCESS"
        )
        return f"Successfully wrote {len(content)} characters to {path}"
    except Exception as e:
        log_sensitive_action(
            category="FILE_WRITE",
            action="write_file",
            details={"path": path, "error": str(e)},
            status="FAILED"
        )
        raise e

def list_directory(path: str) -> str:
    path = safe_path(path)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory not found: {path}")
    items = os.listdir(path)
    lines = []
    for item in items:
        full_path = os.path.join(path, item)
        is_dir = os.path.isdir(full_path)
        size = os.path.getsize(full_path) if not is_dir else 0
        type_str = "DIR" if is_dir else "FILE"
        lines.append(f"[{type_str}] {item} ({size} bytes)" if not is_dir else f"[{type_str}] {item}")
    return "\n".join(lines) if lines else "Directory is empty"

def search_files(query: str, directory: Optional[str] = None) -> str:
    if not directory or not os.path.exists(directory):
        directory = os.getcwd()
    
    matches = []
    for root, dirs, files in os.walk(directory):
        # Prune heavy/system directories for 10x-50x faster searches
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        
        for file in files:
            if query.lower() in file.lower():
                matches.append(os.path.join(root, file))
            # Also search file content for text files
            elif file.endswith((".py", ".txt", ".json", ".md", ".html", ".css", ".js", ".ts", ".tsx")):
                try:
                    full_path = os.path.join(root, file)
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        if query in f.read():
                            matches.append(f"{full_path} (matched content)")
                except Exception:
                    pass
        if len(matches) >= 50:
            break
            
    return "\n".join(matches) if matches else "No matches found"

def move_file(src: str, dst: str) -> str:
    src = safe_path(src)
    dst = safe_path(dst)
    try:
        shutil.move(src, dst)
        log_sensitive_action(
            category="FILE_WRITE",
            action="move_file",
            details={"src": src, "dst": dst},
            status="SUCCESS"
        )
        return f"Moved from {src} to {dst}"
    except Exception as e:
        log_sensitive_action(
            category="FILE_WRITE",
            action="move_file",
            details={"src": src, "dst": dst, "error": str(e)},
            status="FAILED"
        )
        raise e

def delete_file(path: str) -> str:
    try:
        # Support wildcard glob patterns for bulk deletions
        if "*" in path or "?" in path:
            normalized_path = path.replace("\\", "/")
            matched_files = glob.glob(normalized_path)
            if not matched_files:
                log_sensitive_action(
                    category="FILE_DELETE",
                    action="delete_file",
                    details={"path": path, "matched_files": []},
                    status="SUCCESS"
                )
                return "No files matched pattern."
            deleted_count = 0
            for f in matched_files:
                f_safe = safe_path(f)
                if os.path.isdir(f_safe):
                    shutil.rmtree(f_safe)
                elif os.path.exists(f_safe):
                    os.remove(f_safe)
                deleted_count += 1
            log_sensitive_action(
                category="FILE_DELETE",
                action="delete_file",
                details={"path": path, "deleted_count": deleted_count, "matched_files": matched_files},
                status="SUCCESS"
            )
            return f"Bulk deleted {deleted_count} files/directories matching pattern: {path}"

        path = safe_path(path)
        if os.path.isdir(path):
            shutil.rmtree(path)
            log_sensitive_action(
                category="FILE_DELETE",
                action="delete_file",
                details={"path": path, "type": "directory"},
                status="SUCCESS"
            )
            return f"Deleted directory: {path}"
        elif os.path.exists(path):
            os.remove(path)
            log_sensitive_action(
                category="FILE_DELETE",
                action="delete_file",
                details={"path": path, "type": "file"},
                status="SUCCESS"
            )
            return f"Deleted file: {path}"
        else:
            raise FileNotFoundError(f"Target not found: {path}")
    except Exception as e:
        log_sensitive_action(
            category="FILE_DELETE",
            action="delete_file",
            details={"path": path, "error": str(e)},
            status="FAILED"
        )
        raise e
