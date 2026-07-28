"""
test_temporal_consensus.py — Unit tests for temporal date anchoring and false-positive QA reviewer critique filtering.
"""

import pytest
from datetime import datetime
from src.core.mode import build_system_prompt
from src.core.loop import filter_temporal_false_positives, build_consensus_qa_prompt, build_consensus_coder_prompt


def test_build_system_prompt_temporal_anchoring():
    """Verify that build_system_prompt injects system date and temporal anti-hallucination rules."""
    prompt = "Do I have current news for India?"
    sys_prompt = build_system_prompt(prompt, "llama3.2:3b", "http://localhost:11434", "tools_doc")
    
    current_date_str = datetime.now().strftime("%Y-%m-%d")
    assert f"Current System Date: {current_date_str}" in sys_prompt or current_date_str in sys_prompt
    assert "Do NOT flag dates on or before" in sys_prompt or "real-time current events" in sys_prompt


def test_build_consensus_prompts_date_anchoring():
    """Verify that consensus QA and Coder prompts include system date and live web search guidelines."""
    response_text = "Here is today's news for July 28, 2026..."
    current_date_str = datetime.now().strftime("%Y-%m-%d")
    
    qa_prompt = build_consensus_qa_prompt(response_text)
    assert current_date_str in qa_prompt
    assert "search_news" in qa_prompt or "search_web" in qa_prompt
    assert "Do NOT flag dates on or before" in qa_prompt or "verified truth" in qa_prompt

    coder_prompt = build_consensus_coder_prompt(response_text, "Some critique")
    assert current_date_str in coder_prompt or "Refine" in coder_prompt


def test_filter_temporal_false_positives():
    """Verify that false-positive temporal error critiques are accurately filtered or neutralized."""
    current_date_str = datetime.now().strftime("%Y-%m-%d")
    
    # False-positive critique on 2026 search output
    false_critique = (
        "* **Hallucination/Temporal Error:** The response provides news for July 28, 2026, "
        "which is a future date. The agent is fabricating 'current' events."
    )
    
    # Execute filter
    cleaned_critique, is_false_positive = filter_temporal_false_positives(false_critique, current_date_str, executed_search_tool=True)
    assert is_false_positive is True
    assert "Hallucination/Temporal Error" not in cleaned_critique or "BYPASSED" in cleaned_critique or cleaned_critique == ""

    # Real issue critique should NOT be filtered
    real_critique = "* **Syntax Error:** The response JSON is missing a closing brace."
    cleaned_real, is_false_pos_real = filter_temporal_false_positives(real_critique, current_date_str, executed_search_tool=False)
    assert is_false_pos_real is False
    assert cleaned_real == real_critique
