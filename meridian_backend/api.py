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
from src.api.websockets import router as websockets_router
from src.api.browser_extension import router as browser_extension_router
from src.core.lifespan import lifespan
from database import get_ollama_client_host  # re-export for backwards compatibility

class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return "/api/system-usage" not in record.getMessage()

logging.getLogger("uvicorn.access").addFilter(EndpointFilter())




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
    allow_origin_regex=r"^(https?://(localhost|127\.0\.0\.1|\[::1\]|10\.0\.2\.2)(:\d+)?|chrome-extension://.*)$",
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
app.include_router(browser_extension_router)

app.include_router(websockets_router)


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