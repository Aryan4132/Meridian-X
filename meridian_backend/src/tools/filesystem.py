import os
import shutil
import glob
from typing import Dict, Any
from src.core.audit_logger import log_sensitive_action

def safe_path(target_path: str, allowed_roots: list = None) -> str:
    """Canonicalize path and verify it stays within allowed root directories (SEC-13)."""
    abs_target = os.path.abspath(target_path)
    if allowed_roots is None:
        allowed_roots = [os.getcwd(), os.path.dirname(os.getcwd())]
    
    is_safe = False
    for root in allowed_roots:
        abs_root = os.path.abspath(root)
        if abs_target == abs_root or abs_target.startswith(abs_root + os.sep):
            is_safe = True
            break
            
    if not is_safe:
        log_sensitive_action(
            category="SECURITY_VIOLATION",
            action="path_traversal_blocked",
            details={"attempted_path": target_path, "canonical_path": abs_target},
            status="FAILED"
        )
        raise PermissionError(f"Access denied: Path '{target_path}' is outside authorized workspace root.")
    return abs_target

def read_file(path: str) -> str:
    path = safe_path(path)
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def write_file(path: str, content: str) -> str:
    try:
        # BUG-53 fix: guard against empty parent when path is a bare filename (no directory component).
        # os.makedirs("") raises FileNotFoundError; os.path.abspath("file.txt") returns CWD which
        # os.makedirs would redundantly try to create.
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

def search_files(query: str, directory: str) -> str:
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Search directory not found: {directory}")
    
    matches = []
    for root, dirs, files in os.walk(directory):
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
            import glob
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
                if os.path.isdir(f):
                    shutil.rmtree(f)
                elif os.path.exists(f):
                    os.remove(f)
                deleted_count += 1
            log_sensitive_action(
                category="FILE_DELETE",
                action="delete_file",
                details={"path": path, "deleted_count": deleted_count, "matched_files": matched_files},
                status="SUCCESS"
            )
            return f"Bulk deleted {deleted_count} files/directories matching pattern: {path}"

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
