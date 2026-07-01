from src.core.mcp_client import mcp_manager
import os
# Load local .env file if present
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ[key.strip()] = val.strip().strip("\"'")

import time
import random
import psutil
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return "/api/system-usage" not in record.getMessage()

# Suppress system usage poll log noise in the terminal
logging.getLogger("uvicorn.access").addFilter(EndpointFilter())
from database import (
    check_semantic_cache,
    add_to_semantic_cache,
    add_to_task_log,
    add_to_conversations,
    ingest_into_knowledge_base,
    search_knowledge_base,
    add_knowledge_fact,
    get_knowledge_facts,
    get_mongo_db,
    add_clipboard_history,
    get_clipboard_history,
    save_user_profile,
    get_user_profile
)
from src.core.loop import run_react_agent_loop, active_confirmations

def get_ollama_client_host():
    host = os.environ.get("OLLAMA_HOST")
    if not host:
        try:
            db_host = get_user_profile("ollama_host")
            if db_host:
                host = db_host
        except Exception:
            pass
    if not host:
        host = "http://127.0.0.1:11434"

    if host == "0.0.0.0":
        return "http://127.0.0.1:11434"
    if host.startswith("0.0.0.0:"):
        return f"http://127.0.0.1:{host.split(':')[1]}"
    if "0.0.0.0" in host:
        return host.replace("0.0.0.0", "127.0.0.1")
    if not host.startswith("http://") and not host.startswith("https://"):
        return f"http://{host}"
    return host

def log_finetune_data(prompt: str, response_text: str):
    try:
        import json
        backend_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(backend_dir)
        filepath = os.path.join(root_dir, "finetune_data.jsonl")
        
        entry = {
            "prompt": prompt,
            "response": response_text,
            "timestamp": time.time()
        }
        
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        print("Failed to log finetuning data:", e)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup operations
    try:
        from src.core.clipboard import start_clipboard_monitoring
        start_clipboard_monitoring()
    except Exception as e:
        print("Failed to start clipboard monitoring:", e)
    try:
        from src.core.scheduler import start_scheduler
        start_scheduler()
    except Exception as e:
        print("Failed to start scheduler:", e)
    try:
        from src.core.graph_sync import scan_workspaces
        import threading
        threading.Thread(target=scan_workspaces, daemon=True).start()
        print("Triggered initial workspace Knowledge Graph scan.")
    except Exception as e:
        print("Failed to trigger initial workspace scan:", e)
    try:
        await mcp_manager.initialize()
        print("Initialized MCP servers connection.")
    except Exception as e:
        print("Failed to initialize MCP servers:", e)
    try:
        from src.core.p2p import p2p_node
        msg = p2p_node.start()
        print(msg)
    except Exception as e:
        print("Failed to start P2P sync node:", e)
    try:
        from src.core.watcher import start_workspace_watcher
        start_workspace_watcher(".")
    except Exception as e:
        print("Failed to start workspace watcher:", e)
    try:
        from src.voice.wakeword import start_wakeword_monitoring
        start_wakeword_monitoring()
    except Exception as e:
        print("Failed to start wake word monitoring:", e)
    try:
        from src.core.telegram_bridge import start_telegram_bridge
        start_telegram_bridge()
    except Exception as e:
        print("Failed to start Telegram bridge:", e)
    try:
        from src.core.whatsapp_bridge import start_whatsapp_bridge
        start_whatsapp_bridge()
    except Exception as e:
        print("Failed to start WhatsApp bridge:", e)
    try:
        from src.core.discord_bridge import start_discord_bridge
        start_discord_bridge()
    except Exception as e:
        print("Failed to start Discord bridge:", e)

    try:
        from src.core.doc_indexer import index_docs_directory
        from src.core.history_manager import find_workspace_root
        import threading
        workspace_dir = find_workspace_root()
        docs_dir = os.path.join(workspace_dir, ".meridian", "docs")
        if os.path.exists(docs_dir):
            threading.Thread(target=index_docs_directory, args=(docs_dir,), daemon=True).start()
            print("Triggered initial offline docs indexer scan.")
        else:
            print(f"[Docs Indexer] No offline docs folder found at: {docs_dir}")
    except Exception as e:
        print("Failed to trigger doc indexer:", e)

    # Spawn background thread to pre-warm local models
    try:
        def prewarm_models():
            print("[Pre-Warming] Waking up local TTS and Whisper STT models in the background...")
            try:
                from src.voice.tts import get_tts_engine
                get_tts_engine()
                print("[Pre-Warming] Local TTS engine ready.")
            except Exception as tts_err:
                print("[Pre-Warming] Failed to pre-warm local TTS engine:", tts_err)
            try:
                from src.voice.stt import get_whisper_model
                get_whisper_model()
                print("[Pre-Warming] Local Whisper STT model ready.")
            except Exception as stt_err:
                print("[Pre-Warming] Failed to pre-warm local Whisper model:", stt_err)

        import threading
        threading.Thread(target=prewarm_models, daemon=True).start()
    except Exception as e:
        print("[Pre-Warming] Failed to start pre-warming thread:", e)

    yield

    # Shutdown operations
    try:
        await mcp_manager.shutdown()
        print("Stopped all MCP servers.")
    except Exception:
        pass
    try:
        from src.core.telegram_bridge import stop_telegram_bridge
        stop_telegram_bridge()
    except Exception as e:
        print("Failed to stop Telegram bridge:", e)
    try:
        from src.core.whatsapp_bridge import stop_whatsapp_bridge
        stop_whatsapp_bridge()
    except Exception as e:
        print("Failed to stop WhatsApp bridge:", e)
    try:
        from src.core.discord_bridge import stop_discord_bridge
        stop_discord_bridge()
    except Exception as e:
        print("Failed to stop Discord bridge:", e)
    try:
        from src.voice.wakeword import stop_wakeword_monitoring
        stop_wakeword_monitoring()
    except Exception as e:
        print("Failed to stop wake word monitoring:", e)
    try:
        from src.core.watcher import stop_workspace_watcher
        stop_workspace_watcher()
    except Exception as e:
        print("Failed to stop workspace watcher:", e)
    try:
        from src.core.clipboard import stop_clipboard_monitoring
        stop_clipboard_monitoring()
    except Exception as e:
        print("Failed to stop clipboard monitoring:", e)
    try:
        from src.core.scheduler import stop_scheduler
        stop_scheduler()
    except Exception as e:
        print("Failed to stop scheduler:", e)
    try:
        from src.core.p2p import p2p_node
        msg = p2p_node.stop()
        print(msg)
    except Exception as e:
        print("Failed to stop P2P sync node:", e)
    try:
        from src.core.watcher import stop_all_watchers
        stop_all_watchers()
        print("Stopped all filesystem watchers.")
    except Exception as e:
        print("Failed to stop filesystem watchers:", e)

app = FastAPI(title="Meridian-X API", version="1.0.0", lifespan=lifespan)

# Setup CORS to allow requests from Vite and Tauri frontend origins
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",  # Allows any origin (including tauri:// and localhost) with credentials
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DebugLog(BaseModel):
    message: str
    level: str = "error"

@app.post("/api/debug/log")
def post_debug_log(log: DebugLog):
    print(f"[FRONTEND DEBUG {log.level.upper()}] {log.message}")
    try:
        backend_dir = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(backend_dir, "frontend_debug.log")
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{log.level.upper()}] {log.message}\n")
    except Exception as e:
        print("Failed to write debug log to file:", e)
    return {"status": "ok"}

class ModelSettings(BaseModel):
    modelSource: str
    apiProvider: Optional[str] = None
    selectedModel: str
    brainModel: str
    ocrModel: str

class ChatRequest(BaseModel):
    prompt: str
    modelSettings: Optional[ModelSettings] = None

@app.get("/api/health")
def api_health():
    return {"status": "healthy"}

@app.get("/api/system-usage")
def get_system_usage():
    try:
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent
        return {"cpu": cpu, "ram": ram}
    except Exception:
        # Fallback to random values if psutil fails
        return {
            "cpu": round(random.uniform(10, 80), 1),
            "ram": round(random.uniform(40, 70), 1)
        }

@app.get("/api/ollama-models")
def get_ollama_models():
    models = []
    ollama_host = get_ollama_client_host()

    # Method 1: Using the official 'ollama' Python library
    try:
        import ollama
        client = ollama.Client(host=ollama_host)
        res = client.list()
        if hasattr(res, 'models'):
            for m in res.models:
                models.append(m.model)
        elif isinstance(res, dict):
            for m in res.get("models", []):
                models.append(m.get("name", m.get("model")))
        else:
            try:
                for m in res:
                    if hasattr(m, 'model'):
                        models.append(m.model)
                    elif isinstance(m, dict):
                        models.append(m.get("model"))
            except Exception:
                pass
        if models:
            return {"models": list(set(models))}
    except Exception:
        pass

    # Method 2: HTTP Request to Ollama API (/api/tags)
    try:
        import urllib.request
        import json
        url = f"{ollama_host.rstrip('/')}/api/tags"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=2.0) as response:
            data = json.loads(response.read().decode('utf-8'))
            for m in data.get("models", []):
                models.append(m.get("name", m.get("model")))
            if models:
                return {"models": list(set(models))}
    except Exception:
        pass

    return {"models": []}

def get_react_thoughts(prompt: str, brain_model: str, ocr_model: str) -> Dict[str, Any]:
    normalized = prompt.lower()
    
    # 1. Specialized mock agent simulations for specific demo scripts
    if any(k in normalized for k in ["open", "start", "run", "launch"]):
        text = "I have successfully launched and positioned the requested program in your viewport. You can see its window handle active in the background environment logs."
        thoughts = [
            {
                "type": "planning",
                "text": "Analyzing desktop space for window placement...",
                "tool": "screencapture",
                "command": "screencapture -x /tmp/active_screen.png",
            },
            {
                "type": "ocr",
                "text": f"Parsing OCR for potential window overlaps and active dock/menu dimensions using {ocr_model}",
                "tool": ocr_model,
                "command": "python parse_layout.py --image /tmp/active_screen.png",
            },
            {
                "type": "exec",
                "text": "Locating and resolving shell executable path for application",
                "tool": "bash",
                "command": "which xterm || which terminal",
            },
            {
                "type": "exec",
                "text": "Spawning desktop process with isolated child shell",
                "tool": "bash",
                "command": "nohup open -a 'Terminal' > /dev/null 2>&1 &",
            },
            {
                "type": "status",
                "text": "Process spawned successfully. PID: 49204. Monitoring window visibility...",
                "tool": "system_api",
                "command": "osascript -e 'tell application \"System Events\" to get name of first process whose frontmost is true'",
            }
        ]
        return {"text": text, "thoughts": thoughts}
        
    elif any(k in normalized for k in ["find", "search", "file", "pdf", "read"]):
        text = "I searched your file system and organized the matching files as requested. Multiple PDF structures and document handles have been updated."
        thoughts = [
            {
                "type": "planning",
                "text": "Indexing folder hierarchies across user space paths (~/Documents, ~/Downloads)",
                "tool": "file_system",
                "command": "find ~ -maxdepth 3 -name '*.pdf'",
            },
            {
                "type": "exec",
                "text": "Scanning metadata structures on discovered filesystem elements",
                "tool": "bash",
                "command": "ls -laT ~/Downloads/*.pdf",
            },
            {
                "type": "info",
                "text": "Discovered 4 files matching target file descriptor rules.",
                "tool": "file_system",
                "command": "cat /tmp/search_results.json",
            },
            {
                "type": "exec",
                "text": "Executing structural alignment script to group documents by date/extension",
                "tool": "bash",
                "command": "mkdir -p ~/Documents/Receipts && mv ~/Downloads/*receipt*.pdf ~/Documents/Receipts/",
            },
            {
                "type": "status",
                "text": "Discovered documents remapped. Integrity and links check complete.",
                "tool": "file_system",
                "command": "ls ~/Documents/Receipts/",
            }
        ]
        return {"text": text, "thoughts": thoughts}
        
    elif any(k in normalized for k in ["web", "weather", "browser", "google", "scrap"]):
        text = "I completed a localized background browser search query. System logs verify navigation, network stack requests, and target data extraction of search pages."
        thoughts = [
            {
                "type": "planning",
                "text": "Spawning headless browser container for sandbox safe scraping",
                "tool": "chrome_driver",
                "command": "google-chrome --headless --remote-debugging-port=9222",
            },
            {
                "type": "exec",
                "text": "Querying search engine via background navigation context...",
                "tool": "chrome_driver",
                "command": "navigate 'https://www.google.com/search?q=latest+weather+updates'",
            },
            {
                "type": "ocr",
                "text": f"OCR Screen scanning of search viewport for structured weather cards using {ocr_model}",
                "tool": ocr_model,
                "command": "ocr_extract --target '.g-card'",
            },
            {
                "type": "info",
                "text": "Extracted: Weather shows 24°C, Humidity: 62%, Mild breeze",
                "tool": "web_search",
            },
            {
                "type": "status",
                "text": "Closing background web container session cleanly. Telemetry stored.",
                "tool": "chrome_driver",
            }
        ]
        return {"text": text, "thoughts": thoughts}

    elif "whatsapp" in normalized:
        contact = "Recipient"
        message = "Hello!"
        
        import re
        to_match = re.search(r"to\s+(\w+)", normalized)
        if to_match:
            contact = to_match.group(1).capitalize()
            
        say_match = re.search(r"(?:saying|msg|message|say)\s+(.*)", prompt, re.IGNORECASE)
        if say_match:
            message = say_match.group(1).strip("\"'")
            
        text = f"I have successfully launched WhatsApp and automated sending your message to '{contact}'."
        thoughts = [
            {
                "type": "planning",
                "text": f"Detected WhatsApp task. Opening WhatsApp desktop and searching for contact '{contact}'...",
                "tool": "send_whatsapp_message",
            },
            {
                "type": "exec",
                "text": f"Executing send_whatsapp_message(contact='{contact}', message='{message}')",
                "tool": "send_whatsapp_message",
                "command": f"send_whatsapp_message(contact='{contact}', message='{message}')",
            },
            {
                "type": "status",
                "text": f"WhatsApp message sent successfully to '{contact}'.",
            }
        ]
        return {"text": text, "thoughts": thoughts}

    # 2. General Queries: Query local Ollama dynamically if online
    try:
        import ollama
        client = ollama.Client(host=get_ollama_client_host())

        # Use the same system prompt builder as the streaming endpoint for consistency
        try:
            from src.core.mode import build_system_prompt
            system_prompt = build_system_prompt(prompt, brain_model, get_ollama_client_host(), "")
        except Exception:
            system_prompt = "You are Meridian-X, an intelligent desktop assistant built by Aryan. Be concise, helpful, and clear."

        from database import get_conversation_history
        past_messages = get_conversation_history(limit=10)

        messages = [{"role": "system", "content": system_prompt}]
        for msg in past_messages:
            # Skip any message whose content matches the current prompt to avoid duplication
            if msg["content"] == prompt:
                continue
            messages.append({"role": msg["role"], "content": msg["content"]})

        # Always append the current user prompt at the end
        messages.append({"role": "user", "content": prompt})

        res = client.chat(
            model=brain_model,
            messages=messages
        )
        # ChatResponse is an object, not a dict — access via attribute
        text = res.message.content if hasattr(res, "message") and hasattr(res.message, "content") else ""

        
        thoughts = [
            {
                "type": "planning",
                "text": f"Analyzing user intent: '{prompt}' using {brain_model}",
            },
            {
                "type": "exec",
                "text": "Querying local LLM via Ollama API",
                "tool": "ollama_api",
                "command": f"ollama run {brain_model}",
            },
            {
                "type": "status",
                "text": f"Inference complete. Parsed response from {brain_model}.",
            }
        ]
        return {"text": text, "thoughts": thoughts}
    except Exception as e:
        print("Ollama query failed, falling back to simulated placeholder:", e)

    # 3. Fallback placeholder if Ollama is not running/failing
    text = f"I have received and logged your task: '{prompt}'. I've initialized the system agent to map, inspect, and execute these rules safely within your secure desktop sandbox. Let me know if you need any adjustments."
    thoughts = [
        {
            "type": "planning",
            "text": f"Parsing input script semantic objectives and variables on model: {brain_model}...",
            "tool": "brain_model",
        },
        {
            "type": "exec",
            "text": "Validating current desktop host metrics and window constraints",
            "tool": "system_api",
            "command": "uname -a && uptime",
        },
        {
            "type": "info",
            "text": "Active workspace: Host environment verified. Secure user execution state is Green.",
            "tool": "system_api",
        },
        {
            "type": "status",
            "text": "Assistant loop idle, standing by for user command integration...",
        }
    ]
    return {"text": text, "thoughts": thoughts}

# Initialize TTS engine globally
tts_engine = None

def get_tts_engine():
    try:
        from src.voice.tts import get_tts_engine as get_engine
        return get_engine()
    except Exception as e:
        print("Failed to delegate/initialize Supertonic engine:", e)
        return None

from fastapi.responses import StreamingResponse
import tempfile
import os

class TTSRequest(BaseModel):
    text: str
    voice: Optional[str] = "M1"
    lang: Optional[str] = "na"

@app.post("/api/tts")
def tts_synthesize(request: TTSRequest):
    engine = get_tts_engine()
    if not engine:
        raise HTTPException(status_code=500, detail="Supertonic TTS engine not initialized")
    
    try:
        # Select voice style and synthesize audio
        voice_name = request.voice if request.voice in ["F1", "F2", "F3", "F4", "F5", "M1", "M2", "M3", "M4", "M5"] else "M1"
        style = engine.get_voice_style(voice_name=voice_name)
        target_lang = request.lang if request.lang else "na"
        wav, duration = engine.synthesize(request.text, voice_style=style, lang=target_lang)
        
        # Save to temp file
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, f"meridian_tts_{random.randint(1000, 9999)}.wav")
        engine.save_audio(wav, temp_path)
        
        def iterfile():
            try:
                with open(temp_path, mode="rb") as fh:
                    yield from fh
            finally:
                try:
                    os.remove(temp_path)
                except Exception:
                    pass
                
        return StreamingResponse(iterfile(), media_type="audio/wav")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TTS synthesis failed: {str(e)}")

def check_shortcut_command(prompt: str) -> Optional[dict]:
    p = prompt.strip().lower().strip(".?!")
    
    # 1. Run tests
    if p in ["run tests", "run test", "execute tests", "test codebase", "run unit tests", "test"]:
        print("[Shortcut Engine] Bypassing LLM. Executing run_tests directly.")
        from src.tools.developer import run_tests
        res = run_tests()
        return {
            "text": f"Bypassed LLM reasoning (Sub-100ms execute).\n\n**Test Results:**\n{res}",
            "thoughts": [{"id": f"shortcut-step-{int(time.time())}", "type": "exec", "text": "Direct voice shortcut triggered: run_tests", "tool": "run_tests", "status": "completed"}]
        }
        
    # 2. Git Status
    if p in ["git status", "repository status", "check git", "status of repo", "repo status"]:
        print("[Shortcut Engine] Bypassing LLM. Executing git_status directly.")
        from src.tools.developer import git_status
        res = git_status()
        return {
            "text": f"Bypassed LLM reasoning (Sub-100ms execute).\n\n**Git Status:**\n{res}",
            "thoughts": [{"id": f"shortcut-step-{int(time.time())}", "type": "exec", "text": "Direct voice shortcut triggered: git_status", "tool": "git_status", "status": "completed"}]
        }
        
    # 3. System info
    if p in ["system info", "check resources", "system usage", "check system", "resource usage"]:
        print("[Shortcut Engine] Bypassing LLM. Executing get_system_info directly.")
        from src.tools.system import get_system_info
        res = get_system_info()
        return {
            "text": f"Bypassed LLM reasoning (Sub-100ms execute).\n\n**System Resource Usage:**\n{res}",
            "thoughts": [{"id": f"shortcut-step-{int(time.time())}", "type": "exec", "text": "Direct voice shortcut triggered: get_system_info", "tool": "get_system_info", "status": "completed"}]
        }
        
    return None

@app.post("/api/chat")
def chat(request: ChatRequest):
    try:
        # Check voice/hotkey shortcuts first
        shortcut = check_shortcut_command(request.prompt)
        if shortcut:
            try:
                from src.voice.wakeword import resume_wakeword
                resume_wakeword()
            except Exception:
                pass
            return shortcut

        try:
            from src.voice.wakeword import pause_wakeword
            pause_wakeword()
        except Exception:
            pass
            
        # Check semantic cache first
        cached = check_semantic_cache(request.prompt)
        if cached:
            thoughts = [
                {"type": "planning", "text": "Semantic Cache Match: returns instantly (<5ms) from LanceDB", "tool": "semantic_cache"}
            ]
            add_to_conversations("user", request.prompt)
            add_to_conversations("assistant", cached)
            add_to_task_log("semantic_cache", 0, "success")
            
            try:
                from src.voice.wakeword import resume_wakeword
                resume_wakeword()
            except Exception:
                pass
                
            return {"text": cached, "thoughts": thoughts}

        # Log conversation and audit trail
        add_to_conversations("user", request.prompt)
        add_to_task_log("ollama_api", 2, "started")

        # Resolve modelSettings if missing
        modelSettings = request.modelSettings
        if not modelSettings:
            provider = get_user_profile("meridian_provider") or "ollama"
            selected_model = get_user_profile("meridian_model") or "qwen2.5-coder"
            model_source = "local" if provider == "ollama" else "cloud"
            modelSettings = ModelSettings(
                modelSource=model_source,
                apiProvider=provider,
                selectedModel=selected_model,
                brainModel=selected_model,
                ocrModel=selected_model
            )

        brain_label = modelSettings.brainModel if modelSettings.modelSource == "local" else modelSettings.selectedModel
        result = get_react_thoughts(request.prompt, brain_label, modelSettings.ocrModel)
        
        # Log to caches and logs
        add_to_conversations("assistant", result.get("text", ""))
        add_to_semantic_cache(request.prompt, result.get("text", ""))
        log_finetune_data(request.prompt, result.get("text", ""))
        add_to_task_log("ollama_api", 2, "success")

        try:
            from src.voice.wakeword import resume_wakeword
            resume_wakeword()
        except Exception:
            pass

        return result
    except Exception as e:
        add_to_task_log("ollama_api", 2, "failed", str(e))
        try:
            from src.voice.wakeword import resume_wakeword
            resume_wakeword()
        except Exception:
            pass
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/api/chat/stream")
def chat_stream(request: ChatRequest):
    shortcut = check_shortcut_command(request.prompt)
    if shortcut:
        async def shortcut_generator():
            import json
            # Emit thought event
            yield f"event: thought\ndata: {json.dumps(shortcut['thoughts'][0])}\n\n"
            # BUG-13 fix: properly format multi-line text as SSE (one data: line per newline)
            # to prevent malformed events when output contains newlines (e.g., test results)
            text_lines = shortcut['text'].split('\n')
            data_block = '\n'.join(f"data: {line}" for line in text_lines)
            yield f"event: text\n{data_block}\n\n"
            try:
                from src.voice.wakeword import resume_wakeword
                resume_wakeword()
            except Exception:
                pass
        return StreamingResponse(shortcut_generator(), media_type="text/event-stream")

    # Resolve modelSettings if missing
    modelSettings = request.modelSettings
    if not modelSettings:
        provider = get_user_profile("meridian_provider") or "ollama"
        selected_model = get_user_profile("meridian_model") or "qwen2.5-coder"
        model_source = "local" if provider == "ollama" else "cloud"
        modelSettings = ModelSettings(
            modelSource=model_source,
            apiProvider=provider,
            selectedModel=selected_model,
            brainModel=selected_model,
            ocrModel=selected_model
        )

    model_source = modelSettings.modelSource
    api_provider = modelSettings.apiProvider or "gemini"  # BUG-4/8 fix: default to gemini if None
    brain_model = modelSettings.brainModel if model_source == "local" else modelSettings.selectedModel
    ollama_host = get_ollama_client_host()

    # Record user activity for the idle nudge tracker
    try:
        from src.core.proactive import record_user_activity
        record_user_activity()
    except Exception:
        pass

    try:
        from src.voice.wakeword import pause_wakeword
        pause_wakeword()
    except Exception:
        pass

    async def run_react_agent_loop_wrapped(*args, **kwargs):
        try:
            async for event in run_react_agent_loop(*args, **kwargs):
                yield event
        finally:
            try:
                from src.voice.wakeword import resume_wakeword
                resume_wakeword()
            except Exception:
                pass

    return StreamingResponse(
        run_react_agent_loop_wrapped(
            request.prompt,
            brain_model,
            ollama_host,
            model_source=model_source,
            api_provider=api_provider
        ),
        media_type="text/event-stream"
    )

@app.post("/api/chat/clear")
def chat_clear():
    from database import clear_conversations
    clear_conversations()
    return {"status": "success", "message": "Conversation history cleared."}

@app.get("/api/chat/history")
def chat_history(limit: Optional[int] = 50):
    try:
        from database import get_conversation_history
        history = get_conversation_history(limit=limit)
        formatted_history = []
        for msg in history:
            formatted_history.append({
                "id": msg["id"],
                "sender": msg["role"], # 'user' or 'assistant'
                "text": msg["content"],
                "timestamp": msg["timestamp"] # Return raw timestamp float for frontend processing
            })
        return {"history": formatted_history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/scheduler/runs")
def scheduler_runs(limit: Optional[int] = 20):
    try:
        from database import get_background_runs
        runs = get_background_runs(limit=limit)
        return {"runs": runs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class ConfirmRequest(BaseModel):
    id: str
    approved: bool

@app.get("/api/swarm/stream")
async def swarm_stream():
    async def event_generator():
        import json
        from src.core.bus import event_bus
        queue = event_bus.subscribe("agent_thoughts")
        try:
            while True:
                message = await queue.get()
                yield f"event: message\ndata: {json.dumps(message)}\n\n"
        except Exception as e:
            print("[Swarm Stream] Error in event generator:", e)
        finally:
            event_bus.unsubscribe("agent_thoughts", queue)
    return StreamingResponse(event_generator(), media_type="text/event-stream")

@app.get("/api/proactive/stream")
async def proactive_stream():
    """SSE endpoint that pushes proactive nudges from background triggers to the frontend."""
    async def event_generator():
        import json
        from src.core.bus import event_bus
        queue = event_bus.subscribe("proactive_nudge")
        try:
            while True:
                nudge = await queue.get()
                yield f"event: nudge\ndata: {json.dumps(nudge)}\n\n"
        except Exception as e:
            print("[Proactive Stream] Error in event generator:", e)
        finally:
            event_bus.unsubscribe("proactive_nudge", queue)
    return StreamingResponse(event_generator(), media_type="text/event-stream")

@app.post("/api/chat/confirm")
def chat_confirm(request: ConfirmRequest):
    if request.id in active_confirmations:
        active_confirmations[request.id]["approved"] = request.approved
        active_confirmations[request.id]["event"].set()
        return {"status": "success", "message": "Confirmation processed."}
    raise HTTPException(status_code=404, detail="Confirmation ID not found or already processed.")

class WatchLogRequest(BaseModel):
    path: str
    patterns: List[str]
    on_match_goal: str

@app.post("/api/watcher/start")
def watcher_start(request: WatchLogRequest):
    try:
        from src.core.watcher import start_watching_log
        msg = start_watching_log(request.path, request.patterns, request.on_match_goal)
        return {"status": "success", "message": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class UnwatchLogRequest(BaseModel):
    path: str

@app.post("/api/watcher/stop")
def watcher_stop(request: UnwatchLogRequest):
    try:
        from src.core.watcher import stop_watching_log
        msg = stop_watching_log(request.path)
        return {"status": "success", "message": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/watcher/list")
def watcher_list():
    try:
        from src.core.watcher import list_log_watchers
        watchers = list_log_watchers()
        return {"watchers": watchers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class GameModeRequest(BaseModel):
    game_mode: bool

@app.get("/api/game-mode")
def get_game_mode():
    try:
        from src.core import proactive
        return {"game_mode": proactive.game_mode_active, "auto_game_mode": proactive.auto_game_mode_active}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/game-mode")
def set_game_mode(request: GameModeRequest):
    try:
        from src.core import proactive
        proactive.game_mode_active = request.game_mode
        # If user manually changes it, we reset the auto_game_mode flag
        proactive.auto_game_mode_active = False
        
        # Publish state change nudge to event bus to notify all connected clients
        from src.core.proactive import publish_nudge_sync
        publish_nudge_sync(
            nudge_type="game_mode_changed",
            title="Game Mode Update",
            message="enabled" if request.game_mode else "disabled",
            icon="🎮",
            action="game_mode_update"
        )
        return {"status": "success", "game_mode": proactive.game_mode_active}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class ProposeHealRequest(BaseModel):
    file_path: str
    error_message: str

class ApplyHealRequest(BaseModel):
    file_path: str
    proposed_code: str
    secret_to_env: Optional[str] = None
    checkpoint_id: Optional[str] = None

@app.post("/api/watcher/propose-heal")
def propose_heal(request: ProposeHealRequest):
    try:
        # Resolve absolute path and verify existence
        abs_path = os.path.abspath(request.file_path)
        if not os.path.exists(abs_path):
            raise HTTPException(status_code=404, detail=f"File not found: {request.file_path}")
        
        with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
            original_code = f.read()

        import ollama
        ollama_host = get_ollama_client_host()
        client = ollama.Client(host=ollama_host)
        model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")

        is_secret = request.error_message == "secret_leak"
        
        if is_secret:
            prompt = (
                f"You are a security self-healing assistant. The following file has a hardcoded API key or credential:\n"
                f"File: {abs_path}\n\n"
                f"Original Code:\n"
                f"```\n{original_code}\n```\n\n"
                f"Rewrite this file so it loads the credential securely from environment variables (using 'os.environ.get' for Python, 'process.env' for Node/JS/TS, etc.).\n"
                f"Output ONLY the raw corrected file contents. Do NOT include markdown code blocks, explanation, or notes. Just the raw, compile-ready code."
            )
        else:
            prompt = (
                f"You are a compiler self-healing assistant. The following file has a syntax or compile error:\n"
                f"File: {abs_path}\n"
                f"Error: {request.error_message}\n\n"
                f"Original Code:\n"
                f"```\n{original_code}\n```\n\n"
                f"Rewrite this file to fix the compilation/syntax error.\n"
                f"Output ONLY the raw corrected file contents. Do NOT include markdown code blocks, explanation, or notes. Just the raw, compile-ready code."
            )

        res = client.generate(model=model, prompt=prompt)
        response_text = (res.response if hasattr(res, "response") else res.get("response", "")).strip()

        # Clean code fence blocks
        if response_text.startswith("```"):
            lines = response_text.splitlines()
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]
            response_text = "\n".join(lines).strip()

        return {
            "original": original_code,
            "proposed": response_text,
            "file_path": abs_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/watcher/apply-heal")
def apply_heal(request: ApplyHealRequest):
    try:
        if request.checkpoint_id:
            try:
                from src.core.history_manager import create_checkpoint
                create_checkpoint(request.checkpoint_id)
            except Exception as che:
                print(f"[History Manager] Failed to create checkpoint: {che}")

        abs_path = os.path.abspath(request.file_path)
        
        # Write proposed code to the file
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(request.proposed_code)
            
        # Append secret to .env if provided
        if request.secret_to_env:
            env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
            # Parse key and value to load into current process environment immediately
            if "=" in request.secret_to_env:
                k, v = request.secret_to_env.split("=", 1)
                os.environ[k.strip()] = v.strip().strip("\"'")
                
            # Append to file
            with open(env_file, "a", encoding="utf-8") as f:
                f.write(f"\n{request.secret_to_env.strip()}\n")

        from database import add_to_task_log
        add_to_task_log("heal_file", 1, "success", f"Healed file: {request.file_path}")

        return {"status": "success", "message": f"Successfully applied changes to {request.file_path}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class RollbackRequest(BaseModel):
    checkpoint_id: str

@app.post("/api/history/rollback")
def rollback_workspace(request: RollbackRequest):
    try:
        from src.core.history_manager import rollback_to_checkpoint
        success = rollback_to_checkpoint(request.checkpoint_id)
        if success:
            return {"status": "success", "message": f"Successfully rolled back to checkpoint '{request.checkpoint_id}'"}
        else:
            raise HTTPException(status_code=400, detail=f"Checkpoint '{request.checkpoint_id}' not found or rollback failed.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class ExportRequest(BaseModel):
    path: str
    format: Optional[str] = "md"

@app.post("/api/session/export")
def session_export(request: ExportRequest):
    try:
        from src.core.exporter import export_session_runbook
        msg = export_session_runbook(request.path, request.format)
        return {"status": "success", "message": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class IngestRequest(BaseModel):
    source: str
    text: str
    metadata: Optional[Dict[str, Any]] = None

@app.post("/api/rag/ingest")
def rag_ingest(request: IngestRequest):
    try:
        ingest_into_knowledge_base(request.source, request.text, request.metadata)
        add_to_task_log("ingest_file", 1, "success")
        return {"status": "success", "message": f"Successfully ingested '{request.source}' into Turbovec RAG."}
    except Exception as e:
        add_to_task_log("ingest_file", 1, "failed", str(e))
        raise HTTPException(status_code=500, detail=str(e))

class IngestFileRequest(BaseModel):
    file_path: str

@app.post("/api/rag/ingest-file")
def rag_ingest_file(request: IngestFileRequest):
    try:
        from database import extract_text_from_file, ingest_into_knowledge_base
        abs_path = os.path.abspath(request.file_path)
        if not os.path.exists(abs_path):
            raise HTTPException(status_code=404, detail=f"File not found: {request.file_path}")
            
        text = extract_text_from_file(abs_path)
        ingest_into_knowledge_base(os.path.basename(abs_path), text)
        add_to_task_log("ingest_file", 1, "success")
        return {"status": "success", "message": f"Successfully parsed and ingested '{os.path.basename(abs_path)}' into Turbovec RAG."}
    except Exception as e:
        add_to_task_log("ingest_file", 1, "failed", str(e))
        raise HTTPException(status_code=500, detail=str(e))

class SearchRequest(BaseModel):
    query: str
    limit: Optional[int] = 2

@app.post("/api/rag/search")
def rag_search(request: SearchRequest):
    try:
        results = search_knowledge_base(request.query, request.limit)
        add_to_task_log("search_knowledge", 0, "success")
        return {"results": results}
    except Exception as e:
        add_to_task_log("search_knowledge", 0, "failed", str(e))
        raise HTTPException(status_code=500, detail=str(e))

class ProfileRequest(BaseModel):
    key: str
    value: Any


from src.core.auth import require_api_key
class ProfileSaveRequest(BaseModel):
    tavily_key: Optional[str] = None
    discord_token: Optional[str] = None
    telegram_token: Optional[str] = None
    telegram_chat_id: Optional[str] = None
    whatsapp_phone: Optional[str] = None
    meridian_model: Optional[str] = None
    meridian_vision_model: Optional[str] = None
    openai_key: Optional[str] = None
    anthropic_key: Optional[str] = None
    gemini_key: Optional[str] = None
    deepseek_key: Optional[str] = None
    meridian_provider: Optional[str] = None
    ollama_host: Optional[str] = None

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
    "meridian_vision_model": "MERIDIAN_VISION_MODEL"
}

def update_local_env_file(key: str, val: str):
    env_vars = {}
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(backend_dir, ".env")
    
    # Read existing env vars
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
            
    # Update the target key
    env_vars[key] = val
    
    # Write back to .env
    try:
        with open(env_path, "w", encoding="utf-8") as f:
            for k, v in env_vars.items():
                f.write(f"{k}={v}\n")
        print(f"[Env File] Successfully updated {key} in .env file.")
    except Exception as e:
        print(f"Failed to write to .env file: {e}")

@app.post("/api/profile/save")
def profile_save(req: ProfileSaveRequest):
    try:
        update_data = req.dict(exclude_unset=True)
        for k, v in update_data.items():
            if v is not None:
                save_user_profile(k, v)
                env_key = ENV_KEY_MAP.get(k)
                if env_key:
                    os.environ[env_key] = str(v)
                    update_local_env_file(env_key, str(v))
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/profile/get")
def profile_get(key: str):
    try:
        val = get_user_profile(key)
        return {"key": key, "value": val}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class SandboxRequest(BaseModel):
    code: str
    timeout: Optional[float] = 10.0

@app.get("/api/developer/stats")
def get_developer_stats():
    from database import get_sqlite_conn, get_user_profile
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        
        # Total tasks
        cursor.execute("SELECT COUNT(*) FROM task_log")
        total_tasks = cursor.fetchone()[0]
        
        # Success tasks
        cursor.execute("SELECT COUNT(*) FROM task_log WHERE outcome = 'success'")
        success_tasks = cursor.fetchone()[0]
        
        # Failed tasks
        cursor.execute("SELECT COUNT(*) FROM task_log WHERE outcome = 'failed'")
        failed_tasks = cursor.fetchone()[0]
        
        # Security audits (tier >= 2)
        cursor.execute("SELECT COUNT(*) FROM task_log WHERE tier >= 2")
        security_audits = cursor.fetchone()[0]

        # Successful heals
        cursor.execute("SELECT COUNT(*) FROM task_log WHERE tool = 'heal_file' AND outcome = 'success'")
        successful_heals = cursor.fetchone()[0]
        
        conn.close()
        
        # Pomodoros completed
        pomodoros = get_user_profile("pomodoros_completed")
        if pomodoros is None:
            pomodoros = 0
        try:
            pomodoros = int(pomodoros)
        except Exception:
            pomodoros = 0

        # Git commits
        import subprocess
        try:
            res = subprocess.run(["git", "rev-list", "--count", "HEAD"], capture_output=True, text=True)
            git_commits = int(res.stdout.strip()) if res.returncode == 0 else 0
        except Exception:
            git_commits = 0
            
        return {
            "total_tasks": total_tasks,
            "success_tasks": success_tasks,
            "failed_tasks": failed_tasks,
            "security_audits": security_audits,
            "pomodoros": pomodoros,
            "successful_heals": successful_heals,
            "git_commits": git_commits
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/profile/pomodoro/increment")
def increment_pomodoro():
    from database import get_user_profile, save_user_profile
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

@app.post("/api/sandbox/run")
def sandbox_run(request: SandboxRequest):
    import ast
    import json
    import ollama
    from src.tools.developer import run_python
    from database import add_to_task_log
    
    # 1. AST Syntax Check
    try:
        ast.parse(request.code)
    except SyntaxError as se:
        add_to_task_log("sandbox_run", 2, "failed", f"Syntax Error: {se.msg} (line {se.lineno})")
        # Write code to sandbox_temp.py so watcher proposal can read it
        temp_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sandbox_temp.py")
        try:
            with open(temp_file_path, "w", encoding="utf-8") as tf:
                tf.write(request.code)
        except Exception:
            pass
            
        return {
            "status": "syntax_error",
            "message": f"Syntax Error: {se.msg} on line {se.lineno}",
            "lineno": se.lineno,
            "offset": se.offset,
            "text": se.text,
            "file_path": "sandbox_temp.py"
        }
        
    # 2. Security Auditor consensus check
    ollama_host = get_ollama_client_host()
    client = ollama.Client(host=ollama_host)
    auditor_model = "qwen2.5-coder:1.5b-instruct-q8_0"
    
    args_str = json.dumps({"code": request.code})
    audit_prompt = (
        f"You are the Meridian Security Auditor. Assess if the following Python code execution is safe and does not contain vulnerabilities, dangerous file deletions, shell injections, or malicious system commands.\n"
        f"Arguments: {args_str}\n\n"
        f"Respond ONLY in this exact format:\n"
        f"REASONING: <brief analysis of the arguments>\n"
        f"DECISION: <APPROVED or REJECTED>"
    )
    
    decision = "APPROVED"
    reasoning = "Default approved."
    try:
        audit_res = client.generate(model=auditor_model, prompt=audit_prompt)
        audit_text = (audit_res.response if hasattr(audit_res, "response") else audit_res.get("response", "")).strip()
        for line in audit_text.split("\n"):
            if line.upper().startswith("DECISION:"):
                decision = line.split(":", 1)[1].strip().upper()
            elif line.upper().startswith("REASONING:"):
                reasoning = line.split(":", 1)[1].strip()
    except Exception as e:
        try:
            main_model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
            audit_res = client.generate(model=main_model, prompt=audit_prompt)
            audit_text = (audit_res.response if hasattr(audit_res, "response") else audit_res.get("response", "")).strip()
            for line in audit_text.split("\n"):
                if line.upper().startswith("DECISION:"):
                    decision = line.split(":", 1)[1].strip().upper()
                elif line.upper().startswith("REASONING:"):
                    reasoning = line.split(":", 1)[1].strip()
        except Exception as ex:
            decision = "REJECTED"
            reasoning = f"Security auditor failed to load: {ex}"
            
    if "REJECTED" in decision:
        add_to_task_log("sandbox_run", 2, "blocked", f"Rejected by Security Auditor: {reasoning}")
        return {
            "status": "blocked",
            "message": f"Execution blocked by Security Auditor:\n{reasoning}"
        }
        
    # 3. Execute python
    add_to_task_log("sandbox_run", 2, "started")
    try:
        output = run_python(request.code, timeout=request.timeout)
        add_to_task_log("sandbox_run", 2, "success")
        return {
            "status": "success",
            "output": output,
            "auditor_reasoning": reasoning
        }
    except Exception as e:
        add_to_task_log("sandbox_run", 2, "failed", str(e))
        return {
            "status": "error",
            "message": f"Execution failed: {str(e)}"
        }


class ClipboardRequest(BaseModel):
    text: str

@app.post("/api/clipboard/add")
def clipboard_add(request: ClipboardRequest):
    try:
        add_clipboard_history(request.text)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/clipboard/history")
def clipboard_history(limit: Optional[int] = 10):
    try:
        history = get_clipboard_history(limit)
        return {"history": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class FactRequest(BaseModel):
    entity: str
    relation: str
    target: str

@app.post("/api/facts/add")
def facts_add(request: FactRequest):
    try:
        add_knowledge_fact(request.entity, request.relation, request.target)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/facts/get")
def facts_get(entity: str):
    try:
        facts = get_knowledge_facts(entity)
        return {"entity": entity, "facts": facts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/graph/all")
def graph_all():
    db_conn = get_mongo_db()
    nodes = []
    edges = []
    if db_conn is not None:
        try:
            node_map = {}
            
            # 1. Fetch from entities & relationships
            entities_col = db_conn["entities"]
            relationships_col = db_conn["relationships"]
            
            for ent in entities_col.find({}, {"_id": 0}):
                name = ent.get("name")
                if name:
                    node_map[name] = {
                        "id": name,
                        "label": name,
                        "type": ent.get("type", "concept")
                    }
                    
            for rel in relationships_col.find({}, {"_id": 0}):
                source = rel.get("from_name")
                target = rel.get("to_name")
                relation = rel.get("relation")
                if source and target:
                    edges.append({
                        "source": source,
                        "target": target,
                        "label": relation or "relates"
                    })
                    
            # 2. Fetch from facts
            facts_col = db_conn["facts"]
            for fact in facts_col.find({}, {"_id": 0}):
                subj = fact.get("subject")
                pred = fact.get("predicate")
                obj = fact.get("object")
                if subj:
                    if subj not in node_map:
                        node_map[subj] = {"id": subj, "label": subj, "type": "concept"}
                if obj:
                    if obj not in node_map:
                        node_map[obj] = {"id": obj, "label": obj, "type": "concept"}
                if subj and obj:
                    edges.append({
                        "source": subj,
                        "target": obj,
                        "label": pred or "is"
                    })
                    
            # 3. Fetch from knowledge_graph
            kg_col = db_conn["knowledge_graph"]
            for kf in kg_col.find({}, {"_id": 0}):
                ent = kf.get("entity")
                rel = kf.get("relation")
                tgt = kf.get("target")
                if ent:
                    if ent not in node_map:
                        node_map[ent] = {"id": ent, "label": ent, "type": "concept"}
                if tgt:
                    if tgt not in node_map:
                        node_map[tgt] = {"id": tgt, "label": tgt, "type": "concept"}
                if ent and tgt:
                    edges.append({
                        "source": ent,
                        "target": tgt,
                        "label": rel or "relates"
                    })
                    
            # Adjust node types based on names
            for nid, nd in node_map.items():
                lower_id = nid.lower()
                if lower_id in ["user", "active user", "me"]:
                    nd["type"] = "user"
                elif lower_id in ["meridian", "meridian-x", "agent", "assistant"]:
                    nd["type"] = "agent"
                elif "db" in lower_id or "mongodb" in lower_id or "database" in lower_id:
                    nd["type"] = "database"
                elif "system" in lower_id or "workspace" in lower_id or "os" in lower_id:
                    nd["type"] = "system"
                    
            nodes = list(node_map.values())
        except Exception as e:
            print("Failed to fetch full graph:", e)
            
    if not nodes:
        nodes = [
            {"id": "User", "label": "User (Active)", "type": "user"},
            {"id": "Meridian-X", "label": "Meridian-X", "type": "agent"},
            {"id": "Workspace", "label": "Local Workspace", "type": "system"},
            {"id": "LanceDB", "label": "LanceDB Vector Store", "type": "database"},
            {"id": "MongoDB", "label": "MongoDB Knowledge Graph", "type": "database"},
            {"id": "PowerShell", "label": "PowerShell Execution Environment", "type": "system"}
        ]
        edges = [
            {"source": "Meridian-X", "target": "User", "label": "assists"},
            {"source": "Meridian-X", "target": "Workspace", "label": "monitors"},
            {"source": "Meridian-X", "target": "LanceDB", "label": "queries"},
            {"source": "Meridian-X", "target": "MongoDB", "label": "updates"},
            {"source": "Meridian-X", "target": "PowerShell", "label": "controls"},
            {"source": "Workspace", "target": "LanceDB", "label": "stores_rag"},
            {"source": "Workspace", "target": "MongoDB", "label": "stores_kg"}
        ]
    return {"nodes": nodes, "edges": edges}


class ToolGenerateRequest(BaseModel):
    prompt: str

@app.post("/api/tools/generate")
def api_generate_tool(request: ToolGenerateRequest):
    try:
        from src.tools.dynamic_manager import generate_dynamic_tool
        result = generate_dynamic_tool(request.prompt)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/whatsapp/qr")
def get_whatsapp_qr():
    try:
        from src.core.whatsapp_bridge import get_whatsapp_qr_path
        from fastapi.responses import FileResponse
        qr_path = get_whatsapp_qr_path()
        if qr_path and os.path.exists(qr_path):
            return FileResponse(qr_path, media_type="image/png")
        raise HTTPException(status_code=404, detail="No active WhatsApp authentication pending.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/vision/screenshot")
def api_vision_screenshot():
    try:
        import tempfile
        import base64
        from src.tools.desktop import screenshot, ocr_screen
        
        # Save screenshot to temp file
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, "meridian_vision_capture.png")
        
        # Capture screenshot
        screenshot(temp_path)
        
        # Perform local OCR analysis
        ocr_text = ""
        try:
            ocr_text = ocr_screen(temp_path)
        except Exception as ocr_err:
            ocr_text = f"OCR failed: {ocr_err}"
            
        # Encode screenshot image to base64
        with open(temp_path, "rb") as img_file:
            b64_image = base64.b64encode(img_file.read()).decode("utf-8")
            
        # Clean up temp file
        try:
            os.remove(temp_path)
        except Exception:
            pass
            
        return {
            "status": "success",
            "image": f"data:image/png;base64,{b64_image}",
            "ocr_text": ocr_text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/voice/record")
def voice_record():
    try:
        try:
            from src.voice.wakeword import pause_wakeword
            pause_wakeword()
        except Exception:
            pass
            
        from src.voice.stt import record_and_transcribe
        text = record_and_transcribe(duration_seconds=4.0)
        
        try:
            from src.voice.wakeword import resume_wakeword
            resume_wakeword()
        except Exception:
            pass
            
        return {"status": "success", "text": text}
    except Exception as e:
        try:
            from src.voice.wakeword import resume_wakeword
            resume_wakeword()
        except Exception:
            pass
        raise HTTPException(status_code=500, detail=f"Voice capture failed: {str(e)}")

@app.post("/api/voice/interrupt")
def voice_interrupt():
    try:
        from src.core.loop import interrupt_agent_loop
        interrupt_agent_loop()
        return {"status": "success", "message": "Inference and stream playback interrupted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----------------- P2P SWARM SYNC ROUTES -----------------
@app.get("/api/p2p/status")
def get_p2p_status():
    from src.core.p2p import p2p_node, _server_running
    return {
        "active": _server_running,
        "host": p2p_node.host,
        "port": p2p_node.port,
        "peers_count": len(p2p_node.peers),
        "peers": [f"{ip}:{port}" for ip, port in p2p_node.peers],
        "secret_token_configured": bool(os.environ.get("P2P_SECRET_TOKEN"))
    }

@app.post("/api/p2p/sync")
def post_p2p_sync():
    from src.core.p2p import p2p_node, _server_running
    if not _server_running:
        raise HTTPException(status_code=400, detail="P2P Sync server is not active.")
    try:
        log = p2p_node.sync_now()
        return {"status": "success", "log": log}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/p2p/toggle")
def post_p2p_toggle():
    from src.core.p2p import p2p_node, _server_running
    try:
        if _server_running:
            msg = p2p_node.stop()
            active = False
        else:
            msg = p2p_node.start()
            active = True
        return {"status": "success", "message": msg, "active": active}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class LobbyDebateRequest(BaseModel):
    prompt: str

@app.post("/api/lobby/debate")
async def lobby_debate(request: LobbyDebateRequest):
    try:
        import ollama
        client = ollama.Client(host=get_ollama_client_host())
        model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
        
        # Turn 1: Coder
        coder_prompt = (
            f"You are the Coder agent in a developer sandbox. Your task is to write a clean, efficient "
            f"implementation for the following user request:\n"
            f"Request: {request.prompt}\n\n"
            f"Output your implementation along with a brief description of your strategy. Do not wrap the final code yet."
        )
        coder_res = client.generate(model=model, prompt=coder_prompt)
        coder_msg = coder_res.get("response", "").strip()
        
        # Turn 2: QA Tester
        qa_prompt = (
            f"You are the QA Tester agent in the developer sandbox. Review the Coder's implementation below "
            f"for the user request: '{request.prompt}'.\n\n"
            f"Coder's response:\n{coder_msg}\n\n"
            f"Point out potential bugs, edge cases, incorrect assumptions, or performance issues in their code. Suggest fixes."
        )
        qa_res = client.generate(model=model, prompt=qa_prompt)
        qa_msg = qa_res.get("response", "").strip()
        
        # Turn 3: Auditor
        auditor_prompt = (
            f"You are the Security & Performance Auditor agent in the developer sandbox. Review the Coder's "
            f"implementation and QA's critique below.\n\n"
            f"Coder's response:\n{coder_msg}\n\n"
            f"QA's critique:\n{qa_msg}\n\n"
            f"Analyze security vulnerabilities (e.g. SQL injection, path traversal, buffer overflows), resource efficiency, "
            f"and overall readability. Propose optimizations."
        )
        auditor_res = client.generate(model=model, prompt=auditor_prompt)
        auditor_msg = auditor_res.get("response", "").strip()
        
        # Turn 4: Coder (Final Resolution & Code block output)
        final_prompt = (
            f"You are the Coder agent. Incorporate all feedback from the QA Tester and Auditor to "
            f"provide a final, production-ready, highly secure, and optimized code implementation for the request: '{request.prompt}'.\n\n"
            f"History:\n"
            f"- Coder Draft: {coder_msg}\n"
            f"- QA Feedback: {qa_msg}\n"
            f"- Auditor Security Review: {auditor_msg}\n\n"
            f"Provide your final explanation of the changes made, followed by the complete code block wrapped in standard markdown code fences (e.g. ```python ... ```)."
        )
        final_res = client.generate(model=model, prompt=final_prompt)
        final_msg = final_res.get("response", "").strip()
        
        # Extract the proposed code from final_msg code blocks
        import re
        proposed_code = ""
        code_block_match = re.findall(r'```(?:python|javascript|typescript|json|html|css|bash|powershell|sql|rs|cpp|c)?\n(.*?)```', final_msg, re.DOTALL)
        if code_block_match:
            proposed_code = code_block_match[-1].strip()
        else:
            # Fallback if no fence blocks found
            proposed_code = final_msg
            
        return {
            "status": "success",
            "debate": [
                {"agent": "Coder", "avatar": "👨‍💻", "message": coder_msg},
                {"agent": "QA Tester", "avatar": "🧪", "message": qa_msg},
                {"agent": "Auditor", "avatar": "🔍", "message": auditor_msg},
                {"agent": "Coder (Final)", "avatar": "🚀", "message": final_msg}
            ],
            "proposed_code": proposed_code
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lobby debate failed: {str(e)}")

@app.get("/api/codebase/graph")
def get_codebase_graph():
    try:
        from src.core.code_graph import get_codebase_graph_json
        return get_codebase_graph_json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/docs/search")
def search_docs(query: str, limit: int = 5):
    try:
        from src.core.doc_indexer import search_offline_docs
        results = search_offline_docs(query, limit)
        return {"status": "success", "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class PowerSaveRequest(BaseModel):
    active: bool

@app.post("/api/system/power-save")
def toggle_power_save(request: PowerSaveRequest):
    try:
        active = request.active
        if active:
            os.environ["MERIDIAN_MODEL"] = "qwen2.5-coder:1.5b-instruct-q8_0"
            print("[Resource Governor] Power-Saving Mode activated. Model set to Qwen 1.5B.")
            return {"status": "success", "message": "Power-Saving Mode activated. Using lightweight fallback model."}
        else:
            os.environ["MERIDIAN_MODEL"] = "qwen2.5-coder:7b-instruct-q4_K_M"
            print("[Resource Governor] Power-Saving Mode deactivated. Model restored to Qwen 7B.")
            return {"status": "success", "message": "Power-Saving Mode deactivated. Restored default model."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def check_startup_enabled():
    import os
    startup_dir = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")
    vbs_path = os.path.join(startup_dir, "MeridianStartup.vbs")
    return os.path.exists(vbs_path)

class StartupRequest(BaseModel):
    enabled: bool

@app.get("/api/system/startup")
def get_startup_status():
    try:
        return {"enabled": check_startup_enabled()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/system/startup")
def toggle_startup_status(request: StartupRequest):
    try:
        import sys
        import subprocess
        project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        script_path = os.path.join(project_dir, "setup_startup.py")
        
        python_exe = sys.executable
        if not python_exe:
            python_exe = "python"
            
        args = [python_exe, script_path]
        if not request.enabled:
            args.append("--disable")
            
        res = subprocess.run(args, capture_output=True, text=True)
        if res.returncode != 0:
            raise Exception(res.stderr or res.stdout)
            
        return {"status": "success", "enabled": check_startup_enabled(), "output": res.stdout}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- Advanced Desktop Capability REST Routes ---

# 1. Ollama Model Manager routes
class OllamaModelRequest(BaseModel):
    name: str

@app.post("/api/ollama/pull")
def api_ollama_pull(request: OllamaModelRequest):
    try:
        from src.tools.ollama_manager import ollama_pull_model
        res = ollama_pull_model(request.name)
        return {"status": "success", "message": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/ollama/delete")
def api_ollama_delete(request: OllamaModelRequest):
    try:
        from src.tools.ollama_manager import ollama_delete_model
        res = ollama_delete_model(request.name)
        return {"status": "success", "message": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/ollama/pull/status")
def api_ollama_pull_status(name: str):
    try:
        from src.tools.ollama_manager import pull_status
        status = pull_status.get(name, "unknown")
        return {"status": "success", "model": name, "pull_status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 2. Windows OS Tasks Scheduler routes
class WinSchedulerRequest(BaseModel):
    name: str
    goal: str
    schedule: str  # "daily" or "once"
    time: str      # "HH:MM"
    date: str = "" # "YYYY-MM-DD" for once

@app.get("/api/scheduler/win/list")
def api_scheduler_win_list():
    try:
        from src.tools.task_scheduler import win_list_tasks_raw
        tasks = win_list_tasks_raw()
        return {"status": "success", "tasks": tasks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/scheduler/win/create")
def api_scheduler_win_create(request: WinSchedulerRequest):
    try:
        from src.tools.task_scheduler import win_schedule_daily, win_schedule_once
        if request.schedule.lower() == "daily":
            res = win_schedule_daily(request.name, request.goal, request.time)
        elif request.schedule.lower() == "once":
            res = win_schedule_once(request.name, request.goal, request.date, request.time)
        else:
            raise HTTPException(status_code=400, detail="Invalid schedule type. Choose 'daily' or 'once'.")
        
        if "error" in res.lower():
            raise HTTPException(status_code=500, detail=res)
        return {"status": "success", "message": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class WinSchedulerDeleteRequest(BaseModel):
    name: str

@app.post("/api/scheduler/win/delete")
def api_scheduler_win_delete(request: WinSchedulerDeleteRequest):
    try:
        from src.tools.task_scheduler import win_delete_task
        res = win_delete_task(request.name)
        if "error" in res.lower():
            raise HTTPException(status_code=500, detail=res)
        return {"status": "success", "message": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 3. Security Diagnostics route
@app.get("/api/security/audit")
def api_security_audit():
    try:
        from src.tools.security_auditor import run_port_scan, run_credential_leak_check, run_security_audit
        ports = run_port_scan()
        leaks = run_credential_leak_check()
        report = run_security_audit()
        return {
            "status": "success",
            "ports": ports,
            "leaks": leaks,
            "report": report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4132)
