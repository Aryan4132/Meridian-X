import pytest
from fastapi.testclient import TestClient

def test_perception_terminal_crash_endpoint(monkeypatch):
    from api import app
    client = TestClient(app)

    dispatched = []
    def mock_on_terminal_crash(command, exit_code, stderr):
        dispatched.append({"command": command, "exit_code": exit_code, "stderr": stderr})

    monkeypatch.setattr("src.core.proactive.on_terminal_crash", mock_on_terminal_crash)
    monkeypatch.setattr("src.core.proactive.dispatcher.on_terminal_crash", mock_on_terminal_crash)

    payload = {"command": "npm run build", "exit_code": 1, "stderr": "Module not found: error in src/index.ts"}
    res = client.post("/api/perception/terminal-crash", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    assert len(dispatched) == 1
    assert dispatched[0]["exit_code"] == 1

def test_perception_error_sense_endpoint(monkeypatch):
    from api import app
    client = TestClient(app)

    nudges = []
    def mock_publish_nudge_sync(**kwargs):
        nudges.append(kwargs)

    monkeypatch.setattr("src.core.proactive.publish_nudge_sync", mock_publish_nudge_sync)
    monkeypatch.setattr("src.core.proactive.dispatcher.publish_nudge_sync", mock_publish_nudge_sync)

    payload = {
        "app_name": "VS Code",
        "error_type": "SyntaxError",
        "error_text": "Unexpected token in file.tsx line 42",
        "suggested_fix": "Add missing closing brace"
    }
    res = client.post("/api/perception/error-sense", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    assert len(nudges) == 1
    assert "SyntaxError" in nudges[0]["title"]
    assert "file.tsx" in nudges[0]["message"]
