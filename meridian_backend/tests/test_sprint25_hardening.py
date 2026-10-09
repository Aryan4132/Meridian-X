import time
import pytest
from src.core.loop_executor import critique_and_correct_tool_call
from src.core.llm_clients import get_gpu_vram_usage
import src.core.llm_clients as llm_clients

def test_multi_alias_remapping():
    """Verify tool call with multiple aliased parameters remaps all aliases cleanly."""
    # write_to_file expects path and content.
    # We pass both aliased: filepath and content_str
    import json
    tool_args = json.dumps({"filepath": "test.txt", "content_str": "hello world"})
    
    success, corrected_args, msg = critique_and_correct_tool_call(
        tool_name="write_file",
        args_str=tool_args,
        client=None,
        model_source="local"
    )
    
    parsed = json.loads(corrected_args)
    # Both aliases should be canonicalized
    assert "path" in parsed, f"path was not remapped: {parsed}"
    assert "content" in parsed, f"content was not remapped: {parsed}"
    assert parsed["path"] == "test.txt"
    assert parsed["content"] == "hello world"

def test_vram_usage_memoization():
    """Verify get_gpu_vram_usage caches value within 5.0s TTL."""
    # Seed cache
    llm_clients._last_vram_query_time = time.time()
    llm_clients._cached_vram_usage = 42.5
    
    # Within TTL, should return cached 42.5 without running any subprocess
    val = get_gpu_vram_usage()
    assert val == 42.5
