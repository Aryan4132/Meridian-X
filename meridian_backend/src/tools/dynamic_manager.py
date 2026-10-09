"""
dynamic_manager.py — Natural Language Tool Auto-Creator Engine (AST-13)
Enables Meridian-X to write, validate, and safely hot-reload new Python tools at runtime.
"""

import ast
import os
import sys
import logging
from typing import Dict, Any, Optional
from src.core.audit_logger import log_sensitive_action

logger = logging.getLogger("meridian_dynamic_tools")
DYNAMIC_TOOLS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dynamic_tools")


FORBIDDEN_CALLS = {"eval", "exec", "__import__", "compile"}
FORBIDDEN_MODULES = {"subprocess", "socket", "ctypes", "pty", "posix", "nt"}
FORBIDDEN_ATTRS = {"__subclasses__", "__globals__", "__code__", "__closure__", "__bases__"}


def _validate_ast_safety(tree: ast.AST) -> Optional[str]:
    """Inspects AST nodes for dangerous builtins, unsafe imports, and dunder attributes."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in FORBIDDEN_CALLS:
                return f"Disallowed call to '{node.func.id}' in dynamic tool code."
        elif isinstance(node, ast.Import):
            for alias in node.names:
                root_pkg = alias.name.split(".")[0]
                if root_pkg in FORBIDDEN_MODULES:
                    return f"Disallowed module import '{alias.name}' in dynamic tool code."
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                root_pkg = node.module.split(".")[0]
                if root_pkg in FORBIDDEN_MODULES:
                    return f"Disallowed module import '{node.module}' in dynamic tool code."
        elif isinstance(node, ast.Attribute):
            if node.attr in FORBIDDEN_ATTRS:
                return f"Disallowed attribute access '{node.attr}' in dynamic tool code."
    return None


def _ensure_dynamic_tools_dir() -> None:
    os.makedirs(DYNAMIC_TOOLS_DIR, exist_ok=True)

def create_dynamic_tool(tool_name: str, description: str, python_code: str, tier: int = 1) -> str:
    """Validates Python code via AST, writes file, and registers dynamic tool (AST-13)."""
    _ensure_dynamic_tools_dir()
    from src.tools.registry import register_dynamic_tool
    # 1. AST Syntax validation and security check
    try:
        parsed_tree = ast.parse(python_code)
    except SyntaxError as se:
        log_sensitive_action("SECURITY_VIOLATION", "dynamic_tool_syntax_error", {"tool_name": tool_name, "error": str(se)}, "FAILED")
        return f"Error: Provided Python code failed syntax validation: {se}"

    sec_err = _validate_ast_safety(parsed_tree)
    if sec_err:
        log_sensitive_action("SECURITY_VIOLATION", "dynamic_tool_security_violation", {"tool_name": tool_name, "error": sec_err}, "FAILED")
        return f"Error: Security policy violation in dynamic tool: {sec_err}"

    # 2. Persist tool code file
    tool_filename = f"{tool_name.lower().replace(' ', '_')}.py"
    file_path = os.path.join(DYNAMIC_TOOLS_DIR, tool_filename)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(python_code)

    # 3. Dynamic import & registration with restricted scope
    try:
        import builtins
        safe_builtins = {
            k: getattr(builtins, k)
            for k in dir(builtins)
            if k not in FORBIDDEN_CALLS
        }
        module_scope: Dict[str, Any] = {"__builtins__": safe_builtins}
        exec(python_code, module_scope)
        
        func_to_register = None
        for key, val in module_scope.items():
            if callable(val) and not key.startswith("_"):
                func_to_register = val
                break

        if not func_to_register:
            return f"Error: No callable function found in provided code for tool '{tool_name}'."

        register_dynamic_tool(
            name=tool_name,
            func=func_to_register,
            description=description,
            tier=tier
        )

        log_sensitive_action("DYNAMIC_TOOL_CREATED", tool_name, {"file_path": file_path, "tier": tier}, "SUCCESS")
        return f"Successfully created and registered dynamic tool '{tool_name}' (Tier {tier})."
    except Exception as e:
        log_sensitive_action("DYNAMIC_TOOL_FAILED", tool_name, {"error": str(e)}, "FAILED")
        return f"Failed to register dynamic tool '{tool_name}': {e}"

def generate_dynamic_tool(prompt: str, description: Optional[str] = None, python_code: Optional[str] = None, tier: int = 1) -> str:
    """Auto-synthesizes tool metadata and registers dynamic tool."""
    tool_name = prompt.strip().replace(" ", "_").lower()
    desc = description or f"Auto-generated tool from prompt: {prompt}"
    code = python_code or f"def {tool_name}():\n    '''{desc}'''\n    return 'Executed {tool_name}'\n"
    return create_dynamic_tool(tool_name, desc, code, tier=tier)

