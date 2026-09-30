"""
meridian_backend/tests/test_day11_features.py
Verification Test Suite for Day 11 Telephony & Communication Intelligence
"""

import sys
import pytest
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_voip_phone_agent_outbound():
    """Test phone_agent.py outbound call initiation."""
    from src.tools.phone_agent import make_outbound_call, get_call_logs

    res = make_outbound_call(to_number="+18005550199", objective="Verify system deployment")
    assert isinstance(res, dict)
    assert res["to_number"] == "+18005550199"
    assert "call_id" in res

    logs = get_call_logs()
    assert len(logs) > 0


def test_ai_call_screener():
    """Test phone_agent.py AI receptionist call screening."""
    from src.tools.phone_agent import screen_incoming_call

    # Test spam detection
    res_spam = screen_incoming_call(caller_id="+19005550000", transcript_snippet="Calling about your car warranty extension offer")
    assert res_spam["classification"] == "spam"
    assert res_spam["priority"] == "low"

    # Test priority VIP detection
    res_vip = screen_incoming_call(caller_id="+12005551111", transcript_snippet="Hello doctor calling regarding urgent medical test result")
    assert res_vip["classification"] == "priority_vip"
    assert res_vip["priority"] == "high"


def test_post_call_intelligence():
    """Test phone_agent.py post-call intelligence and action item extraction."""
    from src.tools.phone_agent import process_post_call_intelligence

    transcript = [
        "Speaker 1: Hi, calling about tomorrow's 2 PM strategy meeting.",
        "Speaker 2: Please follow up with status report email."
    ]
    res = process_post_call_intelligence(call_id="call_test_1", full_transcript=transcript)
    assert "summary" in res
    assert len(res["action_items"]) > 0
    assert res["task_synced"] is True


def test_emergency_sos_protocol():
    """Test sos_protocol.py emergency SOS location resolution and alert payload."""
    from src.core.sos_protocol import trigger_emergency_sos

    res = trigger_emergency_sos(phrase="help emergency assistance needed")
    assert res["success"] is True
    assert "location" in res
    assert res["siren_triggered"] is True
    assert len(res["alerts_sent"]) > 0


def test_email_zero_triage():
    """Test external_connectors.py email triage and draft reply generation."""
    from src.tools.external_connectors import triage_inbox_emails, generate_draft_reply, manage_unsubscribes

    triage = triage_inbox_emails(limit=5)
    assert isinstance(triage, dict)
    assert "needs_reply" in triage
    assert "fyi" in triage
    assert "noise" in triage

    reply = generate_draft_reply(email_id="msg_test", instructions="Confirm meeting time")
    assert reply["success"] is True
    assert "draft_reply" in reply

    unsub = manage_unsubscribes()
    assert "promotional_newsletters" in unsub


def test_personal_crm_sentinel():
    """Test personal_crm.py contact graph and occasion check."""
    from src.core.personal_crm import add_crm_contact, check_crm_occasions, list_crm_contacts

    add_res = add_crm_contact(name="John Doe", relationship="VIP Partner", birthday="12-25", notes="Loves tech gadgets")
    assert add_res["success"] is True

    occasions = check_crm_occasions()
    assert "upcoming_occasions" in occasions
    assert "silent_vips" in occasions

    contacts = list_crm_contacts()
    assert len(contacts) > 0


def test_meeting_prep_briefing():
    """Test proactive.py T-minus-10-min meeting prep briefing generator."""
    from src.core.proactive import generate_meeting_prep_briefing

    briefing = generate_meeting_prep_briefing(meeting_title="Sprint 2 Design Sync")
    assert briefing["meeting_title"] == "Sprint 2 Design Sync"
    assert briefing["starts_in_minutes"] == 10
    assert len(briefing["attendees"]) > 0


def test_tool_registry_day11_integration():
    """Test registry.py registration of Day 11 tools."""
    from src.tools.registry import TOOL_REGISTRY

    assert "make_outbound_call" in TOOL_REGISTRY
    assert "screen_incoming_call" in TOOL_REGISTRY
    assert "process_post_call_intelligence" in TOOL_REGISTRY
    assert "trigger_emergency_sos" in TOOL_REGISTRY
    assert "triage_inbox_emails" in TOOL_REGISTRY
    assert "generate_draft_reply" in TOOL_REGISTRY
    assert "add_crm_contact" in TOOL_REGISTRY
    assert "check_crm_occasions" in TOOL_REGISTRY
    assert "generate_meeting_prep_briefing" in TOOL_REGISTRY
