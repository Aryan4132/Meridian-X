"""
test_consensus_gate.py — Unit Tests for Consensus Debate Gating Rules
Asserts that debate is correctly bypassed for low-risk conversational turns
(greetings, read-only queries, voice) and triggered only for mutations,
code generation, audits, and multi-step tasks.
"""

import pytest
from src.core.consensus_engine import should_run_debate, should_trigger_consensus_debate


def test_voice_queries_bypass_debate():
    """Voice mode must always bypass consensus debate to protect sub-500ms TTFA."""
    assert should_run_debate(goal="write a python script", is_voice=True) is False
    assert should_run_debate(tool_calls=["write_to_file"], is_voice=True) is False


def test_greetings_bypass_debate():
    """Conversational greetings must never trigger multi-LLM debate overhead."""
    greetings = ["hi", "hello", "hey", "good morning", "good evening", "thanks", "thank you", "who are you"]
    for g in greetings:
        assert should_run_debate(goal=g) is False
        assert should_run_debate(goal=f"{g} meridian") is False


def test_read_only_queries_bypass_debate():
    """Read-only time/status inquiries must bypass debate."""
    read_only = ["what time is it", "current time", "system status", "health check", "weather"]
    for q in read_only:
        assert should_run_debate(goal=q) is False


def test_mutating_tools_trigger_debate():
    """File writes, shell commands, and git operations must trigger debate."""
    assert should_run_debate(tool_calls=["write_to_file"]) is True
    assert should_run_debate(tool_calls=["replace_file_content"]) is True
    assert should_run_debate(tool_calls=["run_command"]) is True
    assert should_run_debate(tool_calls=[{"name": "git_commit"}]) is True
    assert should_run_debate(tool_calls=[{"tool": "browser_use_task"}]) is True


def test_code_blocks_trigger_debate():
    """Substantial code blocks in the finish response must trigger debate."""
    code_text = "Here is the implementation:\n```python\ndef calculate_fibonacci(n):\n    if n <= 1:\n        return n\n    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)\n```\nLet me know if you need more!"
    assert should_run_debate(goal="fibonacci", finish_text=code_text) is True

    # Short trivial snippet without code should not trigger
    trivial = "Sure thing! Here is what you asked."
    assert should_run_debate(goal="tell me a joke", finish_text=trivial) is False


def test_audit_keywords_trigger_debate():
    """Explicit requests for code review or security auditing must trigger debate."""
    assert should_run_debate(goal="please do a code review of this file") is True
    assert should_run_debate(goal="run a security audit on api.py") is True
    assert should_run_debate(goal="find bugs in the auth handler") is True


def test_multi_step_workflows_trigger_debate():
    """Workflows that execute 2 or more tools must trigger debate."""
    assert should_run_debate(tool_calls=["read_file", "search_files"]) is True
    assert should_run_debate(tool_calls=["grep_search", "read_file", "list_dir"]) is True


def test_legacy_alias():
    """Verify should_trigger_consensus_debate alias behaves identically."""
    assert should_trigger_consensus_debate(tool_calls=["write_to_file"]) is True
    assert should_trigger_consensus_debate(goal="hello") is False
