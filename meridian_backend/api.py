import os
import time
import uuid
import json
import random
import platform
import logging
import asyncio
import psutil
from contextlib import asynccontextmanager
from typing import cast, Any, Dict, List, Optional
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, Depends
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from contextvars import ContextVar

from src.core.mcp_client import mcp_manager
from src.core.config import ENV_FILE as env_path
from dotenv import load_dotenv
if os.path.exists(env_path):
    load_dotenv(env_path)

from src.core.auth import require_api_key
from src.core.security_middleware import MaxBodySizeMiddleware, TrustedOriginMiddleware, SecurityHeadersMiddleware
from src.api.deps import (
    limiter,
    TTSRequest,
    ModelSettings,
    ChatRequest,
    generate_sse_session_token,
    validate_sse_session_token,
    run_pip_audit_vulnerability_scanner,
    configure_localhost_tls_cert,
    ENV_KEY_MAP,
    ensure_port_available,
)
from src.api.chat import router as chat_router
import src.api.voice as voice_module
from src.api.voice import router as voice_router

def get_tts_engine():
    return voice_module.get_tts_engine()


from src.api.rag import router as rag_router
from src.api.vault import router as vault_router
from src.api.scheduler import router as scheduler_router
from src.api.mcp import router as mcp_router
from src.api.system import router as system_router
from src.api.perception import router as perception_router
from src.api.models_mgmt import router as models_router
from src.api.automation import router as automation_router
from src.api.swarm import router as swarm_router
from src.api.profile import router as profile_router
from src.api.workspace import router as workspace_router

class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return "/api/system-usage" not in record.getMessage()

logging.getLogger("uvicorn.access").addFilter(EndpointFilter())


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        from database import get_user_profile
        for profile_key, env_key in ENV_KEY_MAP.items():
            if not os.environ.get(env_key):
                val = get_user_profile(profile_key)
                if val is not None and val != "":
                    os.environ[env_key] = str(val)
                    print(f"[Startup] Loaded {env_key} from database profile.")
    except Exception as e:
        print("[Startup] Failed to load database profile keys into env:", e)

    try:
        from src.core.vault import inject_vault_keys_to_env
        inject_vault_keys_to_env()
        print("[Startup] Loaded encrypted Vault custom API keys into environment.")
    except Exception as e:
        print("[Startup] Failed to inject Vault keys:", e)

    try:
        from src.core.logging_config import setup_logger
        log_file = setup_logger()
        logging.info("=========================================")
        logging.info("Starting Meridian-X Backend Service")
        logging.info(f"Process PID: {os.getpid()}")
        logging.info(f"System OS: {platform.system()} {platform.release()}")
        logging.info(f"Python Version: {platform.python_version()}")
        logging.info(f"Log File Location: {log_file}")
        logging.info("=========================================")
    except Exception as e:
        print("Failed to initialize logging:", e)

    try:
        from src.core.proactive import set_main_event_loop
        set_main_event_loop(asyncio.get_running_loop())
        print("[Startup] Bound main FastAPI event loop to proactive publisher.")
    except Exception as e:
        print("Failed to bind proactive event loop:", e)
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
        from src.tools.registry import ensure_plugins_loaded
        ensure_plugins_loaded()
    except Exception as e:
        print("Failed to auto-discover plugins:", e)
    try:
        from src.core.graph_sync import scan_workspaces
        import threading
        try:
            from src.core.history_manager import find_workspace_root
            parent_dir = os.path.dirname(find_workspace_root())
        except Exception:
            parent_dir = os.getcwd()
        threading.Thread(target=scan_workspaces, args=(parent_dir,), daemon=True).start()
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

    if not os.environ.get("TELEGRAM_BOT_TOKEN"):
        print("[Startup] Telegram bridge disabled: TELEGRAM_BOT_TOKEN not set.")
    elif not (os.environ.get("MERIDIAN_ALLOWED_TELEGRAM_IDS", "").strip()
              or os.environ.get("TELEGRAM_AUTHORIZED_CHAT_ID", "").strip()):
        print("[Startup] Telegram bridge will deny all chats: set "
              "MERIDIAN_ALLOWED_TELEGRAM_IDS or TELEGRAM_AUTHORIZED_CHAT_ID.")
    if not os.environ.get("DISCORD_BOT_TOKEN"):
        print("[Startup] Discord bridge disabled: DISCORD_BOT_TOKEN not set.")
    elif not os.environ.get("MERIDIAN_ALLOWED_DISCORD_IDS", "").strip():
        print("[Startup] Discord bridge will deny all users: set "
              "MERIDIAN_ALLOWED_DISCORD_IDS.")
    try:
        from src.core.telegram_bridge import start_telegram_bridge
        start_telegram_bridge()
    except Exception as e:
        print("Failed to start Telegram bridge:", e)

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

    try:
        await mcp_manager.shutdown()
        print("Stopped all MCP servers.")
    except Exception as e:
        print("Failed to shutdown MCP manager:", e)
    try:
        from src.core.telegram_bridge import stop_telegram_bridge
        stop_telegram_bridge()
    except Exception as e:
        print("Failed to stop Telegram bridge:", e)

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
    try:
        from src.core.logging_config import shutdown_logger
        shutdown_logger()
    except Exception as e:
        print("Failed to shut down logging:", e)

REQUEST_COUNT = Counter('meridian_api_requests_total', 'Total API requests', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('meridian_api_request_latency_seconds', 'API request latency in seconds', ['method', 'endpoint'])
ACTIVE_REQUESTS = Gauge('meridian_api_active_requests', 'Number of active API requests')
SYSTEM_CPU_USAGE = Gauge('meridian_system_cpu_usage_percent', 'System CPU usage percentage')
SYSTEM_MEMORY_USAGE = Gauge('meridian_system_memory_usage_percent', 'System memory usage percentage')

app = FastAPI(
    title="Meridian-X API",
    description="Meridian-X Backend API",
    version="1.0.0",
    lifespan=lifespan,
    dependencies=[Depends(require_api_key)],
)
from slowapi import _rate_limit_exceeded_handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, cast(Any, _rate_limit_exceeded_handler))

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    if request.url.path == "/metrics":
        return await call_next(request)
    
    method = request.method
    endpoint = request.url.path
    ACTIVE_REQUESTS.inc()
    start_time = time.time()
    try:
        response = await call_next(request)
        status_code = response.status_code
        REQUEST_COUNT.labels(method=method, endpoint=endpoint, http_status=status_code).inc()
        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(time.time() - start_time)
        return response
    except Exception:
        REQUEST_COUNT.labels(method=method, endpoint=endpoint, http_status=500).inc()
        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(time.time() - start_time)
        raise
    finally:
        ACTIVE_REQUESTS.dec()

@app.get("/metrics")
async def metrics():
    try:
        SYSTEM_CPU_USAGE.set(psutil.cpu_percent())
        SYSTEM_MEMORY_USAGE.set(psutil.virtual_memory().percent)
    except Exception:
        pass
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

correlation_id: ContextVar[str] = ContextVar("correlation_id", default="")

@app.middleware("http")
async def correlation_id_middleware(request: Request, call_next):
    correlation_id_val = request.headers.get("X-Correlation-ID") or str(uuid.uuid4())
    correlation_id.set(correlation_id_val)
    response = await call_next(request)
    response.headers["X-Correlation-ID"] = correlation_id_val
    return response

app.add_middleware(SlowAPIMiddleware)
app.add_middleware(MaxBodySizeMiddleware, max_bytes=10_485_760)
app.add_middleware(TrustedOriginMiddleware)
app.add_middleware(SecurityHeadersMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "tauri://localhost",
        "https://tauri.localhost",
        "http://tauri.localhost",
        "http://localhost",
        "https://localhost",
        "http://localhost:5173",
        "http://localhost:3000",
        "http://localhost:4132",
        "http://localhost:4133",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:4132",
        "http://127.0.0.1:4133",
        "http://10.0.2.2:4132",
        "http://10.0.2.2:4133",
    ],
    allow_origin_regex=r"^https?://(localhost|127\.0\.0\.1|\[::1\]|10\.0\.2\.2)(:\d+)?$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount all modular sub-routers
app.include_router(chat_router)
app.include_router(voice_router)
app.include_router(rag_router)
app.include_router(vault_router)
app.include_router(scheduler_router)
app.include_router(mcp_router)
app.include_router(system_router)
app.include_router(perception_router)
app.include_router(models_router)
app.include_router(automation_router)
app.include_router(swarm_router)
app.include_router(profile_router)
app.include_router(workspace_router)


@app.websocket("/ws")
@app.websocket("/api/ws/mobile")
async def mobile_websocket_endpoint(websocket: WebSocket, device_id: Optional[str] = None):
    """MOB-01: Full-Duplex WebSocket bridge between mobile app (Tauri v2 Android) and backend."""
    from src.core.mobile_bridge import (
        mobile_manager, verify_mobile_ws_token, is_streaming_request,
    )
    if not verify_mobile_ws_token(websocket.query_params.get("token")):
        await websocket.accept()
        await websocket.send_text(json.dumps({
            "type": "command_error",
            "error": "Authentication required. Please configure your pairing password."
        }))
        await websocket.close(code=4401)
        return
    await mobile_manager.connect(websocket, device_id=device_id)
    try:
        while True:
            raw_text = await websocket.receive_text()
            try:
                payload = json.loads(raw_text)
            except Exception:
                payload = {"type": "text_message", "content": raw_text}
            if is_streaming_request(payload):
                await websocket.send_text(json.dumps({"type": "ack", "received": "user_prompt"}))
                asyncio.create_task(
                    mobile_manager.stream_user_prompt(websocket, str(payload.get("content", "")))
                )
                continue
            response_payload = await mobile_manager.process_incoming_message(websocket, raw_text)
            if response_payload:
                await websocket.send_text(json.dumps(response_payload))
    except WebSocketDisconnect:
        mobile_manager.disconnect(websocket)
    except Exception:
        mobile_manager.disconnect(websocket)

@app.websocket("/ws/agent-status")
async def websocket_agent_status_stream(websocket: WebSocket):
    """WebSocket endpoint streaming real-time agent activity events."""
    from src.core.agent_status_stream import agent_status_stream_manager
    await agent_status_stream_manager.register_connection(websocket)
    try:
        while True:
            msg = await websocket.receive_text()
            if msg == "ping":
                await websocket.send_text(json.dumps({"type": "pong", "timestamp": time.time()}))
    except WebSocketDisconnect:
        agent_status_stream_manager.unregister_connection(websocket)
    except Exception:
        agent_status_stream_manager.unregister_connection(websocket)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    from fastapi.openapi.docs import get_swagger_ui_html
    return get_swagger_ui_html(
        openapi_url=app.openapi_url or "/openapi.json",
        title=f"{app.title} - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url or "/docs/oauth2-redirect",
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )

@app.get(app.swagger_ui_oauth2_redirect_url or "/docs/oauth2-redirect", include_in_schema=False)
async def swagger_ui_redirect():
    from fastapi.openapi.docs import get_swagger_ui_oauth2_redirect_html
    return get_swagger_ui_oauth2_redirect_html()


if __name__ == "__main__":
    import uvicorn
    bind_host = os.environ.get("MERIDIAN_BIND_HOST", os.environ.get("HOST", "0.0.0.0"))
    port_raw = os.environ.get("MERIDIAN_PORT", os.environ.get("PORT", "4132"))
    try:
        bind_port = int(port_raw)
    except (TypeError, ValueError):
        bind_port = 4132
    ensure_port_available(bind_port)
    uvicorn.run(app, host=bind_host, port=bind_port)
