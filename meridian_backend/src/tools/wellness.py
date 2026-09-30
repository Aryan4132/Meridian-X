"""
wellness.py — Wellness & Ergonomics Butler (BUTLER-03)
Manages posture reminders, 20-20-20 eye strain alerts, hydration tracking, and daily wellness scoring.
"""

import time
from typing import Dict, Any

_wellness_state: Dict[str, Any] = {
    "hydration_ml": 1250,
    "hydration_target_ml": 2500,
    "stretches_completed": 3,
    "eye_breaks_completed": 4,
    "last_break_timestamp": time.time() - 1800
}

def track_hydration(amount_ml: int = 250) -> str:
    """Logs consumed water volume and returns remaining daily intake target."""
    global _wellness_state
    _wellness_state["hydration_ml"] += amount_ml
    curr = _wellness_state["hydration_ml"]
    target = _wellness_state["hydration_target_ml"]
    pct = min(100, int((curr / target) * 100))
    return f"Logged {amount_ml}ml water. Daily hydration: {curr}/{target} ml ({pct}% of goal)."

def trigger_ergonomic_break(break_type: str = "eye_strain") -> str:
    """Triggers an ergonomic break reminder (eye_strain 20-20-20, posture_check, stretch_break)."""
    global _wellness_state
    btype = break_type.lower().strip()
    _wellness_state["last_break_timestamp"] = time.time()

    if btype in ("eye_strain", "eye", "20-20-20"):
        _wellness_state["eye_breaks_completed"] += 1
        return "20-20-20 Eye Strain Break: Look at an object 20 feet away for 20 seconds to relax ciliary eye muscles."
    elif btype in ("posture", "posture_check"):
        _wellness_state["stretches_completed"] += 1
        return "Posture Check: Pull shoulders back, align spine vertically, uncross legs, and adjust monitor level."
    else:
        _wellness_state["stretches_completed"] += 1
        return "Stretch Break: Stand up, stretch back and neck, take 3 deep breaths, and walk for 60 seconds."

def calculate_daily_wellness_score() -> Dict[str, Any]:
    """Computes daily holistic wellness score (0-100) based on hydration, breaks, and health metrics."""
    from src.tools.health_ingest import get_health_metrics_summary
    health = get_health_metrics_summary()

    hydration_pct = min(1.0, _wellness_state["hydration_ml"] / _wellness_state["hydration_target_ml"])
    step_pct = min(1.0, health.get("steps", 0) / 10000.0)
    sleep_pct = min(1.0, health.get("sleep_hours", 0) / 8.0)
    break_score = min(1.0, (_wellness_state["stretches_completed"] + _wellness_state["eye_breaks_completed"]) / 8.0)

    score = int((hydration_pct * 25) + (step_pct * 30) + (sleep_pct * 25) + (break_score * 20))
    score = max(0, min(100, score))

    return {
        "score": score,
        "hydration_pct": int(hydration_pct * 100),
        "step_count": health.get("steps", 0),
        "sleep_hours": health.get("sleep_hours", 0),
        "breaks_completed": _wellness_state["stretches_completed"] + _wellness_state["eye_breaks_completed"],
        "status": "Optimal" if score >= 80 else ("Fair" if score >= 50 else "Needs Attention")
    }
