"""
meridian_backend/tests/test_silero_vad.py
Comprehensive Verification Test Suite for Silero VAD Integration across
Whisper STT, Duplex Engine, and Continuous Ambient Listener.
"""

import os
import sys
from unittest.mock import MagicMock, patch

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import src.voice.stt as stt_module
from src.voice.ambient_listener import ContinuousAmbientListener
from src.voice.duplex import DuplexVoiceEngine
from src.voice.vad import SileroVADDetector, get_silero_detector


def test_silero_detector_singleton_and_loading():
    """Verify SileroVADDetector initializes and caches singleton instance."""
    detector = get_silero_detector()
    assert detector is not None
    assert isinstance(detector, SileroVADDetector)
    # Bundled faster_whisper neural model should be active
    assert detector.is_neural_available is True


def test_silero_silence_rejection():
    """Verify that pure silence yields negligible speech probability."""
    detector = get_silero_detector()
    silence_pcm = np.zeros(16000, dtype=np.float32)
    prob = detector.get_speech_probability(silence_pcm)
    assert prob < 0.15
    assert detector.is_speech(silence_pcm) is False

    # Also test with raw zero bytes
    zero_bytes = b"\x00" * 3200
    assert detector.is_speech(zero_bytes) is False


def test_silero_heuristic_fallback():
    """Verify graceful fallback when neural model is absent."""
    detector = SileroVADDetector()
    detector.model = None  # Force fallback
    assert detector.is_neural_available is False

    # Quiet signal
    quiet = np.zeros(1000, dtype=np.float32)
    assert detector.get_speech_probability(quiet) == 0.0
    assert detector.is_speech(quiet) is False

    # Loud synthetic audio
    loud = np.ones(1000, dtype=np.float32) * 0.5
    prob_loud = detector.get_speech_probability(loud)
    assert prob_loud > 0.5
    assert detector.is_speech(loud) is True


def test_transcribe_audio_array_passes_vad_filter():
    """Verify transcribe_audio_array calls faster-whisper with vad_filter=True."""
    mock_model = MagicMock()
    mock_segment = MagicMock()
    mock_segment.text = "Testing Silero VAD filter"
    mock_model.transcribe.return_value = ([mock_segment], None)

    with patch.object(stt_module, "get_whisper_model", return_value=mock_model):
        dummy_audio = np.zeros(16000, dtype=np.float32)
        res = stt_module.transcribe_audio_array(dummy_audio)

        assert res == "Testing Silero VAD filter"
        mock_model.transcribe.assert_called_once()
        _, kwargs = mock_model.transcribe.call_args
        assert kwargs.get("vad_filter") is True


def test_transcribe_audio_file_passes_vad_filter(tmp_path):
    """Verify transcribe_audio_file calls faster-whisper with vad_filter=True."""
    dummy_wav = tmp_path / "sample.wav"
    dummy_wav.write_bytes(b"RIFF" + b"\x00" * 40)

    mock_model = MagicMock()
    mock_segment = MagicMock()
    mock_segment.text = "File transcription verified"
    mock_model.transcribe.return_value = ([mock_segment], None)

    with patch.object(stt_module, "get_whisper_model", return_value=mock_model):
        res = stt_module.transcribe_audio_file(str(dummy_wav))

        assert res == "File transcription verified"
        mock_model.transcribe.assert_called_once()
        _, kwargs = mock_model.transcribe.call_args
        assert kwargs.get("vad_filter") is True


def test_duplex_barge_in_neural_and_rms():
    """Verify DuplexVoiceEngine handles both raw audio frames and RMS values for barge-in."""
    engine = DuplexVoiceEngine(vad_threshold=200.0)
    engine.start_duplex_session()
    engine.set_speaking_state(True)

    barge_in_called = []
    engine.on_barge_in_callback = lambda: barge_in_called.append(True)

    # Low RMS float should not trigger
    assert not engine.check_barge_in(50.0)
    assert engine.state == "speaking"

    # Silent audio array should not trigger
    silence = np.zeros(1600, dtype=np.float32)
    assert not engine.check_barge_in(silence)
    assert engine.state == "speaking"

    # High RMS float should trigger
    assert engine.check_barge_in(300.0)
    assert engine.state == "interrupted"
    assert len(barge_in_called) == 1

    # Reset and test audio bytes triggering barge-in via mocked detector
    engine.set_speaking_state(True)
    with patch("src.voice.vad.SileroVADDetector.get_speech_probability", return_value=0.85):
        assert engine.check_barge_in(b"\x01\x02" * 800)
        assert engine.state == "interrupted"


def test_ambient_listener_silero_filtering():
    """Verify ContinuousAmbientListener uses Silero VAD for speech detection."""
    listener = ContinuousAmbientListener(energy_threshold=300.0)

    # Empty and absolute silent audio
    assert listener.is_speech_chunk(b"") is False
    assert listener.is_speech_chunk(b"\x00" * 3200) is False

    # Loud speech segment should trigger
    with patch("src.voice.vad.SileroVADDetector.get_speech_probability", return_value=0.9):
        speech_bytes = b"\x20\x10" * 1600
        assert listener.is_speech_chunk(speech_bytes) is True
