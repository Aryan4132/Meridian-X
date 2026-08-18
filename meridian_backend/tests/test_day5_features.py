import os
import sys
import base64
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api import app
from src.core.auth import API_KEY
from src.voice.duplex import (
    global_duplex_engine,
    is_voice_response_enabled,
    set_voice_response_enabled
)
from src.voice.wakeword import (
    trigger_continuous_window,
    is_continuous_window_active,
    cancel_continuous_window,
    get_continuous_window_remaining
)
from src.voice.voice_biometrics import (
    global_biometrics_engine,
    cosine_similarity
)

client = TestClient(app)
headers = {"X-API-Key": API_KEY}


def test_duplex_voice_engine_core():
    engine = global_duplex_engine
    engine.stop_duplex_session()
    assert engine.state == "idle"
    assert not engine.is_active

    # Start session
    msg = engine.start_duplex_session()
    assert "initialized" in msg or "already active" in msg
    assert engine.is_active
    assert engine.state == "listening"

    # Set speaking state
    engine.set_speaking_state(True)
    assert engine.state == "speaking"

    # Check barge-in under threshold
    assert not engine.check_barge_in(100.0)

    # Check barge-in over threshold
    assert engine.check_barge_in(350.0)
    assert engine.state == "interrupted"

    # Stop session
    msg_stop = engine.stop_duplex_session()
    assert "stopped" in msg_stop
    assert not engine.is_active


def test_voice_response_toggle():
    set_voice_response_enabled(True)
    assert is_voice_response_enabled() is True

    # Test GET endpoint
    res_get = client.get("/api/voice/response/status", headers=headers)
    assert res_get.status_code == 200
    assert res_get.json()["enabled"] is True

    # Test POST toggle disable
    res_toggle_off = client.post("/api/voice/response/toggle?enabled=false", headers=headers)
    assert res_toggle_off.status_code == 200
    assert res_toggle_off.json()["enabled"] is False
    assert is_voice_response_enabled() is False

    # Test POST toggle enable
    res_toggle_on = client.post("/api/voice/response/toggle?enabled=true", headers=headers)
    assert res_toggle_on.status_code == 200
    assert res_toggle_on.json()["enabled"] is True


def test_duplex_api_endpoints():
    # Start endpoint
    res_start = client.post("/api/voice/duplex/start", headers=headers)
    assert res_start.status_code == 200
    assert res_start.json()["status"] == "success"

    # Status endpoint
    res_status = client.get("/api/voice/duplex/status", headers=headers)
    assert res_status.status_code == 200
    assert res_status.json()["duplex_state"]["active"] is True

    # Barge-in endpoint
    res_barge = client.post("/api/voice/duplex/barge-in?rms=400.0", headers=headers)
    assert res_barge.status_code == 200

    # Stop endpoint
    res_stop = client.post("/api/voice/duplex/stop", headers=headers)
    assert res_stop.status_code == 200
    assert res_stop.json()["duplex_state"]["active"] is False


def test_continuous_conversation_window_endpoints():
    cancel_continuous_window()

    # Status initial
    res_status = client.get("/api/voice/continuous-window/status", headers=headers)
    assert res_status.status_code == 200
    assert res_status.json()["active"] is False

    # Start continuous window
    res_start = client.post("/api/voice/continuous-window/start?duration=6.0", headers=headers)
    assert res_start.status_code == 200
    assert res_start.json()["remaining_seconds"] > 0.0

    # Verify status active
    res_status_active = client.get("/api/voice/continuous-window/status", headers=headers)
    assert res_status_active.status_code == 200
    assert res_status_active.json()["active"] is True

    # Cancel
    res_cancel = client.post("/api/voice/continuous-window/cancel", headers=headers)
    assert res_cancel.status_code == 200

    # Verify status inactive
    res_status_final = client.get("/api/voice/continuous-window/status", headers=headers)
    assert res_status_final.status_code == 200
    assert res_status_final.json()["active"] is False


def test_voice_biometrics_core_and_endpoints():
    global_biometrics_engine.reset_biometrics()

    sample_audio_1 = b"SPEAKER_1_VOICE_PRINT_AUDIO_SAMPLE_DATA_AAA"
    sample_audio_2 = b"SPEAKER_2_UNAUTHORIZED_VOICE_SAMPLE_DATA_BBB"

    b64_sample_1 = base64.b64encode(sample_audio_1).decode("utf-8")
    b64_sample_2 = base64.b64encode(sample_audio_2).decode("utf-8")

    # Register voiceprint
    res_reg = client.post(
        "/api/voice/biometrics/register",
        json={"user_id": "test_user", "audio_base64": b64_sample_1},
        headers=headers
    )
    assert res_reg.status_code == 200
    assert res_reg.json()["status"] == "success"

    # Status endpoint
    res_stat = client.get("/api/voice/biometrics/status", headers=headers)
    assert res_stat.status_code == 200
    assert "test_user" in res_stat.json()["biometrics"]["enrolled_users"]

    # Verify matching voiceprint
    res_ver_1 = client.post(
        "/api/voice/biometrics/verify",
        json={"user_id": "test_user", "audio_base64": b64_sample_1},
        headers=headers
    )
    assert res_ver_1.status_code == 200
    assert res_ver_1.json()["verified"] is True
    assert res_ver_1.json()["similarity_score"] >= 0.9

    # Verify non-matching voiceprint
    res_ver_2 = client.post(
        "/api/voice/biometrics/verify",
        json={"user_id": "test_user", "audio_base64": b64_sample_2},
        headers=headers
    )
    assert res_ver_2.status_code == 200
    # Different audio payload produces distinct embedding
    assert res_ver_2.json()["similarity_score"] < 0.95

    # Reset endpoint
    res_reset = client.delete("/api/voice/biometrics/reset", headers=headers)
    assert res_reset.status_code == 200
    assert res_reset.json()["result"]["enrolled_count"] == 0
