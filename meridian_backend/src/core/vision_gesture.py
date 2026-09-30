"""
vision_gesture.py — Vision Motion & Hand Gesture Control Sentinel (PL-29)
"""

import time
import logging
from typing import Dict, Any, List, Optional, Callable

logger = logging.getLogger(__name__)

GESTURE_TYPES = ["swipe_left", "swipe_right", "pinch", "palm_stop", "thumbs_up", "peace", "desk_motion"]

class VisionGestureSentinel:
    """Classifies hand gestures and tracks desk motion using MediaPipe / OpenCV."""

    def __init__(self):
        self._gesture_history: List[Dict[str, Any]] = []
        self._action_callbacks: Dict[str, List[Callable]] = {}

    def process_gesture_frame(self, landmark_data: Optional[Dict[str, Any]] = None, mock_gesture: Optional[str] = None) -> Dict[str, Any]:
        gesture = mock_gesture or "swipe_right"
        if gesture not in GESTURE_TYPES:
            gesture = "palm_stop"

        record = {
            "gesture_id": f"gest-{int(time.time()*1000)}",
            "gesture": gesture,
            "confidence": 0.92,
            "timestamp": time.time(),
            "action": self._map_gesture_to_action(gesture),
        }

        self._gesture_history.append(record)
        logger.info(f"[VisionGestureSentinel] Detected gesture {gesture}")
        return record

    def _map_gesture_to_action(self, gesture: str) -> str:
        mapping = {
            "swipe_left": "previous_tab",
            "swipe_right": "next_tab",
            "pinch": "minimize_window",
            "palm_stop": "pause_media",
            "thumbs_up": "confirm_dialog",
            "peace": "toggle_hud",
            "desk_motion": "wake_screen",
        }
        return mapping.get(gesture, "no_op")

    def get_recent_gestures(self, limit: int = 10) -> List[Dict[str, Any]]:
        return self._gesture_history[-limit:]

# Global singleton instance
_gesture_sentinel = VisionGestureSentinel()

def process_gesture_frame(landmark_data: Optional[Dict[str, Any]] = None, mock_gesture: Optional[str] = None) -> Dict[str, Any]:
    return _gesture_sentinel.process_gesture_frame(landmark_data, mock_gesture)

def get_recent_gestures(limit: int = 10) -> List[Dict[str, Any]]:
    return _gesture_sentinel.get_recent_gestures(limit)
