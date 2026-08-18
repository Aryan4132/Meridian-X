import pytest
import numpy as np
import os
import sys

# Ensure src directory is on sys.path
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

def test_streaming_tts_buffer_chunking():
    from voice.tts import StreamingTTSBuffer
    
    buf = StreamingTTSBuffer(min_words_first_chunk=2, max_words_clause=10)
    
    # 1. Feed 2 words -> should immediately yield first chunk ("Hello world")
    chunks = buf.feed_token("Hello ")
    assert len(chunks) == 0
    
    chunks = buf.feed_token("world. ")
    assert len(chunks) == 1
    assert chunks[0] == "Hello world."
    
    # 2. Feed a full sentence -> should yield clause/sentence
    chunks = buf.feed_token("This is a second sentence testing high speed TTS.")
    assert len(chunks) == 1
    assert "second sentence" in chunks[0]
    
    # 3. Flush remaining buffer
    final_chunks = buf.flush()
    assert isinstance(final_chunks, list)

def test_stt_in_memory_transcribe_stub(monkeypatch):
    from voice.stt import transcribe_audio_array
    
    # Mock whisper model for fast test execution
    class MockWhisperModel:
        def transcribe(self, audio_array, beam_size=1):
            class Segment:
                text = "Hello Meridian"
            return [Segment()], None
            
    monkeypatch.setattr("voice.stt.get_whisper_model", lambda model_size=None: MockWhisperModel())
    
    dummy_audio = np.zeros(16000, dtype=np.float32) # 1 sec of silence @ 16kHz
    result = transcribe_audio_array(dummy_audio)
    assert result == "Hello Meridian"
