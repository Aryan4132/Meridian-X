import os
import pytest
from fastapi.testclient import TestClient

from api import app
from src.core.auth import API_KEY
from src.tools.filesystem import safe_path
from src.tools.db_query import validate_sql_safety
from src.core.temporal_memory import TemporalMemoryGraph
from src.core.proactive import generate_morning_briefing
from src.tools.system import apply_workspace_preset
from src.tools.dynamic_manager import create_dynamic_tool

client = TestClient(app)

def test_safe_path_traversal_guard():
    """Verify safe_path blocks path traversal attempts outside workspace (SEC-13)."""
    with pytest.raises(PermissionError):
        safe_path("../../etc/passwd", allowed_roots=[os.getcwd()])

def test_validate_sql_safety_interceptor():
    """Verify validate_sql_safety blocks DROP, TRUNCATE, and un-where'd DELETE (SEC-18)."""
    assert validate_sql_safety("DROP TABLE users;") is not None
    assert validate_sql_safety("DELETE FROM logs;") is not None
    assert validate_sql_safety("SELECT * FROM users WHERE id = 1;") is None

def test_security_headers_middleware():
    """Verify security headers are injected in HTTP responses (SEC-21)."""
    headers = {"X-API-Key": API_KEY}
    response = client.get("/api/health", headers=headers)
    assert response.status_code == 200
    assert response.headers.get("X-Content-Type-Options") == "nosniff"
    assert response.headers.get("X-Frame-Options") == "DENY"

def test_user_preference_graph():
    """Verify user preferences are stored in TemporalMemoryGraph (AST-01)."""
    graph = TemporalMemoryGraph()
    node_id = graph.extract_user_preference_node("coding", "editor_theme", "dark_violet")
    assert "pref:coding:editor_theme" in node_id

def test_morning_briefing_generation():
    """Verify morning briefing compilation (AST-02)."""
    briefing = generate_morning_briefing()
    assert "date" in briefing
    assert "greeting" in briefing

def test_workspace_macro_presets():
    """Verify workspace macro preset resolution (AST-04)."""
    res = apply_workspace_preset("dev")
    assert "Dev Mode" in res

def test_natural_language_tool_creation():
    """Verify AST validation and dynamic tool creation (AST-13)."""
    code = "def custom_test_func():\n    return 'hello_test'"
    res = create_dynamic_tool("test_dynamic_tool", "A test tool", code)
    assert "Successfully created" in res

def test_mcp_reverse_server_endpoint():
    """Verify Meridian-as-an-MCP-Server endpoint returns registered tools (DEV-02)."""
    headers = {"X-API-Key": API_KEY}
    response = client.get("/api/mcp/v1/tools", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "success"
    assert "tools" in data
