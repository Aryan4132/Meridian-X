import pytest
import os
import asyncio
from fastapi.testclient import TestClient

from api import app
from src.core.proactive_system_guard import system_guard, ProactiveSystemGuard
from src.core.deep_project_context import DeepProjectContextEngine
from src.core.workspace_orchestrator import WorkspaceOrchestrator
from src.core.self_evolving_tooling import SelfEvolvingToolingManager
from src.core.explain_code_engine import ExplainCodeEngine
from src.core.experiment_runner import ExperimentRunner
from src.core.silent_workflow_guardian import SilentWorkflowGuardian
from src.core.what_broke_detective import WhatBrokeDetective
from src.core.boilerplate_genie import BoilerplateGenie
from src.core.commit_whisperer import CommitWhisperer

client = TestClient(app)

@pytest.fixture
def temp_workspace(tmp_path):
    root = str(tmp_path)
    # Create sample files
    py_file = tmp_path / "sample.py"
    py_file.write_text("def hello():\n    print('DEBUG hello')\n", encoding="utf-8")
    return root

def test_proactive_system_guard():
    guard = ProactiveSystemGuard(memory_threshold_mb=10.0)
    res = guard.check_system_resources()
    assert "hogs" in res
    assert "disk_percent" in res

def test_deep_project_context(temp_workspace):
    engine = DeepProjectContextEngine(temp_workspace)
    res = engine.scan_workspace()
    assert res["status"] == "indexed"
    assert res["files_scanned"] >= 1

def test_workspace_orchestrator(temp_workspace):
    orchestrator = WorkspaceOrchestrator(temp_workspace)
    res = orchestrator.launch_preset("coding")
    assert res["preset"] == "coding"
    assert len(res["actions"]) > 0

def test_self_evolving_tooling(temp_workspace):
    tools_dir = os.path.join(temp_workspace, "tools")
    manager = SelfEvolvingToolingManager(tools_dir)

    code = "print('Hello from self evolving tool')"
    ticket = manager.prepare_tool_script("custom_math", code, "Simple math tool")
    assert ticket["status"] == "pending_approval"

    # Execution without approval should fail/prompt
    res_unapproved = manager.execute_in_sandbox(ticket["sandbox_id"], approved_by_user=False)
    assert res_unapproved["success"] is False

    # Execution with user approval should pass
    res_approved = manager.execute_in_sandbox(ticket["sandbox_id"], approved_by_user=True)
    assert res_approved["success"] is True
    assert "Hello from self evolving tool" in res_approved["stdout"]

    # Permanent registration
    reg_res = manager.register_permanent_tool(ticket["sandbox_id"])
    assert reg_res["success"] is True
    assert os.path.exists(reg_res["file_path"])

def test_explain_code_engine(temp_workspace):
    engine = ExplainCodeEngine(temp_workspace)
    res = engine.explain_symbol_or_error("sample.py", 1, "def hello()")
    assert res["file"] == "sample.py"
    assert "explanation" in res

@pytest.mark.asyncio
async def test_experiment_runner():
    runner = ExperimentRunner()
    res = await runner.run_experiment("/health", method="GET", expected_status=200)
    assert res["endpoint"] == "/health"

def test_silent_workflow_guardian(temp_workspace):
    guardian = SilentWorkflowGuardian(temp_workspace)
    alerts = guardian.inspect_recent_changes("sample.py", "print('DEBUG hello')")
    assert len(alerts) >= 1
    assert alerts[0]["type"] == "stray_debug_log"

def test_what_broke_detective(temp_workspace):
    detective = WhatBrokeDetective(temp_workspace)
    diag = detective.diagnose_failures("pydantic")
    assert diag["status"] == "diagnosed"
    assert "prioritized_diagnoses" in diag

def test_boilerplate_genie(temp_workspace):
    genie = BoilerplateGenie(temp_workspace)
    res = genie.generate_component_stub("UserCard", "src/components")
    assert res["component_name"] == "UserCard"
    assert os.path.exists(os.path.join(temp_workspace, res["file_path"]))

def test_commit_whisperer(temp_workspace):
    whisperer = CommitWhisperer(temp_workspace)
    res = whisperer.inspect_staged_commit()
    assert "staged_files" in res
    assert "suggested_version_bump" in res

# --- API ENDPOINTS TESTS ---

def test_api_guard_resources():
    res = client.get("/api/guard/resources")
    assert res.status_code == 200
    assert "disk_percent" in res.json()

def test_api_context_scan():
    res = client.post("/api/context/scan")
    assert res.status_code == 200
    assert res.json()["status"] == "indexed"

def test_api_orchestrator_launch():
    res = client.post("/api/orchestrator/launch", json={"preset": "coding"})
    assert res.status_code == 200

def test_api_self_evolving_flow():
    prep = client.post("/api/self-evolving/prepare", json={
        "tool_name": "test_tool",
        "code": "print('ok')",
        "description": "test"
    })
    assert prep.status_code == 200
    s_id = prep.json()["sandbox_id"]

    exec_res = client.post("/api/self-evolving/sandbox-execute", json={
        "sandbox_id": s_id,
        "approved_by_user": True
    })
    assert exec_res.status_code == 200
    assert exec_res.json()["success"] is True

def test_api_explain_symbol():
    res = client.post("/api/explain/symbol", json={"file_path": "api.py", "line_number": 1})
    assert res.status_code == 200

def test_api_guardian_inspect():
    res = client.post("/api/guardian/inspect", json={"file_path": "user.ts", "content": "console.log('test')" })
    assert res.status_code == 200

def test_api_detective_diagnose():
    res = client.post("/api/detective/diagnose", json={"updated_package": "httpx"})
    assert res.status_code == 200

def test_api_boilerplate_generate():
    res = client.post("/api/boilerplate/generate", json={"component_name": "ProfileHeader"})
    assert res.status_code == 200

def test_api_commit_whisperer_inspect():
    res = client.get("/api/commit-whisperer/inspect")
    assert res.status_code == 200
