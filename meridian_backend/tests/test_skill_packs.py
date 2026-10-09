"""
test_skill_packs.py — Unit Tests for Data-Driven Lazy Skill Packs

Asserts that plugins/skills/*/ packs load, reference real registry tools
with matching tiers, inject on keyword prompts, and keep the presented
prompt under 70 tools.
"""

import os

import pytest

from src.core.skills_loader import (
    load_skill_packs,
    match_skills_for_prompt,
    validate_skill_packs,
)
from src.core.loop_stream import generate_tools_doc
from src.tools.registry import TOOL_REGISTRY

EXPECTED_SKILLS = {"bills", "expiry", "travel", "finance", "home", "health", "geo", "hardening"}


def _count_tools(doc: str) -> int:
    return sum(1 for line in doc.splitlines() if line.startswith("- "))


def test_all_skill_packs_load():
    packs = load_skill_packs()
    assert EXPECTED_SKILLS.issubset(set(packs.keys())), f"missing packs: {EXPECTED_SKILLS - set(packs.keys())}"
    for name, pack in packs.items():
        assert pack["keywords"], f"skill '{name}' has no keywords"
        assert pack["tools"], f"skill '{name}' has no tools"


def test_skill_tools_exist_in_registry_with_matching_tiers():
    packs = load_skill_packs()
    warnings = validate_skill_packs(packs, TOOL_REGISTRY)
    assert warnings == [], "skill/registry mismatches:\n" + "\n".join(warnings)


def test_skill_keyword_injection():
    cases = {
        "my passport expires next month, what should I renew?": "check_document_expiries",
        "which bills are due this week?": "get_bill_due_radar",
        "plan my trip to Tokyo and calculate leave": "create_trip",
        "how is my stock portfolio doing?": "analyze_stock_sentiment",
        "add milk to the grocery list": "add_grocery_item",
        "log my sleep and steps from yesterday": "sync_wearable_health_data",
        "what is the weather like in Berlin?": "get_localized_weather",
        "is this link a phishing attempt?": "check_url_reputation",
    }
    for prompt, expected_tool in cases.items():
        doc = generate_tools_doc(prompt=prompt)
        assert expected_tool in doc, f"prompt {prompt!r} did not inject {expected_tool}"


def test_base_prompt_stays_lean():
    doc = generate_tools_doc(prompt="hello, how are you?")
    assert _count_tools(doc) < 70, f"base prompt has {_count_tools(doc)} tools"
    assert "read_file" in doc  # core primitives still present


def test_skill_prompts_stay_lean():
    prompts = [
        "my visa and passport expire soon and my bills are due",
        "is this wifi safe and is my password strong, also check dns and usb?",
        "plan travel, track stocks, log hydration and check expiry documents",
    ]
    for prompt in prompts:
        doc = generate_tools_doc(prompt=prompt)
        assert _count_tools(doc) < 70, f"prompt {prompt!r} has {_count_tools(doc)} tools"


def test_broken_skill_pack_does_not_break_loader(tmp_path):
    bad = tmp_path / "broken"
    bad.mkdir()
    (bad / "SKILL.md").write_text("no front matter here\n", encoding="utf-8")
    (bad / "tools.yaml").write_text("tools: [unclosed\n", encoding="utf-8")
    packs = load_skill_packs(skills_dir=str(tmp_path), force_reload=True)
    assert packs == {}
    # Restore cache for other tests (reload real packs)
    load_skill_packs(force_reload=True)
    assert EXPECTED_SKILLS.issubset(set(load_skill_packs().keys()))


def test_loader_survives_missing_directory():
    packs = load_skill_packs(skills_dir=os.path.join("nonexistent_dir_xyz"), force_reload=True)
    assert packs == {}
    load_skill_packs(force_reload=True)  # restore cache
