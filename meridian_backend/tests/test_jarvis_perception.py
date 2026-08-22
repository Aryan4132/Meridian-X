"""
test_jarvis_perception.py — Unit test suite for JARVIS Perception & Intelligence Modules
"""

import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.perception import (
    start_gaze_tracking, stop_gaze_tracking, get_current_gaze, update_gaze_position,
    register_camera_feed, list_camera_feeds, ingest_motion_event, get_recent_alerts,
    register_ar_headset, list_ar_headsets, push_ar_hud_payload,
    predict_next_action, prewarm_context_for_intent, get_habit_profile,
    generate_presence_briefing, reset_briefing_cooldown
)
from src.voice.polyglot import translate_speech_to_code


def test_gaze_tracker_lifecycle():
    res_start = start_gaze_tracking()
    assert res_start["status"] == "success"
    
    res_update = update_gaze_position(0.2, 0.5)
    assert res_update["direction"] == "left"
    
    res_status = get_current_gaze()
    assert res_status["active"] is True
    assert res_status["direction"] == "left"
    
    res_stop = stop_gaze_tracking()
    assert res_stop["status"] == "stopped"


def test_camera_sentinel_lifecycle():
    feed = register_camera_feed("cam-01", "rtsp://192.168.1.100/stream", name="Front Door")
    assert feed["camera_id"] == "cam-01"
    
    feeds = list_camera_feeds()
    assert len(feeds) > 0
    
    evt = ingest_motion_event("cam-01", ["person", "car"])
    assert evt["camera_id"] == "cam-01"
    assert "person" in evt["detected_objects"]
    
    alerts = get_recent_alerts()
    assert len(alerts) > 0


def test_ar_bridge_lifecycle():
    headset = register_ar_headset("headset-01", "XREAL Air 2")
    assert headset["device_id"] == "headset-01"
    
    headsets = list_ar_headsets()
    assert len(headsets) > 0
    
    hud = push_ar_hud_payload("headset-01", "Alert", "Battery low")
    assert hud["title"] == "Alert"


def test_polyglot_translation():
    res = translate_speech_to_code("read target file", target_lang="en", code_target="python")
    assert res["status"] == "translated"
    assert "with open" in res["code_output"]


def test_predictive_engine():
    pred = predict_next_action(["git status", "git commit"])
    assert pred["predicted_action"] == "review_diff"
    
    ctx = prewarm_context_for_intent("build_feature")
    assert ctx["intent"] == "build_feature"
    
    habits = get_habit_profile()
    assert "preferred_work_hours" in habits


def test_presence_briefing():
    reset_briefing_cooldown()
    briefing = generate_presence_briefing("Aryan")
    assert briefing["triggered"] is True
    assert "Welcome back Aryan" in briefing["briefing_text"]
