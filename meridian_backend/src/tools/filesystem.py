import os
import shutil
import glob
from typing import Dict, Any
from src.core.audit_logger import log_sensitive_action

def read_file(path: str) -> str:
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
