import os
import pytest
from src.core.auth import verify_provided_token, compute_sha256, API_KEY

def test_verify_provided_token_raw_api_key():
    assert verify_provided_token(API_KEY) is True

def test_verify_provided_token_sha256_api_key():
    hashed_key = compute_sha256(API_KEY)
    assert verify_provided_token(hashed_key) is True

def test_verify_provided_token_custom_password(monkeypatch):
    monkeypatch.setenv("MERIDIAN_PAIRING_PASSWORD", "my_custom_secret_passphrase")
    raw_pwd = "my_custom_secret_passphrase"
    hashed_pwd = compute_sha256(raw_pwd)
    
    assert verify_provided_token(raw_pwd) is True
    assert verify_provided_token(hashed_pwd) is True
    assert verify_provided_token("invalid_password") is False

def test_verify_provided_token_empty():
    assert verify_provided_token("") is False
    assert verify_provided_token(None) is False
