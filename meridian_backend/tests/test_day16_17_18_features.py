"""
test_day16_17_18_features.py — Unit Test Suite for Days 16, 17, and 18 Features
"""

import pytest
import os
import sys

# Ensure backend src is on python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_day16_camera_sentinel():
    from src.core.camera_sentinel import add_camera_feed, list_camera_feeds, process_camera_frame, get_recent_alerts

    feed = add_camera_feed("cam-01", "Front Door", "rtsp://192.168.1.50/live")
    assert feed["camera_id"] == "cam-01"
    assert len(list_camera_feeds()) >= 1

    res = process_camera_frame("cam-01", motion_score=0.9, objects_detected=["person"])
    assert res["status"] == "alert_triggered"
    assert len(get_recent_alerts()) >= 1

def test_day16_presence_briefing():
    from src.core.presence_briefing import generate_presence_briefing, trigger_room_entry_briefing

    briefing = generate_presence_briefing("Aryan")
    assert "Aryan" in briefing["user_name"]
    assert "briefing" in briefing
    assert briefing["duration_seconds"] == 15

    trig = trigger_room_entry_briefing("Aryan")
    assert trig["status"] in ["triggered", "skipped"]

def test_day16_polyglot():
    from src.core.polyglot import get_supported_languages, translate_speech_to_code, detect_programming_intent

    langs = get_supported_languages()
    assert len(langs) >= 50
    assert "Spanish" in langs

    res = translate_speech_to_code("write a python function to compute fibonacci", source_language="Spanish")
    assert res["status"] == "success"
    assert "def " in res["code_snippet"]
    assert detect_programming_intent("write code for sorting list") is True

def test_day16_vision_gesture():
    from src.core.vision_gesture import process_gesture_frame, get_recent_gestures

    res = process_gesture_frame(mock_gesture="swipe_right")
    assert res["gesture"] == "swipe_right"
    assert res["action"] == "next_tab"
    assert len(get_recent_gestures()) >= 1

def test_day16_gaze_tracker():
    from src.core.gaze_tracker import start_gaze_tracking, update_gaze_coordinates, get_current_gaze, stop_gaze_tracking

    assert start_gaze_tracking()["active"] is True
    gaze_res = update_gaze_coordinates(0.1, 0.1)
    assert gaze_res["focused_quadrant"] == "top_left"
    current = get_current_gaze()
    assert current["active"] is True
    assert current["gaze"]["quadrant"] == "top_left"
    assert stop_gaze_tracking()["active"] is False

def test_day16_ar_bridge():
    from src.core.ar_bridge import register_ar_headset, list_ar_headsets, generate_hud_frame

    headset = register_ar_headset("xreal-01", "XREAL Air")
    assert headset["device_id"] == "xreal-01"
    assert len(list_ar_headsets()) >= 1

    hud = generate_hud_frame("Active Task", alerts=["Update available"])
    assert hud["hud_version"] == "1.0"
    assert "widget_data" in hud

def test_day17_workspace_layout():
    from src.tools.workspace_layout import arrange_workspace_grid

    res = arrange_workspace_grid()
    assert res["status"] == "success"
    assert res["layout"] == "2x2_grid"

def test_day18_learning_queue():
    from src.tools.learning_queue import add_to_learning_queue, list_learning_queue, generate_sm2_flashcards, generate_reading_digest

    item = add_to_learning_queue("https://arxiv.org/abs/1234.5678", "AI Research Paper", ["ai", "research"])
    assert item["status"] == "unread"
    assert len(list_learning_queue()) >= 1

    cards = generate_sm2_flashcards("Neural Networks")
    assert len(cards) >= 1

    digest = generate_reading_digest()
    assert digest["digest_title"] == "Weekly Spaced Reading Summary"

def test_day18_price_watcher():
    from src.tools.price_watcher import add_watched_product, list_watched_products, check_price_drops

    prod = add_watched_product("p-01", "Wireless Headphones", "https://amazon.com/dp/xyz", target_price=100.0, current_price=89.99)
    assert prod["alert_triggered"] is True
    assert len(list_watched_products()) >= 1
    drops = check_price_drops()
    assert len(drops) >= 1

def test_day18_networth_tracker():
    from src.tools.networth_tracker import add_asset, add_liability, get_networth_summary

    add_asset("crypto", "Bitcoin", "crypto", 5000.0)
    add_liability("car_loan", "Auto Loan", "loan", 2000.0)
    summary = get_networth_summary()
    assert summary["total_assets"] >= 5000.0
    assert summary["net_worth"] > 0

def test_day18_wifi_assessor():
    from src.tools.wifi_assessor import assess_wifi_security

    res = assess_wifi_security("CoffeeShop_Guest", "Open")
    assert res["risk_level"] == "HIGH"
    assert res["firewall_mode"] == "tightened"

def test_day18_bookmark_manager():
    from src.tools.bookmark_manager import add_bookmark, list_bookmarks, prune_dead_links

    bm = add_bookmark("https://github.com/Meridian-X", "Meridian-X Repo")
    assert "developer" in bm["tags"]
    bms = list_bookmarks("Meridian")
    assert len(bms) >= 1
    pruned = prune_dead_links()
    assert pruned["status"] == "success"
