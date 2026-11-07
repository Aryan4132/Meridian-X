"""
Meridian-X Chrome Extension Bridge WebSocket Router
FastAPI router for handling browser extension connections.
"""

import json
import logging
import time
from typing import Any, Dict
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from src.core.browser_extension_hub import extension_manager, ExtensionConnectionManager

logger = logging.getLogger("meridian.browser_extension_api")

router = APIRouter(prefix="/api/browser", tags=["browser_extension"])

@router.websocket("/extension")
async def websocket_browser_extension(websocket: WebSocket) -> None:
    """WebSocket endpoint connecting the Meridian Manifest V3 extension."""
    await extension_manager.connect(websocket)
    try:
        while True:
            raw = await websocket.receive_text()
            extension_manager.record_activity()
            try:
                data = json.loads(raw)
            except Exception:
                continue

            msg_type = data.get("type")
            if msg_type == "handshake":
                logger.info(f"[Extension Bridge] Extension handshake: {data.get('payload')}")
                await websocket.send_text(json.dumps({
                    "type": "handshake_ack",
                    "status": "ready",
                    "server_time": time.time()
                }))
            elif msg_type == "ping":
                await websocket.send_text(json.dumps({"type": "pong", "time": time.time()}))
            elif msg_type == "rpc_response":
                req_id = data.get("id")
                result = data.get("result", {})
                if req_id:
                    extension_manager.handle_incoming_rpc_response(req_id, result)
            elif msg_type == "page_pushed":
                extension_manager._latest_tab_cache = data.get("data", {})

    except WebSocketDisconnect:
        extension_manager.disconnect(websocket)
    except Exception as e:
        logger.warning(f"[Extension Bridge] WebSocket loop error: {e}")
        extension_manager.disconnect(websocket)

@router.get("/extension/status")
async def get_extension_status() -> dict[str, Any]:
    """HTTP endpoint to check extension bridge connection status."""
    return {
        "connected": extension_manager.is_connected,
        "active_clients": len(extension_manager.active_sockets),
        "last_seen_seconds_ago": round(time.time() - extension_manager.last_seen, 1) if extension_manager.last_seen else None
    }
