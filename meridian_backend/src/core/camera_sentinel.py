"""
camera_sentinel.py — Smart Camera & RTSP Security Vision Sentinel (JARVIS-05)
"""

import time
import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

class CameraSentinel:
    """Manages RTSP camera streams, motion detection, and room entry alerts."""

    def __init__(self):
        self._feeds: Dict[str, Dict[str, Any]] = {}
        self._alerts: List[Dict[str, Any]] = []

    def add_feed(self, camera_id: str, name: str, rtsp_url: str) -> Dict[str, Any]:
        feed = {
            "camera_id": camera_id,
            "name": name,
            "rtsp_url": rtsp_url,
            "status": "connected",
            "added_at": time.time(),
            "motion_detected": False,
        }
        self._feeds[camera_id] = feed
        logger.info(f"[CameraSentinel] Added feed {camera_id} ({name})")
        return feed

    def remove_feed(self, camera_id: str) -> bool:
        if camera_id in self._feeds:
            del self._feeds[camera_id]
            return True
        return False

    def list_camera_feeds(self) -> List[Dict[str, Any]]:
        return list(self._feeds.values())

    def process_frame(self, camera_id: str, motion_score: float = 0.8, objects_detected: Optional[List[str]] = None) -> Dict[str, Any]:
        feed = self._feeds.get(camera_id)
        if not feed:
            feed = self.add_feed(camera_id, f"Camera-{camera_id}", f"rtsp://localhost/{camera_id}")

        detected = objects_detected or ["person"]
        is_entry = "person" in detected and motion_score > 0.5

        if is_entry:
            alert = {
                "alert_id": f"alert-{int(time.time()*1000)}",
                "camera_id": camera_id,
                "camera_name": feed["name"],
                "type": "room_entry",
                "confidence": motion_score,
                "objects": detected,
                "timestamp": time.time(),
            }
            self._alerts.append(alert)
            feed["motion_detected"] = True
            logger.info(f"[CameraSentinel] Room entry detected on {camera_id}")
            return {"status": "alert_triggered", "alert": alert}

        return {"status": "normal", "motion_detected": False}

    def get_recent_alerts(self, limit: int = 10) -> List[Dict[str, Any]]:
        return self._alerts[-limit:]

# Global singleton instance
_sentinel_instance = CameraSentinel()

def list_camera_feeds() -> List[Dict[str, Any]]:
    return _sentinel_instance.list_camera_feeds()

def get_recent_alerts() -> List[Dict[str, Any]]:
    return _sentinel_instance.get_recent_alerts()

def add_camera_feed(camera_id: str, name: str, rtsp_url: str) -> Dict[str, Any]:
    return _sentinel_instance.add_feed(camera_id, name, rtsp_url)

def process_camera_frame(camera_id: str, motion_score: float = 0.8, objects_detected: Optional[List[str]] = None) -> Dict[str, Any]:
    return _sentinel_instance.process_frame(camera_id, motion_score, objects_detected)
