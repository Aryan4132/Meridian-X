import os
import re

def get_file_syntax_status(file_path: str) -> str:
    """Checks if a python file compiles successfully or has syntax errors."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".py":
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            compile(content, file_path, "exec")
            return "success"
        except SyntaxError as se:
            return f"syntax_error: {se.msg} on line {se.lineno}"
        except Exception:
            return "success"
    # For other files, default to success for simplicity
    return "success"

def get_codebase_graph_json(workspace_dir: str = None) -> dict:
    """Scans the codebase, checks syntax errors, compiles dependencies, and outputs nodes and links."""
    from src.core.history_manager import find_workspace_root
    if workspace_dir is None:
        workspace_dir = find_workspace_root()
        
    exclude_dirs = {
        "venv", ".venv", "env", "node_modules", ".git", "dist", "build", 
        "meridian_memory", "__pycache__", ".antigravitycli", ".codegraph",
        "dist-ssr", "target"
    }
    
    nodes = []
    links = []
    
    # We also parse imports to build links
    file_imports = {}
    
    # Simple import extractor
    from src.core.doc_generator import parse_imports_in_file
    
    for root, dirs, files in os.walk(workspace_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in [".py", ".ts", ".tsx", ".js", ".jsx"]:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, workspace_dir).replace("\\", "/")
                
                # Check status
                status = get_file_syntax_status(full_path)
                
                nodes.append({
                    "id": rel_path,
                    "label": file,
                    "type": ext.replace(".", ""),
                    "status": "error" if status.startswith("syntax_error") else "success",
                    "error_message": status if status.startswith("syntax_error") else ""
                })
                
                imports = parse_imports_in_file(full_path)
                file_imports[rel_path] = imports
                
    # Build links based on imports matching file basenames
    for src_path, imports in file_imports.items():
        for imp in imports:
            for target_node in nodes:
                target_name = target_node["id"].split("/")[-1].split(".")[0]
                if imp == target_name and target_node["id"] != src_path:
                    links.append({
                        "source": src_path,
                        "target": target_node["id"]
                    })
                    
    return {
        "nodes": nodes,
        "links": links
    }
