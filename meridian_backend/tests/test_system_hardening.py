import pytest
import os
import sys
import json
from unittest.mock import patch, MagicMock

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)


def test_truncate_tool_observation_preserves_short_content():
    """Verify observations under max_chars are untouched."""
    from src.core.loop_dispatcher import truncate_tool_observation
    short_text = "Standard tool observation result."
    assert truncate_tool_observation(short_text, max_chars=1000) == short_text


def test_truncate_tool_observation_bounds_long_content():
    """Verify observations over limit are truncated cleanly with head + tail + notice."""
    from src.core.loop_dispatcher import truncate_tool_observation
    long_text = "HEAD_MARKER_" + ("x" * 20000) + "_TAIL_MARKER"
    truncated = truncate_tool_observation(long_text, max_chars=1000)

    assert len(truncated) <= 1200
    assert "HEAD_MARKER_" in truncated
    assert "_TAIL_MARKER" in truncated
    assert "Output truncated" in truncated
    assert "omitted" in truncated


def test_sanitize_tool_args_python_dict_literals():
    """Verify single-quoted dictionaries and Python booleans/None are auto-healed into JSON."""
    from src.core.loop_executor import sanitize_tool_args_str

    py_dict_str = "{'path': 'test.py', 'overwrite': True, 'extra': None, 'valid': False}"
    healed = sanitize_tool_args_str(py_dict_str)
    
    parsed = json.loads(healed)
    assert parsed["path"] == "test.py"
    assert parsed["overwrite"] is True
    assert parsed["extra"] is None
    assert parsed["valid"] is False


def test_interrupt_agent_loop_kills_active_tts():
    """Verify interrupting agent loop stops active TTS audio playback."""
    from src.core.loop import interrupt_agent_loop

    with patch("src.voice.tts.stop_active_tts") as mock_stop_tts:
        interrupt_agent_loop(session_id="test-session")
        mock_stop_tts.assert_called_once()
