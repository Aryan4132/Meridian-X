import os
import pytest
from fastapi.testclient import TestClient
from api import app
from src.core.updater import SystemUpdater
from src.core.loop import interrupt_agent_loop, get_session_interrupt_event, _interrupt_event
from src.core.vault import save_secret, get_secret, VAULT_FILE
import tempfile

@pytest.fixture
def client():
    return TestClient(app)

def test_cors_security_headers(client):
    """Verify CORS headers only permit trusted local and tauri origins."""
    # Trusted localhost origin
    res_trusted = client.options(
        "/api/health",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "GET"
        }
    )
    assert res_trusted.headers.get("access-control-allow-origin") == "http://localhost:5173"

    # Untrusted external web origin
    res_untrusted = client.options(
        "/api/health",
        headers={
            "Origin": "https://malicious-website.com",
            "Access-Control-Request-Method": "GET"
        }
    )
    assert res_untrusted.headers.get("access-control-allow-origin") is None

def test_vault_endpoints_permission_gated(client):
    """Verify vault management endpoints reject unauthenticated external requests."""
    # External untrusted origin without admin auth
    res = client.get(
        "/api/vault/keys",
        headers={
            "Origin": "https://malicious-website.com",
            "X-User-Roles": "[\"viewer\"]"
        }
    )
    assert res.status_code in (401, 403)

def test_system_updater_semver_and_swap(tmp_path):
    """Verify SystemUpdater uses semantic version comparison and safe swap."""
    updater = SystemUpdater(version="0.1.5")
    
    # Check that older version does not trigger update
    with pytest.MonkeyPatch.context() as m:
        class MockResponse:
            status_code = 200
            def json(self):
                return {
                    "tag_name": "v0.1.4",
                    "assets": []
                }
        m.setattr("httpx.get", lambda *args, **kwargs: MockResponse())
        res = updater.check_for_updates()
        assert res["update_available"] is False

        # Newer version triggers update
        class MockNewResponse:
            status_code = 200
            def json(self):
                return {
                    "tag_name": "v0.2.0",
                    "assets": []
                }
        m.setattr("httpx.get", lambda *args, **kwargs: MockNewResponse())
        res_new = updater.check_for_updates()
        assert res_new["update_available"] is True

    # Test safe_swap_binary with backup creation
    target_bin = tmp_path / "app.exe"
    new_bin = tmp_path / "app_new.exe"
    target_bin.write_bytes(b"original_app_bytes")
    new_bin.write_bytes(b"updated_app_bytes")

    success, backup_path = updater.safe_swap_binary(str(target_bin), str(new_bin))
    assert success is True
    assert os.path.exists(backup_path)
    assert target_bin.read_bytes() == b"updated_app_bytes"

def test_perception_open_url_safety(client):
    """Verify open-url endpoint blocks non-http schemes."""
    # Attempt file scheme
    res = client.post("/api/utils/open-url", json={"url": "file:///C:/Windows/System32/calc.exe"})
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "error"
    assert "Only HTTP and HTTPS" in data["message"]

def test_loop_session_scoped_interruption():
    """Verify agent loop interrupt events can be scoped per session."""
    session_a = "session_alpha"
    session_b = "session_beta"
    
    ev_a = get_session_interrupt_event(session_a)
    ev_b = get_session_interrupt_event(session_b)
    
    ev_a.clear()
    ev_b.clear()
    _interrupt_event.clear()
    
    # Interrupt only session A
    interrupt_agent_loop(session_id=session_a)
    assert ev_a.is_set() is True
    assert ev_b.is_set() is False
    
    # Global interrupt signals both
    interrupt_agent_loop()
    assert ev_b.is_set() is True
