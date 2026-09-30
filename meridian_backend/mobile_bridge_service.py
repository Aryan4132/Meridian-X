"""
MOB-02: Standalone Resilient Mobile WebSocket Bridge Service.
Runs independently on port 4133 to maintain continuous mobile WebSocket connections
even when the main Meridian-X backend (api.exe on port 4132) closes, restarts, or crashes.
"""

import os
import sys
import time
import json
import asyncio
import logging
from typing import Optional, Dict, Any

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import httpx

# Ensure src module is importable regardless of working directory
backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from src.core.mobile_bridge import get_network_addresses, mobile_manager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (MobileBridgeService) %(message)s"
)
logger = logging.getLogger("meridian.mobile_bridge_service")

PORT = int(os.getenv("MOBILE_BRIDGE_PORT", "8765"))
MAIN_API_URL = os.getenv("MAIN_API_URL", "http://127.0.0.1:4132").rstrip("/")

from contextlib import asynccontextmanager

# Global backend status state
backend_state = {
    "online": False,
    "last_check": 0.0,
    "error_count": 0
}

_health_task: Optional[asyncio.Task] = None


async def monitor_main_backend_health():
    """Background loop polling main API health on port 4132."""
    logger.info(f"Starting main backend health monitor targeting {MAIN_API_URL}")
    while True:
        try:
            # Fresh client per poll so a backend restart can't leave us
            # with a stale connection pool.
            async with httpx.AsyncClient(timeout=1.5) as client:
                try:
                    resp = await client.get(f"{MAIN_API_URL}/api/network/endpoints")
                    is_now_online = (resp.status_code == 200)
                except Exception:
                    is_now_online = False

            was_online = backend_state["online"]
            backend_state["last_check"] = time.time()

            if is_now_online != was_online:
                backend_state["online"] = is_now_online
                status_str = "online" if is_now_online else "restarting"
                logger.info(f"📡 Main backend status transition: {was_online} -> {is_now_online}")

                # Broadcast transition event to all connected mobile clients.
                # Guarded so a broadcast failure can never kill the monitor.
                try:
                    await mobile_manager.broadcast_to_mobile({
                        "type": "backend_status",
                        "status": status_str,
                        "backend_url": MAIN_API_URL,
                        "timestamp": time.time(),
                        "message": "Main backend is online" if is_now_online else "Main backend is restarting/offline. Connection retained."
                    })
                except Exception as b_err:
                    logger.warning(f"Backend-status broadcast failed: {b_err}")
            else:
                backend_state["online"] = is_now_online
        except Exception as loop_err:
            logger.warning(f"Health monitor iteration failed (will retry): {loop_err}")

        await asyncio.sleep(2.0)


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _health_task
    _health_task = asyncio.create_task(monitor_main_backend_health())
    logger.info(f"🚀 Mobile Bridge Service online on port {PORT}")
    yield
    if _health_task:
        _health_task.cancel()
        try:
            await _health_task
        except asyncio.CancelledError:
            pass
    logger.info("Mobile Bridge Service shutting down.")


app = FastAPI(
    title="Meridian-X Resilient Mobile Bridge Service",
    description="Decoupled WebSocket gateway for Meridian-X Mobile Apps.",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    # NOTE: allow_credentials must be False with a "*" origin — Starlette
    # rejects the combination and browsers refuse credentialed responses.
    # The mobile app uses token query params, not cookies, so no credentials
    # are needed.
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/health")
def get_health():
    """Health status endpoint."""
    return {
        "status": "ok",
        "service": "mobile_bridge_service",
        "port": PORT,
        "main_backend_online": backend_state["online"],
        "active_mobile_connections": len(mobile_manager.active_connections),
        "timestamp": time.time()
    }


@app.get("/api/network/endpoints")
def api_network_endpoints():
    """Return surface endpoints including mobile bridge port."""
    return get_network_addresses(port=PORT)


@app.websocket("/ws")
@app.websocket("/api/ws/mobile")
async def mobile_websocket(websocket: WebSocket, device_id: Optional[str] = None):
    """Full-duplex WebSocket bridge connection endpoint."""
    from src.core.mobile_bridge import verify_mobile_ws_token, is_streaming_request
    if not verify_mobile_ws_token(websocket.query_params.get("token")):
        await websocket.accept()
        await websocket.send_text(json.dumps({
            "type": "command_error",
            "error": "Authentication required. Please configure your pairing password."
        }))
        await websocket.close(code=4401)
        return
    await mobile_manager.connect(websocket, device_id=device_id)
    
    # Notify initial backend state right after handshake
    await websocket.send_text(json.dumps({
        "type": "backend_status",
        "status": "online" if backend_state["online"] else "restarting",
        "timestamp": time.time()
    }))

    try:
        while True:
            raw_text = await websocket.receive_text()
            
            try:
                payload = json.loads(raw_text)
            except Exception:
                payload = {"type": "text_message", "content": raw_text}

            msg_type = payload.get("type", "ping")

            if is_streaming_request(payload):
                await websocket.send_text(json.dumps({"type": "ack", "received": "user_prompt"}))
                asyncio.create_task(
                    mobile_manager.stream_user_prompt(websocket, str(payload.get("content", "")))
                )
            elif msg_type == "command":
                # If command received and backend is online, forward to the
                # main API chat pipeline (there is no /api/agent/command
                # route — /api/chat is the supported entry point). The pairing
                # secret is never forwarded upstream.
                command_text = str(payload.get("command", "") or payload.get("content", ""))
                if backend_state["online"] and command_text.strip():
                    try:
                        async with httpx.AsyncClient(timeout=120.0) as client:
                            resp = await client.post(
                                f"{MAIN_API_URL}/api/chat",
                                json={"prompt": command_text}
                            )
                            if resp.status_code == 200:
                                body = resp.json()
                                await websocket.send_text(json.dumps({
                                    "type": "command_ack",
                                    "command": command_text,
                                    "status": "success",
                                    "response": body.get("text", body) if isinstance(body, dict) else body
                                }))
                            else:
                                await websocket.send_text(json.dumps({
                                    "type": "command_ack",
                                    "command": command_text,
                                    "status": "error",
                                    "error": f"API returned status {resp.status_code}"
                                }))
                    except Exception as err:
                        await websocket.send_text(json.dumps({
                            "type": "command_ack",
                            "command": command_text,
                            "status": "proxy_error",
                            "error": str(err)
                        }))
                else:
                    await websocket.send_text(json.dumps({
                        "type": "command_ack",
                        "command": command_text,
                        "status": "queued_offline",
                        "message": "Main backend is currently offline or restarting. Command held."
                    }))
            else:
                # Handle standard ping/pong/handshake
                res = await mobile_manager.process_incoming_message(websocket, raw_text)
                if res:
                    await websocket.send_text(json.dumps(res))

    except WebSocketDisconnect:
        mobile_manager.disconnect(websocket)
    except Exception as e:
        logger.warning(f"WebSocket session error: {e}")
        mobile_manager.disconnect(websocket)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
