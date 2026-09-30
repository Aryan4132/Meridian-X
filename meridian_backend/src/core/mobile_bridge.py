"""
MOB-01: Mobile WebSocket Companion Bridge & Network Interface Resolver.
Supports full-duplex real-time communication between Meridian-X Mobile App (Tauri v2)
and Meridian-X Backend over Local LAN (192.168.x.x) and Tailscale VPN (100.x.y.z & MagicDNS).
"""

import os
import sys
import json
import time
import asyncio
import logging
import socket
from typing import Dict, List, Set, Any, Optional
from fastapi import WebSocket, WebSocketDisconnect

logger = logging.getLogger("meridian.mobile_bridge")


def get_network_addresses() -> Dict[str, Any]:
    """
    Detects active network interfaces to surface LAN IPs (192.168.x.x, 10.x.x.x, 172.16.x.x)
    and Tailscale mesh network IPs (100.x.y.z) & hostnames.
    """
    addresses = {
        "local_ips": [],
        "tailscale_ips": [],
        "hostname": socket.gethostname(),
        "tailscale_fqdn": None,
        "default_port": int(os.getenv("PORT", "4132")),
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
            return {"type": "pong", "timestamp": time.time()}
            
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


# Singleton mobile connection manager
mobile_manager = MobileConnectionManager()
