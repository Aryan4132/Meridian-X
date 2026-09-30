"""
MOB-01: Mobile WebSocket Companion Bridge & Network Interface Resolver.
Supports full-duplex real-time communication between Meridian-X Mobile App (Tauri v2)
and Meridian-X Backend over Local LAN (192.168.x.x) and Tailscale VPN (100.x.y.z & MagicDNS).
"""

import os
import json
import time
import logging
import socket
from typing import Dict, List, Any, Optional
from fastapi import WebSocket

logger = logging.getLogger("meridian.mobile_bridge")


def collect_telemetry() -> Dict[str, Any]:
    """Builds a live telemetry snapshot for mobile clients (cpu/mem via psutil)."""
    cpu_pct = 0.0
    mem_mb = 0.0
    try:
        import psutil
        # interval=0 is non-blocking (returns value since last call, 0.0 on
        # first call) so ping handling never stalls the event loop.
        cpu_pct = float(psutil.cpu_percent(interval=0))
        mem_mb = float(psutil.virtual_memory().used / (1024 * 1024))
    except Exception:
        pass
    return {
        "cpu_percent": round(cpu_pct, 1),
        "memory_mb": round(mem_mb, 1),
        "ping_ms": 0,
        "anti_hallucination": True,
    }


def is_ws_auth_required() -> bool:
    """True when the server has an explicit mobile pairing password or strict auth configured."""
    if os.getenv("DISABLE_AUTH") == "true":
        return False
    if os.getenv("MERIDIAN_REQUIRE_MOBILE_AUTH", "false").lower() in ("true", "1"):
        return True
    return bool(
        os.getenv("MERIDIAN_PAIRING_PASSWORD")
        or os.getenv("MERIDIAN_CUSTOM_PASSWORD")
    )


def verify_mobile_ws_token(token: Optional[str]) -> bool:
    """Validates a mobile WebSocket ?token= against API key (raw or SHA-256),
    custom pairing passwords, or the P2P pairing secret. Open LAN access is
    allowed when no explicit pairing password is configured."""
    if not is_ws_auth_required():
        if not token:
            return True
    if not token:
        return False
    try:
        from src.core.auth import verify_provided_token
        if verify_provided_token(token):
            return True
    except Exception:
        pass
    try:
        from src.core.p2p import verify_mobile_pairing_secret
        if verify_mobile_pairing_secret(token):
            return True
    except Exception:
        pass
    if not is_ws_auth_required():
        return True
    return False


def get_network_addresses(port: Optional[int] = None) -> Dict[str, Any]:
    """
    Detects active network interfaces to surface LAN IPs (192.168.x.x, 10.x.x.x, 172.16.x.x)
    and Tailscale mesh network IPs (100.x.y.z) & hostnames.
    """
    effective_port = port or int(os.getenv("PORT", "4132"))
    addresses: Dict[str, Any] = {
        "local_ips": [],
        "tailscale_ips": [],
        "hostname": socket.gethostname(),
        "tailscale_fqdn": None,
        "default_port": effective_port,
        "endpoints": []
    }


    
    # Attempt hostname resolution
    try:
        host_ip = socket.gethostbyname(socket.gethostname())
        if host_ip and host_ip != "127.0.0.1":
            if host_ip.startswith("100."):
                addresses["tailscale_ips"].append(host_ip)
            else:
                addresses["local_ips"].append(host_ip)
    except Exception:
        pass

    # Interface scan via socket probe
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.5)
        s.connect(("8.8.8.8", 80))
        lan_ip = s.getsockname()[0]
        s.close()
        if lan_ip and lan_ip not in addresses["local_ips"] and lan_ip != "127.0.0.1":
            if lan_ip.startswith("100."):
                if lan_ip not in addresses["tailscale_ips"]:
                    addresses["tailscale_ips"].append(lan_ip)
            else:
                addresses["local_ips"].append(lan_ip)
    except Exception:
        pass

    # Try resolving via psutil if available
    try:
        import psutil
        for net_if, net_addrs in psutil.net_if_addrs().items():
            for addr in net_addrs:
                if addr.family == socket.AF_INET:
                    ip = addr.address
                    if ip == "127.0.0.1":
                        continue
                    if ip.startswith("100."):
                        if ip not in addresses["tailscale_ips"]:
                            addresses["tailscale_ips"].append(ip)
                    elif ip.startswith("192.168.") or ip.startswith("10.") or ip.startswith("172."):
                        if ip not in addresses["local_ips"]:
                            addresses["local_ips"].append(ip)
    except Exception:
        pass

    # Check for Tailscale CLI / FQDN environment if present
    ts_fqdn = os.getenv("TAILSCALE_FQDN")
    if ts_fqdn:
        addresses["tailscale_fqdn"] = ts_fqdn

    port = addresses["default_port"]
    
    # Construct usable WebSocket endpoints
    for ts_ip in addresses["tailscale_ips"]:
        addresses["endpoints"].append({
            "type": "tailscale",
            "ip": ts_ip,
            "ws_url": f"ws://{ts_ip}:{port}/ws",
            "http_url": f"http://{ts_ip}:{port}"
        })
        
    for lan_ip in addresses["local_ips"]:
        addresses["endpoints"].append({
            "type": "lan",
            "ip": lan_ip,
            "ws_url": f"ws://{lan_ip}:{port}/ws",
            "http_url": f"http://{lan_ip}:{port}"
        })

    # Always include localhost fallback
    addresses["endpoints"].append({
        "type": "localhost",
        "ip": "127.0.0.1",
        "ws_url": f"ws://127.0.0.1:{port}/ws",
        "http_url": f"http://127.0.0.1:{port}"
    })
    
    return addresses


class MobileConnectionManager:
    """
    Manages active WebSocket connections from Meridian-X Mobile devices.
    Provides message broadcasting, targeted commands, and telemetry streaming.
    """
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.device_registry: Dict[str, Dict[str, Any]] = {}

    async def connect(self, websocket: WebSocket, device_id: Optional[str] = None):
        """Accepts and registers incoming WebSocket connection."""
        await websocket.accept()
        self.active_connections.append(websocket)
        connected_clients.add(websocket)
        dev_id = device_id or f"device_{id(websocket)}"
        self.device_registry[dev_id] = {
            "websocket": websocket,
            "connected_at": time.time(),
            "device_id": dev_id
        }
        logger.info(f"📱 Mobile device connected: {dev_id}. Total active: {len(self.active_connections)}")
        
        # Send welcome handshake & network information
        welcome_payload = {
            "type": "handshake_ack",
            "status": "connected",
            "device_id": dev_id,
            "server_time": time.time(),
            "network": get_network_addresses()
        }
        await websocket.send_text(json.dumps(welcome_payload))

    def disconnect(self, websocket: WebSocket):
        """Unregisters disconnected WebSocket connection."""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        connected_clients.discard(websocket)
        
        # Clean up device registry
        to_delete = [dev_id for dev_id, info in self.device_registry.items() if info["websocket"] == websocket]
        for dev_id in to_delete:
            del self.device_registry[dev_id]
            logger.info(f"📱 Mobile device disconnected: {dev_id}")

    async def broadcast_to_mobile(self, message: Dict[str, Any]):
        """Broadcasts a JSON message to all connected mobile devices."""
        if not self.active_connections:
            return
            
        payload = json.dumps(message)
        disconnected = []
        
        for connection in list(self.active_connections):
            try:
                await connection.send_text(payload)
            except Exception as e:
                logger.warning(f"Failed to send to mobile client: {e}")
                disconnected.append(connection)
                
        for conn in disconnected:
            self.disconnect(conn)

    async def send_to_device(self, device_id: str, message: Dict[str, Any]) -> bool:
        """Sends a JSON message to a specific registered mobile device."""
        info = self.device_registry.get(device_id)
        if not info:
            return False
            
        try:
            await info["websocket"].send_text(json.dumps(message))
            return True
        except Exception:
            self.disconnect(info["websocket"])
            return False

    async def process_incoming_message(self, websocket: WebSocket, raw_text: str) -> Dict[str, Any]:
        """Processes incoming text payload from mobile socket, returning echo/response."""
        try:
            data = json.loads(raw_text)
        except Exception:
            data = {"type": "text_message", "content": raw_text}
            
        msg_type = data.get("type", "ping")

        if msg_type == "ping":
            return {"type": "pong", "timestamp": time.time(), "telemetry": collect_telemetry()}
            
        elif msg_type == "command":
            secret = data.get("secret", "")
            from src.core.p2p import verify_mobile_pairing_secret
            if not secret or not verify_mobile_pairing_secret(secret):
                return {
                    "type": "command_error",
                    "status": "unauthorized",
                    "error": "Invalid or missing pairing secret."
                }
            command = data.get("command", "")
            return {
                "type": "command_ack",
                "command": command,
                "status": "received",
                "response": f"echo: {command}"
            }
            
        return {
            "type": "ack",
            "received": data
        }

    async def stream_user_prompt(self, websocket: WebSocket, prompt: str) -> None:
        """Runs a mobile prompt through the ReAct agent loop and streams
        thought_step + agent_reply messages back over the socket, using the
        same event parsing as POST /api/chat."""
        import datetime

        async def send(payload: Dict[str, Any]) -> bool:
            try:
                await websocket.send_text(json.dumps(payload))
                return True
            except Exception:
                return False

        step_no = 0

        def iso_now() -> str:
            return datetime.datetime.now().isoformat()

        if not await send({
            "type": "thought_step",
            "data": {
                "id": f"mstep-{time.time()}",
                "step_number": step_no,
                "title": "Analyzing Prompt",
                "detail": prompt,
                "status": "running",
                "timestamp": iso_now(),
            },
        }):
            return

        try:
            from database import get_user_profile, get_ollama_client_host
            from src.core.loop import run_react_agent_loop

            provider = get_user_profile("meridian_provider") or os.environ.get("MERIDIAN_PROVIDER") or "ollama"
            brain_model = (
                get_user_profile("meridian_model")
                or os.environ.get("MERIDIAN_MODEL")
                or ""
            )
            model_source = (
                get_user_profile("meridian_model_source")
                or os.environ.get("MERIDIAN_MODEL_SOURCE")
                or ("local" if provider == "ollama" else "api")
            )
            ollama_host = get_ollama_client_host()

            accumulated_text = ""
            async for event_str in run_react_agent_loop(
                prompt, brain_model, ollama_host,
                model_source=model_source, api_provider=provider,
            ):
                for line in event_str.splitlines():
                    if not line.startswith("data: "):
                        continue
                    raw_data = line[6:]
                    try:
                        parsed = json.loads(raw_data)
                    except Exception:
                        if not raw_data.startswith("{"):
                            accumulated_text += raw_data
                        continue
                    if isinstance(parsed, dict):
                        if "text" in parsed and "type" in parsed:
                            step_no += 1
                            if not await send({
                                "type": "thought_step",
                                "data": {
                                    "id": f"mstep-{time.time()}-{step_no}",
                                    "step_number": step_no,
                                    "title": str(parsed.get("type", "thought")).title(),
                                    "detail": str(parsed.get("text", "")),
                                    "status": "completed",
                                    "timestamp": iso_now(),
                                },
                            }):
                                return
                        elif "chat" in parsed:
                            accumulated_text = parsed["chat"]

            await send({"type": "agent_reply", "content": accumulated_text})
        except Exception as e:
            logger.warning(f"Mobile agent stream failed: {e}")
            await send({"type": "agent_reply", "content": f"Mobile agent run failed: {e}"})


def is_streaming_request(data: Dict[str, Any]) -> bool:
    """True when a parsed WS payload needs multi-message streaming
    (handled via MobileConnectionManager.stream_user_prompt)."""
    return isinstance(data, dict) and data.get("type") == "user_prompt" and bool(str(data.get("content", "")).strip())


# Singleton mobile connection manager
mobile_manager = MobileConnectionManager()
connected_clients = set()

def broadcast_proactive_event_to_mobile(payload: Dict[str, Any]) -> int:
    """Dispatches proactive event notification and action pills to all connected mobile clients."""
    if not connected_clients:
        return 0
    text_data = json.dumps(payload)
    sent_count = 0
    disconnected = []
    for client in list(connected_clients):
        try:
            send_fn = getattr(client, "send_text", None)
            if send_fn:
                import inspect
                import asyncio
                res = send_fn(text_data)
                if inspect.isawaitable(res):
                    async def _await_res(aw):
                        await aw

                    try:
                        loop = asyncio.get_running_loop()
                        loop.create_task(_await_res(res))
                    except RuntimeError:
                        asyncio.run(_await_res(res))
                sent_count += 1
        except Exception as e:
            logger.warning(f"[MobileBridge] Failed dispatching proactive event: {e}")
            disconnected.append(client)

    for dead in disconnected:
        connected_clients.discard(dead)

    return sent_count
