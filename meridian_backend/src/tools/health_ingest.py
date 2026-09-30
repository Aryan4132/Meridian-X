"""
health_ingest.py — Wearable Health Data Ingestion (FIT-01)
Manual-entry health register (steps, sleep, heart rate).

NOTE: no live Google Fit / Apple Health API integration exists in this build.
Values are recorded only when explicitly provided (manual entry or a connected
feed calling sync_wearable_health_data). Unset metrics stay None and are
reported as "no data" — never as fabricated readings.
"""

import time
from typing import Dict, Any, Optional

_health_cache: Dict[str, Any] = {
    "steps": None,
    "sleep_hours": None,
    "resting_heart_rate": None,
    "active_calories": None,
    "last_sync": None,
    "source": "manual_entry",
}


def _fmt(value: Any, unit: str, thousands: bool = False) -> str:
    if value is None:
        return "no data"
    if thousands and isinstance(value, (int, float)):
        return f"{value:,} {unit}"
    return f"{value} {unit}"


def sync_wearable_health_data(
    source: str = "manual_entry",
    steps: Optional[int] = None,
    sleep_hours: Optional[float] = None,
    heart_rate: Optional[int] = None,
) -> str:
    """Records explicitly provided health metrics into the health register."""
    global _health_cache
    _health_cache["source"] = source
    if steps is not None:
        _health_cache["steps"] = int(steps)
    if sleep_hours is not None:
        _health_cache["sleep_hours"] = float(sleep_hours)
    if heart_rate is not None:
        _health_cache["resting_heart_rate"] = int(heart_rate)
    _health_cache["last_sync"] = time.time()

    return (
        f"Health Data Synced ({source.upper()}):\n"
        f"- Steps Today: {_fmt(_health_cache['steps'], '', thousands=True)}\n"
        f"- Sleep Duration: {_fmt(_health_cache['sleep_hours'], 'hours')}\n"
        f"- Resting Heart Rate: {_fmt(_health_cache['resting_heart_rate'], 'bpm')}\n"
        f"- Active Calories: {_fmt(_health_cache['active_calories'], 'kcal')}"
    )


def get_health_metrics_summary() -> Dict[str, Any]:
    """Returns the latest ingested health telemetry dictionary."""
    return dict(_health_cache)
