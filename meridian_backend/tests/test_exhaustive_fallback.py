import pytest
import os
import sys
import json
from unittest.mock import patch, MagicMock

# Ensure backend path is available
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)


def test_system_prompt_contains_exhaustion_rule():
    """Verify system prompt contains anti-surrender EXHAUSTION RULE."""
    from src.core.mode import build_system_prompt
    prompt = build_system_prompt(
        prompt="Search for project config",
        brain_model="test-model",
        ollama_host="http://localhost:11434",
        tools_doc="[tool docs]"
    )
    assert "EXHAUSTION RULE" in prompt
    assert "do NOT emit <finish>" in prompt or "do not emit <finish>" in prompt.lower()
    assert "alternate" in prompt.lower()


def test_granular_retry_budget_by_args():
    """Verify tool retries are scoped to (session_id, tool_name, args_hash)."""
    from src.core.loop_dispatcher import check_and_increment_retry, reset_tool_retry_budget

    session_id = "test-session-budget"
    reset_tool_retry_budget(session_id)

    # 1. First set of arguments - 3 attempts allowed
    args1 = {"path": "file1.txt"}
    assert check_and_increment_retry(session_id, "read_file", args1) is True
    assert check_and_increment_retry(session_id, "read_file", args1) is True
    assert check_and_increment_retry(session_id, "read_file", args1) is True
    assert check_and_increment_retry(session_id, "read_file", args1) is False

    # 2. Second set of arguments with same tool - should still be allowed because args are different
    args2 = {"path": "file2.txt"}
    assert check_and_increment_retry(session_id, "read_file", args2) is True


def test_tot_backtrack_imperative_directive():
    """Verify ToT backtrack message instructs model not to surrender."""
    from src.core.loop_dispatcher import format_tot_backtrack_message

    msg = format_tot_backtrack_message("read_file", {"path": "missing.txt"}, "File not found")
    assert "Error: Execution failed" in msg or "Error: Tool execution failed" in msg
    assert "Do NOT emit <finish>" in msg or "do not emit <finish>" in msg.lower()
    assert "alternative" in msg.lower()


def test_wakeword_fallback_cascade():
    """Verify wakeword does not immediately disable monitoring on missing custom ONNX."""
    import src.voice.wakeword as ww

    with patch("os.path.exists", return_value=False), \
         patch("src.voice.wakeword.logger") as mock_logger:
        # Resolve model path should fall back to default or builtin instead of exiting
        resolved_path, engine = ww.resolve_wakeword_model("missing_model.onnx")
        assert engine in ("builtin", "silero_vad", "openwakeword_default")
