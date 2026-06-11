import os
import ast
import re
import sys
from typing import Dict, Any, Optional

def get_ollama_client_host() -> str:
    host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
    if host == "0.0.0.0":
        return "http://127.0.0.1:11434"
    if host.startswith("0.0.0.0:"):
        return f"http://127.0.0.1:{host.split(':')[1]}"
    if "0.0.0.0" in host:
        return host.replace("0.0.0.0", "127.0.0.1")
    if not host.startswith("http://") and not host.startswith("https://"):
        return f"http://{host}"
    return host

def audit_code_safety(code: str) -> tuple[bool, str]:
    """
    Checks if the code contains dangerous commands, imports, or file operations.
    Returns (is_safe, reason).
    """
    # Parse code into AST to inspect imports
    try:
        root = ast.parse(code)
    except Exception as e:
        return False, f"AST parsing failed: {e}"

    dangerous_modules = {"subprocess", "shutil", "socket", "urllib.request"}
    
    for node in ast.walk(root):
        # Check imports (e.g. import subprocess)
        if isinstance(node, ast.Import):
            for name in node.names:
                if name.name.split('.')[0] in dangerous_modules:
                    return False, f"Importing dangerous module: {name.name}"
        # Check from imports (e.g. from subprocess import Popen)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split('.')[0] in dangerous_modules:
                return False, f"Importing from dangerous module: {node.module}"
        # Check calls (e.g. eval, exec, os.system, os.popen)
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id in {"eval", "exec"}:
                    return False, f"Use of dangerous built-in: {node.func.id}"
            elif isinstance(node.func, ast.Attribute):
                if isinstance(node.func.value, ast.Name):
                    if node.func.value.id == "os" and node.func.attr in {"system", "popen"}:
                        return False, f"Use of dangerous system call: os.{node.func.attr}"

    # Secondary regex check for explicit dangerous tokens in strings/comments
    dangerous_patterns = [
        r"rmdir\s+/s", r"rm\s+-rf", r"format\s+[a-zA-Z]:", r"ctypes\.windll\.kernel32"
    ]
    for pattern in dangerous_patterns:
        if re.search(pattern, code, re.IGNORECASE):
            return False, f"Dangerous command pattern matched: {pattern}"

    return True, "Code passed security audit checks."

def extract_python_code(text: str) -> str:
    """Extracts python code blocks from markdown."""
    pattern = r"```python\n(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # Fallback to general block
    pattern_general = r"```\n(.*?)```"
    match_gen = re.search(pattern_general, text, re.DOTALL)
    if match_gen:
        return match_gen.group(1).strip()
        
    return text.strip()

def generate_dynamic_tool(prompt: str) -> str:
    """
    Generates a Python tool based on user prompt, audits it, 
    self-heals if necessary, and registers it dynamically.
    """
    import ollama
    
    # 1. Prepare system instruction and prompt
    system_prompt = (
        "You are the Meridian-X Developer Agent. Generate a single Python tool function that fulfills the user's request.\n"
        "Rules:\n"
        "1. Write the code inside a standard ```python markdown code block.\n"
        "2. Include a clear docstring, type hints, and return a descriptive string output.\n"
        "3. Use standard libraries, or already imported modules like pyautogui, numpy, sounddevice, scipy, requests.\n"
        "4. DO NOT import or use subprocess, shutil, eval, exec, or raw sockets for safety reasons.\n"
        "5. The function name should be descriptive and lowercase (e.g. custom_volume_control).\n"
        "6. Do not include any test executions or main blocks. Only define the function."
    )
    
    client = ollama.Client(host=get_ollama_client_host())
    model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
    
    code = ""
    error_msg = ""
    attempts = 3
    
    for attempt in range(attempts):
        user_prompt = prompt
        if error_msg:
            user_prompt += f"\n\nCorrection required due to error:\n{error_msg}\nPlease fix the error and output only the corrected function code."
            
        print(f"[Dynamic Skill] Querying model (attempt {attempt+1}/{attempts})...")
        try:
            res = client.chat(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            raw_text = res.message.content
            code = extract_python_code(raw_text)
            
            # Syntax verification
            compile(code, "<string>", "exec")
            
            # Security check
            is_safe, reason = audit_code_safety(code)
            if not is_safe:
                error_msg = f"Security Audit Failed: {reason}"
                continue
                
            # If compile and safety check passed, break out of loop
            error_msg = ""
            break
        except Exception as ce:
            error_msg = f"Syntax Compilation Error: {ce}"
            continue

    if error_msg:
        return f"Failed to generate a valid dynamic tool after {attempts} attempts. Last error: {error_msg}"

    # Extract function name from code to save as plugin name
    # e.g., 'def custom_volume_control('
    match = re.search(r"def\s+(\w+)\(", code)
    if match:
        tool_name = match.group(1)
    else:
        # Generate generic name
        tool_name = f"dynamic_tool_{int(time.time())}"

    # 2. Save code as dynamic plugin file
    try:
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # src/tools -> src -> backend -> root
        root_dir = os.path.dirname(backend_dir)
        plugins_dir = os.path.join(root_dir, "plugins")
        os.makedirs(plugins_dir, exist_ok=True)
        
        plugin_path = os.path.join(plugins_dir, f"{tool_name}.py")
        
        # Write to dynamic plugins folder with TIER = 2 (User approval on execution)
        with open(plugin_path, "w", encoding="utf-8") as f:
            f.write(f"TIER = 2\n\n{code}\n")
            
        # Trigger reload of plugins
        from src.tools.registry import reload_plugins_wrapper
        reload_msg = reload_plugins_wrapper()
        
        return (
            f"Successfully generated, audited, and registered dynamic tool '{tool_name}'!\n"
            f"Save Path: {plugin_path}\n"
            f"Registry Reload: {reload_msg}\n\n"
            f"Generated Code:\n```python\n{code}\n```"
        )
    except Exception as e:
        return f"Failed to register dynamic tool: {e}"
