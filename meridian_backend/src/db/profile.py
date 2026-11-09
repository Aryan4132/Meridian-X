import os
import json
import time
import threading
from typing import Optional, Dict, Any, Tuple, TypedDict

from src.db.connection import get_db_cursor, get_sqlite_conn, get_mongo_db

class UserProfile(TypedDict, total=False):
    meridian_model: str
    meridian_auditor_model: str
    meridian_vision_model: str
    ollama_host: str
    wakeword_model_filename: str
    custom_directives: str

_user_profile_cache: Dict[str, Tuple[Any, float]] = {}
_user_profile_lock = threading.RLock()
_PROFILE_CACHE_TTL = 30.0

_SENSITIVE_PROFILE_MARKERS = (
    "password", "secret", "token", "api_key", "apikey", "private_key",
    "credential", "passphrase",
)

def _is_sensitive_profile_key(key: str) -> bool:
    k = (key or "").lower()
    return any(marker in k for marker in _SENSITIVE_PROFILE_MARKERS)

def _profile_cipher():
    try:
        import base64 as _b64
        import hashlib as _hashlib
        from cryptography.fernet import Fernet
        from src.core.vault import get_vault_passphrase
        digest = _hashlib.sha256(get_vault_passphrase().encode("utf-8")).digest()
        return Fernet(_b64.urlsafe_b64encode(digest))
    except Exception:
        return None

def _seal_profile_value(plain_json: str) -> str:
    """Wrap a json-encoded profile value in an encrypted envelope."""
    cipher = _profile_cipher()
    if cipher is None:
        return plain_json
    try:
        token = cipher.encrypt(plain_json.encode("utf-8")).decode("utf-8")
        return json.dumps({"__enc__": True, "v": token})
    except Exception:
        return plain_json

def _open_profile_value(stored: Any) -> Any:
    """Read back a profile value that may be encrypted or legacy plaintext."""
    if isinstance(stored, str):
        try:
            parsed = json.loads(stored)
        except Exception:
            return stored
        if isinstance(parsed, dict) and parsed.get("__enc__"):
            cipher = _profile_cipher()
            if cipher is None:
                return None
            try:
                raw = cipher.decrypt(parsed["v"].encode("utf-8")).decode("utf-8")
                return json.loads(raw)
            except Exception:
                return None
        return parsed
    return stored

def save_user_profile(key: str, value: Any):
    with _user_profile_lock:
        _user_profile_cache[key] = (value, time.time())

    val_str = json.dumps(value)
    if _is_sensitive_profile_key(key):
        val_str = _seal_profile_value(val_str)

    # 1. Save to SQLite
    try:
        with get_db_cursor() as cursor:
            cursor.execute(
                "INSERT OR REPLACE INTO user_profile (key, value) VALUES (?, ?)",
                (key, val_str)
            )
        print(f"[SQLite User Profile] Updated: '{key}'")
    except Exception as e:
        print(f"[SQLite User Profile] Save failed: {e}")

    # 2. Save to MongoDB if online
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["user_profile"]
            collection.update_one(
                {"key": key},
                {"$set": {"value": val_str, "timestamp": time.time()}},
                upsert=True
            )
            print(f"[MongoDB User Profile] Updated: '{key}'")
        except Exception as e:
            print("[MongoDB User Profile] Save failed:", e)

def get_user_profile(key: Optional[str] = None) -> Any:
    """Retrieves single user profile value by key, or dictionary of all preferences if key is None."""
    if key is None:
        conn = None
        results = {}
        try:
            conn = get_sqlite_conn()
            cursor = conn.cursor()
            cursor.execute("SELECT key, value FROM user_profile")
            for r in cursor.fetchall():
                results[r["key"]] = _open_profile_value(r["value"])
        except Exception as e:
            print(f"[SQLite User Profile] Fetch all failed: {e}")
        finally:
            if conn:
                conn.close()
        return results

    now = time.time()
    with _user_profile_lock:
        if key in _user_profile_cache:
            val, cached_at = _user_profile_cache[key]
            if now - cached_at < _PROFILE_CACHE_TTL:
                return val

    # 1. Try SQLite first
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM user_profile WHERE key = ?", (key,))
        res = cursor.fetchone()
        if res:
            parsed = _open_profile_value(res["value"])
            if parsed is not None:
                with _user_profile_lock:
                    _user_profile_cache[key] = (parsed, now)
            return parsed
    except Exception as e:
        print(f"[SQLite User Profile] Fetch failed: {e}")
    finally:
        if conn:
            conn.close()

    # 2. Fallback to MongoDB
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["user_profile"]
            res = collection.find_one({"key": key})
            if res:
                val = _open_profile_value(res.get("value"))
                if val is not None:
                    with _user_profile_lock:
                        _user_profile_cache[key] = (val, now)
                return val
        except Exception as e:
            print("[MongoDB User Profile] Fetch failed:", e)
    return None

def save_user_preference(key: str, value: Any) -> str:
    """Butler memory helper: Saves user preference rule to database profile."""
    save_user_profile(key, value)
    return f"Successfully saved preference: '{key}' = '{value}'"

def get_user_preference(key: str, default: Any = None) -> Any:
    """Butler memory helper: Retrieves stored user preference rule, returning default if absent."""
    val = get_user_profile(key)
    return val if val is not None else default

def _current_get_user_profile(key: str) -> Any:
    import sys
    db = sys.modules.get("database")
    if db and hasattr(db, "get_user_profile") and db.get_user_profile is not get_user_profile:
        return db.get_user_profile(key)
    return get_user_profile(key)

def get_auditor_model() -> str:
    try:
        model = _current_get_user_profile("meridian_auditor_model")
        if model:
            return str(model)
    except Exception:
        pass
    auditor = os.environ.get("MERIDIAN_AUDITOR_MODEL")
    if auditor:
        return auditor
    return get_brain_model()

def get_model_source() -> str:
    try:
        source = _current_get_user_profile("meridian_model_source")
        if source:
            return str(source).strip()
    except Exception:
        pass
    return os.environ.get("MERIDIAN_MODEL_SOURCE", "local").strip()

def set_model_source(source: str) -> None:
    save_user_profile("meridian_model_source", source)
    os.environ["MERIDIAN_MODEL_SOURCE"] = source

def get_api_provider() -> str:
    try:
        prov = get_user_profile("meridian_provider")
        if prov:
            return str(prov)
    except Exception:
        pass
    return os.environ.get("MERIDIAN_PROVIDER", "ollama").strip()

def set_api_provider(provider: str) -> None:
    save_user_profile("meridian_provider", provider)
    os.environ["MERIDIAN_PROVIDER"] = provider

DEFAULT_TASK_ROUTES = {
    "ENGINEER":   {"provider": "deepseek",  "model": "deepseek-coder",              "source": "cloud"},
    "REVIEWER":   {"provider": "anthropic", "model": "claude-3-5-sonnet-20241022",  "source": "cloud"},
    "RESEARCHER": {"provider": "gemini",    "model": "gemini-2.0-flash",            "source": "cloud"},
    "OPERATOR":   {"provider": "openai",    "model": "gpt-4o",                      "source": "cloud"},
    "ANALYST":    {"provider": "ollama",    "model": "qwen2.5-coder:7b",            "source": "local"},
    "PROACTIVE":  {"provider": "ollama",    "model": "llama3.2:latest",             "source": "local"},
}

def get_task_routing_enabled() -> bool:
    try:
        val = get_user_profile("meridian_task_routing_enabled")
        if val is not None:
            if isinstance(val, bool):
                return val
            if isinstance(val, str):
                return val.lower() in ("true", "1", "yes")
    except Exception:
        pass
    return os.environ.get("MERIDIAN_TASK_ROUTING_ENABLED", "false").lower() in ("true", "1", "yes")

def set_task_routing_enabled(enabled: bool) -> None:
    save_user_profile("meridian_task_routing_enabled", enabled)
    os.environ["MERIDIAN_TASK_ROUTING_ENABLED"] = "true" if enabled else "false"

def get_task_model_routes() -> dict:
    try:
        val = get_user_profile("meridian_task_model_routes")
        if val:
            if isinstance(val, str):
                parsed = json.loads(val)
                if isinstance(parsed, dict):
                    merged = dict(DEFAULT_TASK_ROUTES)
                    merged.update(parsed)
                    return merged
            elif isinstance(val, dict):
                merged = dict(DEFAULT_TASK_ROUTES)
                merged.update(val)
                return merged
    except Exception:
        pass
    return dict(DEFAULT_TASK_ROUTES)

def set_task_model_routes(routes: dict) -> None:
    save_user_profile("meridian_task_model_routes", json.dumps(routes))

def get_brain_model() -> str:
    try:
        model = _current_get_user_profile("meridian_model")
        if model:
            return str(model)
    except Exception:
        pass
    return os.environ.get("MERIDIAN_MODEL", "")

def get_vision_model() -> str:
    try:
        model = _current_get_user_profile("meridian_vision_model")
        if model:
            return str(model)
    except Exception:
        pass
    return os.environ.get("MERIDIAN_VISION_MODEL", "")

def load_db_keys_to_env():
    """Automatically loads configuration settings from database profile into environment variables."""
    try:
        ENV_KEY_MAP = {
            "ollama_host": "OLLAMA_HOST",
            "openai_key": "OPENAI_API_KEY",
            "anthropic_key": "ANTHROPIC_API_KEY",
            "gemini_key": "GEMINI_API_KEY",
            "deepseek_key": "DEEPSEEK_API_KEY",
            "tavily_key": "TAVILY_API_KEY",
            "discord_token": "DISCORD_BOT_TOKEN",
            "telegram_token": "TELEGRAM_BOT_TOKEN",
            "telegram_chat_id": "TELEGRAM_CHAT_ID",
            "whatsapp_phone": "WHATSAPP_PHONE",
            "meridian_provider": "MERIDIAN_PROVIDER",
            "meridian_model": "MERIDIAN_MODEL",
            "meridian_vision_model": "MERIDIAN_VISION_MODEL",
            "meridian_auditor_model": "MERIDIAN_AUDITOR_MODEL",
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
        }
        for profile_key, env_key in ENV_KEY_MAP.items():
            if not os.environ.get(env_key):
                val = get_user_profile(profile_key)
                if val is not None and val != "":
                    os.environ[env_key] = str(val)
    except Exception:
        pass

def get_budget_cap() -> float:
    """Gets configured monthly budget cap in USD (default $10.00)."""
    try:
        val = get_user_profile("monthly_budget_cap")
        return float(val) if val else 10.0
    except Exception:
        return 10.0

def set_budget_cap(cap_usd: float) -> bool:
    """Sets monthly budget cap limit."""
    try:
        save_user_preference("monthly_budget_cap", str(cap_usd))
        return True
    except Exception:
        return False

def get_budget_enabled() -> bool:
    """Gets whether monthly budget cap enforcement is enabled (default True)."""
    try:
        val = get_user_profile("monthly_budget_enabled")
        return str(val).lower() != "false" if val is not None else True
    except Exception:
        return True

def set_budget_enabled(enabled: bool) -> bool:
    """Sets whether monthly budget cap enforcement is enabled."""
    try:
        save_user_preference("monthly_budget_enabled", str(enabled))
        return True
    except Exception:
        return False

def check_budget_exceeded() -> bool:
    """Checks if current month LLM expenditure exceeds user budget cap."""
    if not get_budget_enabled():
        return False
    from src.db.logs import get_spend_stats
    stats = get_spend_stats()
    return stats.get("budget_exceeded", False)

def get_autonomous_mode() -> bool:
    """Returns whether autonomous multi-step loop mode is enabled (default True)."""
    try:
        val = get_user_profile("autonomous_loop_mode")
        return str(val).lower() != "false" if val is not None else True
    except Exception:
        return True

def set_autonomous_mode(enabled: bool) -> bool:
    """Sets whether autonomous multi-step loop mode is enabled."""
    try:
        save_user_preference("autonomous_loop_mode", str(enabled))
        return True
    except Exception:
        return False

def get_security_guard_level() -> int:
    """Gets current System Guard security level (1=Strict Gates, 0=Unrestricted PC Mode). Default 1."""
    try:
        val = get_user_profile("security_guard_level")
        return int(val) if val is not None else 1
    except Exception:
        return 1

def set_security_guard_level(level: int) -> bool:
    """Sets System Guard security level (1=Strict, 0=Unrestricted)."""
    try:
        save_user_preference("security_guard_level", str(level))
        return True
    except Exception:
        return False

def get_unrestricted_pc_access() -> bool:
    """Returns whether Unrestricted PC Access mode is active."""
    return get_security_guard_level() == 0
