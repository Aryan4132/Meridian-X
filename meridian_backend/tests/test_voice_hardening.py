import pytest
import time
import numpy as np
from unittest.mock import patch, MagicMock
import os
import sys

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

import src.voice.wakeword as ww


def test_continuous_window_extension():
    """Verify extending continuous window prolongs the active listening period."""
    ww.cancel_continuous_window()
    assert ww.is_continuous_window_active() is False

    ww.trigger_continuous_window(duration=2.0)
    assert ww.is_continuous_window_active() is True
    initial_remaining = ww.get_continuous_window_remaining()

    # Extend by 3 seconds
    ww.extend_continuous_window(3.0)
    extended_remaining = ww.get_continuous_window_remaining()
    assert extended_remaining > initial_remaining + 1.5

    ww.cancel_continuous_window()
    assert ww.is_continuous_window_active() is False


def test_get_input_device_index_resolution():
    """Verify resolution of audio input devices with graceful fallback."""
    fake_devices = [
        {"name": "Default Mic", "max_input_channels": 2, "index": 0},
        {"name": "USB Studio Mic", "max_input_channels": 1, "index": 1},
    ]

    # Case 1: Configured device matches
    with patch("sounddevice.query_devices", return_value=fake_devices), \
         patch("database.get_user_profile", return_value="USB Studio Mic"):
        idx = ww.get_input_device_index()
        assert idx == 1

    # Case 2: Configured device not found -> fallback to None (system default)
    with patch("sounddevice.query_devices", return_value=fake_devices), \
         patch("database.get_user_profile", return_value="Non-existent Bluetooth"):
        idx = ww.get_input_device_index()
        assert idx is None


def test_silero_vad_integration_fallback():
    """Verify Silero VAD detector evaluates speech probability in wakeword loop."""
    fake_audio = np.zeros(1280, dtype=np.int16)

    with patch("src.voice.vad.get_silero_detector") as mock_get_det:
        mock_detector = MagicMock()
        mock_detector.get_speech_probability.return_value = 0.92
        mock_get_det.return_value = mock_detector

        score = ww.evaluate_audio_chunk(
            audio_data=fake_audio,
            sample_rate=16000,
            engine="silero_vad",
            oww_model=None
        )
        assert score == 0.92
        mock_detector.get_speech_probability.assert_called_once()


def test_post_trigger_debounce_cooldown():
    """Verify wakeword cooldown suppresses immediate echo re-triggers."""
    ww._last_trigger_time = time.time()
    # Immediately after trigger, debounce is active
    assert ww.is_in_debounce_cooldown(cooldown_sec=1.0) is True

    # After cooldown expires, debounce is inactive
    ww._last_trigger_time = time.time() - 2.0
    assert ww.is_in_debounce_cooldown(cooldown_sec=1.0) is False
