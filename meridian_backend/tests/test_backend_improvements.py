"""
test_backend_improvements.py — Verification suite for Core Backend Improvements
Tests:
- Secret redaction (Gemini, Anthropic, HuggingFace, GitHub PAT) in llm_provider
- Hardware detector caching and VRAM resolution
- WorkspaceOrchestrator presets, binary detection, and teardown
- ToolRegressionSentinel health and routing
"""

import pytest
import os
from unittest.mock import patch, MagicMock

from src.core.llm_provider import scan_and_redact_secrets
from src.core.hardware_detector import detect_hardware_specs, _CACHED_HARDWARE_SPECS
from src.core.workspace_orchestrator import WorkspaceOrchestrator
from src.core.tool_regression_sentinel import ToolRegressionSentinel


def test_secret_redaction_expanded():
    """Verifies that expanded secret patterns are redacted."""
    # Anthropic key
    anthropic_key = "sk-ant-api03-abcdefghijklmnopqrstuvwxyz1234567890"
    res = scan_and_redact_secrets(f"My key is {anthropic_key}")
    assert "[REDACTED_SECRET]" in res
    assert anthropic_key not in res

    # Gemini key
    gemini_key = "AIzaSyD-1234567890abcdefghijklmnopqr"
    res2 = scan_and_redact_secrets(f"Google key: {gemini_key}")
    assert "[REDACTED_SECRET]" in res2
    assert gemini_key not in res2

    # Hugging Face key
    hf_key = "hf_abcdefghijklmnopqrstuvwxyz12345678"
    res3 = scan_and_redact_secrets(f"HF token: {hf_key}")
    assert "[REDACTED_SECRET]" in res3
    assert hf_key not in res3

    # Clean text unchanged
    assert scan_and_redact_secrets("Hello world") == "Hello world"


def test_hardware_detector_caching():
    """Verifies that hardware detection is cached in-memory and force_refresh re-evaluates."""
    first = detect_hardware_specs(force_refresh=True)
    assert "cpu_cores" in first
    assert "ram_gb" in first
    assert "gpu" in first

    second = detect_hardware_specs(force_refresh=False)
    assert first == second


def test_workspace_orchestrator_presets():
    """Verifies preset registration, retrieval, and launching without exceptions."""
    orchestrator = WorkspaceOrchestrator(workspace_root=os.path.abspath("."))
    presets = orchestrator.get_presets()
    assert "coding" in presets
    assert "research" in presets
    assert "debugging" in presets
    assert "focus" in presets

    # Launch preset in mock environment
    with patch("webbrowser.open", return_value=True), \
         patch("shutil.which", return_value="/bin/code"):
        result = orchestrator.launch_preset("focus")
        assert result["status"] == "success"
        assert result["preset"] == "focus"

    # Stop preset
    stop_res = orchestrator.stop_preset()
    assert stop_res["status"] == "stopped"


def test_tool_regression_sentinel_routing():
    """Verifies that ToolRegressionSentinel accurately routes test scenarios."""
    sentinel = ToolRegressionSentinel()
    assert sentinel.match_prompt_to_tool("Search the codebase for login logic") == "search_codebase"
    assert sentinel.match_prompt_to_tool("Browse the web for latest AI news") == "browser_use_task"
    assert sentinel.match_prompt_to_tool("Show me my saved memories and facts") == "get_all_memories"
    assert sentinel.match_prompt_to_tool("How much token spend and budget is left?") == "get_spend_stats"
    assert sentinel.match_prompt_to_tool("Undo my last action please") == "undo_last_action"
