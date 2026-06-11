import os
import tempfile
from typing import Optional

def transcribe_audio_file(audio_path: str, model_size: str = "turbo") -> str:
    """Transcribe a local WAV/MP3 audio file using faster-whisper locally."""
    try:
        from faster_whisper import WhisperModel
        
        # Load whisper model with INT8 quantization on CPU
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
        
        segments, info = model.transcribe(audio_path, beam_size=5)
        text = " ".join([segment.text for segment in segments])
        return text.strip()
    except ImportError:
        return "Error: 'faster-whisper' package is not installed."
    except Exception as e:
        return f"Transcription failed: {e}"

def record_and_transcribe(duration_seconds: float = 5.0, model_size: str = "turbo") -> str:
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
        silence_timeout = 1.0 # Stop after 1.0s of silence
        max_duration = max(duration_seconds, 8.0) # Up to 8 seconds maximum
        
        start_time = time.time()
        
        # Audio threshold for speech detection (RMS amplitude)
        threshold = 300.0
        
        with sd.InputStream(samplerate=sample_rate, channels=1, dtype='int16') as stream:
            while time.time() - start_time < max_duration:
                chunk, overflow = stream.read(block_size)
                recording.append(chunk)
                
                # Calculate root-mean-square (RMS) energy
                rms = np.sqrt(np.mean(chunk**2)) if chunk.size > 0 else 0
                
                if rms > threshold:
                    if not speech_detected:
                        print("[Voice STT] Speech activity detected...")
                        speech_detected = True
                    silence_start = None
                else:
                    if speech_detected:
                        if silence_start is None:
                            silence_start = time.time()
                        elif time.time() - silence_start > silence_timeout:
                            print(f"[Voice STT] User finished speaking. Silence timeout reached.")
                            break
                            
        if not recording:
            return "No audio captured."
            
        audio_data = np.concatenate(recording, axis=0)
        
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
