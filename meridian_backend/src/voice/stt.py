import os
import tempfile
import threading
from typing import Optional
import numpy as np

_cached_whisper_model = None
_whisper_lock = threading.Lock()

def get_whisper_model(model_size: Optional[str] = None):
    """Get or initialize the cached Whisper model instance."""
    global _cached_whisper_model
    if model_size is None:
        try:
            from database import get_user_profile
            model_size = get_user_profile("stt_model_size")
        except Exception:
            pass
        if not model_size:
            model_size = "base"

    if _cached_whisper_model is None:
        with _whisper_lock:
            if _cached_whisper_model is None:
                from faster_whisper import WhisperModel
                
                device = "cpu"
                compute_type = "int8"
                
                # Dynamically detect CUDA GPU availability via torch
                try:
                    import torch
                    if torch.cuda.is_available():
                        device = "cuda"
                        compute_type = "float16"
                        print("[Whisper STT] CUDA GPU detected. Running on GPU with float16.")
                    else:
                        print("[Whisper STT] CUDA GPU not available. Running on CPU with int8.")
                except ImportError:
                    print("[Whisper STT] PyTorch not installed. Defaulting to CPU with int8.")
                except Exception as e:
                    print(f"[Whisper STT] Error detecting GPU status: {e}. Defaulting to CPU.")
                
                # BUG-50 fix: expanded CPU guard to include all heavy models.
                # Only 'turbo' was downgraded before; large/large-v2/large-v3 are
                # equally slow on CPU and should also be swapped to 'base'.
                CPU_HEAVY_MODELS = {"turbo", "large", "large-v2", "large-v3"}
                if device == "cpu" and model_size in CPU_HEAVY_MODELS:
                    print(f"[Whisper STT] Warning: '{model_size}' model is slow on CPU. Swapping to 'base' for faster performance.")
                    model_size = "base"
                
                _cached_whisper_model = WhisperModel(model_size, device=device, compute_type=compute_type)
    return _cached_whisper_model

def transcribe_audio_file(audio_path: str, model_size: Optional[str] = None) -> str:
    """Transcribe a local WAV/MP3 audio file using faster-whisper locally."""
    try:
        model = get_whisper_model(model_size)
        segments, info = model.transcribe(audio_path, beam_size=5)
        text = " ".join([segment.text for segment in segments])
        return text.strip()
    except ImportError:
        return "Error: 'faster-whisper' package is not installed."
    except Exception as e:
        return f"Transcription failed: {e}"

def record_and_transcribe(duration_seconds: float = 5.0, model_size: Optional[str] = None) -> str:
    """Record audio from the microphone and automatically stop when silence is detected using energy VAD."""
    try:
        import sounddevice as sd
        import numpy as np
        import scipy.io.wavfile as wav
        import time
        
        sample_rate = 16000
        block_duration = 0.1 # 100ms chunks
        block_size = int(sample_rate * block_duration)
        
        print("[Voice STT] Opening stream with dynamic VAD...")
        
        recording = []
        speech_detected = False
        silence_start = None
        
        # Load VAD parameters dynamically from database profile
        try:
            from database import get_user_profile
            silence_timeout_val = get_user_profile("stt_silence_timeout")
            silence_timeout = float(silence_timeout_val) if silence_timeout_val is not None else 1.0
            
            threshold_val = get_user_profile("stt_vad_threshold")
            threshold = float(threshold_val) if threshold_val is not None else 300.0
            
            max_duration_val = get_user_profile("stt_max_duration")
            max_duration_limit = float(max_duration_val) if max_duration_val is not None else 8.0
        except Exception:
            silence_timeout = 1.0
            threshold = 300.0
            max_duration_limit = 8.0

        max_duration = max(duration_seconds, max_duration_limit)
        start_time = time.time()
        
        with sd.InputStream(samplerate=sample_rate, channels=1, dtype='int16') as stream:
            while time.time() - start_time < max_duration:
                chunk, overflow = stream.read(block_size)
                
                # Calculate root-mean-square (RMS) energy
                rms = np.sqrt(np.mean(chunk.astype(np.float32)**2)) if chunk.size > 0 else 0.0
                pitch = estimate_pitch_centroid(chunk, sample_rate)
                
                # BK-04: Pitch centroid filtering — speech requires both valid RMS and human speech pitch range
                is_valid_speech = (rms > threshold) and (pitch > 0.0 or not speech_detected)
                
                if is_valid_speech and rms > threshold:
                    recording.append(chunk)
                    if not speech_detected:
                        print(f"[Voice STT] Speech activity detected (RMS: {rms:.1f}, Pitch: {pitch:.1f}Hz)...")
                        speech_detected = True
                    silence_start = None
                else:
                    if speech_detected:
                        recording.append(chunk)
                        if silence_start is None:
                            silence_start = time.time()
                        elif time.time() - silence_start > silence_timeout:
                            print(f"[Voice STT] User finished speaking. Silence timeout reached.")
                            break
                            
        if not recording:
            return "No audio captured."
            
        raw_audio = np.concatenate(recording, axis=0)
        
        # BK-09: Apply spectral RMS noise gate attenuation before Whisper inference
        audio_data = apply_noise_gate(raw_audio, threshold=threshold * 0.5)
        
        # Save to temp file
        temp_dir = tempfile.gettempdir()
        temp_wav = os.path.join(temp_dir, "meridian_stt_temp.wav")
        wav.write(temp_wav, sample_rate, audio_data)
        
        print("[Voice STT] Transcribing audio pipeline...")
        transcription = transcribe_audio_file(temp_wav, model_size)
        
        # Clean up
        try:
            os.remove(temp_wav)
        except Exception:
            pass
            
        return transcription
    except ImportError:
        return "Error: 'sounddevice', 'numpy' or 'scipy' is not installed for recording."
    except Exception as e:
        return f"Recording and transcription failed: {e}"

def apply_noise_gate(audio_data: np.ndarray, threshold: float = 150.0, attenuation: float = 0.05) -> np.ndarray:
    """BK-09: Filter out sub-threshold background noise frames using dynamic RMS noise gate."""
    if audio_data is None or len(audio_data) == 0:
        return audio_data
    try:
        import numpy as np
        frame_size = 320 # 20ms at 16kHz
        processed = audio_data.copy().astype(np.float32)
        for i in range(0, len(processed), frame_size):
            frame = processed[i:i + frame_size]
            rms = np.sqrt(np.mean(frame**2)) if frame.size > 0 else 0.0
            if rms < threshold:
                processed[i:i + frame_size] *= attenuation
        return np.clip(processed, -32768, 32767).astype(np.int16)
    except Exception:
        return audio_data

def estimate_pitch_centroid(chunk: np.ndarray, sample_rate: int = 16000) -> float:
    """BK-04: Estimate fundamental speech frequency F0 via autocorrelation to filter out ambient noise."""
    if chunk is None or len(chunk) < 64:
        return 0.0
    try:
        import numpy as np
        signal = chunk.astype(np.float32).flatten()
        signal = signal - np.mean(signal) # Remove DC offset
        
        # Autocorrelation
        corr = np.correlate(signal, signal, mode='full')
        corr = corr[len(corr) // 2:]
        
        # Human pitch range search (80 Hz to 350 Hz)
        min_lag = int(sample_rate / 350)
        max_lag = int(sample_rate / 80)
        
        if max_lag >= len(corr) or min_lag >= max_lag:
            return 0.0
            
        peak_idx = min_lag + np.argmax(corr[min_lag:max_lag])
        if corr[0] > 0 and corr[peak_idx] / corr[0] > 0.25:
            pitch = float(sample_rate / peak_idx)
            return pitch if 80.0 <= pitch <= 350.0 else 0.0
        return 0.0
    except Exception:
        return 0.0

