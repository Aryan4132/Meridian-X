"""
test_backlog_sprint.py — Unit tests for BK-22 to BK-25 backlog modules.
"""

import pytest
import asyncio
from meridian_backend.src.core.mcp_executor import McpToolExecutor
from meridian_backend.src.core.prompt_templates import PromptTemplateEngine
from meridian_backend.src.core.rag_optimizer import RAGContextOptimizer
from meridian_backend.src.core.temporal_memory import TemporalMemoryGraph


def test_mcp_tool_executor_registration():
    executor = McpToolExecutor()
    assert len(executor.clients) == 0


def test_prompt_template_engine():
    engine = PromptTemplateEngine()
    prompt = engine.render_prompt("coding_agent", context="Write Python unit test")
    assert "Coding Agent" in prompt
    assert "Write Python unit test" in prompt

    engine.register_tool_schema("test_tool", "A test tool", {"type": "object"})
    schemas = engine.get_tool_schemas(["test_tool"])
    assert len(schemas) == 1
    assert schemas[0]["function"]["name"] == "test_tool"


def test_rag_context_optimizer():
    optimizer = RAGContextOptimizer(min_relevance_threshold=0.1)
    docs = [
        {"content": "Model Context Protocol tools and servers integration"},
        {"content": "Irrelevant document about baking cakes"}
    ]
    results = optimizer.rerank_and_optimize(query="MCP tools", documents=docs)
    assert len(results) >= 1
    assert "MCP" in results[0]["document"]["content"] or "Model Context Protocol" in results[0]["document"]["content"]


def test_temporal_memory_graph():
    graph = TemporalMemoryGraph()
    e1 = graph.add_event("entity:project", "state_change", {"status": "in_progress"})
    e2 = graph.add_event("entity:project", "state_change", {"status": "completed"})

    history = graph.query_entity_history("entity:project")
    assert len(history) == 2
    assert history[0]["id"] == e1
    assert history[1]["id"] == e2
    assert history[1]["state"]["status"] == "completed"
