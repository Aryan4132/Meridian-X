"""
presence_briefing.py — Executive Room Arrival Briefing Engine (JARVIS-06)
"""

import time
import logging
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)

class PresenceBriefingEngine:
    """Generates 15-second room entry executive voice reports."""

    def __init__(self):
        self._last_briefing_time: float = 0.0
        self._briefing_cooldown: float = 300.0  # 5 minutes

    def generate_presence_briefing(self, user_name: Optional[str] = "User", context_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        name = user_name or "User"
        ctx = context_data or {}

        schedule_summary = ctx.get("schedule", "2 upcoming meetings today")
        unread_alerts = ctx.get("unread_alerts", 3)
        weather = ctx.get("weather", "72°F and clear")
        system_status = ctx.get("system_status", "All systems operational")

        briefing_text = (
            f"Good arrival, {name}. Weather is {weather}. "
            f"You have {unread_alerts} priority notifications and {schedule_summary}. "
            f"System status: {system_status}."
        )

        now = time.time()
        self._last_briefing_time = now

        return {
            "user_name": name,
            "briefing": briefing_text,
            "duration_seconds": 15,
            "timestamp": now,
            "tts_payload": {
                "text": briefing_text,
                "voice": "en-US-Neural2-F",
                "speed": 1.1,
            },
            "metrics": {
                "unread_alerts": unread_alerts,
                "weather": weather,
                "schedule": schedule_summary,
            },
        }

    def trigger_room_entry_briefing(self, user_name: str = "User") -> Dict[str, Any]:
        now = time.time()
        if now - self._last_briefing_time < self._briefing_cooldown:
            return {"status": "skipped", "reason": "cooldown_active", "seconds_remaining": int(self._briefing_cooldown - (now - self._last_briefing_time))}

        briefing = self.generate_presence_briefing(user_name)
        return {"status": "triggered", "briefing": briefing}

# Global instance
_briefing_engine = PresenceBriefingEngine()

def generate_presence_briefing(user_name: Optional[str] = "User", context_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return _briefing_engine.generate_presence_briefing(user_name, context_data)

def trigger_room_entry_briefing(user_name: str = "User") -> Dict[str, Any]:
    return _briefing_engine.trigger_room_entry_briefing(user_name)
