"""
duplex.py — Real-Time Full-Duplex Voice & Barge-In Engine (BK-11)
Provides low-latency continuous STT/TTS streaming with real-time speech interruption handling.
"""

import time
import asyncio
from typing import Dict, Any, Optional, Callable


class DuplexVoiceEngine:
    """Manages full-duplex real-time voice streaming with barge-in speech interruption."""

    def __init__(self, sample_rate: int = 16000, vad_threshold: float = 250.0):
        self.sample_rate = sample_rate
        self.vad_threshold = vad_threshold
        self.state = "idle" # idle | listening | speaking | interrupted
        self.is_active = False
        self._interrupted_flag = False
        self.on_barge_in_callback: Optional[Callable[[], None]] = None

    def start_duplex_session(self) -> str:
        """Starts a full-duplex voice session."""
        if self.is_active:
            return "Duplex session is already active."
        self.is_active = True
        self.state = "listening"
        self._interrupted_flag = False
        print(f"[Duplex Voice] Session started (VAD Threshold: {self.vad_threshold}). State: {self.state}")
        return "Duplex voice session initialized."

    def stop_duplex_session(self) -> str:
        """Stops the active full-duplex voice session."""
        self.is_active = False
        self.state = "idle"
        self._interrupted_flag = False
        print(f"[Duplex Voice] Session stopped.")
        return "Duplex voice session stopped."

    def check_barge_in(self, audio_chunk_rms: float) -> bool:
        """
        Checks if user audio energy exceeds threshold while assistant is speaking.
        Triggers instant speech cancellation if barge-in occurs.
        """
        if self.state == "speaking" and audio_chunk_rms > self.vad_threshold:
            print(f"[Duplex Voice] Barge-in detected (RMS: {audio_chunk_rms:.1f})! Interrupting TTS...")
            self.state = "interrupted"
            self._interrupted_flag = True
            if self.on_barge_in_callback:
                try:
                    self.on_barge_in_callback()
                except Exception as e:
                    print(f"[Duplex Voice] Error in barge-in callback: {e}")
            return True
        return False

    def set_speaking_state(self, is_speaking: bool) -> None:
        """Updates voice engine state to speaking or listening."""
        if not self.is_active:
            return
        if is_speaking:
            self.state = "speaking"
            self._interrupted_flag = False
        else:
            self.state = "listening"

    def get_status(self) -> Dict[str, Any]:
        """Returns current duplex voice engine diagnostic status."""
        return {
            "active": self.is_active,
            "state": self.state,
            "sample_rate": self.sample_rate,
            "vad_threshold": self.vad_threshold,
            "interrupted": self._interrupted_flag
        }
