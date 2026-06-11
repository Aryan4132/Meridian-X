from src.voice.stt import record_and_transcribe
from src.voice.tts import speak_text

def voice_record_and_transcribe(duration_seconds: float = 5.0) -> str:
    """Record local microphone input for a specified duration and return the transcribed text."""
    transcription = record_and_transcribe(duration_seconds)
    if not transcription.strip():
        return "No speech detected or recording failed."
    return f"Transcription result:\n{transcription}"

def voice_speak(text: str) -> str:
    """Synthesize text into speech and play it out loud through default speakers."""
    return speak_text(text)
