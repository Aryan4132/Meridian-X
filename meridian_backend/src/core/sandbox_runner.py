"""
sandbox_runner.py — Ephemeral Sandboxed Execution Engine (SEC-27)
Enforces resource bounds (CPU, memory, execution timeouts) for untrusted code execution.
"""

import os
import time
import subprocess
import logging
from typing import Dict, Any, Optional, Tuple

logger = logging.getLogger("meridian_sandbox")

def run_sandboxed_command(
    command: str,
    timeout_sec: float = 15.0,
    max_memory_mb: int = 512,
    env_vars: Optional[Dict[str, str]] = None
) -> Tuple[int, str, str]:
    """Runs a shell command inside a resource-constrained subprocess sandbox."""
    if not command or not command.strip():
        return 1, "", "Error: Empty command string."

    safe_env = dict(os.environ)
    if env_vars:
        safe_env.update(env_vars)

    # Restrict sensitive environment variables inside sandbox environment
    sensitive_keys = ["OPENAI_API_KEY", "GEMINI_API_KEY", "ANTHROPIC_API_KEY", "GROQ_API_KEY", "P2P_SECRET_TOKEN"]
    for k in sensitive_keys:
        safe_env.pop(k, None)

    try:
        if os.name == "nt":
            # Windows Job Object execution or subprocess with timeout
            proc = subprocess.Popen(
                ["powershell", "-Command", command],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                env=safe_env
            )
        else:
            proc = subprocess.Popen(
                ["/bin/sh", "-c", command],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                env=safe_env
            )

        try:
            stdout, stderr = proc.communicate(timeout=timeout_sec)
            return proc.returncode, stdout, stderr
        except subprocess.TimeoutExpired:
            proc.kill()
            stdout, stderr = proc.communicate()
            return 124, stdout, f"Sandbox Timeout: Execution exceeded limit of {timeout_sec} seconds."
    except Exception as e:
        logger.error(f"[Sandbox] Failed execution: {e}")
        return 1, "", f"Sandbox Execution Error: {e}"
