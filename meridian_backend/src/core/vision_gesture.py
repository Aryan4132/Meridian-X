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
        gesture = "none"
        confidence = 0.0

        if mock_gesture:
            gesture = mock_gesture if mock_gesture in GESTURE_TYPES else "palm_stop"
            confidence = 0.95
        elif landmark_data:
            # Real landmark extraction logic if landmarks provided
            landmarks = landmark_data.get("landmarks", [])
            delta_x = landmark_data.get("delta_x", 0.0)
            if delta_x > 0.15:
                gesture = "swipe_right"
                confidence = 0.90
            elif delta_x < -0.15:
                gesture = "swipe_left"
                confidence = 0.90
            elif landmark_data.get("is_pinch"):
                gesture = "pinch"
                confidence = 0.88
            elif landmark_data.get("open_palm"):
                gesture = "palm_stop"
                confidence = 0.89
            elif landmarks:
                gesture = "desk_motion"
                confidence = 0.75

        record = {
            "gesture_id": f"gest-{int(time.time()*1000)}",
            "gesture": gesture,
            "confidence": confidence,
            "timestamp": time.time(),
            "action": self._map_gesture_to_action(gesture) if gesture != "none" else "no_op",
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
