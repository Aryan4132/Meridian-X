import pytest
import asyncio
from fastapi.testclient import TestClient
from api import app
from src.core.local_model_manager import local_model_manager, LocalModelConfig, QUANTIZATION_PRESETS
from src.core.memory_consolidation import memory_consolidation_engine, ConsolidationRequest
from src.core.dev_automation import dev_automation_engine, FormatCodeRequest, RunTestsRequest
from src.core.agent_status_stream import agent_status_stream_manager

client = TestClient(app)

# 1. Local Model Management Tests
def test_quantization_presets():
    assert "Q4_K_M" in QUANTIZATION_PRESETS
    assert QUANTIZATION_PRESETS["Q4_K_M"]["bits_per_weight"] == 4.5

def test_vram_estimation():
    req = local_model_manager.estimate_resource_requirements(8.0, "Q4_K_M")
    assert req["parameter_count_billion"] == 8.0
    assert req["quantization"] == "Q4_K_M"
    assert req["estimated_vram_gb"] > 4.0

def test_local_model_endpoints():
    res = client.get("/api/models/quantization-options")
    assert res.status_code == 200
    data = res.json()
    assert "presets" in data
    assert len(data["presets"]) >= 4

    res_est = client.post("/api/models/estimate-resources", json={"param_count_billion": 7.0, "quantization": "Q5_K_M"})
    assert res_est.status_code == 200
    assert res_est.json()["estimated_vram_gb"] > 0

    res_active = client.post("/api/models/local/active", json={
        "model_name": "llama3:8b-instruct-q4_K_M",
        "quantization": "Q4_K_M",
        "context_window": 4096,
        "temperature": 0.7
    })
    assert res_active.status_code == 200
    assert res_active.json()["config"]["model_name"] == "llama3:8b-instruct-q4_K_M"

# 2. Memory Summarization & Consolidation Tests
def test_memory_summarization():
    messages = [
        {"role": "user", "content": "I prefer using Q4_K_M quantization for local models."},
        {"role": "assistant", "content": "Got it. I will configure Q4_K_M for your local setup."},
        {"role": "user", "content": "We decided to deploy the backend on port 4132."}
    ]

    res = client.post("/api/memory/summarize", json={"messages": messages})
    assert res.status_code == 200
    data = res.json()
    assert "summary" in data
    assert len(data["key_topics"]) > 0

def test_memory_consolidation():
    messages = [
        {"role": "user", "content": "I prefer dark mode in all UI components."},
        {"role": "user", "content": "We decided to build dev automation endpoints."}
    ]

    res = client.post("/api/memory/consolidate", json={"session_id": "test_sess_1", "messages": messages})
    assert res.status_code == 200
    data = res.json()
    assert len(data["extracted_nodes"]) >= 2

    res_status = client.get("/api/memory/consolidation-status")
    assert res_status.status_code == 200
    assert res_status.json()["total_consolidation_runs"] >= 1

# 3. Dev Automation Endpoints Tests
def test_dev_automation_git_status():
    res = client.get("/api/automation/git/status")
    assert res.status_code == 200
    data = res.json()
    assert "is_git_repo" in data

def test_dev_automation_format_and_test():
    res_fmt = client.post("/api/automation/code/format", json={"file_path": "src/core/config.py", "formatter": "black"})
    assert res_fmt.status_code == 200

# 4. Agent Status & Activity Stream Tests
def test_agent_status_snapshot_and_emit():
    res_snap = client.get("/api/agent/status")
    assert res_snap.status_code == 200
    assert "status" in res_snap.json()

    res_emit = client.post("/api/agent/activity/event", json={
        "status": "executing_tool",
        "message": "Running unit test suite",
        "tool": "pytest",
        "task": "Test feature endpoints"
    })
    assert res_emit.status_code == 200
    assert res_emit.json()["status"] == "broadcasted"

    res_snap2 = client.get("/api/agent/status")
    assert res_snap2.json()["status"] == "executing_tool"
