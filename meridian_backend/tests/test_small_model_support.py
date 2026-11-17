"""
Tests for Small Model (SLM) Optimization & Resilient Tool Call Recovery.
Verifies that models <=8B (e.g. llama3.2:1b, granite4.1:3b, qwen2.5:3b) can:
1. Use compact system prompt & pruned tool lists (<800 tokens).
2. Auto-heal non-standard JSON argument formats (bare strings, key=val, single quotes).
3. Extract tool calls from Markdown JSON, OpenAI tags, function calls, and ReAct formats.
"""

import json
import pytest
from src.core.mode import is_small_model, build_system_prompt
from src.core.loop_stream import generate_tools_doc
from src.core.loop_executor import sanitize_tool_args_str, clean_final_text
from src.core.loop_parser import fallback_extract_tool_calls


def test_is_small_model():
    # Should identify small models
    assert is_small_model("llama3.2:1b") is True
    assert is_small_model("llama3.2:3b") is True
    assert is_small_model("granite4.1:3b") is True
    assert is_small_model("qwen2.5:1.5b") is True
    assert is_small_model("qwen2.5:3b") is True
    assert is_small_model("qwen2.5:7b") is True
    assert is_small_model("smollm2:135m") is True
    assert is_small_model("phi3:mini") is True
    assert is_small_model("gemma:2b") is True

    # Should not flag large/cloud models
    assert is_small_model("deepseek-chat") is False
    assert is_small_model("gpt-4o") is False
    assert is_small_model("claude-3-5-sonnet") is False
    assert is_small_model("llama-3.3-70b-versatile") is False
    assert is_small_model(None) is False


def test_compact_tools_doc_for_small_model():
    prompt = "list all files in the current folder"
    slm_tools = generate_tools_doc(prompt=prompt, brain_model="llama3.2:1b")
    cloud_tools = generate_tools_doc(prompt=prompt, brain_model="gpt-4o")

    # SLM doc must be concise (under 15 lines of tools), cloud doc has 28+ tools
    slm_lines = [l for l in slm_tools.split("\n") if l.strip()]
    cloud_lines = [l for l in cloud_tools.split("\n") if l.strip()]

    assert len(slm_lines) <= 10
    assert len(cloud_lines) >= 25
    assert len(slm_tools) < len(cloud_tools)


def test_compact_system_prompt_for_small_model():
    prompt = "create a new script"
    tools_doc = "- shell(command): Run shell command\n- write_file(path, content): Write file"
    
    slm_prompt = build_system_prompt(prompt, "llama3.2:3b", "http://localhost:11434", tools_doc)
    large_prompt = build_system_prompt(prompt, "gpt-4o", "http://localhost:11434", tools_doc)

    # Small model prompt must be compact (< 1500 chars) vs large prompt (> 3000 chars)
    assert len(slm_prompt) < 1500
    assert len(large_prompt) > 3000
    assert "HOW TO EXECUTE TOOLS" in slm_prompt


def test_sanitize_tool_args_str_variations():
    # 1. Standard JSON
    assert sanitize_tool_args_str('{"command": "dir"}', tool_name="shell") == '{"command": "dir"}'

    # 2. Single quotes
    res = json.loads(sanitize_tool_args_str("{'command': 'dir'}", tool_name="shell"))
    assert res == {"command": "dir"}

    # 3. Key-value assignment (command="dir")
    res = json.loads(sanitize_tool_args_str('command="dir"', tool_name="shell"))
    assert res == {"command": "dir"}

    # 4. Bare string for shell
    res = json.loads(sanitize_tool_args_str("dir /w", tool_name="shell"))
    assert res == {"command": "dir /w"}

    # 5. Bare path for read_file
    res = json.loads(sanitize_tool_args_str('"C:/path/file.txt"', tool_name="read_file"))
    assert res == {"path": "C:/path/file.txt"}

    # 6. Trailing comma
    res = json.loads(sanitize_tool_args_str('{"command": "dir",}', tool_name="shell"))
    assert res == {"command": "dir"}

    # 7. Unquoted keys
    res = json.loads(sanitize_tool_args_str('{command: "dir"}', tool_name="shell"))
    assert res == {"command": "dir"}


def test_fallback_extract_tool_calls_markdown_json():
    text = """
    I will execute the command to list files.
    ```json
    {
      "tool": "shell",
      "command": "dir"
    }
    ```
    """
    calls = fallback_extract_tool_calls(text)
    assert len(calls) == 1
    assert calls[0][0] == "shell"
    assert json.loads(calls[0][1]) == {"command": "dir"}


def test_fallback_extract_tool_calls_openai_tag():
    text = """
    <tool_call>
    {"name": "shell", "arguments": {"command": "echo hello"}}
    </tool_call>
    """
    calls = fallback_extract_tool_calls(text)
    assert len(calls) == 1
    assert calls[0][0] == "shell"
    assert json.loads(calls[0][1]) == {"command": "echo hello"}


def test_fallback_extract_tool_calls_relaxed_xml():
    # Relaxed unclosed XML or raw content inside tag
    text = "Let me check: <call:shell>dir /s</call:shell>"
    calls = fallback_extract_tool_calls(text)
    assert len(calls) == 1
    assert calls[0][0] == "shell"
    assert json.loads(calls[0][1]) == {"command": "dir /s"}


def test_fallback_extract_tool_calls_function_syntax():
    text = 'I will read the configuration: read_file(path="config.json")'
    calls = fallback_extract_tool_calls(text)
    assert len(calls) == 1
    assert calls[0][0] == "read_file"
    assert json.loads(calls[0][1]) == {"path": "config.json"}


def test_clean_final_text_removes_slm_artifacts():
    dirty = """
    <thought>Thinking about this</thought>
    ```json
    {"tool": "shell", "command": "dir"}
    ```
    Here is the final result of your directory listing:
    Everything is up to date!
    """
    cleaned = clean_final_text(dirty)
    assert "<thought>" not in cleaned
    assert '{"tool": "shell"' not in cleaned
    assert "Here is the final result of your directory listing:\n    Everything is up to date!" in cleaned

