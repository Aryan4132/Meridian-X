import pytest
import os
import sys
import json
from unittest.mock import patch, MagicMock

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)


def test_task_routing_db_helpers(monkeypatch):
    """Verify get/set of task routing flags and route configs in database."""
    from database import (
        get_task_routing_enabled,
        set_task_routing_enabled,
        get_task_model_routes,
        set_task_model_routes,
        DEFAULT_TASK_ROUTES,
    )

    # Initial state or default
    set_task_routing_enabled(False)
    assert get_task_routing_enabled() is False

    set_task_routing_enabled(True)
    assert get_task_routing_enabled() is True

    # Test routes retrieval
    routes = get_task_model_routes()
    assert "ENGINEER" in routes
    assert "REVIEWER" in routes
    assert "RESEARCHER" in routes
    assert "OPERATOR" in routes
    assert "ANALYST" in routes
    assert "PROACTIVE" in routes

    # Custom update
    custom_routes = dict(routes)
    custom_routes["ENGINEER"] = {"provider": "openai", "model": "gpt-4o", "source": "cloud"}
    set_task_model_routes(custom_routes)

    fetched = get_task_model_routes()
    assert fetched["ENGINEER"]["provider"] == "openai"
    assert fetched["ENGINEER"]["model"] == "gpt-4o"

    # Reset
    set_task_model_routes(DEFAULT_TASK_ROUTES)
    set_task_routing_enabled(False)


def test_resolve_route_for_task_when_disabled():
    """Verify route resolver returns user default model/provider when multi-mode is disabled."""
    from src.core.loop_planning import resolve_route_for_task

    with patch("database.get_task_routing_enabled", return_value=False):
        mode, model, prov, src = resolve_route_for_task(
            prompt="Write a python script to parse logs",
            default_model="default-brain",
            default_provider="ollama",
            default_source="local",
        )
        assert mode == "ENGINEER"
        assert model == "default-brain"
        assert prov == "ollama"
        assert src == "local"


def test_resolve_route_for_task_when_enabled_with_key():
    """Verify route resolver selects mode-specific cloud model when API key is present."""
    from src.core.loop_planning import resolve_route_for_task

    with patch("database.get_task_routing_enabled", return_value=True), \
         patch("src.core.llm_provider.get_api_key", return_value="sk-valid-key"):
        
        mode, model, prov, src = resolve_route_for_task(
            prompt="Search google and find out latest papers on transformer reasoning",
            default_model="default-brain",
            default_provider="ollama",
            default_source="local",
        )
        assert mode == "RESEARCHER"
        assert prov == "gemini"
        assert "gemini" in model.lower()
        assert src == "cloud"


def test_resolve_route_for_task_fallback_on_missing_key():
    """Verify route resolver safely falls back to default brain model if target provider lacks API key."""
    from src.core.loop_planning import resolve_route_for_task

    def mock_key(provider):
        return None  # No key for any cloud provider

    with patch("database.get_task_routing_enabled", return_value=True), \
         patch("src.core.llm_provider.get_api_key", side_effect=mock_key):
        
        mode, model, prov, src = resolve_route_for_task(
            prompt="Refactor this python function and fix the bug",
            default_model="my-local-llama",
            default_provider="ollama",
            default_source="local",
        )
        assert mode == "ENGINEER"
        # Should gracefully fall back to default because deepseek has no API key!
        assert model == "my-local-llama"
        assert prov == "ollama"
        assert src == "local"


def test_resolve_route_for_task_local_always_valid():
    """Verify local routes (e.g., Ollama) do not require cloud API keys and resolve cleanly."""
    from src.core.loop_planning import resolve_route_for_task

    with patch("database.get_task_routing_enabled", return_value=True):
        mode, model, prov, src = resolve_route_for_task(
            prompt="Analyze system cpu and ram usage and inspect memory",
            default_model="cloud-gpt",
            default_provider="openai",
            default_source="cloud",
        )
        assert mode == "ANALYST"
        assert prov == "ollama"
        assert src == "local"


def test_task_routes_api_endpoints():
    """Verify GET and POST endpoints for task routing configuration and testing."""
    from fastapi.testclient import TestClient
    from api import app

    client = TestClient(app)

    # 1. GET /api/settings/task-routes
    res = client.get("/api/settings/task-routes")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    assert "enabled" in data
    assert "routes" in data
    assert "default_routes" in data

    # 2. POST /api/settings/task-routes
    routes = dict(data["routes"])
    routes["OPERATOR"] = {"provider": "openai", "model": "gpt-4o", "source": "cloud"}
    post_res = client.post("/api/settings/task-routes", json={
        "enabled": True,
        "routes": routes
    })
    assert post_res.status_code == 200
    post_data = post_res.json()
    assert post_data["enabled"] is True
    assert post_data["routes"]["OPERATOR"]["model"] == "gpt-4o"

    # 3. POST /api/settings/task-routes/test
    test_res = client.post("/api/settings/task-routes/test", json={
        "prompt": "Click on the login button and browse the dashboard"
    })
    assert test_res.status_code == 200
    sim_data = test_res.json()
    assert sim_data["status"] == "success"
    assert sim_data["classified_mode"] == "OPERATOR"
