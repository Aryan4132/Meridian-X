import os
from typing import Optional, List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database import (
    get_sqlite_conn,
    get_user_profile,
    save_user_profile,
    get_mongo_db,
    add_clipboard_history,
    get_clipboard_history
)
from src.api.deps import update_local_env_file

router = APIRouter(tags=["profile"])

ENV_KEY_MAP = {
    "ollama_host": "OLLAMA_HOST",
    "groq_key": "GROQ_API_KEY",
    "openrouter_key": "OPENROUTER_API_KEY",
    "mistral_key": "MISTRAL_API_KEY",
    "openai_key": "OPENAI_API_KEY",
    "anthropic_key": "ANTHROPIC_API_KEY",
    "gemini_key": "GEMINI_API_KEY",
    "deepseek_key": "DEEPSEEK_API_KEY",
    "tavily_key": "TAVILY_API_KEY",
    "discord_token": "DISCORD_BOT_TOKEN",
    "telegram_token": "TELEGRAM_BOT_TOKEN",
    "telegram_chat_id": "TELEGRAM_CHAT_ID",
    "meridian_provider": "MERIDIAN_PROVIDER",
    "meridian_model": "MERIDIAN_MODEL",
    "meridian_vision_model": "MERIDIAN_VISION_MODEL",
    "meridian_auditor_model": "MERIDIAN_AUDITOR_MODEL",
    "embedding_model": "EMBEDDING_MODEL",
    "meridian_voice": "MERIDIAN_VOICE",
    "wakeword_threshold": "WAKEWORD_THRESHOLD",
    "wakeword_model_filename": "WAKEWORD_MODEL_FILENAME",
    "wakeword_phrase": "WAKEWORD_PHRASE",
    "stt_model_size": "STT_MODEL_SIZE",
    "stt_silence_timeout": "STT_SILENCE_TIMEOUT",
    "stt_vad_threshold": "STT_VAD_THRESHOLD",
    "stt_max_duration": "STT_MAX_DURATION",
    "browser_viewport_width": "BROWSER_VIEWPORT_WIDTH",
    "browser_viewport_height": "BROWSER_VIEWPORT_HEIGHT",
    "cpu_warn_threshold": "CPU_WARN_THRESHOLD",
    "ram_warn_threshold": "RAM_WARN_THRESHOLD",
    "disk_warn_threshold": "DISK_WARN_THRESHOLD",
    "distraction_sites": "DISTRACTION_SITES",
    "smtp_server": "SMTP_SERVER",
    "smtp_port": "SMTP_PORT",
    "smtp_email": "SMTP_EMAIL",
    "smtp_password": "SMTP_PASSWORD",
    "imap_server": "IMAP_SERVER",
    "mongodb_uri": "MONGODB_URI",
    "meridian_log_level": "MERIDIAN_LOG_LEVEL"
}

class ProfileSaveRequest(BaseModel):
    tavily_key: Optional[str] = None
    discord_token: Optional[str] = None
    telegram_token: Optional[str] = None
    telegram_chat_id: Optional[str] = None
    meridian_model: Optional[str] = None
    meridian_vision_model: Optional[str] = None
    meridian_model_source: Optional[str] = None
    groq_key: Optional[str] = None
    openrouter_key: Optional[str] = None
    mistral_key: Optional[str] = None
    openai_key: Optional[str] = None
    anthropic_key: Optional[str] = None
    gemini_key: Optional[str] = None
    deepseek_key: Optional[str] = None
    meridian_provider: Optional[str] = None
    ollama_host: Optional[str] = None
    first_run_completed: Optional[bool] = None
    meridian_auditor_model: Optional[str] = None
    meridian_voice: Optional[str] = None
    wakeword_threshold: Optional[float] = None
    wakeword_model_filename: Optional[str] = None
    wakeword_phrase: Optional[str] = None
    stt_model_size: Optional[str] = None
    stt_silence_timeout: Optional[float] = None
    stt_vad_threshold: Optional[float] = None
    stt_max_duration: Optional[float] = None
    browser_viewport_width: Optional[int] = None
    browser_viewport_height: Optional[int] = None
    cpu_warn_threshold: Optional[float] = None
    ram_warn_threshold: Optional[float] = None
    disk_warn_threshold: Optional[float] = None
    distraction_sites: Optional[List[str]] = None
    smtp_server: Optional[str] = None
    smtp_port: Optional[int] = None
    smtp_email: Optional[str] = None
    smtp_password: Optional[str] = None
    imap_server: Optional[str] = None
    mongodb_uri: Optional[str] = None
    meridian_log_level: Optional[str] = None
    embedding_model: Optional[str] = None

class ClipboardRequest(BaseModel):
    text: str

@router.post("/api/profile/save")
def profile_save(req: ProfileSaveRequest):
    try:
        update_data = req.model_dump(exclude_unset=True)
        for k, v in update_data.items():
            if v is not None:
                save_user_profile(k, v)
                env_key = ENV_KEY_MAP.get(k)
                if env_key:
                    os.environ[env_key] = str(v)
                    update_local_env_file(env_key, str(v))
        save_user_profile("first_run_completed", True)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/profile/all")
def profile_get_all():
    try:
        keys = [
            "tavily_key", "discord_token", "telegram_token", "telegram_chat_id",
            "meridian_model", "meridian_vision_model", "meridian_model_source",
            "openai_key", "anthropic_key", "gemini_key", "deepseek_key", "groq_key", "openrouter_key", "mistral_key",
            "meridian_provider", "ollama_host", "first_run_completed",
            "meridian_auditor_model", "meridian_voice", "wakeword_threshold",
            "wakeword_model_filename", "wakeword_phrase", "stt_model_size",
            "stt_silence_timeout", "stt_vad_threshold", "stt_max_duration",
            "browser_viewport_width", "browser_viewport_height",
            "cpu_warn_threshold", "ram_warn_threshold", "disk_warn_threshold",
            "distraction_sites", "smtp_server", "smtp_port", "smtp_email",
            "smtp_password", "imap_server", "mongodb_uri", "meridian_log_level"
        ]
        profile = {}
        for k in keys:
            val = get_user_profile(k)
            if val is not None:
                profile[k] = val
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/profile/get")
def profile_get(key: str):
    try:
        val = get_user_profile(key)
        return {"key": key, "value": val}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/profile/pomodoro/increment")
def increment_pomodoro():
    try:
        current = get_user_profile("pomodoros_completed")
        if current is None:
            current = 0
        try:
            current = int(current)
        except Exception:
            current = 0
        new_val = current + 1
        save_user_profile("pomodoros_completed", new_val)
        return {"status": "success", "pomodoros_completed": new_val}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/clipboard/add")
def clipboard_add(request: ClipboardRequest):
    try:
        add_clipboard_history(request.text)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/clipboard/history")
def clipboard_history(limit: Optional[int] = 50):
    try:
        history = get_clipboard_history(limit or 50)
        return {"history": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/clipboard/clear")
def clipboard_clear():
    try:
        db = get_mongo_db()
        if db is not None:
            try:
                db["smart_clipboard"].delete_many({})
            except Exception:
                pass
        conn = get_sqlite_conn()
        conn.execute("DELETE FROM clipboard_history;")
        conn.commit()
        conn.close()
        return {"status": "cleared"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
