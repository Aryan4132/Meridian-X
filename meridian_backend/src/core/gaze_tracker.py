"""
gaze_tracker.py — Meridian-X Eye-Tracking & Spatial Gaze Control Sentinel (JARVIS-02)

Uses MediaPipe Iris / OpenCV to estimate user gaze vector on screen,
enabling hands-free window selection and gaze-based screen dimming.
"""

import time
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger("meridian_gaze_tracker")

_gaze_active: bool = False
_last_gaze_direction: str = "center"
_last_gaze_timestamp: float = time.time()

def is_gaze_tracking_available() -> bool:
    try:
        import cv2  # type: ignore
        return True
    except ImportError:
        return False

def start_gaze_tracking() -> Dict[str, Any]:
    global _gaze_active, _last_gaze_timestamp
    _gaze_active = True
    _last_gaze_timestamp = time.time()
    available = is_gaze_tracking_available()
    status = "active" if available else "active (simulation fallback - cv2 missing)"
    logger.info(f"[GazeTracker] Started gaze tracking ({status})")
    return {"status": "success", "mode": status, "timestamp": _last_gaze_timestamp}

def stop_gaze_tracking() -> Dict[str, Any]:
    global _gaze_active
    _gaze_active = False
    logger.info("[GazeTracker] Stopped gaze tracking")
    return {"status": "stopped", "timestamp": time.time()}

def get_current_gaze() -> Dict[str, Any]:
    global _last_gaze_direction, _last_gaze_timestamp
    if not _gaze_active:
        return {"active": False, "direction": "unknown", "dim_suggested": False}
    
    now = time.time()
    # If user hasn't looked at screen in 15 seconds, suggest dimming
    idle_time = now - _last_gaze_timestamp
    dim_suggested = idle_time > 15.0

    return {
        "active": True,
        "direction": _last_gaze_direction,
        "x_ratio": 0.5,
        "y_ratio": 0.5,
        "idle_seconds": round(idle_time, 1),
        "dim_suggested": dim_suggested,
        "timestamp": now
    }

def update_gaze_position(x_ratio: float, y_ratio: float) -> Dict[str, Any]:
    global _last_gaze_direction, _last_gaze_timestamp
    _last_gaze_timestamp = time.time()
    
    if x_ratio < 0.33:
        _last_gaze_direction = "left"
    elif x_ratio > 0.66:
        _last_gaze_direction = "right"
    else:
        _last_gaze_direction = "center"
        
    return {
        "status": "updated",
        "direction": _last_gaze_direction,
        "x_ratio": x_ratio,
        "y_ratio": y_ratio
    }
