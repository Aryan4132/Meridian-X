"""
confirmations.py — Human-in-the-loop approval gates and safety confirmations for agent tool executions.
"""

import os
import asyncio
from typing import Dict, Any, Tuple, Optional

active_confirmations: Dict[str, Any] = {}
_confirmations_lock: asyncio.Lock = asyncio.Lock()


def get_confirmations_lock() -> asyncio.Lock:
    return _confirmations_lock


async def register_confirmation(conf_id: str, conf_event: asyncio.Event) -> None:
    async with get_confirmations_lock():
        active_confirmations[conf_id] = {
            "event": conf_event,
            "approved": False
        }


async def approve_confirmation(conf_id: str, approved: bool) -> bool:
    async with get_confirmations_lock():
        if conf_id in active_confirmations:
            active_confirmations[conf_id]["approved"] = approved
            active_confirmations[conf_id]["event"].set()
            return True
        return False


async def pop_confirmation(conf_id: str) -> bool:
    async with get_confirmations_lock():
        conf_data = active_confirmations.pop(conf_id, {})
        return conf_data.get("approved", False)


def check_approval_gate(tool_name: str, kwargs: Optional[Dict[str, Any]] = None, **extra: Any) -> Tuple[bool, str]:
    """Evaluates whether a tool execution requires human approval gate (PL-12)."""
    args_map = dict(kwargs or {})
    args_map.update(extra)

    # Check force flag or env override or Level 0 Unrestricted Mode
    if args_map.get("force") or args_map.get("bypass_guard") or os.getenv("MERIDIAN_DISABLE_SYSTEM_GUARD") == "1":
        return False, ""

    try:
        from database import get_unrestricted_pc_access
        if get_unrestricted_pc_access():
            return False, ""
    except Exception:
        pass

    if tool_name in ("delete_file", "db_execute", "kill_process"):
        return True, f"Action '{tool_name}' requires explicit user confirmation."

    if tool_name in ("run_command", "nl_run", "shell", "terminal", "nl_to_shell"):
        cmd = str(args_map.get("command", "") or args_map.get("cmd", "") or args_map.get("natural_language", "")).lower()
        dangerous = ["rm ", "rmdir", "format ", "drop ", "del /", "kill ", "sudo "]
        if any(d in cmd for d in dangerous):
            return True, f"Potentially dangerous command detected ('{cmd}'). Explicit confirmation required."
    return False, ""
