import threading
import time
import os
import sys
import logging
from typing import Optional, Tuple, Any
import numpy as np
logger = logging.getLogger(__name__)

try:
    import sounddevice as sd
except Exception as err:
    logger.warning("sounddevice module not available for wakeword: %s", err)
    sd = None
from src.core.proactive import publish_nudge_sync

WAKEWORD_ACTIVE = False
WAKEWORD_PAUSED = False
_thread = None

CONTINUOUS_WINDOW_ACTIVE = False
CONTINUOUS_WINDOW_EXPIRES_AT = 0.0
CONTINUOUS_WINDOW_DURATION = 10.0

def trigger_continuous_window(duration: float = 10.0):
    """Activates follow-up listening mode for duration seconds."""
    global CONTINUOUS_WINDOW_ACTIVE, CONTINUOUS_WINDOW_EXPIRES_AT, CONTINUOUS_WINDOW_DURATION
    CONTINUOUS_WINDOW_DURATION = duration
    CONTINUOUS_WINDOW_EXPIRES_AT = time.time() + duration
    CONTINUOUS_WINDOW_ACTIVE = True
    logger.info("[Wake Word] Continuous listening window triggered for %s seconds.", duration)

def extend_continuous_window(extra_seconds: float = 3.0):
    """Dynamically extends the continuous listening window upon detected user speech."""
    global CONTINUOUS_WINDOW_ACTIVE, CONTINUOUS_WINDOW_EXPIRES_AT
    if not CONTINUOUS_WINDOW_ACTIVE:
        trigger_continuous_window(extra_seconds)
    else:
        CONTINUOUS_WINDOW_EXPIRES_AT = max(CONTINUOUS_WINDOW_EXPIRES_AT, time.time()) + extra_seconds
        logger.debug("[Wake Word] Continuous listening window extended by %s seconds.", extra_seconds)

def is_continuous_window_active() -> bool:
    """Returns True if continuous listening window is currently active and unexpired."""
    global CONTINUOUS_WINDOW_ACTIVE, CONTINUOUS_WINDOW_EXPIRES_AT
    if not CONTINUOUS_WINDOW_ACTIVE:
        return False
    if time.time() >= CONTINUOUS_WINDOW_EXPIRES_AT:
        CONTINUOUS_WINDOW_ACTIVE = False
        return False
    return True

def cancel_continuous_window():
    """Cancels continuous listening mode immediately."""
    global CONTINUOUS_WINDOW_ACTIVE, CONTINUOUS_WINDOW_EXPIRES_AT
    CONTINUOUS_WINDOW_ACTIVE = False
    CONTINUOUS_WINDOW_EXPIRES_AT = 0.0
    logger.info("[Wake Word] Continuous listening window cancelled.")

def get_continuous_window_remaining() -> float:
    """Returns remaining seconds for continuous listening window."""
    global CONTINUOUS_WINDOW_ACTIVE, CONTINUOUS_WINDOW_EXPIRES_AT
    if not is_continuous_window_active():
        return 0.0
    return max(0.0, CONTINUOUS_WINDOW_EXPIRES_AT - time.time())

_last_trigger_time: float = 0.0

def is_in_debounce_cooldown(cooldown_sec: float = 1.0) -> bool:
    """Returns True if within debounce cooldown period to prevent echo double-triggers."""
    global _last_trigger_time
    return (time.time() - _last_trigger_time) < cooldown_sec

def get_input_device_index() -> Optional[int]:
    """Resolves target input device index from user profile with graceful fallback to default."""
    if sd is None:
        return None
    try:
        from database import get_user_profile
        configured = get_user_profile("audio_input_device")
        if not configured:
            return None
        devices = sd.query_devices()
        target = str(configured).strip().lower()
        for idx, dev in enumerate(devices):
            if dev.get("max_input_channels", 0) > 0:
                dev_name = str(dev.get("name", "")).strip().lower()
                if target in dev_name or str(idx) == target:
                    return idx
    except Exception as e:
        logger.debug("[Wake Word] Audio device lookup exception: %s", e)
    return None


def start_wakeword_monitoring():
    """Starts the background wake word monitoring thread."""
    global WAKEWORD_ACTIVE, _thread
    if sd is None:
        logger.warning("[Wake Word] sounddevice unavailable on this platform. Monitoring disabled.")
        return
    if WAKEWORD_ACTIVE:
        return
    WAKEWORD_ACTIVE = True
    _thread = threading.Thread(target=_listen_loop, daemon=True)
    _thread.start()
    logger.info("[Wake Word] Background monitoring thread started.")

def stop_wakeword_monitoring():
    """Stops the background wake word monitoring thread."""
    global WAKEWORD_ACTIVE
    WAKEWORD_ACTIVE = False
    logger.info("[Wake Word] Background monitoring thread stopped.")

def pause_wakeword():
    """Pauses the wake word monitoring to avoid mic sharing conflicts."""
    global WAKEWORD_PAUSED
    WAKEWORD_PAUSED = True
    logger.info("[Wake Word] Paused monitoring.")

def resume_wakeword():
    """Resumes the wake word monitoring."""
    global WAKEWORD_PAUSED
    WAKEWORD_PAUSED = False
    logger.info("[Wake Word] Resumed monitoring.")

def resolve_wakeword_model(wakeword_filename: str = "hey_meridian.onnx") -> Tuple[Optional[str], str]:
    """
    Resolves the wake word model path with graceful fallback cascade:
    1. Custom ONNX file (absolute or workspace root).
    2. Built-in openWakeWord pre-trained model.
    3. Silero VAD / Heuristic energy detection fallback.
    """
    if os.path.isabs(wakeword_filename) and os.path.exists(wakeword_filename):
        return wakeword_filename, "custom"

    if getattr(sys, 'frozen', False):
        base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        onnx_path = os.path.join(base_dir, wakeword_filename)
    else:
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        root_dir = os.path.dirname(backend_dir)
        onnx_path = os.path.join(root_dir, wakeword_filename)

    if os.path.exists(onnx_path):
        return onnx_path, "custom"

    logger.warning("[Wake Word] Custom model not found at '%s'. Falling back to built-in openWakeWord / VAD cascade.", onnx_path)
    try:
        import openwakeword  # type: ignore
        return None, "builtin"
    except ImportError:
        pass

    return None, "silero_vad"


def evaluate_audio_chunk(
    audio_data: np.ndarray,
    sample_rate: int = 16000,
    engine: str = "silero_vad",
    oww_model: Optional[Any] = None
) -> float:
    """Evaluates audio chunk using openWakeWord or neural Silero VAD detector with graceful fallback."""
    if oww_model is not None:
        try:
            predictions = oww_model.predict(audio_data)
            return max(predictions.values()) if predictions else 0.0
        except Exception as e:
            logger.debug("[Wake Word] openWakeWord predict failed: %s", e)

    if engine == "silero_vad" or oww_model is None:
        try:
            from src.voice.vad import get_silero_detector
            silero = get_silero_detector()
            return float(silero.get_speech_probability(audio_data, sample_rate))
        except Exception as e:
            logger.debug("[Wake Word] Silero VAD neural check failed (%s). Falling back to RMS.", e)
            rms = np.sqrt(np.mean(audio_data.astype(np.float32) ** 2))
            return 0.85 if rms > 1500.0 else 0.0

    return 0.0


def _listen_loop():
    global WAKEWORD_ACTIVE, WAKEWORD_PAUSED, _last_trigger_time
    if sd is None:
        WAKEWORD_ACTIVE = False
        return
    
    wakeword_filename = "hey_meridian.onnx"
    try:
        from database import get_user_profile
        custom_filename = get_user_profile("wakeword_model_filename")
        if custom_filename:
            wakeword_filename = str(custom_filename)
    except (ImportError, KeyError, ValueError, AttributeError) as err:
        logger.debug("Using default wakeword filename: %s", err)

    onnx_path, engine = resolve_wakeword_model(wakeword_filename)
    oww_model = None

    if engine in ("custom", "builtin"):
        try:
            from openwakeword.model import Model  # type: ignore
            if engine == "custom" and onnx_path:
                oww_model = Model(wakeword_models=[onnx_path])
            else:
                oww_model = Model()
        except Exception as e:
            logger.warning("[Wake Word] Failed to load openwakeword model: %s. Falling back to VAD.", e)
            engine = "silero_vad"
            oww_model = None

    if oww_model is None and engine != "silero_vad":
        engine = "silero_vad"
        
    sample_rate = 16000
    chunk_size = 1280
    
    threshold = 0.6
    wakeword_phrase_val = "Hey Meridian"
    try:
        from database import get_user_profile
        t_val = get_user_profile("wakeword_threshold")
        if t_val is not None:
            threshold = float(t_val)
        custom_phrase = get_user_profile("wakeword_phrase")
        if custom_phrase:
            wakeword_phrase_val = str(custom_phrase)
    except Exception:
        pass

    while WAKEWORD_ACTIVE:
        if WAKEWORD_PAUSED:
            time.sleep(0.2)
            continue
            
        try:
            if sd is None:
                break
            device_idx = get_input_device_index()
            with sd.InputStream(device=device_idx, samplerate=sample_rate, channels=1, dtype='int16') as stream:
                logger.info("[Wake Word] Audio stream opened successfully (Device: %s, Engine: %s). Monitoring for '%s'...", device_idx, engine, wakeword_phrase_val)
                while WAKEWORD_ACTIVE:
                    if WAKEWORD_PAUSED:
                        break
                        
                    chunk, overflow = stream.read(chunk_size)
                    audio_data = chunk.flatten()
                    
                    score = evaluate_audio_chunk(audio_data, sample_rate=sample_rate, engine=engine, oww_model=oww_model)

                    if is_continuous_window_active():
                        if score > 0.4:
                            extend_continuous_window(2.0)
                        logger.info("[Wake Word] Continuous conversation window active! Triggering follow-up voice command.")
                        cancel_continuous_window()
                        _last_trigger_time = time.time()
                        pause_wakeword()
                        try:
                            from src.voice.tts import stop_active_tts
                            stop_active_tts()
                        except Exception:
                            pass
                        publish_nudge_sync(
                            nudge_type="wakeword",
                            title="🎙️ Continuous Follow-Up Listening",
                            message="Continuous conversation window active. Listening...",
                            action_hint="Listening for follow-up voice command...",
                            icon="🎙️",
                            mascot_state="happy",
                            action="start_voice_command"
                        )
                        break

                    if score > threshold:
                        if is_in_debounce_cooldown(cooldown_sec=1.5):
                            time.sleep(0.01)
                            continue

                        logger.info("[Wake Word] Wake trigger '%s' detected (score=%.3f, engine=%s)! Pausing and triggering action.", wakeword_phrase_val, score, engine)
                        _last_trigger_time = time.time()
                        pause_wakeword()
                        try:
                            from src.voice.tts import stop_active_tts
                            stop_active_tts()
                        except Exception:
                            pass
                        
                        publish_nudge_sync(
                            nudge_type="wakeword",
                            title="🎙️ Wake Word Detected",
                            message=f"Wake word '{wakeword_phrase_val}' detected. Listening...",
                            action_hint="Listening for voice command...",
                            icon="🎙️",
                            mascot_state="happy",
                            action="start_voice_command"
                        )
                        break
                    
                    time.sleep(0.01)
                    
        except Exception as e:
            logger.error("[Wake Word] Audio stream error: %s. Retrying in 5 seconds...", e)
            time.sleep(5.0)
