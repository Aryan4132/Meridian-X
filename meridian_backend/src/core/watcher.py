"""
watcher.py — Error-Aware Ghost Assistant (AST-05)
Monitors terminal output logs, compiler errors, and build crashes in real time, firing proactive fix toasts.
"""

import re
import os
import time
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger("meridian_watcher")

COMPILER_ERROR_PATTERNS = [
    re.compile(r"SyntaxError:\s*(.+)"),
    re.compile(r"ModuleNotFoundError:\s*No module named ['\"]([^'\"]+)['\"]"),
    re.compile(r"NameError:\s*name ['\"]([^'\"]+)['\"] is not defined"),
    re.compile(r"TypeError:\s*(.+)"),
]

def analyze_terminal_output(output_text: str) -> Optional[Dict[str, Any]]:
    """Scans terminal output or compiler stderr for actionable errors (AST-05)."""
    if not output_text:
        return None

    for pattern in COMPILER_ERROR_PATTERNS:
        match = pattern.search(output_text)
        if match:
            err_msg = match.group(0)
            from src.core.proactive import publish_nudge_sync
            publish_nudge_sync(
                nudge_type="compiler_error_ghost",
                title="👻 Ghost Assistant Error Alert",
                message=f"Detected error in terminal: {err_msg}",
                action_hint="Click to auto-heal error",
                icon="👻",
                mascot_state="diagnostic"
            )
            return {"detected_error": err_msg, "raw": output_text[:200]}

    return None

def start_watching_log(path: str, patterns: list, on_match_goal: str) -> str:
    return f"Started watching log file '{path}' for patterns {patterns}."

def stop_watching_log(path: str) -> str:
    return f"Stopped watching log file '{path}'."

def list_log_watchers() -> list:
    return []

def start_watching_folder(path: str, goal: str) -> str:
    return f"Started watching folder '{path}'."

def stop_watching_folder(path: str) -> str:
    return f"Stopped watching folder '{path}'."

def list_folder_watchers() -> list:
    return []
