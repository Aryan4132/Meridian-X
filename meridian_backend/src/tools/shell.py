import os
import subprocess
import time
import ollama
from typing import List, Dict, Any
from src.core.audit_logger import log_sensitive_action
from database import get_ollama_client_host
from database import get_mongo_db

def _get_active_model() -> str:
    from database import get_brain_model
    return get_brain_model()

def nl_to_shell(natural_language: str) -> str:
    """Translate a natural language description into a valid Windows PowerShell command."""
    try:
        client = ollama.Client(host=get_ollama_client_host())
        prompt = (
            "You are a command-line translator. Translate the following plain-English command description "
            "into a single valid Windows PowerShell command line. Respond with ONLY the raw command string. "
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

def nl_run(natural_language: str) -> str:
    """Translate a natural language command and execute it on the host OS after verifying safety checks."""
    command = nl_to_shell(natural_language)
    if command.startswith("Error"):
        log_sensitive_action(
            category="SHELL_EXECUTION",
            action=natural_language,
            details={"error": command},
            status="FAILED"
        )
        return command
        
    # Check for destructive/critical commands in translated result
    cmd_lower = command.lower()
    dangerous_patterns = [
        "format", "remove-item", "rmdir", "del ", "stop-computer", "restart-computer", 
        "reg delete", "reg add", "net user", "net localgroup", "netsh firewall", 
        "kill ", "stop-process", "force", "recurse", "mkfs"
    ]
    blocked_patterns = [p for p in dangerous_patterns if p in cmd_lower]
    if blocked_patterns:
        log_sensitive_action(
            category="SHELL_EXECUTION",
            action=command,
            details={"natural_language": natural_language, "reason": f"Safety Gate blocked: {', '.join(blocked_patterns)}"},
            status="BLOCKED"
        )
        return (
            f"Blocked execution of translated command: '{command}'\n"
            f"Reason: Contains dangerous/destructive keywords: {', '.join(blocked_patterns)}.\n"
            f"Safety Gate blocked this operation. Refusing execution."
        )
        
    print(f"[NL Shell] Running translated command: '{command}'")
    try:
        # Run PowerShell command
        res = subprocess.run(
            ["powershell", "-Command", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        status = "SUCCESS" if res.returncode == 0 else "FAILED"
        log_sensitive_action(
            category="SHELL_EXECUTION",
            action=command,
            details={
                "natural_language": natural_language,
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
                
                prompt = (
                    f"You are a command line terminal self-healing assistant. A Windows PowerShell command just failed.\n"
                    f"Failed Command: {command}\n"
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
                        message=f"Command '{command[:30]}...' failed. Speculative fix generated.",
                        action_hint=f"Execute: {fix_command}",
                        icon="💻",
                        mascot_state="diagnostic",
                        action="run_repair",
                        patch={"file_path": "PowerShell", "proposed": fix_command, "original": command, "error_message": res.stderr}
                    )
                except Exception as ex:
                    print(f"[Terminal Self-Healing] Failed to dispatch nudge: {ex}")

        output = []
        if res.stdout.strip():
            output.append(f"STDOUT:\n{res.stdout}")
        if res.stderr.strip():
            output.append(f"STDERR:\n{res.stderr}")
            
        result = "\n".join(output) if output else "Command executed successfully with no console output."
        return f"Translated Command: {command}\n\nExecution Result:\n{result}"
    except Exception as e:
        log_sensitive_action(
            category="SHELL_EXECUTION",
            action=command,
            details={"natural_language": natural_language, "error": str(e)},
            status="FAILED"
        )
        return f"Failed to execute command '{command}': {e}"

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
    
    print(f"[Process Monitor] Running command: {command} for {duration_seconds}s...")
    try:
        proc = subprocess.Popen(
            ["powershell", "-Command", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        
        start_time = time.time()
        stdout_lines = []
        stderr_lines = []
        
        while time.time() - start_time < duration_seconds:
            ret = proc.poll()
            try:
                stdout, stderr = proc.communicate(timeout=0.5)
                if stdout:
                    stdout_lines.append(stdout)
                if stderr:
                    stderr_lines.append(stderr)
            except subprocess.TimeoutExpired:
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
                
        stdout, stderr = proc.communicate()
        if stdout:
            stdout_lines.append(stdout)
        if stderr:
            stderr_lines.append(stderr)
            
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

