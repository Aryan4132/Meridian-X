import os
import time
import threading
import httpx
from typing import Optional, Dict

TELEGRAM_ACTIVE = False
_thread = None

# ---------------------------------------------------------------------------
# Per-user token bucket rate limiter: max 5 messages per 60 seconds per user
# ---------------------------------------------------------------------------
_rate_lock = threading.Lock()
_rate_buckets: Dict[int, Dict] = {}  # {chat_id: {tokens, last_refill}}
_RATE_LIMIT = 5        # max messages per window
_RATE_WINDOW = 60.0    # seconds


def _is_rate_limited(chat_id: int) -> bool:
    """Return True if chat_id has exceeded the rate limit."""
    with _rate_lock:
        now = time.time()
        bucket = _rate_buckets.get(chat_id)
        if bucket is None:
            _rate_buckets[chat_id] = {"tokens": _RATE_LIMIT - 1, "last_refill": now}
            return False
        # Refill tokens if window elapsed
        elapsed = now - bucket["last_refill"]
        if elapsed >= _RATE_WINDOW:
            bucket["tokens"] = _RATE_LIMIT - 1
            bucket["last_refill"] = now
            return False
        if bucket["tokens"] > 0:
            bucket["tokens"] -= 1
            return False
        return True


# ---------------------------------------------------------------------------
# Message chunker: Telegram's max message length is 4096 chars
# ---------------------------------------------------------------------------
_TG_MAX_LEN = 4096


def _send_telegram_message(client: httpx.Client, token: str, chat_id: int, text: str) -> None:
    """Send text to Telegram, splitting into chunks if > 4096 chars."""
    if not text:
        return
    # Chunk on paragraph boundary when possible
    chunks = []
    while len(text) > _TG_MAX_LEN:
        split_at = text.rfind("\n\n", 0, _TG_MAX_LEN)
        if split_at == -1:
            split_at = text.rfind("\n", 0, _TG_MAX_LEN)
        if split_at == -1:
            split_at = _TG_MAX_LEN
        chunks.append(text[:split_at].strip())
        text = text[split_at:].strip()
    if text:
        chunks.append(text)

    for i, chunk in enumerate(chunks):
        suffix = f"\n_(Part {i+1}/{len(chunks)})_" if len(chunks) > 1 else ""
        try:
            client.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                json={"chat_id": chat_id, "text": chunk + suffix, "parse_mode": "Markdown"},
            )
        except Exception:
            # Fall back without Markdown parsing if it fails
            try:
                client.post(
                    f"https://api.telegram.org/bot{token}/sendMessage",
                    json={"chat_id": chat_id, "text": chunk + suffix},
                )
            except Exception:
                pass


# ---------------------------------------------------------------------------
# Bot command handlers
# ---------------------------------------------------------------------------
def _handle_slash_command(client: httpx.Client, token: str, chat_id: int, command: str) -> bool:
    """Handle /status, /cancel, /help bot commands. Returns True if handled."""
    cmd = command.strip().lower().split()[0] if command.strip() else ""
    if cmd == "/help":
        help_text = (
            "🤖 *Meridian-X Bot Commands*\n\n"
            "/help — Show this help message\n"
            "/status — Check Meridian-X backend health\n"
            "/cancel — Interrupt the current agent loop\n\n"
            "_Send any other message to invoke the agent._"
        )
        _send_telegram_message(client, token, chat_id, help_text)
        return True
    elif cmd == "/status":
        try:
            res = httpx.get("http://localhost:4132/api/health", timeout=5.0)
            if res.status_code == 200:
                data = res.json()
                status_text = (
                    f"✅ *Meridian-X Status*\n"
                    f"• Backend: {data.get('status', 'unknown')}\n"
                    f"• SQLite: {data.get('sqlite', 'unknown')}\n"
                    f"• MongoDB: {data.get('mongodb', 'unknown')}\n"
                    f"• Ollama: {data.get('ollama', 'unknown')}"
                )
            else:
                status_text = f"⚠️ Backend returned HTTP {res.status_code}."
        except Exception as e:
            status_text = f"❌ Backend unreachable: {e}"
        _send_telegram_message(client, token, chat_id, status_text)
        return True
    elif cmd == "/cancel":
        try:
            from src.core.loop import interrupt_agent_loop
            interrupt_agent_loop()
            _send_telegram_message(client, token, chat_id, "⛔ Agent loop interrupted.")
        except Exception as e:
            _send_telegram_message(client, token, chat_id, f"⚠️ Could not interrupt: {e}")
        return True
    return False


# ---------------------------------------------------------------------------
# Bridge lifecycle
# ---------------------------------------------------------------------------
def start_telegram_bridge():
    global TELEGRAM_ACTIVE, _thread
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        print("[Telegram Bridge] TELEGRAM_BOT_TOKEN not configured in .env. Bot bridge disabled.")
        return
        
    if TELEGRAM_ACTIVE:
        return
        
    TELEGRAM_ACTIVE = True
    _thread = threading.Thread(target=_poll_loop, daemon=True)
    _thread.start()
    print("[Telegram Bridge] Background polling thread started.")

def stop_telegram_bridge():
    global TELEGRAM_ACTIVE
    TELEGRAM_ACTIVE = False
    print("[Telegram Bridge] Background polling thread stopped.")

def _poll_loop():
    global TELEGRAM_ACTIVE
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    auth_chat_id = os.environ.get("TELEGRAM_AUTHORIZED_CHAT_ID")
    
    if auth_chat_id:
        try:
            auth_chat_id = int(auth_chat_id)
        except ValueError:
            print("[Telegram Bridge] Authorized Chat ID must be an integer. Continuing without strict filter.")
            auth_chat_id = None
            
    offset = 0
    client = httpx.Client(timeout=15.0)
    
    print("[Telegram Bridge] Monitoring updates...")
    
    while TELEGRAM_ACTIVE:
        try:
            url = f"https://api.telegram.org/bot{token}/getUpdates"
            params = {"offset": offset, "timeout": 10}
            res = client.get(url, params=params)
            
            if res.status_code != 200:
                time.sleep(5.0)
                continue
                
            data = res.json()
            if not data.get("ok"):
                time.sleep(5.0)
                continue
                
            for update in data.get("result", []):
                offset = update["update_id"] + 1
                message = update.get("message")
                if not message:
                    continue
                    
                chat = message.get("chat", {})
                chat_id = chat.get("id")
                
                # Security Check
                if auth_chat_id and chat_id != auth_chat_id:
                    print(f"[Telegram Bridge] Blocked unauthorized access from Chat ID: {chat_id}")
                    try:
                        client.post(
                            f"https://api.telegram.org/bot{token}/sendMessage",
                            json={"chat_id": chat_id, "text": "⚠️ Access Denied: You are not authorized to control this Meridian-X instance."}
                        )
                    except Exception:
                        pass
                    continue

                # Rate Limit Check
                if _is_rate_limited(chat_id):
                    print(f"[Telegram Bridge] Rate limit hit for chat_id {chat_id}. Dropping message.")
                    try:
                        client.post(
                            f"https://api.telegram.org/bot{token}/sendMessage",
                            json={"chat_id": chat_id, "text": "⏳ Rate limit reached. Please wait a moment before sending more messages."}
                        )
                    except Exception:
                        pass
                    continue
                
                # Check for voice message
                voice = message.get("voice")
                text_content = message.get("text")
                
                prompt_text = ""
                
                if voice:
                    file_id = voice.get("file_id")
                    # Retrieve file path
                    file_info_res = client.get(f"https://api.telegram.org/bot{token}/getFile", params={"file_id": file_id})
                    if file_info_res.status_code == 200 and file_info_res.json().get("ok"):
                        file_path = file_info_res.json()["result"].get("file_path")
                        file_url = f"https://api.telegram.org/file/bot{token}/{file_path}"
                        # BUG-67 fix: stream OGG download in chunks to avoid loading
                        # up to 20MB entirely into RAM before writing to disk.
                        import tempfile
                        temp_dir = tempfile.gettempdir()
                        temp_ogg = os.path.join(temp_dir, f"meridian_telegram_voice_{int(time.time())}.ogg")
                        with client.stream("GET", file_url) as r:
                            with open(temp_ogg, "wb") as f:
                                for chunk in r.iter_bytes(chunk_size=8192):
                                    f.write(chunk)

                        # Transcribe voice note using faster-whisper VAD pipeline
                        try:
                            from src.voice.stt import transcribe_audio_file
                            print("[Telegram Bridge] Transcribing voice note...")
                            transcription = transcribe_audio_file(temp_ogg)
                            prompt_text = transcription
                            print(f"[Telegram Bridge] Voice transcription: '{prompt_text}'")
                        except Exception as te:
                            prompt_text = ""
                            print(f"[Telegram Bridge] STT failed: {te}")
                        finally:
                            try:
                                os.remove(temp_ogg)
                            except Exception:
                                pass
                elif text_content:
                    # Handle bot slash commands before routing to agent
                    if text_content.strip().startswith("/"):
                        if _handle_slash_command(client, token, chat_id, text_content.strip()):
                            continue
                    prompt_text = text_content
                    print(f"[Telegram Bridge] Received message: '{prompt_text}'")
                    
                if not prompt_text:
                    continue
                    
                # Process prompt through agent loop
                try:
                    # Let the user know the agent is thinking
                    client.post(
                        f"https://api.telegram.org/bot{token}/sendMessage",
                        json={"chat_id": chat_id, "text": "🤔 Processing command..."}
                    )
                    
                    # Call local agent loop asynchronously
                    import asyncio
                    from src.core.loop import run_react_agent_loop
                    
                    model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
                    ollama_host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
                    
                    # BUG-56 fix: use isolated new_event_loop without asyncio.set_event_loop().
                    loop = asyncio.new_event_loop()
                    reply_parts = []
                    
                    async def _run():
                        async for event in run_react_agent_loop(prompt_text, model, ollama_host):
                            if event.startswith("event: text\n"):
                                for line in event.splitlines():
                                    if line.startswith("data: "):
                                        reply_parts.append(line[6:])
                    try:
                        loop.run_until_complete(_run())
                    finally:
                        loop.close()
                        
                    reply_text = "".join(reply_parts).strip() or "Task completed."
                    
                    # Log to database conversation history
                    from database import add_to_conversations
                    add_to_conversations("user", prompt_text)
                    add_to_conversations("assistant", reply_text)
                    
                    # 1. Send Text Reply (chunked if > 4096 chars)
                    _send_telegram_message(client, token, chat_id, reply_text)
                    
                    # 2. Synthesize TTS and send as Voice if original input was a voice note
                    if voice:
                        try:
                            from src.voice.tts import get_tts_engine
                            engine = get_tts_engine()
                            if engine:
                                print("[Telegram Bridge] Synthesizing speech reply...")
                                style = engine.get_voice_style(voice_name="M1")
                                wav, duration = engine.synthesize(reply_text, voice_style=style, lang="na")
                                
                                import tempfile
                                temp_dir = tempfile.gettempdir()
                                temp_wav = os.path.join(temp_dir, f"meridian_telegram_reply_{int(time.time())}.wav")
                                engine.save_audio(wav, temp_wav)
                                
                                # Send voice note back
                                with open(temp_wav, "rb") as voice_file:
                                    files = {"voice": voice_file}
                                    client.post(
                                        f"https://api.telegram.org/bot{token}/sendVoice",
                                        data={"chat_id": chat_id},
                                        files=files
                                    )
                                    
                                try:
                                    os.remove(temp_wav)
                                except Exception:
                                    pass
                        except Exception as tse:
                            print(f"[Telegram Bridge] TTS feedback failed: {tse}")
                            
                except Exception as ae:
                    print(f"[Telegram Bridge] Error executing command: {ae}")
                    if isinstance(ae, httpx.TransportError):
                        print("[Telegram Bridge] Transport error during update lifecycle. Recreating client...")
                        try:
                            client.close()
                        except Exception:
                            pass
                        client = httpx.Client(timeout=15.0)
                    try:
                        client.post(
                            f"https://api.telegram.org/bot{token}/sendMessage",
                            json={"chat_id": chat_id, "text": f"❌ Error executing command: {ae}"}
                        )
                    except Exception:
                        pass
                        
        except httpx.TransportError as te:
            print(f"[Telegram Bridge] Transport error: {te}. Recreating client...")
            try:
                client.close()
            except Exception:
                pass
            client = httpx.Client(timeout=15.0)
            time.sleep(5.0)
        except Exception as e:
            print(f"[Telegram Bridge] Polling error: {e}")
            time.sleep(5.0)
            
    client.close()
