import os
import sys
import time
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api import app
from src.core.auth import API_KEY
from src.voice.wakeword import (
    trigger_continuous_window,
    is_continuous_window_active,
    cancel_continuous_window,
    get_continuous_window_remaining
)

client = TestClient(app)
headers = {"X-API-Key": API_KEY}

def test_wakeword_continuous_state():
    cancel_continuous_window()
    assert not is_continuous_window_active()
    assert get_continuous_window_remaining() == 0.0

    trigger_continuous_window(duration=2.0)
    assert is_continuous_window_active()
    remaining = get_continuous_window_remaining()
    assert 0.0 < remaining <= 2.0

    cancel_continuous_window()
    assert not is_continuous_window_active()
    assert get_continuous_window_remaining() == 0.0

def test_wakeword_continuous_expiration():
    cancel_continuous_window()
    trigger_continuous_window(duration=0.1)
    assert is_continuous_window_active()
    time.sleep(0.15)
    assert not is_continuous_window_active()
    assert get_continuous_window_remaining() == 0.0

def test_continuous_window_api_endpoints():
    cancel_continuous_window()

    # Test status initial
    res_status = client.get("/api/voice/continuous-window/status", headers=headers)
    assert res_status.status_code == 200
    assert res_status.json()["active"] is False

    # Test start endpoint
    res_start = client.post("/api/voice/continuous-window/start?duration=5.0", headers=headers)
    assert res_start.status_code == 200
    data_start = res_start.json()
    assert data_start["status"] == "success"
    assert data_start["remaining_seconds"] > 0.0

    # Test status active
    res_status_active = client.get("/api/voice/continuous-window/status", headers=headers)
    assert res_status_active.status_code == 200
    assert res_status_active.json()["active"] is True

    # Test cancel endpoint
    res_cancel = client.post("/api/voice/continuous-window/cancel", headers=headers)
    assert res_cancel.status_code == 200
    assert res_cancel.json()["status"] == "success"

    # Test status after cancel
    res_status_final = client.get("/api/voice/continuous-window/status", headers=headers)
    assert res_status_final.status_code == 200
    assert res_status_final.json()["active"] is False
