"""
test_cognitive_graph.py — Verification suite for Unified Cognitive Graph
Tests relational multi-hop graph storage, BFS traversal, and tool execution.
"""

import os
import pytest
from src.core.cognitive_graph import UnifiedCognitiveGraph
from src.tools.registry import query_cognitive_graph, TOOL_REGISTRY


@pytest.fixture
def temp_graph(tmp_path):
    """Provides an isolated UnifiedCognitiveGraph instance in a temp directory."""
    db_file = str(tmp_path / "test_cog.db")
    return UnifiedCognitiveGraph(db_path=db_file)


def test_node_lifecycle(temp_graph):
    """Test adding and retrieving nodes."""
    node = temp_graph.add_node("code:auth.py", "python_file", "Authentication Module", {"lines": 120})
    assert node["id"] == "code:auth.py"
    assert node["type"] == "python_file"

    fetched = temp_graph.get_node("code:auth.py")
    assert fetched is not None
    assert fetched["name"] == "Authentication Module"
    assert fetched["metadata"]["lines"] == 120

    # Upsert test
    temp_graph.add_node("code:auth.py", "python_file", "Auth Module v2", {"lines": 150})
    updated = temp_graph.get_node("code:auth.py")
    assert updated["name"] == "Auth Module v2"
    assert updated["metadata"]["lines"] == 150


def test_edge_and_neighbor_traversal(temp_graph):
    """Test creating edges and querying neighbors."""
    temp_graph.add_node("view:Timeline", "frontend_view", "Timeline UI")
    temp_graph.add_node("api:chat", "backend_route", "/api/chat/stream")
    temp_graph.add_node("code:loop", "core_backend", "Agent Loop")

    temp_graph.add_edge("view:Timeline", "api:chat", "calls")
    temp_graph.add_edge("api:chat", "code:loop", "invokes")

    # Check outgoing neighbors from Timeline
    out_neighbors = temp_graph.get_neighbors("view:Timeline", direction="out")
    assert len(out_neighbors) == 1
    assert out_neighbors[0]["node"]["id"] == "api:chat"
    assert out_neighbors[0]["relation"] == "calls"

    # Check incoming neighbors to loop
    in_neighbors = temp_graph.get_neighbors("code:loop", direction="in")
    assert len(in_neighbors) == 1
    assert in_neighbors[0]["node"]["id"] == "api:chat"


def test_bfs_multi_hop_traversal(temp_graph):
    """Test BFS traversal out to specified depth."""
    # Chain: A -> B -> C -> D
    for item in ["A", "B", "C", "D"]:
        temp_graph.add_node(item, "concept", f"Node {item}")

    temp_graph.add_edge("A", "B", "leads_to")
    temp_graph.add_edge("B", "C", "leads_to")
    temp_graph.add_edge("C", "D", "leads_to")

    # 1 hop from A should reach B only
    res_1 = temp_graph.traverse("A", max_hops=1)
    assert res_1["total_nodes"] == 2
    node_ids_1 = {n["id"] for n in res_1["nodes"]}
    assert node_ids_1 == {"A", "B"}

    # 2 hops from A should reach B and C
    res_2 = temp_graph.traverse("A", max_hops=2)
    assert res_2["total_nodes"] == 3
    node_ids_2 = {n["id"] for n in res_2["nodes"]}
    assert node_ids_2 == {"A", "B", "C"}

    # 3 hops should reach all 4
    res_3 = temp_graph.traverse("A", max_hops=3)
    assert res_3["total_nodes"] == 4


def test_find_nodes_and_auto_link(temp_graph):
    """Test keyword node search and auto linking core endpoints."""
    links_count = temp_graph.auto_link_endpoints()
    assert links_count > 0

    # Search for timeline
    matches = temp_graph.find_nodes("timeline")
    assert len(matches) >= 1
    assert any("Timeline" in m["name"] for m in matches)

    # Search for chat
    matches_chat = temp_graph.find_nodes("chat")
    assert len(matches_chat) >= 1
    assert any("/api/chat/stream" in m["id"] for m in matches_chat)


def test_unified_context_generation(temp_graph):
    """Test formatting interconnected graph context for prompts."""
    temp_graph.auto_link_endpoints()
    context = temp_graph.get_unified_context("how does chat streaming work?")
    assert "COGNITIVE GRAPH — Interconnected System Map" in context
    assert "Timeline.tsx" in context or "chat/stream" in context


def test_query_cognitive_graph_tool_registered():
    """Verify tool is exposed in TOOL_REGISTRY with tier 0."""
    assert "query_cognitive_graph" in TOOL_REGISTRY
    assert TOOL_REGISTRY["query_cognitive_graph"]["tier"] == 0


def test_query_cognitive_graph_tool_execution():
    """Verify executing query_cognitive_graph returns formatted string."""
    # Test with query
    out_query = query_cognitive_graph(query="stream")
    assert isinstance(out_query, str)
    assert "Cognitive Graph" in out_query

    # Test with start_node
    out_node = query_cognitive_graph(start_node="code:meridian_frontend/src/views/Timeline.tsx", max_hops=2)
    assert isinstance(out_node, str)
    assert ("Cognitive Graph neighborhood" in out_node) or ("Discovered" in out_node)


def test_fts5_search_and_temporal_decay(temp_graph):
    """Test FTS5 keyword indexing and exponential time decay."""
    temp_graph.add_node("mem:perf", "user_preference", "Fast GPU inference preference", {"note": "CUDA fp16"})
    temp_graph.add_node("task:git_audit", "task_outcome", "Audited git status changes", {"clean": True})

    # Test FTS5 search
    results = temp_graph.fts_search("inference")
    assert len(results) >= 1
    assert results[0]["id"] == "mem:perf"

    results_task = temp_graph.fts_search("audited")
    assert len(results_task) >= 1
    assert results_task[0]["id"] == "task:git_audit"

    # Test temporal decay
    import time
    now = time.time()
    
    # Architecture symbol should not decay (factor 1.0)
    w_arch = temp_graph.compute_decayed_weight(1.0, now - 86400 * 30, node_type="ast_symbol")
    assert w_arch == 1.0

    # Old task outcome (e.g. 6 days ago with 3-day half life should decay to ~0.25)
    w_task = temp_graph.compute_decayed_weight(1.0, now - 86400 * 6, node_type="task_outcome")
    assert w_task < 0.35

