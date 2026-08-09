import pytest
import asyncio
from fastapi.testclient import TestClient
from src.core.bus import event_bus
import src.core.proactive as proactive
from src.tools.registry import TOOL_REGISTRY
from api import app

client = TestClient(app)

def test_dispatch_notification_event_bus():
    async def run_test():
        loop = asyncio.get_running_loop()
        proactive.set_main_event_loop(loop)
        
        queue = event_bus.subscribe("proactive_nudge")
        
        # Test dispatch_notification
        res = proactive.dispatch_notification(
            title="System Security Alert",
            message="Suspicious activity blocked",
            priority="high",
            category="security",
            action_hint="View Audit Log",
            mascot_state="worried"
        )
        assert res["status"] == "dispatched"
        assert res["priority"] == "high"
        
        event = await asyncio.wait_for(queue.get(), timeout=2.0)
        assert event["title"] == "System Security Alert"
        assert event["type"] == "notification_security"
        assert event["icon"] == "🚨"
        assert event["mascot_state"] == "worried"

    asyncio.run(run_test())


def test_terminal_crash_and_presence_triggers():
    async def run_test():
        loop = asyncio.get_running_loop()
        proactive.set_main_event_loop(loop)
        queue = event_bus.subscribe("proactive_nudge")
        
        # Test on_terminal_crash
        proactive.on_terminal_crash("pytest tests/", 1, "AssertionError in test_main.py")
        event1 = await asyncio.wait_for(queue.get(), timeout=2.0)
        assert event1["type"] == "terminal_error"
        assert "pytest tests/" in event1["message"]
        
        # Test on_user_motion_return
        proactive.on_user_motion_return()
        event2 = await asyncio.wait_for(queue.get(), timeout=2.0)
        assert event2["type"] == "presence_return"
        assert event2["action"] == "view_briefing"

    asyncio.run(run_test())


def test_proactive_tool_registry():
    assert "send_proactive_notification" in TOOL_REGISTRY
    tool = TOOL_REGISTRY["send_proactive_notification"]
    assert tool["tier"] == 1
    
    # Test tool invocation
    res = tool["func"](title="Tool Nudge", message="Testing tool", priority="medium")
    assert res["status"] == "dispatched"


from src.core.auth import API_KEY

def test_proactive_api_endpoint():
    payload = {
        "title": "API Test Nudge",
        "message": "Testing proactive API endpoint",
        "priority": "high",
        "category": "system",
        "action_hint": "Dismiss",
        "mascot_state": "happy"
    }
    headers = {"X-API-Key": API_KEY}
    response = client.post("/api/proactive/notify", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["data"]["title"] == "API Test Nudge"

