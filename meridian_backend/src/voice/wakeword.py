import threading
import time
import os
import numpy as np
import sounddevice as sd
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
    print(f"[Wake Word] Continuous listening window triggered for {duration} seconds.")

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
    print("[Wake Word] Continuous listening window cancelled.")

def get_continuous_window_remaining() -> float:
    """Returns remaining seconds for continuous listening window."""
    global CONTINUOUS_WINDOW_ACTIVE, CONTINUOUS_WINDOW_EXPIRES_AT
    if not is_continuous_window_active():
        return 0.0
    return max(0.0, CONTINUOUS_WINDOW_EXPIRES_AT - time.time())


def start_wakeword_monitoring():
    """Starts the background wake word monitoring thread."""
    global WAKEWORD_ACTIVE, _thread
    if WAKEWORD_ACTIVE:
        return
    WAKEWORD_ACTIVE = True
    _thread = threading.Thread(target=_listen_loop, daemon=True)
    _thread.start()
    print("[Wake Word] Background monitoring thread started.")

def stop_wakeword_monitoring():
    """Stops the background wake word monitoring thread."""
    global WAKEWORD_ACTIVE
    WAKEWORD_ACTIVE = False
    print("[Wake Word] Background monitoring thread stopped.")

def pause_wakeword():
    """Pauses the wake word monitoring to avoid mic sharing conflicts."""
    global WAKEWORD_PAUSED
    WAKEWORD_PAUSED = True
    print("[Wake Word] Paused monitoring.")

def resume_wakeword():
    """Resumes the wake word monitoring."""
    global WAKEWORD_PAUSED
    WAKEWORD_PAUSED = False
    print("[Wake Word] Resumed monitoring.")

def _listen_loop():
    global WAKEWORD_ACTIVE, WAKEWORD_PAUSED
    
    wakeword_filename = "hey_meridian.onnx"
    try:
        from database import get_user_profile
        custom_filename = get_user_profile("wakeword_model_filename")
        if custom_filename:
            wakeword_filename = str(custom_filename)
    except Exception:
        pass

    if os.path.isabs(wakeword_filename) and os.path.exists(wakeword_filename):
        onnx_path = wakeword_filename
    else:
        if getattr(sys, 'frozen', False):
            base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))


            onnx_path = os.path.join(base_dir, wakeword_filename)
        else:
            backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            root_dir = os.path.dirname(backend_dir)
            onnx_path = os.path.join(root_dir, wakeword_filename)
    
    if not os.path.exists(onnx_path):
        print(f"[Wake Word] Custom model not found at {onnx_path}. Wake word monitoring disabled.")
        WAKEWORD_ACTIVE = False
        return
        
    try:
        from openwakeword.model import Model
        oww_model = Model(wakeword_models=[onnx_path])
    except Exception as e:
        print(f"[Wake Word] Failed to load openwakeword model: {e}")
        WAKEWORD_ACTIVE = False
        return
        
    sample_rate = 16000
    chunk_size = 1280
    
    while WAKEWORD_ACTIVE:
        if WAKEWORD_PAUSED:
            time.sleep(0.2)
            continue
            
        try:
            with sd.InputStream(samplerate=sample_rate, channels=1, dtype='int16') as stream:
                print("[Wake Word] Audio stream opened successfully. Monitoring for 'Hey Meridian'...")
                while WAKEWORD_ACTIVE:
                    if WAKEWORD_PAUSED:
                        break
                        
                    chunk, overflow = stream.read(chunk_size)
                    audio_data = chunk.flatten()
                    
                    if is_continuous_window_active():
                        print("[Wake Word] Continuous conversation window active! Triggering follow-up voice command.")
                        cancel_continuous_window()
                        pause_wakeword()
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

                    predictions = oww_model.predict(audio_data)

                    score = max(predictions.values()) if predictions else 0.0
                    
                    try:
                        from database import get_user_profile
                        threshold = get_user_profile("wakeword_threshold")
                        if threshold is None:
                            threshold = 0.6
                        else:
                            threshold = float(threshold)
                    except Exception:
                        threshold = 0.6

                    if score > threshold:
                        # Load custom wake word phrase from database profile
                        wakeword_phrase_val = "Hey Meridian"
                        try:
                            from database import get_user_profile
                            custom_phrase = get_user_profile("wakeword_phrase")
                            if custom_phrase:
                                wakeword_phrase_val = str(custom_phrase)
                        except Exception:
                            pass

                        print(f"[Wake Word] Wake word '{wakeword_phrase_val}' detected with score {score:.3f}! Pausing and triggering action.")
                        pause_wakeword()
                        
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
            print(f"[Wake Word] Audio stream error: {e}. Retrying in 5 seconds...")
            time.sleep(5.0)
