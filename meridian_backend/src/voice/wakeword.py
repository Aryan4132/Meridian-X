import threading
import time
import os
import numpy as np
import sounddevice as sd
from openwakeword.model import Model
from src.core.proactive import publish_nudge_sync

WAKEWORD_ACTIVE = False
WAKEWORD_PAUSED = False
_thread = None

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
    
    backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    root_dir = os.path.dirname(backend_dir)
    onnx_path = os.path.join(root_dir, "hey_meridian.onnx")
    
    if not os.path.exists(onnx_path):
        print(f"[Wake Word] Custom model not found at {onnx_path}. Wake word monitoring disabled.")
        WAKEWORD_ACTIVE = False
        return
        
    try:
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
                    
                    predictions = oww_model.predict(audio_data)
                    score = predictions.get('hey_meridian', 0.0)
                    
                    if score > 0.6:
                        print(f"[Wake Word] Wake word detected with score {score:.3f}! Pausing and triggering action.")
                        pause_wakeword()
                        
                        publish_nudge_sync(
                            nudge_type="wakeword",
                            title="🎙️ Wake Word Detected",
                            message="Wake word 'Hey Meridian' detected. Listening...",
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
