import pytest
import asyncio
import json
import sys
import os

# Ensure backend path is available
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from src.core.confirmations import check_approval_gate, get_confirmations_lock
from src.core.loop_stream import async_iter_stream


def test_approval_gate_shell_and_aliases():
    """Verify that dangerous commands dispatched to shell/terminal aliases trigger the approval gate."""
    # shell alias
    req, msg = check_approval_gate("shell", command="rm -rf /important")
    assert req is True
    assert "Potentially dangerous command detected" in msg

    # cmd parameter variant
    req, msg = check_approval_gate("shell", cmd="del /f C:\\Windows")
    assert req is True

    # terminal alias
    req, msg = check_approval_gate("terminal", command="kill 999")
    assert req is True

    # nl_to_shell alias
    req, msg = check_approval_gate("nl_to_shell", natural_language="sudo rm -rf /")
    assert req is True

    # Safe command should NOT require approval
    req, msg = check_approval_gate("shell", command="git status")
    assert req is False
    assert msg == ""


def test_confirmations_lock_singleton():
    """Verify confirmations lock is valid asyncio.Lock and idempotent."""
    lock1 = get_confirmations_lock()
    lock2 = get_confirmations_lock()
    assert isinstance(lock1, asyncio.Lock)
    assert lock1 is lock2


@pytest.mark.asyncio
async def test_async_iter_stream_no_dropped_items():
    """Verify async_iter_stream streams all elements cleanly through backpressure."""
    def sample_gen():
        for i in range(100):
            yield {"item": i}

    collected = []
    async for chunk in async_iter_stream(sample_gen()):
        collected.append(chunk)

    assert len(collected) == 100
    assert collected[0] == {"item": 0}
    assert collected[-1] == {"item": 99}


def test_chat_sse_accumulation_parsing():
    """Verify non-streaming chat helper parses multiline text and finish JSON correctly."""
    from src.api.chat import parse_sse_events_for_chat

    # Case 1: Finish JSON block containing chat field
    events_1 = [
        'event: thought\ndata: {"text": "Thinking...", "type": "plan"}\n\n',
        'event: text\ndata: {"chat": "Hello, how can I help you?", "speech": "Hello"}\n\n'
    ]
    text, thoughts = parse_sse_events_for_chat(events_1)
    assert text == "Hello, how can I help you?"
    assert len(thoughts) == 1
    assert thoughts[0]["text"] == "Thinking..."

    # Case 2: Multiline raw text output
    events_2 = [
        'event: text\ndata: Line 1\ndata: Line 2\ndata: Line 3\n\n'
    ]
    text, thoughts = parse_sse_events_for_chat(events_2)
    assert text == "Line 1\nLine 2\nLine 3"

    # Case 3: Stray non-text events should not pollute chat text
    events_3 = [
        'event: confirmation_required\ndata: {"id": "123", "tool": "shell"}\n\n',
        'event: proactive_suggestions\ndata: {"suggestions": []}\n\n',
        'event: text\ndata: Final response here\n\n'
    ]
    text, thoughts = parse_sse_events_for_chat(events_3)
    assert text == "Final response here"


def test_validate_and_heal_tool_arguments_lint_variations():
    """Verify LLM code linter accepts valid responses and detects explicit errors."""
    from unittest.mock import patch
    from src.core.loop_executor import critique_and_correct_tool_call

    valid_py = '{"code": "def hello():\\n    return 42"}'

    # Case 1: Auditor returns "No issues detected." -> must accept
    with patch("src.core.llm_provider.call_llm_sync", return_value="No issues detected."):
        valid, args_str, note = critique_and_correct_tool_call("run_python", valid_py)
        assert valid is True

    # Case 2: Auditor returns standard "OK" -> must accept
    with patch("src.core.llm_provider.call_llm_sync", return_value="OK"):
        valid, args_str, note = critique_and_correct_tool_call("run_python", valid_py)
        assert valid is True

    # Case 3: Auditor detects explicit undefined name / warning -> must fail
    with patch("src.core.llm_provider.call_llm_sync", return_value="WARNING: Undefined name 'foo' detected."):
        valid, args_str, note = critique_and_correct_tool_call("run_python", valid_py)
        assert valid is False
        assert "Python Lint Warning" in note

