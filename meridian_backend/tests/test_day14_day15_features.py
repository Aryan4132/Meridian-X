"""
test_day14_day15_features.py — Verification Test Suite for Day 14 & Day 15 Features
Covering:
- Day 14: SwarmAgent heterogeneous model binding (PL-10), P2P QR pairing & token validation (ECO-01, OPS-02), WhatsApp call bridge (CALL-05)
- Day 15: Wearable Health Ingestion (FIT-01), Wellness & Ergonomics (BUTLER-03), Evening Wind-Down Digest (BUTLER-07), Voice Thought Bucket (BUTLER-25), Memory Time Machine (BUTLER-26)
"""

import pytest
import os
import time

def test_swarm_heterogeneous_model_binding():
    from src.core.swarm import SwarmAgent, SWARM_ROLE_MODELS
    
    researcher = SwarmAgent(role="researcher")
    assert researcher.model == SWARM_ROLE_MODELS["researcher"]
    assert researcher.model == "gemini-1.5-flash"

    auditor = SwarmAgent(role="auditor")
    assert auditor.model == "deepseek-coder"

    custom_agent = SwarmAgent(role="planner", model="custom-gpt-5")
    assert custom_agent.model == "custom-gpt-5"

def test_p2p_qr_pairing_and_token_verification():
    from src.core.p2p import generate_qr_pairing_payload, verify_mobile_pairing_secret, _bootstrap_p2p_token

    payload = generate_qr_pairing_payload()
    assert payload["app"] == "Meridian-X"
    assert "secret" in payload
    assert payload["port"] == 8009

    secret = payload["secret"]
    assert verify_mobile_pairing_secret(secret) is True
    assert verify_mobile_pairing_secret("invalid_secret_123") is False

def test_whatsapp_voice_call_bridge():
    from src.tools.whatsapp_manager import bridge_whatsapp_voice_call
    res = bridge_whatsapp_voice_call("Alex Mercer")
    assert "WhatsApp Voice Call Bridge" in res or "Initiated WhatsApp voice call bridge" in res

def test_wearable_health_ingestion():
    from src.tools.health_ingest import sync_wearable_health_data, get_health_metrics_summary

    res = sync_wearable_health_data(source="apple_health", steps=10500, sleep_hours=8.0, heart_rate=64)
    assert "Steps Today: 10,500" in res
    assert "8.0 hours" in res

    summary = get_health_metrics_summary()
    assert summary["steps"] == 10500
    assert summary["sleep_hours"] == 8.0
    assert summary["source"] == "apple_health"

def test_wellness_and_ergonomics_butler():
    from src.tools.wellness import track_hydration, trigger_ergonomic_break, calculate_daily_wellness_score

    res_h = track_hydration(amount_ml=500)
    assert "Logged 500ml water" in res_h

    res_b = trigger_ergonomic_break("eye_strain")
    assert "20-20-20 Eye Strain Break" in res_b

    score_dict = calculate_daily_wellness_score()
    assert "score" in score_dict
    assert 0 <= score_dict["score"] <= 100
    assert score_dict["status"] in ("Optimal", "Fair", "Needs Attention")

def test_evening_winddown_digest():
    from src.core.proactive import generate_evening_winddown_digest
    digest = generate_evening_winddown_digest()
    assert digest["tasks_completed"] == 8
    assert "wellness_score" in digest
    assert len(digest["shutdown_ritual"]) >= 3

def test_voice_thought_bucket():
    from src.core.temporal_memory import capture_voice_thought, query_voice_thoughts

    thought = capture_voice_thought("Remind me to refactor the AST code graph indexer tomorrow.", tags=["refactor", "ast"])
    assert thought["status"] == "success"
    assert "refactor" in thought["tags"]

    queried = query_voice_thoughts("ast")
    assert len(queried) >= 1
    assert "AST code graph" in queried[0]["transcript"]

def test_memory_time_machine():
    from src.core.memory_backup import create_encrypted_snapshot, list_memory_snapshots, restore_memory_snapshot

    snap = create_encrypted_snapshot("test_run")
    assert snap["status"] == "success"
    assert snap["snapshot_id"].startswith("snapshot_")

    snapshots = list_memory_snapshots()
    assert len(snapshots) >= 1

    res = restore_memory_snapshot(snap["snapshot_id"])
    assert res["status"] == "success"
