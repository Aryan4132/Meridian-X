"""
ar_bridge.py — Dynamic AR Smart Glasses & Headset Mirroring Bridge (JARVIS-08)

Compatibility shim over src.core.perception, which owns the canonical headset
store (register/list/unregister/push). All state lives there so headsets
registered via the API and via tools are visible in both places.
"""

import time
import logging
from typing import List, Dict, Any, Optional

from src.core import perception as _perception

logger = logging.getLogger(__name__)

SUPPORTED_HEADSETS = ["XREAL Air", "XREAL Air 2", "Meta Ray-Ban", "Apple Vision Pro", "Vuzix Blade", "Generic WebXR"]


def _normalize_device_type(device_type: str) -> str:
    if device_type not in SUPPORTED_HEADSETS:
        return "Generic WebXR"
    return device_type


def list_ar_headsets() -> List[Dict[str, Any]]:
    return _perception.list_ar_headsets()


def register_ar_headset(device_id: str, device_type: str = "XREAL Air") -> Dict[str, Any]:
    return _perception.register_ar_headset(device_id, _normalize_device_type(device_type))


def unregister_ar_headset(device_id: str) -> bool:
    return _perception.unregister_ar_headset(device_id)


def push_ar_hud_payload(
    device_id: str, title: str, text: str, hud_position: str = "top_right"
) -> Dict[str, Any]:
    return _perception.push_ar_hud_payload(device_id, title, text, hud_position)


def generate_hud_frame(
    status_summary: str = "System Online",
    alerts: Optional[List[str]] = None,
    active_task: Optional[str] = "Idle",
) -> Dict[str, Any]:
    return {
        "hud_version": "1.0",
        "timestamp": time.time(),
        "widget_data": {
            "status": status_summary,
            "active_task": active_task or "Idle",
            "alerts": alerts or [],
            "battery_level": 94,
            "ar_overlay_opacity": 0.85,
        },
    }
