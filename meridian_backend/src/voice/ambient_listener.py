"""
meridian_backend/src/voice/ambient_listener.py — PL-02 Production Backend Module
Continuous Ambient Listener with VAD & Speech Stream
"""

import asyncio
import logging
import time
from collections.abc import Callable
from typing import Any

logger = logging.getLogger("meridian_ambient_listener")

_RECENT_SPEECH_LOGS: list[dict[str, Any]] = []
_MAX_LOGS = 50


class ContinuousAmbientListener:
    """
    Background ambient audio listener with energy/VAD filtering
    and continuous speech transcription.
    """

    def __init__(self, sample_rate: int = 16000, energy_threshold: float = 300.0):
        self.sample_rate = sample_rate
        self.energy_threshold = energy_threshold
        self.is_listening = False
        self.listeners: list[Callable[[dict[str, Any]], None]] = []
        self._loop_task: asyncio.Task | None = None

    def add_speech_callback(self, callback: Callable[[dict[str, Any]], None]):
        """Register callback for transcribed ambient speech events."""
        self.listeners.append(callback)

    def is_speech_chunk(self, audio_data: bytes) -> bool:
        """Silero neural VAD calculation for raw PCM audio data with heuristic fallback."""
        if not audio_data:
            return False
        # Calculate RMS energy first for baseline silence detection
        try:
            import struct
            samples = struct.unpack(f"<{len(audio_data)//2}h", audio_data)
            if not samples:
                return False
            sum_squares = sum(s * s for s in samples)
            rms = (sum_squares / len(samples)) ** 0.5
            if rms < 5.0:  # Absolute silence
                return False
        except Exception:
            rms = 0.0

        # Try Silero neural VAD
        try:
            from src.voice.vad import get_silero_detector
            silero = get_silero_detector()
            if silero.get_speech_probability(audio_data) >= 0.5:
                return True
        except Exception as e:
            logger.debug("[AmbientListener] Silero check fallback: %s", e)

        # Fallback to energy threshold
        return rms > self.energy_threshold if rms > 0.0 else len(audio_data) > 3200


    async def process_audio_segment(self, audio_bytes: bytes, speaker_hint: str = "ambient") -> dict[str, Any]:
        """Transcribe incoming raw audio segment."""
        from src.voice.stt import transcribe_audio

        timestamp = time.time()
        is_speech = self.is_speech_chunk(audio_bytes)

        if not is_speech:
            return {
                "success": True,
                "speech_detected": False,
                "text": "",
                "timestamp": timestamp
            }

        # Transcribe audio segment
        try:
            transcript = await transcribe_audio(audio_bytes)
        except Exception as exc:
            logger.warning("[AmbientListener] STT error: %s", exc)
            transcript = ""

        result = {
            "success": True,
            "speech_detected": True,
            "text": transcript.strip() if transcript else "",
            "speaker": speaker_hint,
            "timestamp": timestamp
        }

        if result["text"]:
            _RECENT_SPEECH_LOGS.append(result)
            if len(_RECENT_SPEECH_LOGS) > _MAX_LOGS:
                _RECENT_SPEECH_LOGS.pop(0)

            for cb in self.listeners:
                try:
                    if asyncio.iscoroutinefunction(cb):
                        await cb(result)
                    else:
                        cb(result)
                except Exception as ex:
                    logger.warning("[AmbientListener] Callback error: %s", ex)

        return result

    async def start(self):
        """Start ambient listening loop."""
        self.is_listening = True
        logger.info("[AmbientListener] Continuous ambient listening active.")

    async def stop(self):
        """Stop ambient listening loop."""
        self.is_listening = False
        if self._loop_task:
            self._loop_task.cancel()
        logger.info("[AmbientListener] Continuous ambient listening stopped.")


_global_ambient_listener = ContinuousAmbientListener()


def get_ambient_listener() -> ContinuousAmbientListener:
    return _global_ambient_listener


def get_recent_ambient_transcripts(limit: int = 10) -> list[dict[str, Any]]:
    """Return recent ambient speech logs."""
    return _RECENT_SPEECH_LOGS[-limit:]
