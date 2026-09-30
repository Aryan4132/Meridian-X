import pytest
import io
import soundfile as sf
import numpy as np
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient

def test_tts_memory_wav_synthesis():
    """Verify that /api/tts synthesizes audio into an in-memory WAV buffer without disk I/O."""
    from api import app, TTSRequest
    
    mock_engine = MagicMock()
    mock_engine.sample_rate = 24000
    mock_engine.get_voice_style.return_value = "style_m1"
    
    # Generate 0.25 seconds of dummy audio sine wave
    duration = 0.25
    sample_rate = 24000
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    dummy_audio = (np.sin(2 * np.pi * 440 * t) * 0.5).astype(np.float32)
    mock_engine.synthesize.return_value = (dummy_audio, duration)
    
    with patch("api.get_tts_engine", return_value=mock_engine):
        client = TestClient(app)
        response = client.post("/api/tts", json={"text": "Meridian voice engine ready", "voice": "M1", "lang": "na"})
        
        assert response.status_code == 200
        assert response.headers["content-type"] == "audio/wav"
        
        # Verify valid WAV format in content
        wav_bytes = response.content
        assert len(wav_bytes) > 44
        assert wav_bytes[:4] == b"RIFF"
        assert wav_bytes[8:12] == b"WAVE"
        
        # Ensure it reads back through soundfile successfully
        buf = io.BytesIO(wav_bytes)
        data, read_fs = sf.read(buf)
        assert read_fs == 24000
        assert len(data) == len(dummy_audio)

def test_stt_model_cpu_defaults():
    """Verify that Whisper STT defaults to tiny.en on CPU for low latency."""
    with patch.dict("sys.modules", {"torch": MagicMock(cuda=MagicMock(is_available=lambda: False))}):
        with patch("faster_whisper.WhisperModel") as mock_whisper:
            import src.voice.stt as stt_module
            stt_module._cached_whisper_model = None
            
            with patch("database.get_user_profile", return_value=None):
                model = stt_module.get_whisper_model(model_size=None)
                
                # Check that tiny.en was selected for CPU
                mock_whisper.assert_called_with("tiny.en", device="cpu", compute_type="int8")
            
            # Reset cache
            stt_module._cached_whisper_model = None

def test_stt_transcribe_audio_array():
    """Verify in-memory audio array transcription."""
    import src.voice.stt as stt_module
    
    mock_model = MagicMock()
    mock_segment = MagicMock()
    mock_segment.text = "Hello Meridian"
    mock_model.transcribe.return_value = ([mock_segment], None)
    
    with patch.object(stt_module, "get_whisper_model", return_value=mock_model):
        dummy_audio = np.zeros(16000, dtype=np.float32)
        result = stt_module.transcribe_audio_array(dummy_audio)
        
        assert result == "Hello Meridian"
        mock_model.transcribe.assert_called_once()

def test_detect_user_language_accuracy():
    """Verify that English greetings and prepositions are not falsely detected as Hinglish."""
    from src.core.mode import detect_user_language

    # English phrases that previously false-positive triggered on "hi" or "to"
    english_cases = [
        "Hi",
        "Hi Meridian",
        "Talk to me",
        "How to run tests",
        "Say hi to my friend",
        "Go to bed",
        "Where to start",
        "What time is it?",
        "Can you help me with this code?",
        "Please check the git status",
        "voice output is slow as f",
    ]
    for prompt in english_cases:
        lang = detect_user_language(prompt)
        assert lang == "ENGLISH", f"Expected 'ENGLISH' for '{prompt}', got '{lang}'"

    # Real Hinglish phrases that should be detected as Hinglish
    hinglish_cases = [
        "aap kaise ho",
        "kya kar rahe ho",
        "mujhe batao yaar",
        "mera kaam karoge",
    ]
    for prompt in hinglish_cases:
        lang = detect_user_language(prompt)
        assert lang == "HINGLISH", f"Expected 'HINGLISH' for '{prompt}', got '{lang}'"

    # Direct Devanagari Hindi
    devanagari_cases = [
        "आप कैसे हैं?",
        "नमस्ते मेरिडियन",
    ]
    for prompt in devanagari_cases:
        lang = detect_user_language(prompt)
        assert lang == "HINDI", f"Expected 'HINDI' for '{prompt}', got '{lang}'"

@pytest.mark.asyncio
async def test_process_final_response_skips_english_transliteration():
    """Verify that process_final_response skips transliteration when user_lang is English."""
    from src.core.loop_parser import process_final_response
    mock_client = MagicMock()

    json_payload = '{"chat": "I am doing well, how can I help you?", "speech": "I am doing well, how can I help you?", "lang": "en"}'
    res = await process_final_response(json_payload, user_lang="ENGLISH", client=mock_client)

    # client.chat must NOT be called for English responses
    mock_client.chat.assert_not_called()
    assert "I am doing well" in res

def test_should_trigger_consensus_debate_smart_gate():
    """Verify that consensus debate is safely bypassed for conversational queries and triggered for mutations."""
    from src.core.consensus_engine import should_trigger_consensus_debate

    # Conversational turns -> should bypass debate (returns False)
    assert not should_trigger_consensus_debate("Hi", '{"chat": "Hello! How can I help?", "speech": "Hello!"}', [])
    assert not should_trigger_consensus_debate("What time is it?", '{"chat": "It is 10:30 PM", "speech": "It is 10:30 PM"}', ["get_time"])
    assert not should_trigger_consensus_debate("Who are you?", '{"chat": "I am Meridian", "speech": "I am Meridian"}', [])

    # Code mutation tools executed -> should trigger debate (returns True)
    assert should_trigger_consensus_debate("Write a test", '{"chat": "Done"}', ["write_to_file"])
    assert should_trigger_consensus_debate("Refactor code", '{"chat": "Done"}', ["replace_file_content"])
    assert should_trigger_consensus_debate("Run migration", '{"chat": "Done"}', ["run_command"])

    # Code blocks inside finish text -> should trigger debate (returns True)
    code_finish = '{"chat": "```python\\ndef add(a, b):\\n    return a + b\\n```\\nHere is the function implemented for your project with full typing."}'
    long_code_finish = code_finish + " " * 150
    assert should_trigger_consensus_debate("Create add function", long_code_finish, [])


