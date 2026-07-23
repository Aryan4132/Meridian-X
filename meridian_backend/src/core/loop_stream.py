"""
loop_stream.py — SSE Event Stream & Token Budget Sub-module
Formats Server-Sent Events (SSE), handles mid-stream cancellation signals,
and tracks token budget heuristics for context window management.
"""

import json
import asyncio
from typing import Dict, Any, Optional

# Global mid-stream cancellation flags: {session_id: cancel_requested_bool}
_cancel_signals: Dict[str, bool] = {}


def request_stream_cancellation(session_id: str) -> None:
    """Sets mid-stream cancel flag for the active session."""
    _cancel_signals[session_id] = True


def is_cancellation_requested(session_id: str) -> bool:
    """Checks if user requested stream cancellation."""
    return _cancel_signals.get(session_id, False)


def clear_cancellation_signal(session_id: str) -> None:
    """Clears cancel flag on session startup or completion."""
    _cancel_signals.pop(session_id, None)


def format_sse_event(event_type: str, data: Any) -> str:
    """Formats payload as standard Server-Sent Event string."""
    payload = json.dumps({"event": event_type, "data": data}, ensure_ascii=False)
    return f"data: {payload}\n\n"


def estimate_token_count(text: str) -> int:
    """Fast token heuristic (1 token ~ 4 characters)."""
    if not text:
        return 0
    return max(1, len(text) // 4)


def trim_history_to_token_budget(messages: list, max_tokens: int = 8000) -> list:
    """
    Trims conversation message history from the top (preserving system prompt)
    if estimated total tokens exceeds max_tokens budget.
    """
    if not messages:
        return messages

    system_msg = messages[0] if messages[0].get("role") == "system" else None
    working = messages[1:] if system_msg else list(messages)

    current_tokens = sum(estimate_token_count(m.get("content", "")) for m in messages)
    while current_tokens > max_tokens and len(working) > 2:
        # Drop oldest user/assistant pair
        working.pop(0)
        current_tokens = (estimate_token_count(system_msg.get("content", "")) if system_msg else 0) + sum(estimate_token_count(m.get("content", "")) for m in working)

    return ([system_msg] + working) if system_msg else working
