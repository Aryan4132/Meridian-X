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

os.makedirs(DYNAMIC_TOOLS_DIR, exist_ok=True)

def create_dynamic_tool(tool_name: str, description: str, python_code: str, tier: int = 1) -> str:
    """Validates Python code via AST, writes file, and registers dynamic tool (AST-13)."""
    from src.tools.registry import register_dynamic_tool
    # 1. AST Syntax validation
    try:
        ast.parse(python_code)
    except SyntaxError as se:
        log_sensitive_action("SECURITY_VIOLATION", "dynamic_tool_syntax_error", {"tool_name": tool_name, "error": str(se)}, "FAILED")
        return f"Error: Provided Python code failed syntax validation: {se}"

    # 2. Persist tool code file
    tool_filename = f"{tool_name.lower().replace(' ', '_')}.py"
    file_path = os.path.join(DYNAMIC_TOOLS_DIR, tool_filename)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(python_code)

    # 3. Dynamic import & registration
    try:
        module_scope: Dict[str, Any] = {}
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

# Alias for registry compatibility
generate_dynamic_tool = create_dynamic_tool
