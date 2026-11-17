"""
test_timeline_completion.py — Comprehensive Test Suite for Day 19 to Day 22 Milestones

Covers:
- Day 19: Butler Rituals, Smart Home, Concierge, Etiquette, Routine Executor
- Day 20: OS Automation Macros, Android ADB, Device Handoff, Device Sentinel
- Day 21: Voice Biometrics & STT/TTS Streaming
- Day 22: Camera Sentinel & Vision Perception
"""

import pytest
import time
from typing import Dict, Any

from src.core.butler_ritual import ButlerRitualEngine, RitualConfig
from src.tools.home_assistant import HomeAssistantSentinel
from src.core.concierge_agent import ConciergeAgent, ConciergeProfile
from src.core.butler_etiquette import ButlerEtiquetteEngine
from src.core.routine_executor import RoutineExecutor
from src.tools.os_automation import OSAutomationEngine
from src.core.android_automation import AndroidADBBridge
from src.core.device_handoff import DeviceHandoffEngine
from src.core.device_sentinel import DeviceSentinelEngine
from src.core.camera_sentinel import CameraSentinel
from src.voice.voice_biometrics import VoiceBiometricsEngine
from src.tools.registry import TOOL_REGISTRY


# ==========================================
# Day 19: Executive Butler Suite Tests
# ==========================================

def test_butler_morning_ritual():
    engine = ButlerRitualEngine()
    weather = {"temp_c": 11, "condition": "Light Rain", "rain_prob": 0.7}
    events = [{"title": "Client Executive Review", "time": "10:00"}]

    res = engine.execute_morning_ritual("Aryan", weather_data=weather, calendar_events=events)
    assert res["status"] == "completed"
    assert res["user"] == "Aryan"
    assert "daylight_focus" in res["lighting_preset"]
    assert res["outfit_recommendation"]["formality"] == "Executive Business Formal"
    assert res["outfit_recommendation"]["rain_caution"] is True
    assert len(engine.get_ritual_history()) >= 1


def test_butler_evening_ritual():
    engine = ButlerRitualEngine()
    res = engine.execute_evening_ritual("Aryan", completed_tasks=["Refactor STT", "Write tests"], uncompleted_tasks=[])
    assert res["status"] == "completed"
    assert res["completed_tasks_count"] == 2
    assert "warm_ember" in res["lighting_preset"]


def test_home_assistant_sentinel():
    sentinel = HomeAssistantSentinel()
    entities = sentinel.list_entities(domain="light")
    assert len(entities) >= 1
    assert any("light." in e["entity_id"] for e in entities)

    ctrl_res = sentinel.control_light("light.desk_ambient", state="on", brightness=240)
    assert ctrl_res["status"] == "success"
    assert ctrl_res["applied_params"]["brightness"] == 240

    climate_res = sentinel.set_climate("climate.office_thermostat", target_temp=22.5, hvac_mode="heat")
    assert climate_res["temperature"] == 22.5

    lock_res = sentinel.toggle_lock("lock.office_door", lock_action="lock")
    assert lock_res["lock_state"] == "lock"


def test_concierge_agent():
    concierge = ConciergeAgent(ConciergeProfile(dietary_preferences=["Vegan"]))
    dining = concierge.search_dining_recommendations("Tokyo", cuisine="Japanese Kaiseki")
    assert len(dining) >= 1
    assert "Tokyo" in dining[0]["name"]

    buffer_calc = concierge.calculate_travel_buffers(
        flight_departure_iso="2026-11-15T10:00:00",
        origin_address="100 Tech Blvd",
        airport_code="SFO",
        is_international=True
    )
    assert buffer_calc["total_lead_time_minutes"] > 100
    assert buffer_calc["is_international"] is True

    booking = concierge.record_reservation("hotel", "Aman Tokyo", "2026-12-01", {"nights": 3})
    assert booking["title"] == "Aman Tokyo"
    assert len(concierge.list_itinerary()) >= 1


def test_butler_etiquette_engine():
    engine = ButlerEtiquetteEngine(default_formality=0.9)
    assert "British Butler" in engine.get_tone_label()
    directive = engine.generate_etiquette_directive()
    assert "British" in directive

    engine.set_formality(0.1)
    assert "Wingman" in engine.get_tone_label()
    casual_directive = engine.generate_etiquette_directive()
    assert "startup" in casual_directive.lower() or "wingman" in casual_directive.lower()


def test_routine_executor(tmp_path):
    executor = RoutineExecutor(data_dir=str(tmp_path))
    cleanup = executor.perform_disk_cleanup(dry_run=True)
    assert cleanup["status"] == "success"
    assert cleanup["dry_run"] is True

    report = executor.generate_weekly_status_email(
        user_name="Aryan",
        completed_highlights=["Shipped Day 19 butler rituals", "Completed cross-device handoff"]
    )
    assert "Shipped Day 19" in report["body"]
    assert "Aryan" in report["body"]


# ==========================================
# Day 20: Cross-Device Automation Tests
# ==========================================

def test_os_automation_macro():
    engine = OSAutomationEngine()
    steps = [
        {"action": "wait", "params": {"seconds": 0.01}},
        {"action": "type", "params": {"text": "echo test"}},
        {"action": "wait", "params": {"seconds": 0.01}}
    ]
    reg = engine.register_macro("quick_test", steps)
    assert reg["status"] == "registered"

    exec_res = engine.execute_macro("quick_test", dry_run=True)
    assert exec_res["status"] == "success"
    assert exec_res["total_steps"] == 3


def test_android_automation_commands():
    bridge = AndroidADBBridge()
    # Test safe invocation without blocking
    devices = bridge.list_devices()
    assert isinstance(devices, list)

    tap_res = bridge.tap(100, 200)
    assert tap_res["x"] == 100
    assert tap_res["y"] == 200

    swipe_res = bridge.swipe(0, 500, 0, 100, duration_ms=200)
    assert swipe_res["duration_ms"] == 200


def test_device_handoff_engine():
    engine = DeviceHandoffEngine()
    clip = engine.sync_clipboard_content("export TOKEN=xyz", source_device="desktop")
    assert clip["text"] == "export TOKEN=xyz"
    assert engine.get_shared_clipboard()["text"] == "export TOKEN=xyz"

    sess = engine.create_task_handoff(
        origin_device="desktop",
        target_device="mobile",
        task_goal="Verify voice pipeline",
        open_files=["stt.py", "tts.py"]
    )
    assert sess.session_id.startswith("handoff-")

    claimed = engine.claim_task_handoff(sess.session_id)
    assert claimed is not None
    assert claimed["task_goal"] == "Verify voice pipeline"
    assert "stt.py" in claimed["open_files"]


def test_device_sentinel():
    sentinel = DeviceSentinelEngine()
    sentinel.update_telemetry(
        device_id="mobile_companion",
        name="Pixel 9 Pro",
        platform="android",
        battery=15.0,  # low battery threshold
        is_charging=False,
        free_storage_gb=3.5,  # low storage threshold
        latency_ms=18.5
    )

    devices = sentinel.list_connected_devices()
    mobile = next((d for d in devices if d["device_id"] == "mobile_companion"), None)
    assert mobile is not None
    assert mobile["alerts"]["low_battery_warning"] is True
    assert mobile["alerts"]["low_storage_warning"] is True

    ping = sentinel.ping_device("mobile_companion")
    assert ping["status"] == "pong"
    assert ping["latency_ms"] == 18.5


# ==========================================
# Day 21 & 22: Voice & Vision Sentinel Tests
# ==========================================

def test_voice_biometrics_verification():
    engine = VoiceBiometricsEngine(threshold=0.75)
    sample_audio_a = b"VOICE_SAMPLE_ARYAN_SECRET_PHRASE_1234567890"
    sample_audio_b = b"VOICE_SAMPLE_ARYAN_SECRET_PHRASE_1234567890"
    different_audio = b"UNKNOWN_ATTACKER_SPOOF_SAMPLE_999999999999"

    enroll_res = engine.register_speaker("aryan_owner", sample_audio_a)
    assert enroll_res["status"] == "enrolled"
    assert enroll_res["vector_dim"] == 128

    # Verify identical sample
    verified, score = engine.verify_speaker(sample_audio_b, "aryan_owner")
    assert verified is True
    assert score > 0.95

    # Verify different speaker rejected
    verified_bad, score_bad = engine.verify_speaker(different_audio, "aryan_owner")
    assert score_bad < 0.85


def test_camera_sentinel_room_entry():
    sentinel = CameraSentinel()
    sentinel.add_feed("desk_cam", "Desk Overhead", "rtsp://localhost/desk")

    # Simulate room entry frame
    frame_res = sentinel.process_frame("desk_cam", motion_score=0.85, objects_detected=["person"])
    assert frame_res["status"] == "alert_triggered"
    assert frame_res["alert"]["type"] == "room_entry"
    assert len(sentinel.get_recent_alerts()) >= 1


def test_tool_registry_day19_day20_presence():
    """Validates that all new tools are properly registered in TOOL_REGISTRY."""
    expected_tools = [
        "run_morning_ritual",
        "run_evening_ritual",
        "hass_list_devices",
        "hass_set_light",
        "hass_set_temperature",
        "concierge_find_dining",
        "concierge_calculate_transit_buffer",
        "set_butler_formality",
        "execute_disk_cleanup",
        "prepare_weekly_report",
        "run_os_macro",
        "save_os_macro",
        "adb_list_devices",
        "adb_launch_application",
        "handoff_sync_clipboard",
        "handoff_create_session",
        "list_mesh_devices",
        "log_vehicle_service",
        "get_vehicle_service_prediction",
        "family_post_announcement",
        "family_add_task",
        "family_get_board",
        "organize_index_photo",
        "organize_find_duplicate_photos",
        "compose_save_routine",
        "compose_run_routine",
        "compose_list_routines",
        "plan_executive_day",
        "secure_shred_file",
        "add_pool_expense",
        "get_pool_settlement",
        "set_kids_screen_budget",
        "check_kids_url",
        "habit_log",
        "habit_get_summary"
    ]
    for tool_name in expected_tools:
        assert tool_name in TOOL_REGISTRY, f"Tool '{tool_name}' missing from TOOL_REGISTRY"


# ==========================================
# Day 23 & 24: Lifestyle, Family & Security Tests
# ==========================================

def test_car_logbook_prediction():
    from src.tools.car_logbook import car_logbook_sentinel
    entry = car_logbook_sentinel.log_maintenance("primary_auto", "oil_change", 45000, cost=120.0)
    assert entry["service_type"] == "oil_change"

    prediction = car_logbook_sentinel.predict_next_service("primary_auto")
    assert prediction["vehicle_id"] == "primary_auto"
    assert prediction["km_until_service"] >= 0


def test_family_board_and_tasks():
    from src.tools.family_board import family_board_sentinel
    msg = family_board_sentinel.post_announcement("Aryan", "Dinner at 7:30pm")
    assert msg["author"] == "Aryan"

    task = family_board_sentinel.add_shared_task("Pick up groceries", "Aryan", "Today")
    assert task["completed"] is False

    done = family_board_sentinel.complete_shared_task(task["task_id"])
    assert done["completed"] is True


def test_photo_organizer(tmp_path):
    from src.tools.photo_organizer import photo_organizer_sentinel
    dummy_img = tmp_path / "vacation_photo.jpg"
    dummy_img.write_bytes(b"JPEG_MOCK_BYTES_DATA_123456")

    indexed = photo_organizer_sentinel.index_photo(str(dummy_img))
    assert indexed["filename"] == "vacation_photo.jpg"
    assert indexed["photo_id"].startswith("img-")


def test_routine_composer():
    from src.tools.routine_composer import routine_composer_sentinel
    routine = routine_composer_sentinel.compose_routine(
        name="nightly_lockdown",
        description="Shuts down monitors, locks doors, and prepares morning digest",
        steps=[{"tool": "execute_disk_cleanup", "args": {}}]
    )
    assert routine["name"] == "nightly_lockdown"

    res = routine_composer_sentinel.execute_routine("nightly_lockdown")
    assert res["status"] == "success"
    assert res["executed_steps_count"] == 1


def test_day_planner():
    from src.tools.day_planner import day_planner_sentinel
    plan = day_planner_sentinel.generate_day_plan(
        user_name="Aryan",
        weather_forecast={"condition": "Clear", "temp_c": 24},
        calendar_events=[{"time": "11:00", "title": "Client Sync", "location": "Headquarters"}]
    )
    assert plan["user"] == "Aryan"
    assert len(plan["timeline_items"]) >= 3


def test_secure_shredder(tmp_path):
    from src.tools.secure_shredder import secure_shredder_sentinel
    secret_file = tmp_path / "classified_plan.txt"
    secret_file.write_text("SUPER_SECRET_TOKEN_9999999")

    cert = secure_shredder_sentinel.shred_file(str(secret_file), passes=3)
    assert cert["status"] == "permanently_destroyed"
    assert not secret_file.exists()


def test_expense_pool_settlement():
    from src.tools.expense_pool import expense_pool_sentinel
    pool_id = "test_sprint_dinner"
    expense_pool_sentinel.create_pool(pool_id, "Sprint Dinner", ["Alice", "Bob", "Charlie"])

    expense_pool_sentinel.add_expense(pool_id, payer="Alice", amount=90.0, description="Sushi dinner", beneficiaries=["Alice", "Bob", "Charlie"])
    settle = expense_pool_sentinel.calculate_settlement(pool_id)
    assert settle["total_expenses"] == 90.0
    assert len(settle["settlement_transactions"]) >= 1


def test_parental_controls():
    from src.tools.parental_controls import parental_controls_sentinel
    parental_controls_sentinel.set_screen_quota("kids_profile", minutes=60)
    usage = parental_controls_sentinel.log_screen_usage("kids_profile", elapsed_minutes=70)
    assert usage["locked"] is True

    url_check = parental_controls_sentinel.check_url_allowed("kids_profile", "https://tiktok.com/viral")
    assert url_check["allowed"] is False


def test_habit_tracker():
    from src.tools.habit_tracker import habit_tracker_sentinel
    res = habit_tracker_sentinel.log_habit_completion("daily_reading")
    assert res["status"] == "logged"
    assert res["current_streak"] >= 1

    summary = habit_tracker_sentinel.get_habit_summary()
    assert summary["active_habits_count"] >= 1
