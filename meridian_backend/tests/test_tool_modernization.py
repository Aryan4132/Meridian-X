import pytest
import asyncio
from unittest.mock import patch, MagicMock
from src.core.loop_stream import generate_tools_doc, get_dynamic_tool_signature, TOOL_SIGNATURES, CORE_TOOLS_LIST
from src.tools.registry import TOOL_REGISTRY, call_tool, register_dynamic_tool


def sample_sync_tool(path: str, count: int = 10, verbose: bool = False) -> str:
    """Sample sync tool docstring."""
    return f"processed {path} with count={count}"


async def sample_async_slow_tool(delay: float = 2.0) -> str:
    """Async tool that sleeps."""
    await asyncio.sleep(delay)
    return "done sleeping"


def test_get_dynamic_tool_signature():
    sig = get_dynamic_tool_signature("sample_sync_tool", sample_sync_tool)
    assert sig.startswith("sample_sync_tool(")
    assert 'path="<path>"' in sig
    assert "count=10" in sig
    assert "verbose=False" in sig


def test_generate_tools_doc_includes_dynamic_signatures():
    # 1. Verify standard tools without hardcoded signatures have dynamic inspect reflection
    doc = generate_tools_doc()
    assert 'git_diff(repo_path="<repo_path>")' in doc
    assert 'delete_file(path="<path>")' in doc
    assert 'git_commit(message="<message>", repo_path="<repo_path>")' in doc

    # 2. Verify dynamically registered tools appended to CORE_TOOLS_LIST reflect accurately
    register_dynamic_tool("test_custom_dynamic_tool", sample_sync_tool, description="Dynamic test tool", tier=1)
    CORE_TOOLS_LIST.append("test_custom_dynamic_tool")
    try:
        doc_with_custom = generate_tools_doc()
        assert "test_custom_dynamic_tool" in doc_with_custom
        assert 'path="<path>"' in doc_with_custom
        assert "count=10" in doc_with_custom
    finally:
        CORE_TOOLS_LIST.remove("test_custom_dynamic_tool")


def test_shell_aliases_registered():
    for alias in ["shell", "terminal", "run_command", "nl_run", "nl_to_shell"]:
        assert alias in TOOL_REGISTRY, f"Alias '{alias}' missing from TOOL_REGISTRY"
        assert callable(TOOL_REGISTRY[alias]["func"])
        assert TOOL_REGISTRY[alias]["tier"] in (0, 1, 2)


@pytest.mark.asyncio
async def test_call_tool_alias_invocation():
    mock_func = MagicMock(return_value="mock output: hello world")
    orig_shell = TOOL_REGISTRY["shell"]["func"]
    orig_run_command = TOOL_REGISTRY["run_command"]["func"]
    try:
        TOOL_REGISTRY["shell"]["func"] = mock_func
        TOOL_REGISTRY["run_command"]["func"] = mock_func

        res = await call_tool("shell", {"command": "echo hello world"})
        assert "hello world" in res
        mock_func.assert_called_with(command="echo hello world")

        res_term = await call_tool("run_command", {"command": "echo test"})
        assert "hello world" in res_term
        mock_func.assert_called_with(command="echo test")
    finally:
        TOOL_REGISTRY["shell"]["func"] = orig_shell
        TOOL_REGISTRY["run_command"]["func"] = orig_run_command


@pytest.mark.asyncio
async def test_call_tool_timeout_guard():
    # Register slow tool
    register_dynamic_tool("test_hanging_tool", sample_async_slow_tool, description="Hangs", tier=1)
    
    # Simulate timeout while closing coroutine
    async def mock_timeout(fut, timeout=None):
        if asyncio.iscoroutine(fut):
            fut.close()
        raise asyncio.TimeoutError()

    with patch("src.tools.registry.asyncio.wait_for", side_effect=mock_timeout):
        res = await call_tool("test_hanging_tool", {"delay": 10.0})
        assert "Tool execution timed out" in res


@pytest.mark.asyncio
async def test_call_tool_unknown_tool_raises():
    with pytest.raises(ValueError, match="Unknown tool"):
        await call_tool("non_existent_tool_xyz_999", {})
