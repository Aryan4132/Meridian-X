import pytest
import asyncio
from src.core.loop_dispatcher import check_and_increment_retry, reset_tool_retry_budget, dispatch_tool_batch
from src.core.loop_stream import format_sse_event, estimate_token_count, trim_history_to_token_budget, request_stream_cancellation, is_cancellation_requested, clear_cancellation_signal

def test_retry_budget():
    reset_tool_retry_budget("test_session")
    assert check_and_increment_retry("test_session", "read_file") is True
    assert check_and_increment_retry("test_session", "read_file") is True
    assert check_and_increment_retry("test_session", "read_file") is True
    assert check_and_increment_retry("test_session", "read_file") is False  # 4th attempt exceeded

def test_stream_helpers():
    assert estimate_token_count("Hello World!") == 3
    event_str = format_sse_event("delta", {"content": "hi"})
    assert "data: " in event_str
    assert '"event": "delta"' in event_str

    request_stream_cancellation("sess1")
    assert is_cancellation_requested("sess1") is True
    clear_cancellation_signal("sess1")
    assert is_cancellation_requested("sess1") is False

def test_trim_history():
    messages = [
        {"role": "system", "content": "System prompt instructions"},
        {"role": "user", "content": "A" * 4000},
        {"role": "assistant", "content": "B" * 4000},
        {"role": "user", "content": "C" * 4000},
    ]
    trimmed = trim_history_to_token_budget(messages, max_tokens=1500)
    assert len(trimmed) < len(messages)
    assert trimmed[0]["role"] == "system"
