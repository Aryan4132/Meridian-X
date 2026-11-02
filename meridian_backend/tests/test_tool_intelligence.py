import inspect
import pytest
from src.core.tool_indexer import tokenize, build_tool_index, find_relevant_tools
from src.core.loop_executor import auto_heal_tool_args, critique_and_correct_tool_call
from src.core.loop_stream import generate_tools_doc


def test_tokenize():
    tokens = tokenize("calculateLeaveByTime_test with snake_case and STOPWORDS")
    assert "calculate" in tokens
    assert "leave" in tokens
    assert "time" in tokens
    assert "snake" in tokens
    assert "case" in tokens
    assert "stopword" in tokens
    assert "with" not in tokens
    assert "and" not in tokens


def test_tool_index_and_find_relevant_tools():
    index = build_tool_index()
    assert len(index) > 50
    assert "browser_open" in index

    # Niche queries that are NOT in hardcoded KEYWORD_SKILLS_MAP
    trip_tools = find_relevant_tools("I need to calculate leave by time for my trip", top_k=3)
    assert any(t in trip_tools for t in ("calculate_leave_by_time", "create_trip", "get_upcoming_trips"))

    detonate_tools = find_relevant_tools("detonate suspicious sample attachment in sandbox", top_k=3)
    assert "detonate_attachment_sample" in detonate_tools

    usb_tools = find_relevant_tools("audit my connected usb peripherals", top_k=3)
    assert "audit_usb_peripherals" in usb_tools

    empty = find_relevant_tools("   ")
    assert empty == []


def test_generate_tools_doc_semantic_integration():
    doc = generate_tools_doc(prompt="Please detonate suspicious sample in sandbox")
    assert "detonate_attachment_sample" in doc


def test_auto_heal_tool_args_types():
    def sample_func(path: str, count: int, ratio: float, active: bool = False):
        pass

    sig = inspect.signature(sample_func)

    raw_args = {
        "path": '"C:\\workspace\\project\\src\\main.py"',
        "count": "42",
        "ratio": "3.14",
        "active": "true"
    }

    healed_args, changed = auto_heal_tool_args(sig, raw_args)
    assert changed is True
    assert healed_args["count"] == 42
    assert healed_args["ratio"] == 3.14
    assert healed_args["active"] is True
    assert healed_args["path"] == "C:/workspace/project/src/main.py"


def test_critique_and_correct_tool_call_auto_heals():
    # Calling browser_scroll with string amount instead of int
    success, corrected, msg = critique_and_correct_tool_call(
        "browser_scroll",
        '{"direction": "down", "amount": "250"}'
    )
    assert success is True or "Auto-corrected" in msg or "250" in corrected
    import json
    data = json.loads(corrected)
    assert data["amount"] == 250
