import pytest
import threading
import json
from unittest.mock import MagicMock, patch

from src.core.mode import MODE_DIRECTIVES
from src.core.loop_dispatcher import process_tool_turn


def test_mode_directives_prioritize_headless():
    researcher_directive = MODE_DIRECTIVES["RESEARCHER"]
    assert "search_web" in researcher_directive
    assert "autonomous_research" in researcher_directive
    assert "prioritize fast headless search" in researcher_directive.lower()
    assert "do not run `browser_use_task` in parallel with `search_web`" in researcher_directive.lower()

    auto_directive = MODE_DIRECTIVES["AUTO"]
    assert "search_web" in auto_directive or "autonomous_research" in auto_directive
    assert "browser_use_task" in auto_directive


@pytest.mark.asyncio
async def test_loop_dispatcher_suppresses_redundant_browser_use_task():
    calls = [
        ("search_web", json.dumps({"query": "quantum computing breakthroughs"})),
        ("browser_use_task", json.dumps({"task": "look up quantum computing"})),
    ]
    history = []
    client = MagicMock()
    state = {}
    interrupt_event = threading.Event()
    tool_retries = {}
    temp_files = []

    with patch("src.core.loop_dispatcher.dispatch_tool_batch") as mock_dispatch:
        mock_dispatch.return_value = [
            {"tool": "search_web", "status": "SUCCESS", "result": "Title: Quantum update\nSnippet: Done"}
        ]
        events = []
        async for sse in process_tool_turn(
            calls_to_execute=calls,
            history=history,
            client=client,
            active_model="test-model",
            model_source="local",
            session_id="test-session",
            tool_retry_counts=tool_retries,
            created_temp_files=temp_files,
            state=state,
            interrupt_event=interrupt_event,
            exempt_tools=set(),
            prompt="tell me about quantum computing breakthroughs",
        ):
            events.append(sse)

        # Ensure dispatch_tool_batch was called with search_web ONLY (not browser_use_task)
        assert mock_dispatch.called
        dispatched_tools = [c["name"] for c in mock_dispatch.call_args[0][0]]
        assert "search_web" in dispatched_tools
        assert "browser_use_task" not in dispatched_tools

        # Ensure an optimization message was streamed
        assert any("Suppressed redundant 'browser_use_task'" in e for e in events)


@pytest.mark.asyncio
async def test_loop_dispatcher_retains_browser_when_prompt_requests_it():
    calls = [
        ("search_web", json.dumps({"query": "quantum computing breakthroughs"})),
        ("browser_use_task", json.dumps({"task": "look up quantum computing"})),
    ]
    history = []
    client = MagicMock()
    state = {}
    interrupt_event = threading.Event()
    tool_retries = {}
    temp_files = []

    with patch("src.core.loop_dispatcher.dispatch_tool_batch") as mock_dispatch, \
         patch("src.core.loop_dispatcher.score_candidate_branch", return_value=0.9):
        mock_dispatch.return_value = [
            {"tool": "search_web", "status": "SUCCESS", "result": "search output"}
        ]
        events = []
        # Prompt explicitly mentions browser
        async for sse in process_tool_turn(
            calls_to_execute=calls,
            history=history,
            client=client,
            active_model="test-model",
            model_source="local",
            session_id="test-session",
            tool_retry_counts=tool_retries,
            created_temp_files=temp_files,
            state=state,
            interrupt_event=interrupt_event,
            exempt_tools=set(),
            prompt="open browser and search quantum computing breakthroughs",
        ):
            events.append(sse)

        # Both tools should be retained since browser was explicitly requested
        assert not any("Suppressed redundant" in e for e in events)


@pytest.mark.asyncio
async def test_loop_dispatcher_retains_browser_when_no_headless_search():
    calls = [
        ("browser_use_task", json.dumps({"task": "click the login button"})),
    ]
    history = []
    client = MagicMock()
    state = {}
    interrupt_event = threading.Event()
    tool_retries = {}
    temp_files = []

    with patch("src.core.loop_dispatcher.score_candidate_branch", return_value=0.9):
        events = []
        async for sse in process_tool_turn(
            calls_to_execute=calls,
            history=history,
            client=client,
            active_model="test-model",
            model_source="local",
            session_id="test-session",
            tool_retry_counts=tool_retries,
            created_temp_files=temp_files,
            state=state,
            interrupt_event=interrupt_event,
            exempt_tools=set(),
            prompt="click the button on the screen",
        ):
            events.append(sse)

        # browser_use_task alone should NOT be suppressed
        assert not any("Suppressed redundant" in e for e in events)
