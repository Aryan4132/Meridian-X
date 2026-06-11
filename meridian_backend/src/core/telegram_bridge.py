import os
import time
import threading
import httpx
from typing import Optional

TELEGRAM_ACTIVE = False
_thread = None

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
                    # Send warning back to unauthorized user
                    try:
                        client.post(
                            f"https://api.telegram.org/bot{token}/sendMessage",
                            json={"chat_id": chat_id, "text": "⚠️ Access Denied: You are not authorized to control this Meridian-X instance."}
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
                        
                        # Download voice note (.ogg)
                        ogg_data = client.get(file_url).content
                        
                        # Save to temp file
                        import tempfile
                        temp_dir = tempfile.gettempdir()
                        temp_ogg = os.path.join(temp_dir, f"meridian_telegram_voice_{int(time.time())}.ogg")
                        with open(temp_ogg, "wb") as f:
                            f.write(ogg_data)
                            
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
                    
                    # Call local agent loop
                    from api import get_react_thoughts
                    # Set settings: run default local/Ollama model
                    model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
                    ocr_model = "PaddleOCR-v4"
                    
                    result = get_react_thoughts(prompt_text, model, ocr_model)
                    reply_text = result.get("text", "Task completed.")
                    
                    # Log to database conversation history
                    from database import add_to_conversations
                    add_to_conversations("user", prompt_text)
                    add_to_conversations("assistant", reply_text)
                    
                    # 1. Send Text Reply
                    client.post(
                        f"https://api.telegram.org/bot{token}/sendMessage",
                        json={"chat_id": chat_id, "text": reply_text}
                    )
                    
                    # 2. Synthesize TTS and send as Voice if original input was a voice note
                    if voice:
                        try:
                            from api import get_tts_engine
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
                    try:
                        client.post(
                            f"https://api.telegram.org/bot{token}/sendMessage",
                            json={"chat_id": chat_id, "text": f"❌ Error executing command: {ae}"}
                        )
                    except Exception:
                        pass
                        
        except Exception as e:
            print(f"[Telegram Bridge] Polling error: {e}")
            time.sleep(5.0)
            
    client.close()
