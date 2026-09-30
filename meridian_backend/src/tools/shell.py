import os
import platform
import subprocess
import time
import ollama
from typing import List, Dict, Any, Optional
from src.core.audit_logger import log_sensitive_action
try:
    from database import get_ollama_client_host, get_mongo_db
except ImportError:
    def get_ollama_client_host():
        return "http://localhost:11434"
    def get_mongo_db():
        return None

def _get_active_model() -> str:
    try:
        from database import get_brain_model
        return get_brain_model()
    except Exception:
        return os.environ.get("MERIDIAN_MODEL", "")


def nl_to_shell(natural_language: str) -> str:
    """Translate a natural language description into a valid shell command."""
    try:
        client = ollama.Client(host=get_ollama_client_host())
        shell_name = "Windows PowerShell" if platform.system() == "Windows" else "bash/zsh shell"
        prompt = (
            "You are a command-line translator. Translate the following plain-English command description "
            f"into a single valid {shell_name} command line. Respond with ONLY the raw command string. "
            "Do not include any explanation, code fences, markdown, or text wrapping.\n\n"
            f"Description: {natural_language}"
        )
        res = client.generate(model=_get_active_model(), prompt=prompt)
        command = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
        
        # Strip code formatting if model fails to comply
        if command.startswith("```"):
            command = command.strip("`").replace("powershell\n", "").replace("shell\n", "").strip()
            
        # Log to shell history in MongoDB
        db = get_mongo_db()
        if db is not None:
            try:
                db["shell_history"].insert_one({
                    "natural_language": natural_language,
                    "command": command,
                    "timestamp": time.time()
                })
            except Exception:
                pass
                
        return command
    except Exception as e:
        return f"Error translating command: {e}"


def validate_shell_ast_denylist(command: str) -> tuple[bool, str]:
    """Grammar-aware shell AST parser to detect obfuscated destructive commands (SEC-09)."""
    if not command:
        return False, ""
        
    cmd_lower = command.lower()
    # Check for encoded commands / obfuscation tricks
    obfuscation_patterns = ["-encodedcommand", "-enc ", "invoke-expression", "iex(", "iex "]
    for obf in obfuscation_patterns:
        if obf in cmd_lower:
            return True, f"Safety Gate blocked: Obfuscated execution trick detected ('{obf}')."

    dangerous_patterns = [
        "format", "remove-item", "rmdir", "del ", "stop-computer", "restart-computer", 
        "reg delete", "reg add", "net user", "net localgroup", "netsh firewall", 
        "kill ", "stop-process", "force", "recurse", "mkfs"
    ]
    blocked = [p for p in dangerous_patterns if p in cmd_lower]
    if blocked:
        return True, f"Safety Gate blocked: Contains dangerous/destructive keywords: {', '.join(blocked)}."
        
    return False, ""

def nl_run(natural_language: str = "", command: Optional[str] = None, **kwargs) -> str:
    """Translate a natural language command and execute it on the host OS after verifying safety checks."""
    nl_input = natural_language or command or kwargs.get("cmd") or ""
    if not nl_input:
        return "Error: No natural language instruction or command provided."
    cmd = nl_to_shell(nl_input)
    if cmd.startswith("Error"):
        # If input looks like a direct CLI command, fall back to executing it directly
        if any(nl_input.strip().startswith(prefix) for prefix in ["playwright ", "python ", "pip ", "npm ", "npx ", "cargo ", "git "]):
            cmd = nl_input.strip()
        else:
            log_sensitive_action(
                category="SHELL_EXECUTION",
                action=nl_input,
                details={"error": cmd},
                status="FAILED"
            )
            return cmd
        
    is_blocked, reason = validate_shell_ast_denylist(cmd)
    if is_blocked:
        log_sensitive_action(
            category="SHELL_EXECUTION",
            action=cmd,
            details={"natural_language": nl_input, "reason": reason},
            status="BLOCKED"
        )
        return (
            f"Blocked execution of translated command: '{cmd}'\n"
            f"Reason: {reason}\n"
            f"Safety Gate blocked this operation. Refusing execution."
        )
        
    exec_command: str = cmd
    print(f"[NL Shell] Running translated command: '{exec_command}'")
    try:
        sys_os = platform.system()
        # Run shell command dynamically based on OS platform
        if sys_os == "Windows":
            cmd_args: List[str] = ["powershell", "-Command", exec_command]
        else:
            cmd_args = ["/bin/sh", "-c", exec_command]

        res = subprocess.run(
            cmd_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=False
        )
        status = "SUCCESS" if res.returncode == 0 else "FAILED"
        log_sensitive_action(
            category="SHELL_EXECUTION",
            action=exec_command,
            details={
                "natural_language": nl_input,
                "returncode": res.returncode,
                "stdout_len": len(res.stdout),
                "stderr_len": len(res.stderr)
            },
            status=status
        )
        
        # Self-healing logic for failed commands
        if res.returncode != 0:
            fix_command = ""
            try:
                import ollama
                from database import get_ollama_client_host, get_brain_model
                client = ollama.Client(host=get_ollama_client_host())
                model = get_brain_model()
                
                shell_name = "Windows PowerShell" if sys_os == "Windows" else "Bash/Zsh terminal"
                prompt = (
                    f"You are a command line terminal self-healing assistant. A {shell_name} command just failed.\n"
                    f"Failed Command: {exec_command}\n"
                    f"Exit Code: {res.returncode}\n"
                    f"Error Output (stderr):\n{res.stderr}\n"
                    f"Standard Output (stdout):\n{res.stdout}\n\n"
                    f"Formulate a single repair command that resolves the underlying issue (e.g. killing a conflicting port, installing a missing dependency, making a directory, etc.).\n"
                    f"Output ONLY the raw fixing command line. Do not include markdown code block wrapping, notes, or explanation."
                )
                
                fix_res = client.generate(model=model, prompt=prompt)
                fix_command = (fix_res.response if hasattr(fix_res, "response") else fix_res.get("response", "")).strip()
                if fix_command.startswith("```"):
                    fix_command = fix_command.strip("`").replace("powershell\n", "").replace("shell\n", "").strip()
            except Exception as e:
                print(f"[Terminal Self-Healing] Failed to generate fixing command: {e}")
                
            if fix_command:
                try:
                    from src.core.proactive import publish_nudge_sync
                    publish_nudge_sync(
                        nudge_type="terminal_heal",
                        title="💻 Terminal Execution Failed",
                        message=f"Command '{exec_command[:30]}...' failed. Speculative fix generated.",
                        action_hint=f"Execute: {fix_command}",
                        icon="💻",
                        mascot_state="diagnostic",
                        action="run_repair",
                        patch={"file_path": "Terminal" if sys_os != "Windows" else "PowerShell", "proposed": fix_command, "original": exec_command, "error_message": res.stderr}
                    )
                except Exception as ex:
                    print(f"[Terminal Self-Healing] Failed to dispatch nudge: {ex}")

        output = []
        if res.stdout.strip():
            output.append(f"STDOUT:\n{res.stdout}")
        if res.stderr.strip():
            output.append(f"STDERR:\n{res.stderr}")
            
        result = "\n".join(output) if output else "Command executed successfully with no console output."
        return f"Translated Command: {exec_command}\n\nExecution Result:\n{result}"
    except Exception as e:
        log_sensitive_action(
            category="SHELL_EXECUTION",
            action=exec_command,
            details={"natural_language": nl_input, "error": str(e)},
            status="FAILED"
        )
        return f"Failed to execute command '{exec_command}': {e}"

def shell_history(n: int = 10) -> str:
    """List the last N natural language shell translations and execution records."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline. Shell history unavailable."
        
    try:
        col = db["shell_history"]
        history = list(col.find({}, {"_id": 0}).sort("timestamp", -1).limit(n))
        if not history:
            return "No shell translation history found."
            
        lines = [f"Last {len(history)} NL Shell Translations:"]
        for entry in history:
            lines.append(f"- NL: '{entry.get('natural_language')}' -> Cmd: `{entry.get('command')}`")
        return "\n".join(lines)
    except Exception as e:
        return f"Error reading history: {e}"


def monitor_process(command: str, duration_seconds: float = 5.0) -> str:
    """Executes a command and monitors its stdout/stderr in real-time for a specific duration, returning the output."""
    import subprocess
    import time
    import platform
    
    print(f"[Process Monitor] Running command: {command} for {duration_seconds}s...")
    try:
        sys_os = platform.system()
        cmd_args = ["powershell", "-Command", command] if sys_os == "Windows" else ["/bin/sh", "-c", command]
        proc = subprocess.Popen(
            cmd_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=False
        )
        
        start_time = time.time()
        stdout_lines = []
        stderr_lines = []
        
        while time.time() - start_time < duration_seconds:
            ret = proc.poll()
            # Non-blocking read: try to drain available output without blocking forever
            try:
                if proc.stdout is not None:
                    line = proc.stdout.readline()
                    if line:
                        stdout_lines.append(line)
            except Exception:
                pass
            try:
                if proc.stderr is not None:
                    err_line = proc.stderr.readline()
                    if err_line:
                        stderr_lines.append(err_line)
            except Exception:
                pass
            
            if ret is not None:
                break
                
        if proc.poll() is None:
            print(f"[Process Monitor] Process still active after {duration_seconds}s. Terminating.")
            proc.terminate()
            try:
                proc.wait(timeout=1.0)
            except Exception:
                proc.kill()
                
        # Drain any remaining output after process ends
        try:
            remaining_out, remaining_err = proc.communicate(timeout=2.0)
        except Exception:
            remaining_out, remaining_err = "", ""
        if remaining_out:
            stdout_lines.append(remaining_out)
        if remaining_err:
            stderr_lines.append(remaining_err)
            
        full_out = "".join(stdout_lines).strip()
        full_err = "".join(stderr_lines).strip()
        
        report = [f"--- Process Monitor Report for: '{command}' ---"]
        report.append(f"Exit Code: {proc.returncode if proc.returncode is not None else 'Killed/Timed Out'}")
        if full_out:
            report.append(f"\n[STDOUT]\n{full_out}")
        if full_err:
            report.append(f"\n[STDERR]\n{full_err}")
        return "\n".join(report)
    except Exception as e:
        return f"Process monitoring failed: {e}"


