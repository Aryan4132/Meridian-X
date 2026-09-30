"""
Unit and integration tests for Standalone Resilient Mobile Bridge Service (MOB-02).
"""

import sys
import os
import json
import pytest
from fastapi.testclient import TestClient

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from mobile_bridge_service import app, backend_state
from src.core.mobile_bridge import get_network_addresses


@pytest.fixture
def client():
    return TestClient(app)


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "mobile_bridge_service"
    assert data["port"] == 4133
    assert "main_backend_online" in data


def test_network_endpoints_custom_port(client):
    response = client.get("/api/network/endpoints")
    assert response.status_code == 200
    data = response.json()
    assert data["default_port"] == 4133
    assert len(data["endpoints"]) > 0
    assert any(ep["ws_url"].endswith(":4133/ws") for ep in data["endpoints"])


def test_websocket_connection_and_ping(client):
    with client.websocket_connect("/ws") as websocket:
        # Handshake Ack received
        handshake = websocket.receive_json()
        assert handshake["type"] in ["handshake_ack", "backend_status"]

        # Backend initial status received
        status_msg = websocket.receive_json()
        assert status_msg["type"] in ["backend_status", "handshake_ack"]

        # Send ping payload
        websocket.send_json({"type": "ping"})
        response = websocket.receive_json()
        assert response["type"] == "pong"
        assert "timestamp" in response


def test_websocket_command_offline(client):
    backend_state["online"] = False
    with client.websocket_connect("/ws") as websocket:
        # Drain handshake messages
        websocket.receive_json()
        websocket.receive_json()

        # Send command when main backend is offline
        websocket.send_json({"type": "command", "command": "restart_test"})
        ack = websocket.receive_json()
        assert ack["type"] == "command_ack"
        assert ack["status"] == "queued_offline"
