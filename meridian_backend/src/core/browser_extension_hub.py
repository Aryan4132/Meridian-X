"""
Meridian-X Chrome Extension Connection Manager Singleton
Decoupled from FastAPI routers to completely prevent circular imports with tool registry.
"""

import asyncio
import json
import logging
import time
import uuid
from typing import Any, Dict, List, Optional

logger = logging.getLogger("meridian.browser_extension_hub")

class ExtensionConnectionManager:
    """Manages active Chrome extension WebSocket clients and dispatches RPC requests."""

    def __init__(self) -> None:
        self.active_sockets: list[Any] = []
        self._pending_requests: dict[str, asyncio.Future[dict[str, Any]]] = {}
        self._latest_tab_cache: dict[str, Any] = {}
        self.last_seen: float = 0.0

    @property
    def is_connected(self) -> bool:
        return len(self.active_sockets) > 0 and (time.time() - self.last_seen < 60)

    async def connect(self, websocket: Any) -> None:
        await websocket.accept()
        self.active_sockets.append(websocket)
        self.last_seen = time.time()
        logger.info(f"[ExtensionManager] Chrome extension connected. Total active: {len(self.active_sockets)}")

    def disconnect(self, websocket: Any) -> None:
        if websocket in self.active_sockets:
            self.active_sockets.remove(websocket)
        logger.info(f"[ExtensionManager] Chrome extension disconnected. Remaining: {len(self.active_sockets)}")

    def record_activity(self) -> None:
        self.last_seen = time.time()

    async def send_rpc(self, action: str, params: Optional[dict[str, Any]] = None, timeout: float = 12.0) -> dict[str, Any]:
        """Send an RPC request to the connected Chrome extension and wait for correlation response."""
        if not self.active_sockets:
            return {"success": False, "error": "Chrome extension is not currently connected to Meridian"}

        ws = self.active_sockets[-1]
        req_id = str(uuid.uuid4())[:8]
        fut: asyncio.Future[dict[str, Any]] = asyncio.get_running_loop().create_future()
        self._pending_requests[req_id] = fut

        payload = {
            "id": req_id,
            "action": action,
            "params": params or {}
        }

        try:
            await ws.send_text(json.dumps(payload))
            self.record_activity()
            result = await asyncio.wait_for(fut, timeout=timeout)
            return result
        except asyncio.TimeoutError:
            return {"success": False, "error": f"Chrome extension timed out executing action: {action}"}
        except Exception as e:
            return {"success": False, "error": f"Chrome extension RPC failed: {str(e)}"}
        finally:
            self._pending_requests.pop(req_id, None)

    def handle_incoming_rpc_response(self, req_id: str, result: dict[str, Any]) -> None:
        self.record_activity()
        fut = self._pending_requests.get(req_id)
        if fut and not fut.done():
            fut.set_result(result)

# Decoupled global singleton
extension_manager = ExtensionConnectionManager()

