"""
MOB-01: Pytest verification suite for Mobile WebSocket Companion Bridge & Tailscale Network Resolver.
"""

import sys
import os
import json
import pytest
from fastapi.testclient import TestClient

# Ensure meridian_backend root is on sys.path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from api import app
from src.core.mobile_bridge import get_network_addresses, mobile_manager


def test_network_address_resolver():
    """Verify get_network_addresses returns structured IP & endpoint list."""
    net_info = get_network_addresses()
    assert isinstance(net_info, dict)
    assert "local_ips" in net_info
    assert "tailscale_ips" in net_info
    assert "hostname" in net_info
    assert "endpoints" in net_info
    assert len(net_info["endpoints"]) > 0
    
    # Check endpoint structure
    for ep in net_info["endpoints"]:
        assert "type" in ep
        assert "ip" in ep
        assert "ws_url" in ep
        assert "http_url" in ep
        assert ep["ws_url"].startswith("ws://")


def test_network_endpoints_api():
    """Verify REST GET /api/network/endpoints endpoint returns 200 OK."""
    client = TestClient(app)
    response = client.get("/api/network/endpoints")
    assert response.status_code == 200
    data = response.json()
    assert "endpoints" in data
    assert "hostname" in data


def test_mobile_websocket_handshake_and_echo():
    """Verify full-duplex WebSocket connection, handshake ACK, ping/pong, and echo response."""
    client = TestClient(app)
    
    with client.websocket_connect("/ws?device_id=test_phone_01") as websocket:
        # 1. Receive handshake ACK
        welcome_str = websocket.receive_text()
        welcome_data = json.loads(welcome_str)
        assert welcome_data["type"] == "handshake_ack"
        assert welcome_data["status"] == "connected"
        assert welcome_data["device_id"] == "test_phone_01"
        assert "network" in welcome_data

        # 2. Send ping
        websocket.send_text(json.dumps({"type": "ping"}))
        ping_resp_str = websocket.receive_text()
        ping_resp = json.loads(ping_resp_str)
        assert ping_resp["type"] == "pong"

        # 3. Send command (hello from phone)
        from src.core.p2p import _bootstrap_p2p_token
        secret = os.environ.get("P2P_SECRET_TOKEN", "") or _bootstrap_p2p_token()
        websocket.send_text(json.dumps({"type": "command", "command": "hello from phone", "secret": secret}))
        cmd_resp_str = websocket.receive_text()
        cmd_resp = json.loads(cmd_resp_str)
        assert cmd_resp["type"] == "command_ack"
        assert cmd_resp["command"] == "hello from phone"
        assert "echo: hello from phone" in cmd_resp["response"]


def test_mobile_websocket_broadcast():
    """Verify broadcasting message to connected mobile devices."""
    client = TestClient(app)
    
    with client.websocket_connect("/api/ws/mobile?device_id=test_phone_02") as websocket:
        # Read handshake ACK
        _ = websocket.receive_text()
        
        # Trigger broadcast via mobile_manager inside thread pool to prevent event loop collision
        import asyncio
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            pool.submit(lambda: asyncio.run(mobile_manager.broadcast_to_mobile({"type": "server_push", "event": "alert", "text": "Laptop alert"}))).result()
        
        broadcast_str = websocket.receive_text()
        broadcast_data = json.loads(broadcast_str)
        assert broadcast_data["type"] == "server_push"
        assert broadcast_data["text"] == "Laptop alert"
