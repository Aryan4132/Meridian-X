import pytest
import asyncio
import os
import sys
from fastapi.testclient import TestClient

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.swarm import AutonomousBugFixer, SwarmAgent
from src.tools.registry import TOOL_REGISTRY, call_tool
from src.core.auth import API_KEY
from api import app

client = TestClient(app)
headers = {"X-API-Key": API_KEY}


def test_parse_pytest_output_with_failures():
    fixer = AutonomousBugFixer()
    mock_pytest_output = """
============================= FAILURES =============================
_________________________ test_example_fail _________________________

    def test_example_fail():
>       assert 1 == 2
E       assert 1 == 2

test_sample.py:15: AssertionError
=========================== short test summary info ===========================
FAILED test_sample.py::test_example_fail - assert 1 == 2
================ 1 failed, 5 passed in 0.12s ================
"""
    parsed = fixer.parse_pytest_output(mock_pytest_output)
    assert parsed["failed"] == 1
    assert parsed["passed"] == 5
    assert len(parsed["failures"]) == 1
    assert parsed["failures"][0]["test_name"] == "test_example_fail"
    assert parsed["failures"][0]["file_path"] == "test_sample.py"
    assert parsed["failures"][0]["line_number"] == 15
    assert "assert 1 == 2" in parsed["failures"][0]["exception"]


def test_parse_pytest_output_all_passed():
    fixer = AutonomousBugFixer()
    mock_output = "================ 12 passed in 0.45s ================"
    parsed = fixer.parse_pytest_output(mock_output)
    assert parsed["failed"] == 0
    assert parsed["passed"] == 12
    assert len(parsed["failures"]) == 0


@pytest.mark.asyncio
async def test_run_test_suite_execution():
    fixer = AutonomousBugFixer()
    # Run test suite on wakeword test file which passes cleanly
    test_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_wakeword_onnx.py"))
    res = await fixer.run_test_suite(target_path=test_path)
    assert "passed" in res
    assert "failed" in res
    assert res["failed"] == 0


@pytest.mark.asyncio
async def test_auto_fix_pipeline_clean_run():
    fixer = AutonomousBugFixer()
    test_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_wakeword_onnx.py"))
    res = await fixer.auto_fix_pipeline(target_path=test_path)
    assert res["status"] == "no_action_needed"
    assert res["initial_results"]["failed"] == 0


@pytest.mark.asyncio
async def test_bug_fixer_role_registration():
    agent = SwarmAgent(role="bug_fixer")
    assert agent.role == "bug_fixer"
    assert "run_test_suite" in agent.allowed_tools
    assert "commit_verified_fix" in agent.allowed_tools


@pytest.mark.asyncio
async def test_tool_registry_auto_bug_fixer():
    assert "run_autonomous_bug_fixer" in TOOL_REGISTRY
    test_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_wakeword_onnx.py"))
    result = await call_tool("run_autonomous_bug_fixer", {"target_path": test_path})
    assert "no_action_needed" in result


def test_api_swarm_auto_fix_endpoint():
    test_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_wakeword_onnx.py"))
    response = client.post("/api/swarm/auto-fix", json={"target_path": test_path}, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["data"]["status"] == "no_action_needed"
