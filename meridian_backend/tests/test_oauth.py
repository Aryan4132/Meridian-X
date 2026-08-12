import os
import sys
import time
import pytest

# Ensure meridian_backend root is in PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.oauth_manager import (
    generate_pkce_pair,
    verify_pkce_challenge,
    create_pkce_auth_state,
    pop_pkce_state,
    create_jwt_token,
    decode_jwt_token,
    save_oauth_tokens,
    get_oauth_tokens,
    delete_oauth_tokens,
    refresh_expired_tokens,
    OAUTH_PROVIDERS
)


def test_pkce_generation_and_verification():
    pkce = generate_pkce_pair()
    assert "code_verifier" in pkce
    assert "code_challenge" in pkce
    assert pkce["code_challenge_method"] == "S256"
    
    # Valid verifier matching challenge
    assert verify_pkce_challenge(pkce["code_verifier"], pkce["code_challenge"]) is True
    
    # Invalid verifier
    assert verify_pkce_challenge("wrong_verifier_12345", pkce["code_challenge"]) is False


def test_pkce_state_store():
    state_info = create_pkce_auth_state("google", "http://localhost:3000/callback")
    state = state_info["state"]
    assert state is not None
    
    popped = pop_pkce_state(state)
    assert popped is not None
    assert popped["provider"] == "google"
    assert popped["redirect_uri"] == "http://localhost:3000/callback"
    
    # Second pop should return None (one-time use state)
    assert pop_pkce_state(state) is None


def test_jwt_create_and_decode():
    payload = {"sub": "user_123", "role": "admin"}
    token = create_jwt_token(payload, expires_in_seconds=300)
    assert isinstance(token, str)
    assert len(token) > 20
    
    decoded = decode_jwt_token(token)
    assert decoded is not None
    assert decoded["sub"] == "user_123"
    assert decoded["role"] == "admin"
    assert "exp" in decoded


def test_jwt_expiration():
    payload = {"sub": "user_expired"}
    # Token expired 10 seconds ago
    token = create_jwt_token(payload, expires_in_seconds=-10)
    decoded = decode_jwt_token(token)
    assert decoded is None


def test_encrypted_vault_oauth_tokens():
    test_data = {
        "access_token": "mock_access_12345",
        "refresh_token": "mock_refresh_67890",
        "token_type": "Bearer",
        "expires_in": 3600
    }
    
    saved = save_oauth_tokens("github", test_data, "test_user")
    assert saved is True
    
    retrieved = get_oauth_tokens("github", "test_user")
    assert retrieved is not None
    assert retrieved["access_token"] == "mock_access_12345"
    assert retrieved["refresh_token"] == "mock_refresh_67890"
    
    deleted = delete_oauth_tokens("github", "test_user")
    assert deleted is True


def test_token_auto_rotator():
    test_data = {
        "access_token": "expiring_access",
        "refresh_token": "valid_refresh",
        "expires_at": time.time() + 100  # Expiring within 5 mins
    }
    save_oauth_tokens("google", test_data, "rotator_user")
    
    status = refresh_expired_tokens("rotator_user")
    assert "google" in status
    assert status["google"] is True
    
    refreshed = get_oauth_tokens("google", "rotator_user")
    assert refreshed["expires_at"] > time.time() + 1000
