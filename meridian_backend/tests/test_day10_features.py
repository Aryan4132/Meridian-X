"""
meridian_backend/tests/test_day10_features.py
Verification Test Suite for Day 10 Ambient Perception & Multimodal Vision/Screen Context
"""

import sys
import pytest
import asyncio
from unittest.mock import AsyncMock, patch, MagicMock

# Ensure meridian_backend is in sys.path
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.mark.asyncio
async def test_multimodal_vision():
    """Test vision.py provider-aware multimodal screen vision fallback."""
    from src.core.vision import analyze_screen_multimodal
    import tempfile
    from PIL import Image

    dummy_path = tempfile.mktemp(suffix=".png", prefix="test_vision_")
    try:
        img = Image.new("RGB", (200, 200), color="blue")
        img.save(dummy_path)

        # Test fallback to mock when no API keys are present
        with patch.dict(os.environ, {}, clear=True):
            res = await analyze_screen_multimodal(
                prompt="Test prompt",
                crop_box={"left": 0, "top": 0, "width": 100, "height": 100},
                image_path=dummy_path
            )
            assert res["success"] is True
            assert res["provider"] in ["mock", "ollama"]
            assert "analysis" in res
    finally:
        if os.path.exists(dummy_path):
            os.remove(dummy_path)



def test_active_window_sense():
    """Test screen_sense.py active window metadata tracking."""
    from src.core.screen_sense import get_active_window_metadata, ScreenSenseTracker

    meta = get_active_window_metadata()
    assert isinstance(meta, dict)
    assert "title" in meta
    assert "process" in meta
    assert "pid" in meta

    tracker = ScreenSenseTracker()
    key = tracker.get_window_key(meta)
    assert isinstance(key, str)


@pytest.mark.asyncio
async def test_ambient_listener():
    """Test ambient_listener.py VAD audio processing and speech event callback."""
    from src.voice.ambient_listener import get_ambient_listener, get_recent_ambient_transcripts

    listener = get_ambient_listener()
    callback_fired = []

    def mock_callback(data):
        callback_fired.append(data)

    listener.add_speech_callback(mock_callback)

    # Silent audio bytes
    silent_pcm = b"\x00" * 3200
    res_silent = await listener.process_audio_segment(silent_pcm)
    assert res_silent["speech_detected"] is False

    # Loud dummy audio bytes triggering VAD
    loud_pcm = b"\x7f\x7f" * 3200
    with patch("src.voice.stt.transcribe_audio", new=AsyncMock(return_value="hello assistant help me")):
        res_speech = await listener.process_audio_segment(loud_pcm)
        assert res_speech["speech_detected"] is True
        assert "hello" in res_speech["text"]
        assert len(callback_fired) > 0

    transcripts = get_recent_ambient_transcripts()
    assert isinstance(transcripts, list)


def test_vision_face_presence():
    """Test vision_face.py face registration and presence status."""
    from src.core.vision_face import get_presence_state, register_user_face, process_face_frame

    reg = register_user_face("test_user")
    assert reg["success"] is True
    assert reg["user_id"] == "test_user"

    frame_state = process_face_frame()
    assert frame_state["status"] in ["present", "away"]
    assert "emotion" in frame_state

    current = get_presence_state()
    assert current["status"] in ["present", "away"]


@pytest.mark.asyncio
async def test_proactive_nudge_synthesis():
    """Test proactive.py multi-modal nudge synthesizer."""
    from src.core.proactive import synthesize_ambient_nudge

    with patch("src.core.vision_face.get_presence_state", return_value={"emotion": "fatigued", "status": "present"}):
        res = await synthesize_ambient_nudge()
        assert res["nudge_issued"] is True
        assert res["nudge_type"] == "fatigue_alert"


def test_predictive_context_prewarmer():
    """Test predictive_engine.py habit recording and developer context prewarming."""
    from src.core.predictive_engine import prewarm_dev_context, predict_next_action, get_habit_profile

    res = prewarm_dev_context("code.exe", "VS Code — main.py")
    assert res["recorded"] == "code.exe:VS Code — main.py"
    assert res["prewarmed"]["prewarmed"] is True

    profile = get_habit_profile()
    assert "transitions" in profile
    assert profile["last_active_app"] == "code.exe:VS Code — main.py"

    prediction = predict_next_action()
    assert "suggested_action" in prediction


def test_tool_registry_day10_integration():
    """Test registry.py registration of Day 10 tools."""
    from src.tools.registry import TOOL_REGISTRY

    assert "analyze_active_screen" in TOOL_REGISTRY
    assert "get_active_window_sense" in TOOL_REGISTRY
    assert "get_presence_state" in TOOL_REGISTRY
    assert "get_ambient_speech_context" in TOOL_REGISTRY
    assert "synthesize_ambient_nudge" in TOOL_REGISTRY
