"""
dispatcher.py — Core notification & nudge dispatching pipeline for proactive intelligence.
"""

import os
import time
import asyncio
from datetime import datetime
from typing import Optional, List, Dict, Any

from src.core.bus import event_bus

# Main event loop reference for cross-thread event bus publishing
_main_loop: Optional[asyncio.AbstractEventLoop] = None


def set_main_event_loop(loop: asyncio.AbstractEventLoop):
    """Binds active FastAPI / main application event loop for proactive publishing."""
    global _main_loop
    _main_loop = loop


def get_main_event_loop() -> Optional[asyncio.AbstractEventLoop]:
    return _main_loop


def _now_str() -> str:
    return datetime.now().strftime("%H:%M:%S")


def publish_nudge_sync(
    nudge_type: str,
    title: str,
    message: str,
    action_hint: Optional[str] = None,
    icon: str = "💡",
    mascot_state: str = "default",
    action: Optional[str] = None,
    patch: Optional[Dict[str, Any]] = None
):
    """Thread-safe helper: schedule nudge publish onto running event loop."""
    import src.core.proactive as proactive
    # Suppress notifications if Game Mode is active, unless it is a game mode state update
    if getattr(proactive, "game_mode_active", False) and nudge_type != "game_mode_changed":
        print(f"[Proactive] Suppressed nudge '{title}' due to active Game Mode.")
        return

    payload: Dict[str, Any] = {
        "type": nudge_type,
        "title": title,
        "message": message,
        "action_hint": action_hint,
        "icon": icon,
        "timestamp": _now_str(),
        "id": f"nudge-{nudge_type}-{int(time.time())}",
        "mascot_state": mascot_state,
        "action": action
    }
    if patch:
        payload["patch"] = patch

    # Resolve target main loop first to avoid publishing onto disposable temporary loops
    target_loop = _main_loop
    if target_loop is None or target_loop.is_closed():
        try:
            target_loop = asyncio.get_running_loop()
        except RuntimeError:
            target_loop = None

    if target_loop and target_loop.is_running():
        asyncio.run_coroutine_threadsafe(
            event_bus.publish("proactive_nudge", payload), target_loop
        )
    else:
        print(f"[Proactive Nudge] ({title}): {message}")


def push_day8_context_nudge(
    nudge_type: str,
    title: str,
    message: str,
    icon: str = "💡",
    action: Optional[str] = None
) -> None:
    """Dispatches ambient context nudge (face, gesture, window, ambient audio) to UI."""
    import src.core.proactive as proactive
    proactive.publish_nudge_sync(
        nudge_type=nudge_type,
        title=title,
        message=message,
        icon=icon,
        action=action,
        mascot_state="alert" if nudge_type in ("wellbeing", "hitl_approval") else "default"
    )


async def push_proactive_nudge(
    nudge_type: str,
    title: str,
    message: str,
    actions: Optional[List[Any]] = None,
    icon: str = "💡"
) -> None:
    """Async wrapper for publishing proactive nudges."""
    import src.core.proactive as proactive
    proactive.publish_nudge_sync(nudge_type=nudge_type, title=title, message=message, icon=icon)


def dispatch_notification(
    title: str,
    message: str,
    priority: str = "medium",
    category: str = "general",
    action_hint: Optional[str] = None,
    mascot_state: str = "default"
) -> Dict[str, Any]:
    """Unified multi-channel proactive notification dispatcher (PL-28)."""
    import src.core.proactive as proactive
    icon_map = {
        "high": "🚨",
        "medium": "💡",
        "low": "ℹ️"
    }
    icon = icon_map.get(priority.lower(), "💡")

    proactive.publish_nudge_sync(
        nudge_type=f"notification_{category}",
        title=title,
        message=message,
        action_hint=action_hint,
        icon=icon,
        mascot_state=mascot_state
    )
    return {"status": "dispatched", "title": title, "priority": priority}


def on_terminal_crash(command: str, exit_code: int, stderr: str):
    """Proactive intervention trigger for terminal failures."""
    import src.core.proactive as proactive
    stderr_snippet = (stderr or "Unknown error")[:200]
    proactive.publish_nudge_sync(
        nudge_type="terminal_error",
        title="⚠️ Terminal Command Failed",
        message=f"Command '{command}' exited with code {exit_code}.\nError: {stderr_snippet}",
        action_hint="1-Click Auto Fix",
        icon="🛠️",
        mascot_state="worried",
        action="auto_fix_command"
    )


def on_user_motion_return():
    """Proactive intervention trigger when user returns to desk after away period."""
    import src.core.proactive as proactive
    proactive.publish_nudge_sync(
        nudge_type="presence_return",
        title="👋 Welcome Back!",
        message="You returned to your desk. Ready to resume session briefing or view pending task notifications?",
        action_hint="View Session Briefing",
        icon="👋",
        mascot_state="happy",
        action="view_briefing"
    )
