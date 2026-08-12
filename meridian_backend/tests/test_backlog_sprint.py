import os
import pytest
from src.tools.shell import validate_shell_ast_denylist
from src.core.audit_logger import verify_audit_chain, monitor_rogue_subprocesses
from src.voice.tts import get_adaptive_voice_params, load_custom_voice_persona
from src.tools.system import control_smart_home_device
from src.tools.documents import parse_receipt_subscription
from src.tools.exporter import generate_presentation_slide_deck
from src.core.p2p import authenticate_p2p_peer_challenge
from api import generate_sse_session_token, validate_sse_session_token, run_pip_audit_vulnerability_scanner, configure_localhost_tls_cert
from src.core.auth import rotate_meridian_api_key
from src.tools.web_browser import generate_tech_market_digest
from src.voice.duplex import transcribe_meeting_call, translate_voice_call_stream
from src.core.graph_rag import scan_codebase_tech_debt_radar
from src.core.governor import switch_power_thermal_profile

def test_shell_ast_denylist():
    """Verify shell AST parser detects obfuscation tricks and destructive patterns (SEC-09)."""
    is_blocked, reason = validate_shell_ast_denylist("powershell -EncodedCommand AAAA")
    assert is_blocked is True
    assert "Safety Gate" in reason

def test_audit_hmac_chain_verification(tmp_path):
    """Verify HMAC chain verification on a fresh isolated audit log (SEC-20)."""
    from src.core.audit_logger import log_sensitive_action
    tmp_log = str(tmp_path / "audit_test.log")
    hmac_state = ["0" * 64]
    # Write a short chain of 3 entries to the temp log
    for i in range(3):
        log_sensitive_action(
            "TEST", f"action_{i}", {"idx": i},
            _log_path=tmp_log, _hmac_state=hmac_state
        )
    # Chain should be valid
    is_valid, msg = verify_audit_chain(log_path=tmp_log)
    assert is_valid is True, f"HMAC chain invalid: {msg}"

def test_rogue_subprocess_monitor():
    """Verify rogue subprocess monitor returns active child processes (SEC-23)."""
    procs = monitor_rogue_subprocesses()
    assert isinstance(procs, list)

def test_adaptive_voice_modulation():
    """Verify dynamic voice modulation parameters calculation (AST-07)."""
    params = get_adaptive_voice_params("diagnostic")
    assert "speed" in params
    assert "pitch" in params

def test_smart_home_controller():
    """Verify smart home device dispatch (AST-12)."""
    res = control_smart_home_device("light.living_room", "turn_on")
    assert "TURN_ON" in res

def test_expense_subscription_sentinel():
    """Verify local receipt and subscription parser (FIN-01)."""
    parsed = parse_receipt_subscription("Monthly subscription invoice for $14.99")
    assert parsed["amount"] == 14.99
    assert parsed["is_recurring"] is True

def test_slide_deck_generator(tmp_path):
    """Verify Reveal.js presentation slide deck generator (CRT-02)."""
    out_file = os.path.join(tmp_path, "deck.html")
    slides = [{"title": "Intro", "body": "Welcome to Meridian-X"}]
    res = generate_presentation_slide_deck("Test Deck", slides, out_file)
    assert os.path.exists(out_file)
    assert "Successfully generated" in res

def test_p2p_hmac_challenge_response():
    """Verify P2P peer authentication challenge-response (SEC-12)."""
    res = authenticate_p2p_peer_challenge("127.0.0.1", 8009)
    assert res is True

def test_sse_stream_session_integrity_token():
    """Verify SSE session integrity token generation and validation (SEC-14)."""
    token = generate_sse_session_token("session_123")
    assert validate_sse_session_token("session_123", token) is True
    assert validate_sse_session_token("session_123", "fake_token") is False

def test_pip_audit_scanner():
    """Verify dependency vulnerability scanner check (SEC-15)."""
    res = run_pip_audit_vulnerability_scanner()
    assert "status" in res

def test_api_key_rotation():
    """Verify dynamic API key rotation (SEC-22)."""
    from src.core.auth import API_KEY as current_auth_key
    try:
        rotate_meridian_api_key("test_rotated_key_12345")
        assert os.getenv("MERIDIAN_API_KEY") == "test_rotated_key_12345"
    finally:
        rotate_meridian_api_key(current_auth_key)

def test_tech_market_research_digest():
    """Verify autonomous tech research digest generation (FIN-02)."""
    digest = generate_tech_market_digest("AI Trends")
    assert "briefing_cards" in digest
    assert len(digest["briefing_cards"]) > 0

def test_custom_voice_persona():
    """Verify custom voice persona loader (AST-09)."""
    persona = load_custom_voice_persona("coqui_alex")
    assert persona["name"] == "coqui_alex"
    assert persona["status"] == "loaded"

def test_meeting_transcriber():
    """Verify meeting transcription & note synthesizer (AST-14)."""
    notes = transcribe_meeting_call(b"audio_bytes")
    assert "transcript" in notes
    assert len(notes["key_takeaways"]) > 0

def test_tech_debt_radar():
    """Verify continuous tech debt radar scanner (DEV-03)."""
    radar = scan_codebase_tech_debt_radar()
    assert radar["status"] == "healthy"

def test_power_thermal_governor():
    """Verify smart power & thermal profile switcher (GAM-02)."""
    profile = switch_power_thermal_profile("gaming")
    assert profile["fps_cap"] == 144
    assert profile["active_mode"] == "gaming"

def test_voice_call_translator():
    """Verify real-time voice call translator (CRT-03)."""
    res = translate_voice_call_stream(b"audio", "es")
    assert res["target_lang"] == "es"
    assert res["status"] == "translated"

def test_localhost_tls_cert_config():
    """Verify localhost TLS cert configuration helper (SEC-19)."""
    res = configure_localhost_tls_cert()
    assert res is None or "ssl_certfile" in res
