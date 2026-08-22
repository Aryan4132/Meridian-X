"""
perception.py — Consolidated JARVIS Perception, Sensor & Spatial Intelligence Engine
"""

import time
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger("meridian_perception")

# -------------------------------------------------------------------
# Gaze Tracker & Visual Control
# -------------------------------------------------------------------
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

# -------------------------------------------------------------------
# Camera Sentinel & Motion Feeds
# -------------------------------------------------------------------
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

# -------------------------------------------------------------------
# AR Smart Glasses HUD Bridge
# -------------------------------------------------------------------
_connected_headsets: Dict[str, Dict[str, Any]] = {}

def register_ar_headset(device_id: str, device_type: str = "XREAL Air 2", resolution: str = "1920x1080") -> Dict[str, Any]:
    headset = {
        "device_id": device_id,
        "device_type": device_type,
        "resolution": resolution,
        "status": "online",
        "connected_at": time.time(),
        "last_ping": time.time()
    }
    _connected_headsets[device_id] = headset
    logger.info(f"[AR Bridge] Registered AR headset {device_id} ({device_type})")
    return headset

def list_ar_headsets() -> List[Dict[str, Any]]:
    return list(_connected_headsets.values())

def unregister_ar_headset(device_id: str) -> bool:
    if device_id in _connected_headsets:
        del _connected_headsets[device_id]
        logger.info(f"[AR Bridge] Disconnected AR headset {device_id}")
        return True
    return False

def push_ar_hud_payload(device_id: str, title: str, text: str, hud_position: str = "top_right") -> Dict[str, Any]:
    payload = {
        "device_id": device_id,
        "title": title,
        "text": text,
        "position": hud_position,
        "timestamp": time.time()
    }
    if device_id in _connected_headsets:
        _connected_headsets[device_id]["last_ping"] = time.time()
    logger.info(f"[AR Bridge] Pushed HUD overlay to {device_id}: {title}")
    return payload

# -------------------------------------------------------------------
# Predictive Engine & Context Pre-Warmer
# -------------------------------------------------------------------
_habit_model: Dict[str, Any] = {
    "preferred_work_hours": "09:00-18:00",
    "frequent_tools": ["read_file", "search_web", "git_status"],
    "active_project": None
}
_prewarmed_contexts: Dict[str, Any] = {}

def prewarm_context_for_intent(intent: str, workspace_path: str = ".") -> Dict[str, Any]:
    now = time.time()
    context_doc = {
        "intent": intent,
        "workspace": workspace_path,
        "prewarmed_at": now,
        "prefetched_files": [],
        "status": "ready"
    }
    _prewarmed_contexts[intent] = context_doc
    logger.info(f"[PredictiveEngine] Pre-warmed context for intent '{intent}' in '{workspace_path}'")
    return context_doc

def predict_next_action(user_history: List[str]) -> Dict[str, Any]:
    if not user_history:
        return {"predicted_action": "search_files", "confidence": 0.5}
        
    last_cmd = user_history[-1].lower()
    if "test" in last_cmd:
        predicted = "git_status"
        confidence = 0.85
    elif "git" in last_cmd or "commit" in last_cmd:
        predicted = "review_diff"
        confidence = 0.90
    else:
        predicted = "read_file"
        confidence = 0.60
        
    return {
        "predicted_action": predicted,
        "confidence": confidence,
        "timestamp": time.time()
    }

def get_habit_profile() -> Dict[str, Any]:
    return _habit_model

# -------------------------------------------------------------------
# Presence Briefing Generator
# -------------------------------------------------------------------
_last_briefing_time: float = 0.0
_BRIEFING_COOLDOWN: float = 1800.0

def generate_presence_briefing(user_name: str = "User") -> Dict[str, Any]:
    global _last_briefing_time
    now = time.time()
    if now - _last_briefing_time < _BRIEFING_COOLDOWN:
        time_remaining = int(_BRIEFING_COOLDOWN - (now - _last_briefing_time))
        return {
            "triggered": False,
            "reason": f"Briefing cooldown active ({time_remaining}s remaining)",
            "briefing_text": ""
        }
        
    _last_briefing_time = now
    from datetime import datetime
    today = datetime.now().strftime("%A, %B %d")
    briefing_text = (
        f"Welcome back {user_name}. Today is {today}. "
        f"All system services are online. You have no urgent threat alerts."
    )
    
    logger.info(f"[PresenceBriefing] Generated executive briefing for {user_name}")
    return {
        "triggered": True,
        "briefing_text": briefing_text,
        "generated_at": now
    }

def reset_briefing_cooldown():
    global _last_briefing_time
    _last_briefing_time = 0.0
