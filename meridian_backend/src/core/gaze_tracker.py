"""
gaze_tracker.py — Eye-Tracking & Spatial Gaze Control Sentinel (JARVIS-02)
"""

import time
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class GazeTrackerSentinel:
    """Tracks MediaPipe Iris gaze coordinates to support hands-free spatial window selection."""

    def __init__(self):
        self._active: bool = False
        self._current_x: float = 0.5
        self._current_y: float = 0.5
        self._focused_quadrant: str = "center"

    def start_gaze_tracking(self) -> Dict[str, Any]:
        self._active = True
        logger.info("[GazeTracker] Gaze tracking activated")
        return {"status": "gaze_tracker_started", "active": True}

    def stop_gaze_tracking(self) -> Dict[str, Any]:
        self._active = False
        logger.info("[GazeTracker] Gaze tracking deactivated")
        return {"status": "gaze_tracker_stopped", "active": False}

    def update_gaze_coordinates(self, norm_x: float, norm_y: float) -> Dict[str, Any]:
        self._current_x = max(0.0, min(1.0, norm_x))
        self._current_y = max(0.0, min(1.0, norm_y))
        self._focused_quadrant = self._resolve_quadrant(self._current_x, self._current_y)

        return {
            "status": "active" if self._active else "inactive",
            "x": self._current_x,
            "y": self._current_y,
            "focused_quadrant": self._focused_quadrant,
            "timestamp": time.time(),
        }

    def get_current_gaze(self) -> Dict[str, Any]:
        return {
            "active": self._active,
            "gaze": {
                "x": self._current_x,
                "y": self._current_y,
                "quadrant": self._focused_quadrant,
            } if self._active else None
        }

    def _resolve_quadrant(self, x: float, y: float) -> str:
        if x < 0.33 and y < 0.5:
            return "top_left"
        elif x > 0.66 and y < 0.5:
            return "top_right"
        elif x < 0.33 and y >= 0.5:
            return "bottom_left"
        elif x > 0.66 and y >= 0.5:
            return "bottom_right"
        elif y < 0.33:
            return "top_center"
        elif y > 0.66:
            return "bottom_center"
        return "center"

# Global singleton instance
_gaze_sentinel = GazeTrackerSentinel()

def get_current_gaze() -> Dict[str, Any]:
    return _gaze_sentinel.get_current_gaze()

def start_gaze_tracking() -> Dict[str, Any]:
    return _gaze_sentinel.start_gaze_tracking()

def stop_gaze_tracking() -> Dict[str, Any]:
    return _gaze_sentinel.stop_gaze_tracking()

def update_gaze_coordinates(norm_x: float, norm_y: float) -> Dict[str, Any]:
    return _gaze_sentinel.update_gaze_coordinates(norm_x, norm_y)
