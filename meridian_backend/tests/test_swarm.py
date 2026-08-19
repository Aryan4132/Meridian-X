import pytest
import asyncio
import os
import sys
from unittest.mock import MagicMock, patch

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.swarm import SwarmAgent, SwarmOrchestrator
from src.tools.registry import TOOL_REGISTRY, call_tool


@pytest.mark.asyncio
async def test_swarm_agent_execution():
    agent = SwarmAgent(role="researcher")
    assert agent.role == "researcher"
    assert agent.name == "Swarm-ResearcherAgent"
    assert len(agent.allowed_tools) > 0

    mock_client = MagicMock()
    mock_chunk = MagicMock()
    mock_chunk.message.content = "Completed analysis of system logs."
    mock_client.chat.return_value = [mock_chunk]

    with patch("src.core.loop.get_cached_ollama_client", return_value=mock_client):
        res = await agent.execute("Analyze system logs")
        assert res["status"] == "success"
        assert res["role"] == "researcher"
        assert "Completed analysis" in res["output"]


@pytest.mark.asyncio
async def test_swarm_orchestrator_parallel_run():
    mock_client = MagicMock()
    mock_chunk = MagicMock()
    mock_chunk.message.content = "Completed swarm task."
    mock_client.chat.return_value = [mock_chunk]

    orchestrator = SwarmOrchestrator()
    with patch("src.core.loop.get_cached_ollama_client", return_value=mock_client):
        res = await orchestrator.run_swarm(
            goal="Audit codebase security and performance",
            subagent_roles=["auditor", "researcher", "planner"]
        )

    assert res["subagent_count"] == 3
    assert len(res["results"]) == 3
    assert "Synthesis Report" in res["synthesis"]
    assert all(r["status"] == "success" for r in res["results"])


@pytest.mark.asyncio
async def test_swarm_tool_registry_integration():
    assert "run_agent_swarm" in TOOL_REGISTRY
    result_text = await call_tool(
        "run_agent_swarm",
        {"goal": "Check system health", "roles": "researcher,auditor"}
    )
    assert "[Swarm] Multi-Agent Execution Synthesis Report" in result_text
    assert "Swarm-ResearcherAgent" in result_text
