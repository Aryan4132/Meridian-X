"""
gaze_tracker.py — Gaze & Eye Tracking Stub (JARVIS-02)
"""
from typing import Dict, Any

def get_current_gaze() -> Dict[str, Any]:
    return {"status": "inactive", "gaze": None}

def start_gaze_tracking() -> Dict[str, Any]:
    return {"status": "gaze_tracker_started"}

def stop_gaze_tracking() -> Dict[str, Any]:
    return {"status": "gaze_tracker_stopped"}
