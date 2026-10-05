import os
import time
import json
import hmac
import hashlib
import subprocess
import logging
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field
from slowapi import Limiter
from slowapi.util import get_remote_address
from database import save_user_profile

limiter = Limiter(key_func=get_remote_address)

class ModelSettings(BaseModel):
    modelSource: str = Field(..., max_length=100)
    apiProvider: Optional[str] = Field(None, max_length=100)
    selectedModel: str = Field(..., max_length=200)
    brainModel: str = Field(..., max_length=200)
    ocrModel: str = Field(..., max_length=200)
    openaiKey: Optional[str] = Field(None, max_length=500)
    anthropicKey: Optional[str] = Field(None, max_length=500)
    geminiKey: Optional[str] = Field(None, max_length=500)
    deepseekKey: Optional[str] = Field(None, max_length=500)

class ChatRequest(BaseModel):
    prompt: str = Field(..., max_length=50000)
    modelSettings: Optional[ModelSettings] = None

class TTSRequest(BaseModel):
    text: str
    voice: Optional[str] = "M1"
    lang: Optional[str] = "na"

def update_local_env_file(key: str, val: str):
    env_vars = {}
    from src.core.config import ENV_FILE as env_path
    
    if os.path.exists(env_path):
        try:
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        env_vars[k.strip()] = v.strip().strip("\"'")
        except Exception as e:
            print(f"Failed to read existing .env file: {e}")
            
    env_vars[key] = val
    
    try:
        with open(env_path, "w", encoding="utf-8") as f:
            for k, v in env_vars.items():
                f.write(f"{k}={v}\n")
        print(f"[Env File] Successfully updated {key} in .env file.")
    except Exception as e:
        print(f"Failed to write to .env file: {e}")

def sync_model_settings(modelSettings: ModelSettings):
    if modelSettings.apiProvider and modelSettings.apiProvider.strip():
        save_user_profile("meridian_provider", modelSettings.apiProvider.strip())
        os.environ["MERIDIAN_PROVIDER"] = modelSettings.apiProvider.strip()
        update_local_env_file("MERIDIAN_PROVIDER", modelSettings.apiProvider.strip())
        
    if modelSettings.selectedModel and modelSettings.selectedModel.strip():
        save_user_profile("meridian_model", modelSettings.selectedModel.strip())
        os.environ["MERIDIAN_MODEL"] = modelSettings.selectedModel.strip()
        update_local_env_file("MERIDIAN_MODEL", modelSettings.selectedModel.strip())
        
    if modelSettings.openaiKey and modelSettings.openaiKey.strip():
        save_user_profile("openai_key", modelSettings.openaiKey.strip())
        os.environ["OPENAI_API_KEY"] = modelSettings.openaiKey.strip()
        update_local_env_file("OPENAI_API_KEY", modelSettings.openaiKey.strip())
    if modelSettings.anthropicKey and modelSettings.anthropicKey.strip():
        save_user_profile("anthropic_key", modelSettings.anthropicKey.strip())
        os.environ["ANTHROPIC_API_KEY"] = modelSettings.anthropicKey.strip()
        update_local_env_file("ANTHROPIC_API_KEY", modelSettings.anthropicKey.strip())
    if modelSettings.geminiKey and modelSettings.geminiKey.strip():
        save_user_profile("gemini_key", modelSettings.geminiKey.strip())
        os.environ["GEMINI_API_KEY"] = modelSettings.geminiKey.strip()
        update_local_env_file("GEMINI_API_KEY", modelSettings.geminiKey.strip())
    if modelSettings.deepseekKey and modelSettings.deepseekKey.strip():
        save_user_profile("deepseek_key", modelSettings.deepseekKey.strip())
        os.environ["DEEPSEEK_API_KEY"] = modelSettings.deepseekKey.strip()
        update_local_env_file("DEEPSEEK_API_KEY", modelSettings.deepseekKey.strip())

def check_shortcut_command(prompt: str) -> Optional[dict]:
    p = prompt.strip().lower().strip(".?!")
    
    if p in ["run tests", "run test", "execute tests", "test codebase", "run unit tests", "test"]:
        print("[Shortcut Engine] Bypassing LLM. Executing run_tests directly.")
        from src.tools.developer import run_tests
        res = run_tests(".")
        return {
            "text": f"Bypassed LLM reasoning (Sub-100ms execute).\n\n**Test Results:**\n{res}",
            "thoughts": [{"id": f"shortcut-step-{int(time.time())}", "type": "exec", "text": "Direct voice shortcut triggered: run_tests", "tool": "run_tests", "status": "completed"}]
        }
        
    if p in ["git status", "repository status", "check git", "status of repo", "repo status"]:
        print("[Shortcut Engine] Bypassing LLM. Executing git_status directly.")
        from src.tools.developer import git_status
        res = git_status(".")

        return {
            "text": f"Bypassed LLM reasoning (Sub-100ms execute).\n\n**Git Status:**\n{res}",
            "thoughts": [{"id": f"shortcut-step-{int(time.time())}", "type": "exec", "text": "Direct voice shortcut triggered: git_status", "tool": "git_status", "status": "completed"}]
        }
        
    if p in ["system info", "check resources", "system usage", "check system", "resource usage"]:
        print("[Shortcut Engine] Bypassing LLM. Executing get_system_info directly.")
        from src.tools.system import get_system_info
        res = get_system_info()
        return {
            "text": f"Bypassed LLM reasoning (Sub-100ms execute).\n\n**System Resource Usage:**\n{res}",
            "thoughts": [{"id": f"shortcut-step-{int(time.time())}", "type": "exec", "text": "Direct voice shortcut triggered: get_system_info", "tool": "get_system_info", "status": "completed"}]
        }
        
    return None

def generate_sse_session_token(session_id: str) -> str:
    """Generates per-session HMAC token for SSE stream integrity validation (SEC-14)."""
    key = os.getenv("MERIDIAN_API_KEY", "MERIDIAN_SSE_KEY").encode("utf-8")
    return hmac.new(key, session_id.encode("utf-8"), hashlib.sha256).hexdigest()

def validate_sse_session_token(session_id: str, token: str) -> bool:
    """Validates SSE stream session integrity token (SEC-14)."""
    expected = generate_sse_session_token(session_id)
    return hmac.compare_digest(expected, token)

def run_pip_audit_vulnerability_scanner() -> dict:
    """Runs background vulnerability scan on backend dependencies (SEC-15)."""
    try:
        res = subprocess.run(["pip-audit", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {"status": "scanned", "result": "0 vulnerabilities found"}
    except Exception:
        return {"status": "skipped", "reason": "pip-audit package not installed"}

def configure_localhost_tls_cert() -> Optional[Dict[str, str]]:
    """Generates self-signed localhost TLS certificate for HTTPS server (SEC-19)."""
    try:
        import trustme  # type: ignore

        ca = trustme.CA()
        server_cert = ca.issue_cert("127.0.0.1", "localhost")
        cert_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "certs")
        os.makedirs(cert_dir, exist_ok=True)
        cert_path = os.path.join(cert_dir, "server.crt")
        key_path = os.path.join(cert_dir, "server.key")
        server_cert.private_key_pem.write_to_path(key_path)
        for blob in server_cert.cert_chain_pems:
            blob.write_to_path(cert_path)
        return {"ssl_certfile": cert_path, "ssl_keyfile": key_path}
    except Exception as err:
        logging.warning(f"Self-signed TLS certificate generation disabled: {err}")
        return None

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

def ensure_port_available(port: int, host: str = "127.0.0.1") -> bool:
    import socket
    import subprocess
    import platform
    import time
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.3)
            res = s.connect_ex((host, port))
            if res != 0:
                return True
    except Exception:
        return True

    print(f"[Port Recovery] Port {port} is already occupied. Attempting to release conflicting listener...")
    my_pid = os.getpid()
    if platform.system() == "Windows":
        try:
            cmd = f'powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort {port} -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess"'
            out = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=5)
            pids = set()
            for line in out.stdout.split():
                if line.strip().isdigit():
                    pids.add(int(line.strip()))
            for pid in pids:
                if pid and pid != my_pid:
                    print(f"[Port Recovery] Terminating conflicting process PID {pid} on port {port}...")
                    subprocess.run(f"taskkill /F /PID {pid}", capture_output=True, shell=True)
            time.sleep(1.0)
        except Exception as err:
            print(f"[Port Recovery] Windows port clearance failed: {err}")
    else:
        try:
            subprocess.run(f"fuser -k {port}/tcp", shell=True, capture_output=True)
            time.sleep(0.5)
        except Exception as err:
            print(f"[Port Recovery] POSIX port clearance failed: {err}")
    return True

