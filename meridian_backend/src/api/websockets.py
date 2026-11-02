"""Meridian-X WebSocket & API Documentation Endpoints."""

import os
import json
import time
import asyncio
from typing import Optional
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html

router = APIRouter(tags=["websockets"])


@router.websocket("/ws")
@router.websocket("/api/ws/mobile")
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


@router.websocket("/ws/agent-status")
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


@router.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Meridian-X API - Swagger UI",
        oauth2_redirect_url="/docs/oauth2-redirect",
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )


@router.get("/docs/oauth2-redirect", include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()
