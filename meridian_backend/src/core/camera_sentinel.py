"""
camera_sentinel.py — Smart Camera & RTSP Security Vision Sentinel (JARVIS-05)

Monitors RTSP security camera streams, performs motion detection & vision alerts
when visitors or unauthorized people enter workspace bounds.
"""

import time
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger("meridian_camera_sentinel")

_camera_feeds: Dict[str, Dict[str, Any]] = {}
_motion_alerts: List[Dict[str, Any]] = []

def register_camera_feed(camera_id: str, rtsp_url: str, name: str = "Workspace Cam") -> Dict[str, Any]:
    doc = {
        "camera_id": camera_id,
        "rtsp_url": rtsp_url,
        "name": name,
        "status": "connected",
        "registered_at": time.time(),
        "last_motion": None
    }
    _camera_feeds[camera_id] = doc
    logger.info(f"[CameraSentinel] Registered camera feed '{name}' ({camera_id})")
    return doc

def list_camera_feeds() -> List[Dict[str, Any]]:
    return list(_camera_feeds.values())

def unregister_camera_feed(camera_id: str) -> bool:
    if camera_id in _camera_feeds:
        del _camera_feeds[camera_id]
        logger.info(f"[CameraSentinel] Unregistered camera feed {camera_id}")
        return True
    return False

def ingest_motion_event(camera_id: str, detected_objects: List[str], snapshot_url: Optional[str] = None) -> Dict[str, Any]:
    now = time.time()
    event = {
        "event_id": f"evt-{int(now * 1000)}",
        "camera_id": camera_id,
        "detected_objects": detected_objects,
        "snapshot_url": snapshot_url,
        "timestamp": now
    }
    if camera_id in _camera_feeds:
        _camera_feeds[camera_id]["last_motion"] = now
    
    _motion_alerts.insert(0, event)
    if len(_motion_alerts) > 50:
        _motion_alerts.pop()
        
    logger.info(f"[CameraSentinel] Motion alert on {camera_id}: {detected_objects}")
    return event

def get_recent_alerts(limit: int = 10) -> List[Dict[str, Any]]:
    return _motion_alerts[:limit]
