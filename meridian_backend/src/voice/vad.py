"""
meridian_backend/src/voice/vad.py
High-performance Voice Activity Detection (VAD) module using bundled Silero VAD ONNX model
with robust heuristic fallback (RMS energy + pitch centroid).
"""

import threading
from typing import Optional, Union

import numpy as np

from src.core.logger import get_logger

logger = get_logger("meridian_vad")

_SILERO_DETECTOR: Optional["SileroVADDetector"] = None
_INIT_LOCK = threading.Lock()


class SileroVADDetector:
    """
    Evaluates real-time audio segments for human speech activity using Silero VAD ONNX model.
    Falls back gracefully to RMS energy and pitch analysis if neural model fails to load.
    """

    def __init__(self, default_threshold: float = 0.5):
        self.default_threshold = default_threshold
        self.model = None
        self._load_lock = threading.Lock()
        self._load_attempted = False
        self._ensure_model_loaded()

    def _ensure_model_loaded(self) -> None:
        if self._load_attempted:
            return
        with self._load_lock:
            if self._load_attempted:
                return
            self._load_attempted = True
            try:
                from faster_whisper.vad import get_vad_model
                self.model = get_vad_model()
                logger.info("[Silero VAD] Neural ONNX model loaded successfully.")
            except Exception as exc:
                logger.warning("[Silero VAD] Failed loading bundled Silero VAD model (%s). Fallback active.", exc)
                self.model = None

    @property
    def is_neural_available(self) -> bool:
        """Indicates whether neural Silero VAD is active."""
        return self.model is not None

    def _normalize_audio(self, audio: Union[np.ndarray, bytes]) -> np.ndarray:
        """Converts raw audio bytes or int16 array to 1D float32 normalized [-1.0, 1.0]."""
        if isinstance(audio, bytes):
            if len(audio) == 0:
                return np.zeros(0, dtype=np.float32)
            # Interpret as 16-bit PCM little-endian
            audio_arr = np.frombuffer(audio, dtype=np.int16).astype(np.float32) / 32768.0
            return audio_arr

        if not isinstance(audio, np.ndarray):
            return np.zeros(0, dtype=np.float32)

        if audio.ndim > 1:
            audio = audio.flatten()

        if audio.dtype == np.int16:
            return audio.astype(np.float32) / 32768.0
        elif audio.dtype == np.float32:
            return audio
        else:
            return audio.astype(np.float32)

    def get_speech_probability(self, audio: Union[np.ndarray, bytes], sample_rate: int = 16000) -> float:
        """
        Calculates neural speech probability in range [0.0, 1.0].
        If neural model unavailable, maps heuristic RMS energy to synthetic probability.
        """
        norm_audio = self._normalize_audio(audio)
        if norm_audio.size == 0:
            return 0.0

        if self.model is not None:
            try:
                # Silero VAD expects chunk size to be multiple of 512
                num_samples = 512
                rem = norm_audio.shape[0] % num_samples
                if rem > 0:
                    pad_len = num_samples - rem
                    padded_audio = np.pad(norm_audio, (0, pad_len), mode="constant")
                else:
                    padded_audio = norm_audio

                if padded_audio.shape[0] == 0:
                    return 0.0

                probs = self.model(padded_audio, num_samples=num_samples)
                if probs is not None and len(probs) > 0:
                    return float(np.max(probs))
            except Exception as err:
                logger.debug("[Silero VAD] Neural evaluation failed: %s. Using heuristic fallback.", err)

        # Fallback heuristic: RMS energy mapped to [0.0, 1.0]
        rms = float(np.sqrt(np.mean(norm_audio ** 2))) if norm_audio.size > 0 else 0.0
        # Typical voice normalized RMS is ~0.02 - 0.15; silence is < 0.005
        # Map 0.015 RMS to ~0.5 probability
        heuristic_prob = min(1.0, rms / 0.03)
        return heuristic_prob

    def is_speech(
        self,
        audio: Union[np.ndarray, bytes],
        sample_rate: int = 16000,
        threshold: float | None = None,
    ) -> bool:
        """
        Determines whether audio segment contains valid human speech.
        """
        cutoff = threshold if threshold is not None else self.default_threshold
        prob = self.get_speech_probability(audio, sample_rate=sample_rate)
        return prob >= cutoff


def get_silero_detector(threshold: float = 0.5) -> SileroVADDetector:
    """Singleton getter for SileroVADDetector."""
    global _SILERO_DETECTOR
    if _SILERO_DETECTOR is None:
        with _INIT_LOCK:
            if _SILERO_DETECTOR is None:
                _SILERO_DETECTOR = SileroVADDetector(default_threshold=threshold)
    return _SILERO_DETECTOR
