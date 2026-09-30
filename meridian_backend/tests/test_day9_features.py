"""
test_day9_features.py — Unit & Integration Tests for Day 9 Features
Tests Memory Editor (TRUST-01), Cloud Spend Meter (TRUST-03), Air-Gap Mode (OPS-04), Updater (OPS-01), and Action Journal Undo (BUTLER-14).
"""

import pytest
import os
import json
from src.core.memory_editor import MemoryEditor
from src.core.updater import SystemUpdater
from src.core.action_journal import ActionJournal
from src.core.mode import get_local_only_mode, set_local_only_mode, get_airgap_proof_badge
from database import record_token_spend, get_spend_stats, set_budget_cap, get_budget_cap


def test_memory_editor_crud():
    """Tests MemoryEditor fetch, search, update, forget, and JSON export (TRUST-01)."""
    editor = MemoryEditor()

    # 1. Fetch memories
    memories = editor.get_all_memories()
    assert isinstance(memories, list)

    # 2. Update preference
    updated = editor.update_memory_entry("pref:test_key_day9", "value_day9")
    assert updated is True

    # 3. Search memory
    filtered = editor.get_all_memories(query="test_key_day9")
    assert len(filtered) >= 1
    assert any("test_key_day9" in str(m) for m in filtered)

    # 4. Export JSON
    export_bundle = editor.export_memory_json()
    assert "preferences" in export_bundle
    assert "temporal_nodes" in export_bundle
    assert "all_memories_flat" in export_bundle

    # 5. Forget entity
    forgot_count = editor.forget_entity("pref:test_key_day9")
    assert forgot_count >= 1


def test_cloud_spend_and_token_meter():
    """Tests token spend logging, cost calculation, and budget cap checks (TRUST-03)."""
    # 1. Set budget cap
    assert set_budget_cap(15.0) is True
    assert get_budget_cap() == 15.0

    # 2. Record token spend
    record_token_spend("openai", "gpt-4o", 1000, 500, 0.0075)

    # 3. Retrieve stats
    stats = get_spend_stats()
    assert "monthly_cost_usd" in stats
    assert stats["monthly_cost_usd"] >= 0.0075
    assert "by_provider" in stats
    assert "openai" in stats["by_provider"]


def test_airgap_local_only_mode():
    """Tests Air-Gap Local-Only mode toggle and proof badge generation (OPS-04)."""
    # 1. Toggle Air-Gap mode on
    set_local_only_mode(True)
    assert get_local_only_mode() is True

    # 2. Verify proof badge
    badge = get_airgap_proof_badge()
    assert badge["airgap_active"] is True
    assert badge["proof_badge"].startswith("AG-")
    assert len(badge["signature"]) == 64

    # 3. Toggle off
    set_local_only_mode(False)
    assert get_local_only_mode() is False


def test_self_updater_functions(tmp_path):
    """Tests SystemUpdater version check, SHA256 verification, and safe swap (OPS-01)."""
    updater = SystemUpdater(version="0.1.0")

    # 1. Check updates
    res = updater.check_for_updates()
    assert "current_version" in res
    assert res["current_version"] == "0.1.0"

    # 2. SHA256 checksum test
    test_file = tmp_path / "test_bin.exe"
    test_file.write_bytes(b"meridian_binary_content_day9")
    import hashlib
    expected_hash = hashlib.sha256(b"meridian_binary_content_day9").hexdigest()
    assert updater.verify_sha256(str(test_file), expected_hash) is True

    # 3. Safe swap test
    target_bin = tmp_path / "target.exe"
    new_bin = tmp_path / "new.exe"
    target_bin.write_bytes(b"v1_binary")
    new_bin.write_bytes(b"v2_binary")

    success, backup_path = updater.safe_swap_binary(str(target_bin), str(new_bin))
    assert success is True
    assert os.path.exists(backup_path)
    assert target_bin.read_bytes() == b"v2_binary"


def test_action_journal_and_undo():
    """Tests ActionJournal recording and inverse action execution (BUTLER-14)."""
    journal = ActionJournal()

    # 1. Record reversible preference change action
    action_id = journal.record_action(
        tool="save_user_preference",
        arguments={"key": "theme", "value": "cyberpunk"},
        inverse_tool="save_user_preference",
        inverse_arguments={"key": "theme", "value": "dark"},
        description="Changed UI theme to cyberpunk"
    )
    assert action_id.startswith("act_")

    # 2. Fetch recent actions
    recent = journal.get_recent_actions(10)
    assert len(recent) > 0
    assert any(a["id"] == action_id for a in recent)

    # 3. Execute undo
    undo_res = journal.undo_action(action_id=action_id)
    assert undo_res["success"] is True
    assert undo_res["action_id"] == action_id


def test_transient_phrase_filtering():
    """Tests that short filler phrases like 'try again' are skipped from DB storage."""
    from database import is_transient_phrase, add_to_conversations, get_conversation_history

    assert is_transient_phrase("try again") is True
    assert is_transient_phrase("retry.") is True
    assert is_transient_phrase("thanks") is True
    assert is_transient_phrase("Build a python web app") is False

    # Verify add_to_conversations skips storing transient phrase
    initial_count = len(get_conversation_history(100))
    add_to_conversations("user", "try again")
    after_count = len(get_conversation_history(100))
    assert initial_count == after_count


def test_airgap_cloud_model_and_host_blocking():
    """Tests that cloud Ollama models and remote Ollama host URLs are hard-blocked in Air-Gap mode."""
    from src.core.mode import set_local_only_mode
    from src.core.llm_provider import generate_completion_stream
    import asyncio

    set_local_only_mode(True)

    async def _run():
        res = []
        async for chunk in generate_completion_stream([], provider="ollama", model="gemma4:32b-cloud"):
            res.append(chunk)
        return "".join(res)

    out = asyncio.run(_run())
    assert "Error: Local-Only Air-Gap Mode is active" in out
    assert "hard-blocked" in out
    set_local_only_mode(False)


def test_security_guard_unrestricted_mode():
    """Tests System Guard level 0 (Unrestricted PC Mode) approval gate bypass."""
    from database import set_security_guard_level, get_security_guard_level, get_unrestricted_pc_access
    from src.core.loop import check_approval_gate

    # Level 1 Strict Mode
    set_security_guard_level(1)
    assert get_security_guard_level() == 1
    req, _ = check_approval_gate("delete_file", {"filepath": "important.txt"})
    assert req is True

    # Level 0 Unrestricted PC Mode
    set_security_guard_level(0)
    assert get_security_guard_level() == 0
    assert get_unrestricted_pc_access() is True
    req_unrestricted, _ = check_approval_gate("delete_file", {"filepath": "important.txt"})
    assert req_unrestricted is False

    # Restore Level 1
    set_security_guard_level(1)


