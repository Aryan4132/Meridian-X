import os
import tempfile
import random
from typing import Optional

def speak_text(text: str, voice_name: str = "M1") -> str:
    """Synthesize text into speech using Supertonic ONNX and play it locally on host audio outputs."""
    try:
        from supertonic import TTS
        import sounddevice as sd
        import soundfile as sf
        
        # Initialize engine
        engine = TTS(auto_download=True)
        style = engine.get_voice_style(voice_name=voice_name)
        
        # Synthesize audio array
        wav, duration = engine.synthesize(text, voice_style=style, lang="na")
        
        # Temp save path
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, f"meridian_tts_speak_{random.randint(1000, 9999)}.wav")
        engine.save_audio(wav, temp_path)
        
        # Load and play audio file using soundfile and sounddevice
        data, fs = sf.read(temp_path)
        sd.play(data, fs)
        sd.wait() # Wait until audio completes
        
        # Clean up
        try:
            os.remove(temp_path)
        except Exception:
            pass
            
        return f"Successfully spoke text: '{text}' (Duration: {duration:.2f}s)"
    except ImportError:
        return f"Error: 'supertonic', 'sounddevice', or 'soundfile' is not installed for audio playback."
    except Exception as e:
        return f"TTS speech output failed: {e}"
