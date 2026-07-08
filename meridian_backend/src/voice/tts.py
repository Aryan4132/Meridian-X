import os
import tempfile
import random
import re
import queue
import threading
from typing import Optional, List

# Global variable to cache the TTS engine
_cached_tts_engine = None
_tts_lock = threading.Lock()

def get_tts_engine():
    """Get or initialize the cached Supertonic TTS engine."""
    global _cached_tts_engine
    if _cached_tts_engine is None:
        with _tts_lock:
            if _cached_tts_engine is None:
                from supertonic import TTS
                _cached_tts_engine = TTS(auto_download=True)
    return _cached_tts_engine

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

def speak_text(text: str, voice_name: str = "M1") -> str:
    """Synthesize text into speech using Supertonic ONNX and play it locally on host audio outputs.
    
    This uses a background thread to synthesize text chunks in parallel while the main thread
    plays back the synthesized audio, minimizing Time-to-First-Audio (TTFA).
    """
    try:
        from supertonic import TTS
        import sounddevice as sd
        import soundfile as sf
        
        # 1. Initialize or retrieve the cached TTS engine
        engine = get_tts_engine()
        # BUG-62 fix: validate voice_name against available voices before calling get_voice_style.
        # An invalid name causes a cryptic/unhelpful supertonic exception with no context.
        try:
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
            for i, chunk in enumerate(chunks):
                try:
                    # Synthesize chunk
                    wav, duration = engine.synthesize(chunk, voice_style=style, lang="na")
                    
                    # Save chunk to temp file to safely read the exact sample rate (fs)
                    temp_dir = tempfile.gettempdir()
                    temp_path = os.path.join(
                        temp_dir, 
                        f"meridian_tts_chunk_{random.randint(1000, 9999)}_{i}.wav"
                    )
                    engine.save_audio(wav, temp_path)
                    
                    # Read back data and sample rate in-memory
                    data, fs = sf.read(temp_path)
                    
                    # Cleanup the temporary file immediately
                    try:
                        os.remove(temp_path)
                    except Exception:
                        pass
                        
                    audio_queue.put((data, fs))
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
