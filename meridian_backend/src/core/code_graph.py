import os
import re
from typing import Optional, List, Dict, Any

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

def get_codebase_graph_json(workspace_dir: Optional[str] = None) -> dict:
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


def parse_python_ast(file_path: str) -> dict:
    """Parses a Python file using standard `ast` to extract classes, functions, calls, and docstrings."""
    import ast

    if not os.path.exists(file_path) or not file_path.endswith(".py"):
        return {"symbols": [], "calls": []}

    symbols = []
    calls = []

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()

        tree = ast.parse(code, filename=file_path)

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                doc = ast.get_docstring(node) or ""
                symbols.append({
                    "name": node.name,
                    "kind": "function",
                    "line": node.lineno,
                    "docstring": doc,
                    "file_path": file_path
                })
            elif isinstance(node, ast.ClassDef):
                doc = ast.get_docstring(node) or ""
                symbols.append({
                    "name": node.name,
                    "kind": "class",
                    "line": node.lineno,
                    "docstring": doc,
                    "file_path": file_path
                })
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        method_doc = ast.get_docstring(item) or ""
                        symbols.append({
                            "name": f"{node.name}.{item.name}",
                            "kind": "method",
                            "line": item.lineno,
                            "docstring": method_doc,
                            "file_path": file_path
                        })
            elif isinstance(node, ast.Call):
                call_name = ""
                if isinstance(node.func, ast.Name):
                    call_name = node.func.id
                elif isinstance(node.func, ast.Attribute):
                    call_name = node.func.attr
                if call_name:
                    calls.append({
                        "name": call_name,
                        "line": getattr(node, "lineno", 0),
                        "file_path": file_path
                    })

    except Exception:
        pass

    return {"symbols": symbols, "calls": calls}


def search_codebase_symbols(query: str, workspace_dir: Optional[str] = None) -> list:
    """Searches AST symbols across Python files in workspace_dir."""
    from src.core.history_manager import find_workspace_root
    if workspace_dir is None:
        workspace_dir = find_workspace_root()

    results = []
    query_lower = query.lower()
    exclude_dirs = {"venv", ".venv", "env", "node_modules", ".git", "build", "dist", "__pycache__"}

    for root, dirs, files in os.walk(workspace_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, workspace_dir).replace("\\", "/")
                ast_data = parse_python_ast(full_path)
                for sym in ast_data["symbols"]:
                    if query_lower in sym["name"].lower() or query_lower in sym["docstring"].lower():
                        sym_copy = dict(sym)
                        sym_copy["relative_path"] = rel_path
                        results.append(sym_copy)

    return results


def trace_symbol_callers(symbol_name: str, workspace_dir: Optional[str] = None) -> list:
    """Traces callers referencing symbol_name in Python files across workspace."""
    from src.core.history_manager import find_workspace_root
    if workspace_dir is None:
        workspace_dir = find_workspace_root()

    callers = []
    exclude_dirs = {"venv", ".venv", "env", "node_modules", ".git", "build", "dist", "__pycache__"}
    target = symbol_name.split(".")[-1]

    for root, dirs, files in os.walk(workspace_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, workspace_dir).replace("\\", "/")
                ast_data = parse_python_ast(full_path)
                for call in ast_data["calls"]:
                    if call["name"] == target:
                        callers.append({
                            "caller_file": rel_path,
                            "line": call["line"],
                            "target_symbol": symbol_name
                        })

    return callers


def trace_symbol_callees(symbol_name: str, workspace_dir: Optional[str] = None) -> list:
    """Traces symbols called inside a target function/method or class."""
    from src.core.history_manager import find_workspace_root
    if workspace_dir is None:
        workspace_dir = find_workspace_root()

    callees = []
    matches = search_codebase_symbols(symbol_name, workspace_dir=workspace_dir)
    if not matches:
        return callees

    target_match = matches[0]
    full_path = os.path.join(workspace_dir, target_match["relative_path"])
    ast_data = parse_python_ast(full_path)
    for call in ast_data["calls"]:
        callees.append({
            "callee_name": call["name"],
            "line": call["line"],
            "file_path": target_match["relative_path"]
        })

    return callees


def analyze_change_impact(target_symbol_or_file: str, workspace_dir: Optional[str] = None) -> dict:
    """Analyzes impact of modifying target_symbol_or_file, listing affected symbols and dependent files."""
    from src.core.history_manager import find_workspace_root
    if workspace_dir is None:
        workspace_dir = find_workspace_root()

    callers = trace_symbol_callers(target_symbol_or_file, workspace_dir=workspace_dir)
    affected_files = sorted(list(set(c["caller_file"] for c in callers)))

    return {
        "target": target_symbol_or_file,
        "caller_count": len(callers),
        "affected_files_count": len(affected_files),
        "affected_files": affected_files,
        "callers": callers,
        "impact_score": "HIGH" if len(affected_files) > 5 else "MEDIUM" if len(affected_files) > 0 else "LOW"
    }

