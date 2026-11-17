"""
butler_ritual.py — Executive Morning & Evening Ritual Protocol (BUTLER-28)

Orchestrates automated wake/sleep routines, light sync, ambient soundscapes,
and context-aware outfit recommendations for executive workflows.
"""

import time
import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

@dataclass
class RitualConfig:
    wake_time: str = "07:00"
    sleep_time: str = "23:00"
    morning_soundscape: str = "sunrise_acoustic"
    evening_soundscape: str = "rain_and_fireplace"
    morning_lighting: str = "daylight_focus_5500k"
    evening_lighting: str = "warm_ember_2200k"
    auto_briefing_enabled: bool = True
    outfit_advisor_enabled: bool = True

class ButlerRitualEngine:
    """Manages high-tier executive morning and evening daily rituals."""

    def __init__(self, config: Optional[RitualConfig] = None):
        self.config = config or RitualConfig()
        self._history: List[Dict[str, Any]] = []

    def execute_morning_ritual(
        self,
        user_name: str = "User",
        weather_data: Optional[Dict[str, Any]] = None,
        calendar_events: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """Runs the morning wake-up ritual with lighting, soundscape, schedule, and outfit advice."""
        weather = weather_data or {"temp_c": 21, "condition": "Clear", "rain_prob": 0.1}
        events = calendar_events or []

        outfit = self.recommend_outfit(weather, events)

        ritual_payload = {
            "ritual_type": "morning_executive",
            "timestamp": time.time(),
            "user": user_name,
            "lighting_preset": self.config.morning_lighting,
            "soundscape": self.config.morning_soundscape,
            "outfit_recommendation": outfit,
            "agenda_count": len(events),
            "status": "completed",
            "speech_summary": (
                f"Good morning, {user_name}. Lights adjusted to {self.config.morning_lighting}. "
                f"Weather is {weather.get('condition', 'clear')} at {weather.get('temp_c', 20)}°C. "
                f"Recommended attire: {outfit['summary']}. You have {len(events)} calendar commitments today."
            )
        }
        self._history.append(ritual_payload)
        logger.info(f"[ButlerRitual] Executed morning ritual for {user_name}")
        return ritual_payload

    def execute_evening_ritual(
        self,
        user_name: str = "User",
        completed_tasks: Optional[List[str]] = None,
        uncompleted_tasks: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Runs evening wind-down ritual with warm lighting, sleep soundscape, and day recap."""
        completed = completed_tasks or []
        remaining = uncompleted_tasks or []

        ritual_payload = {
            "ritual_type": "evening_wind_down",
            "timestamp": time.time(),
            "user": user_name,
            "lighting_preset": self.config.evening_lighting,
            "soundscape": self.config.evening_soundscape,
            "completed_tasks_count": len(completed),
            "deferred_tasks_count": len(remaining),
            "status": "completed",
            "speech_summary": (
                f"Good evening, {user_name}. Shifting environment to {self.config.evening_lighting} "
                f"with {self.config.evening_soundscape}. You completed {len(completed)} tasks today. "
                f"Workstation locked and ready for rest."
            )
        }
        self._history.append(ritual_payload)
        logger.info(f"[ButlerRitual] Executed evening ritual for {user_name}")
        return ritual_payload

    def recommend_outfit(self, weather: Dict[str, Any], events: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Provides context-aware attire advice based on weather and meeting formality."""
        temp = weather.get("temp_c", 20)
        condition = weather.get("condition", "").lower()
        rain_prob = weather.get("rain_prob", 0.0)

        is_formal = any(
            "client" in e.get("title", "").lower() or "exec" in e.get("title", "").lower() or "board" in e.get("title", "").lower()
            for e in events
        )

        layers = []
        if temp < 12:
            layers.append("wool coat or heavy tailored jacket")
        elif temp < 20:
            layers.append("merino knitwear or tailored blazer")
        else:
            layers.append("breathable linen or crisp cotton shirt")

        if rain_prob > 0.4 or "rain" in condition:
            layers.append("water-repellent trench and compact umbrella")

        formality = "Executive Business Formal" if is_formal else "Smart Casual Minimalist"
        summary = f"{formality} — {', '.join(layers)}"

        return {
            "formality": formality,
            "recommended_layers": layers,
            "rain_caution": rain_prob > 0.3 or "rain" in condition,
            "summary": summary
        }

    def get_ritual_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        return self._history[-limit:]

# Global engine singleton
butler_ritual_engine = ButlerRitualEngine()

def run_morning_ritual(user_name: str = "User", weather: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return butler_ritual_engine.execute_morning_ritual(user_name=user_name, weather_data=weather)

def run_evening_ritual(user_name: str = "User") -> Dict[str, Any]:
    return butler_ritual_engine.execute_evening_ritual(user_name=user_name)

