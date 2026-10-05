import os
import io
import random
import tempfile
import base64
from typing import Optional
from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel
import soundfile as sf
import numpy as np

from src.api.deps import TTSRequest

router = APIRouter(tags=["voice"])

class BiometricRegisterRequest(BaseModel):
    user_id: Optional[str] = "default_user"
    audio_base64: str

class BiometricVerifyRequest(BaseModel):
    user_id: Optional[str] = "default_user"
    audio_base64: str

import src.api.voice as _self_voice

def get_tts_engine():
    import sys
    if "api" in sys.modules and hasattr(sys.modules["api"], "get_tts_engine") and sys.modules["api"].get_tts_engine is not get_tts_engine:
        res = sys.modules["api"].get_tts_engine()
        if res is not None:
            return res
    try:
        from src.voice.tts import get_tts_engine as get_engine
        return get_engine()
    except Exception as e:
        print("Failed to delegate/initialize Supertonic engine:", e)
        return None

@router.post("/api/tts")
def tts_synthesize(request: TTSRequest):
    import sys
    engine = None
    if "api" in sys.modules and hasattr(sys.modules["api"], "get_tts_engine"):
        engine = sys.modules["api"].get_tts_engine()
    if not engine:
        engine = get_tts_engine()


    if not engine:
        raise HTTPException(status_code=500, detail="Supertonic TTS engine not initialized")
    
    try:
        voice_name = request.voice if request.voice in ["F1", "F2", "F3", "F4", "F5", "M1", "M2", "M3", "M4", "M5"] else "M1"
        style = engine.get_voice_style(voice_name=voice_name)
        target_lang = request.lang if request.lang else "na"
        wav, duration = engine.synthesize(request.text, voice_style=style, lang=target_lang)
        
        sample_rate = getattr(engine, 'sample_rate', 24000)
        try:
            if hasattr(wav, 'numpy'):
                audio_data = wav.numpy().squeeze()
            elif isinstance(wav, np.ndarray):
                audio_data = wav.squeeze()
            else:
                audio_data = np.array(wav, dtype=np.float32).squeeze()
            
            buf = io.BytesIO()
            sf.write(buf, audio_data, samplerate=sample_rate, format='WAV')
            return Response(content=buf.getvalue(), media_type="audio/wav")
        except Exception:
            temp_dir = tempfile.gettempdir()
            temp_path = os.path.join(temp_dir, f"meridian_tts_{random.randint(1000, 9999)}.wav")
            engine.save_audio(wav, temp_path)
            with open(temp_path, mode="rb") as fh:
                wav_bytes = fh.read()
            try:
                os.remove(temp_path)
            except Exception:
                pass
            return Response(content=wav_bytes, media_type="audio/wav")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TTS synthesis failed: {str(e)}")

@router.get("/api/voice/onnx-models")
def get_onnx_models():
    """Scans project directory and user folders for available ONNX wake word model files."""
    scanned_models = []
    seen_paths = set()

    search_dirs = []
    backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    root_dir = os.path.dirname(backend_dir)
    search_dirs.extend([backend_dir, root_dir])

    home_dir = os.path.expanduser("~")
    if home_dir:
        search_dirs.extend([
            home_dir,
            os.path.join(home_dir, "Downloads"),
            os.path.join(home_dir, "Documents"),
            os.path.join(home_dir, ".meridian"),
            os.path.join(home_dir, ".openwakeword")
        ])

    for sdir in search_dirs:
        if not sdir or not os.path.exists(sdir):
            continue
        try:
            for item in os.listdir(sdir):
                if item.lower().endswith(".onnx"):
                    full_path = os.path.abspath(os.path.join(sdir, item))
                    if full_path not in seen_paths:
                        seen_paths.add(full_path)
                        scanned_models.append({
                            "name": item,
                            "path": full_path,
                            "folder": os.path.dirname(full_path)
                        })
        except Exception:
            continue

    return {"status": "success", "models": scanned_models}

@router.post("/api/voice/record")
def voice_record():
    try:
        try:
            from src.voice.wakeword import pause_wakeword
            pause_wakeword()
        except Exception:
            pass
            
        from src.voice.stt import record_and_transcribe
        text = record_and_transcribe(duration_seconds=4.0)
        
        try:
            from src.voice.wakeword import resume_wakeword
            resume_wakeword()
        except Exception:
            pass
            
        return {"status": "success", "text": text}
    except Exception as e:
        try:
            from src.voice.wakeword import resume_wakeword
            resume_wakeword()
        except Exception:
            pass
        raise HTTPException(status_code=500, detail=f"Voice capture failed: {str(e)}")

@router.post("/api/voice/interrupt")
def voice_interrupt():
    try:
        from src.core.loop import interrupt_agent_loop
        interrupt_agent_loop()
        try:
            from src.voice.tts import stop_active_tts
            stop_active_tts()
        except Exception:
            pass
        return {"status": "success", "message": "Inference and stream playback interrupted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/voice/continuous-window/status")
async def get_continuous_window_status_api():
    """AST-08: Returns status and remaining seconds for continuous conversation window."""
    from src.voice.wakeword import is_continuous_window_active, get_continuous_window_remaining
    return {
        "status": "success",
        "active": is_continuous_window_active(),
        "remaining_seconds": round(get_continuous_window_remaining(), 2)
    }

@router.post("/api/voice/continuous-window/start")
async def start_continuous_window_api(duration: float = 10.0):
    """AST-08: Activates continuous follow-up listening window for duration seconds."""
    from src.voice.wakeword import trigger_continuous_window, get_continuous_window_remaining
    trigger_continuous_window(duration)
    return {
        "status": "success",
        "message": f"Continuous window activated for {duration} seconds.",
        "remaining_seconds": round(get_continuous_window_remaining(), 2)
    }

@router.post("/api/voice/continuous-window/cancel")
async def cancel_continuous_window_api():
    """AST-08: Cancels continuous conversation window immediately."""
    from src.voice.wakeword import cancel_continuous_window
    cancel_continuous_window()
    return {"status": "success", "message": "Continuous listening window cancelled."}

@router.post("/api/voice/duplex/start")
async def start_duplex_session_api():
    """AST-15: Initializes a real-time full-duplex voice streaming session."""
    from src.voice.duplex import global_duplex_engine
    msg = global_duplex_engine.start_duplex_session()
    return {"status": "success", "message": msg, "duplex_state": global_duplex_engine.get_status()}

@router.post("/api/voice/duplex/stop")
async def stop_duplex_session_api():
    """AST-15: Stops the active full-duplex voice session."""
    from src.voice.duplex import global_duplex_engine
    msg = global_duplex_engine.stop_duplex_session()
    return {"status": "success", "message": msg, "duplex_state": global_duplex_engine.get_status()}

@router.get("/api/voice/duplex/status")
async def get_duplex_status_api():
    """AST-15: Returns diagnostic status for real-time duplex voice engine."""
    from src.voice.duplex import global_duplex_engine
    return {"status": "success", "duplex_state": global_duplex_engine.get_status()}

@router.post("/api/voice/duplex/barge-in")
async def trigger_duplex_barge_in_api(rms: float = 300.0):
    """AST-15: Triggers/simulates audio barge-in interruption."""
    from src.voice.duplex import global_duplex_engine
    interrupted = global_duplex_engine.check_barge_in(rms)
    return {"status": "success", "interrupted": interrupted, "rms": rms, "duplex_state": global_duplex_engine.get_status()}

@router.get("/api/voice/response/status")
async def get_voice_response_status_api():
    """Returns current voice response output toggle state."""
    from src.voice.duplex import is_voice_response_enabled
    return {"status": "success", "enabled": is_voice_response_enabled()}

@router.post("/api/voice/response/toggle")
async def toggle_voice_response_api(enabled: bool = True):
    """Toggles voice response output state (enabled/disabled)."""
    from src.voice.duplex import set_voice_response_enabled
    new_state = set_voice_response_enabled(enabled)
    return {"status": "success", "enabled": new_state}

@router.post("/api/voice/biometrics/register")
async def register_voice_biometric_api(payload: BiometricRegisterRequest):
    """JARVIS-03: Registers speaker voiceprint from reference audio payload."""
    from src.voice.voice_biometrics import global_biometrics_engine
    try:
        audio_bytes = base64.b64decode(payload.audio_base64)
    except Exception:
        audio_bytes = payload.audio_base64.encode("utf-8")

    res = global_biometrics_engine.register_speaker(payload.user_id or "default_user", audio_bytes)
    return {"status": "success", "enrollment": res}

@router.post("/api/voice/biometrics/verify")
async def verify_voice_biometric_api(payload: BiometricVerifyRequest):
    """JARVIS-03: Verifies speaker voice sample against enrolled user voiceprint."""
    from src.voice.voice_biometrics import global_biometrics_engine
    try:
        audio_bytes = base64.b64decode(payload.audio_base64)
    except Exception:
        audio_bytes = payload.audio_base64.encode("utf-8")

    verified, score = global_biometrics_engine.verify_speaker(audio_bytes, payload.user_id or "default_user")
    return {
        "status": "success",
        "verified": verified,
        "similarity_score": score,
        "threshold": global_biometrics_engine.threshold
    }

@router.get("/api/voice/biometrics/status")
async def get_biometric_status_api():
    """JARVIS-03: Returns biometric speaker verification engine status."""
    from src.voice.voice_biometrics import global_biometrics_engine
    return {"status": "success", "biometrics": global_biometrics_engine.get_status()}

@router.delete("/api/voice/biometrics/reset")
async def reset_biometric_voiceprints_api(user_id: Optional[str] = None):
    """JARVIS-03: Clears enrolled speaker voiceprints."""
    from src.voice.voice_biometrics import global_biometrics_engine
    res = global_biometrics_engine.reset_biometrics(user_id)
    return {"status": "success", "result": res}
