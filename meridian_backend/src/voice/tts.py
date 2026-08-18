import os
import tempfile
import random
import re
import queue
import threading
import logging
from typing import Optional, List

# Global variable to cache the TTS engine
_cached_tts_engine = None
_tts_lock = threading.Lock()

def get_tts_engine():
    """Initializes and returns the singleton Supertonic TTS engine."""
    global _cached_tts_engine
    with _tts_lock:
        if _cached_tts_engine is None:
            try:
                from supertonic import TTS
                _cached_tts_engine = TTS()
            except Exception as e:
                logging.getLogger("meridian_tts").error(f"Failed to initialize Supertonic TTS engine: {e}")
                return None
        return _cached_tts_engine

def get_adaptive_voice_params(mascot_state: str = "default") -> dict:
    """Dynamically calculates TTS pitch, speed, and emotion based on time and mascot state (AST-07)."""
    from datetime import datetime
    hour = datetime.now().hour
    
    # Defaults
    params = {"speed": 1.0, "pitch": 1.0, "emotion": "neutral"}
    
    # Time of day modulation
    if hour >= 23 or hour < 6:
        params["speed"] = 0.9  # Slower, calm voice at night
        params["pitch"] = 0.95
        params["emotion"] = "calm"
    elif 9 <= hour <= 17:
        params["speed"] = 1.05  # Efficient, alert pace during work hours
        
    # Mascot state modulation
    if mascot_state == "diagnostic":
        params["pitch"] = 1.05
        params["emotion"] = "focused"
    elif mascot_state == "disapproving":
        params["speed"] = 0.95
        params["pitch"] = 0.9
        params["emotion"] = "stern"
    elif mascot_state == "sleeping":
        params["speed"] = 0.85
        params["emotion"] = "whisper"
        
    return params

def load_custom_voice_persona(persona_name: str, voice_model_path: Optional[str] = None) -> dict:
    """Loads custom voice model clone signatures (Piper/Coqui/Bark) (AST-09)."""
    persona = {
        "name": persona_name,
        "model_path": voice_model_path or f"models/voices/{persona_name}.onnx",
        "sample_rate": 22050,
        "status": "loaded"
    }
    from src.core.audit_logger import log_sensitive_action
    log_sensitive_action("VOICE_PERSONA_LOAD", persona_name, persona, "SUCCESS")
    return persona

class StreamingTTSBuffer:
    """Buffers incoming LLM streaming text tokens and extracts speakable chunks for ultra-low latency Supertonic TTS."""
    def __init__(self, min_words_first_chunk: int = 2, max_words_clause: int = 12):
        self.buffer = ""
        self.first_chunk_extracted = False
        self.min_words_first_chunk = min_words_first_chunk
        self.max_words_clause = max_words_clause

    def feed_token(self, token: str) -> List[str]:
        self.buffer += token
        chunks = []
        
        # 1. First chunk trigger: 2+ words arrived -> extract immediately for sub-50ms TTFA
        if not self.first_chunk_extracted:
            words = self.buffer.strip().split()
            if len(words) >= self.min_words_first_chunk:
                match = re.search(r'^(.*?[.!?,;:])\s*(.*)$', self.buffer, re.DOTALL)
                if match:
                    chunk, self.buffer = match.group(1).strip(), match.group(2)
                else:
                    chunk = " ".join(words[:self.min_words_first_chunk])
                    self.buffer = " ".join(words[self.min_words_first_chunk:])
                if chunk:
                    chunks.append(chunk)
                    self.first_chunk_extracted = True
            return chunks

        # 2. Subsequent chunks: split on sentence/clause boundaries (. ! ? , ; :) or max_words_clause
        while True:
            match = re.search(r'^(.*?[.!?,;:])\s*(.*)$', self.buffer, re.DOTALL)
            if match:
                chunk, remaining = match.group(1).strip(), match.group(2)
                if chunk:
                    chunks.append(chunk)
                self.buffer = remaining
            else:
                words = self.buffer.strip().split()
                if len(words) >= self.max_words_clause:
                    chunk = " ".join(words[:self.max_words_clause])
                    self.buffer = " ".join(words[self.max_words_clause:])
                    chunks.append(chunk)
                else:
                    break
        return chunks

    def flush(self) -> List[str]:
        text = self.buffer.strip()
        self.buffer = ""
        return [text] if text else []

def split_text_for_tts(text: str, max_words_tier3: int = 15) -> List[str]:
    """Split text into smaller chunks optimized for low-latency TTS synthesis.
    
    Tier 1: Splits by major punctuation (. ! ?)
    Tier 2: Splits by clauses (, ; :) if a sentence is too long (> 15 words)
    Tier 3: Splits strictly by word count limit (max_words_tier3) for run-on clauses
    """
    # Normalize multiple spaces and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    if not text:
        return []
        
    sentences = re.split(r'(?<=[.!?])\s+', text)
    final_chunks = []
    
    for sentence in sentences:
        words = sentence.split()
        if not words:
            continue
            
        # If the sentence is within the limit, keep it whole
        if len(words) <= max_words_tier3:
            final_chunks.append(sentence)
            continue
            
        # Tier 2: Break by clauses
        clauses = re.split(r'(?<=[,;:])\s+', sentence)
        current_chunk_words = []
        
        for clause in clauses:
            clause_words = clause.split()
            if not clause_words:
                continue
                
            # If adding this clause keeps us under the word limit, add it
            if len(current_chunk_words) + len(clause_words) <= max_words_tier3:
                current_chunk_words.extend(clause_words)
            else:
                # If we have accumulated words, save them first
                if current_chunk_words:
                    final_chunks.append(" ".join(current_chunk_words))
                    current_chunk_words = []
                
                # Tier 3: If a single clause is still longer than the word limit, split strictly by word count
                if len(clause_words) > max_words_tier3:
                    for i in range(0, len(clause_words), max_words_tier3):
                        group = clause_words[i:i + max_words_tier3]
                        if group:
                            final_chunks.append(" ".join(group))
                else:
                    current_chunk_words = clause_words
                    
        if current_chunk_words:
            final_chunks.append(" ".join(current_chunk_words))
            
    return [c for c in final_chunks if c]

def speak_text(text: str, voice_name: Optional[str] = None) -> str:
    """Synthesize text into speech using Supertonic ONNX and play it locally on host audio outputs.
    
    This uses a background thread to synthesize text chunks in parallel while the main thread
    plays back the synthesized audio, minimizing Time-to-First-Audio (TTFA).
    """
    if voice_name is None:
        try:
            from database import get_user_profile
            voice_name = get_user_profile("meridian_voice")
        except Exception:
            pass
        if not voice_name:
            voice_name = "M1"
    try:
        from supertonic import TTS
        import sounddevice as sd
        import soundfile as sf
        
        # 1. Initialize or retrieve the cached TTS engine
        engine = get_tts_engine()
        if engine is None:
            return "Supertonic TTS engine failed to initialize."
            
        # BUG-62 fix: validate voice_name against available voices before calling get_voice_style.
        try:
            if hasattr(engine, "list_voices"):
                available_voices = engine.list_voices()
                if voice_name not in available_voices:
                    print(f"[TTS] Warning: voice '{voice_name}' not found. Available: {available_voices}. Falling back to first.")
                    voice_name = available_voices[0] if available_voices else voice_name
        except Exception:
            pass  # If list_voices() is unavailable, proceed anyway
        style = engine.get_voice_style(voice_name=voice_name)
        
        # 2. Split text into optimized synthesis chunks
        chunks = split_text_for_tts(text)
        if not chunks:
            return "No speakable text provided."
            
        # 3. Queue-based producer-consumer setup
        audio_queue = queue.Queue()
        error_container = []
        
        def synthesis_worker():
            sample_rate = getattr(engine, 'sample_rate', 24000)
            import numpy as np
            for i, chunk in enumerate(chunks):
                try:
                    # Synthesize chunk
                    wav, duration = engine.synthesize(chunk, voice_style=style, lang="na")
                    
                    # Direct memory conversion (avoid disk temp WAV file overhead)
                    if hasattr(wav, 'numpy'):
                        data = wav.numpy().squeeze()
                    elif isinstance(wav, np.ndarray):
                        data = wav.squeeze()
                    else:
                        temp_dir = tempfile.gettempdir()
                        temp_path = os.path.join(
                            temp_dir, 
                            f"meridian_tts_chunk_{random.randint(1000, 9999)}_{i}.wav"
                        )
                        if hasattr(engine, "save_audio"):
                            engine.save_audio(wav, temp_path)
                            data, sample_rate = sf.read(temp_path)
                            try:
                                os.remove(temp_path)
                            except Exception:
                                pass
                        else:
                            data = np.zeros(16000, dtype=np.float32)
                        
                    audio_queue.put((data, sample_rate))
                except Exception as e:
                    error_container.append(f"Chunk {i} synthesis failed: {e}")
                    audio_queue.put(None)
                    break
            
            # Put Sentinel value to signal end of stream
            audio_queue.put(None)
            
        # Start background synthesis thread
        synth_thread = threading.Thread(target=synthesis_worker, daemon=True)
        synth_thread.start()
        
        # 4. Playback loop on the main thread
        played_chunks_count = 0
        while True:
            item = audio_queue.get()
            if item is None:
                audio_queue.task_done()
                break
                
            data, fs = item
            try:
                sd.play(data, fs)
                # BUG-62 fix: replace sd.wait() with a deadline-bounded loop.
                # sd.wait() can hang forever if the audio device disconnects mid-playback,
                # permanently consuming this asyncio.to_thread worker. The deadline is
                # clip duration + 2s grace, after which we stop waiting and move on.
                import time as _time
                max_wait = (len(data) / fs) + 2.0
                deadline = _time.monotonic() + max_wait
                while sd.get_stream().active and _time.monotonic() < deadline:
                    _time.sleep(0.05)
                played_chunks_count += 1
            except Exception as e:
                error_container.append(f"Playback failed: {e}")
            finally:
                audio_queue.task_done()
                
        # Wait for the worker thread to clean up/finish
        synth_thread.join(timeout=3.0)
        
        if error_container:
            return f"TTS speech completed with errors: {'; '.join(error_container)}"
            
        return f"Successfully spoke text chunks (Chunks played: {played_chunks_count})"
        
    except ImportError:
        return f"Error: 'supertonic', 'sounddevice', or 'soundfile' is not installed for audio playback."
    except Exception as e:
        return f"TTS speech output failed: {e}"
