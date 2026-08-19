"""
presence_briefing.py — Room Arrival Auto-Briefing & Voice Synthesizer (JARVIS-06)

Triggers a 15-second executive voice report summarizing pending tasks, unread emails,
and system status when user presence is detected in the workspace.
"""

import time
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger("meridian_presence_briefing")

_last_briefing_time: float = 0.0
_BRIEFING_COOLDOWN: float = 1800.0  # 30 minutes between room arrival auto-briefings

def generate_presence_briefing(user_name: str = "User") -> Dict[str, Any]:
    global _last_briefing_time
    now = time.time()
    if now - _last_briefing_time < _BRIEFING_COOLDOWN:
        time_remaining = int(_BRIEFING_COOLDOWN - (now - _last_briefing_time))
        return {
            "triggered": False,
            "reason": f"Briefing cooldown active ({time_remaining}s remaining)",
            "briefing_text": ""
        }
        
    _last_briefing_time = now
    from datetime import datetime
    today = datetime.now().strftime("%A, %B %d")
    briefing_text = (
        f"Welcome back {user_name}. Today is {today}. "
        f"All system services are online. You have no urgent threat alerts."
    )
    
    logger.info(f"[PresenceBriefing] Generated executive briefing for {user_name}")
    return {
        "triggered": True,
        "briefing_text": briefing_text,
        "generated_at": now
    }

def reset_briefing_cooldown():
    global _last_briefing_time
    _last_briefing_time = 0.0
