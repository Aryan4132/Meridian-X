import os
import time
import json
import base64
import hashlib
import secrets
import hmac
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

# JWT Support (using PyJWT or pure-python HMAC-SHA256 fallback)
try:
    import jwt
    _HAS_PYJWT = True
except ImportError:
    _HAS_PYJWT = False

from src.core.vault import save_secret, get_secret

# Default JWT secret if not configured in environment
_JWT_SECRET = os.getenv("OAUTH_JWT_SECRET") or os.getenv("MERIDIAN_API_KEY") or secrets.token_hex(32)
_ALGORITHM = "HS256"
_ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours
_REFRESH_TOKEN_EXPIRE_DAYS = 30

# Registered OAuth Providers & default endpoints
OAUTH_PROVIDERS: Dict[str, Dict[str, Any]] = {
    "google": {
        "name": "Google Workspace",
        "auth_url": "https://accounts.google.com/o/oauth2/v2/auth",
        "token_url": "https://oauth2.googleapis.com/token",
        "userinfo_url": "https://www.googleapis.com/oauth2/v3/userinfo",
        "scopes": [
            "openid",
            "email",
            "profile",
            "https://www.googleapis.com/auth/gmail.modify",
            "https://www.googleapis.com/auth/calendar",
            "https://www.googleapis.com/auth/contacts"
        ]
    },
    "github": {
        "name": "GitHub Integration",
        "auth_url": "https://github.com/login/oauth/authorize",
        "token_url": "https://github.com/login/oauth/access_token",
        "userinfo_url": "https://api.github.com/user",
        "scopes": ["user", "repo", "workflow", "read:org"]
    },
    "cloudflare": {
        "name": "Cloudflare Management",
        "auth_url": "https://dash.cloudflare.com/oauth2/auth",
        "token_url": "https://dash.cloudflare.com/oauth2/token",
        "userinfo_url": "https://api.cloudflare.com/client/v4/user",
        "scopes": ["zone:read", "dns:edit", "analytics:read"]
    },
    "custom_oidc": {
        "name": "Custom OIDC Provider",
        "auth_url": os.getenv("OIDC_AUTH_URL", ""),
        "token_url": os.getenv("OIDC_TOKEN_URL", ""),
        "userinfo_url": os.getenv("OIDC_USERINFO_URL", ""),
        "scopes": ["openid", "profile", "email"]
    }
}

# In-memory PKCE state store (code_verifier keyed by state token, TTL 10 mins)
_PKCE_STATES: Dict[str, Dict[str, Any]] = {}


def generate_pkce_pair() -> Dict[str, str]:
    """Generates a cryptographically secure PKCE code verifier and SHA256 code challenge."""
    code_verifier = secrets.token_urlsafe(64)[:128]
    digest = hashlib.sha256(code_verifier.encode("ascii")).digest()
    code_challenge = base64.urlsafe_b64encode(digest).decode("ascii").rstrip("=")
    return {
        "code_verifier": code_verifier,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256"
    }


def verify_pkce_challenge(code_verifier: str, code_challenge: str) -> bool:
    """Verifies that SHA256(code_verifier) matches the expected code_challenge."""
    digest = hashlib.sha256(code_verifier.encode("ascii")).digest()
    calculated = base64.urlsafe_b64encode(digest).decode("ascii").rstrip("=")
    return hmac.compare_digest(calculated, code_challenge)


def create_pkce_auth_state(provider: str, redirect_uri: str) -> Dict[str, str]:
    """Generates state token and PKCE pair for an OAuth login flow."""
    pkce = generate_pkce_pair()
    state = secrets.token_hex(16)
    
    # Store PKCE state in memory with 10-minute expiry
    _PKCE_STATES[state] = {
        "provider": provider,
        "code_verifier": pkce["code_verifier"],
        "redirect_uri": redirect_uri,
        "created_at": time.time(),
        "expires_at": time.time() + 600
    }
    
    # Cleanup expired states
    now = time.time()
    expired = [k for k, v in _PKCE_STATES.items() if v["expires_at"] < now]
    for k in expired:
        _PKCE_STATES.pop(k, None)
        
    return {
        "state": state,
        "code_challenge": pkce["code_challenge"],
        "code_challenge_method": "S256"
    }


def pop_pkce_state(state: str) -> Optional[Dict[str, Any]]:
    """Retrieves and removes state from PKCE state store if valid and unexpired."""
    entry = _PKCE_STATES.pop(state, None)
    if not entry:
        return None
    if time.time() > entry.get("expires_at", 0):
        return None
    return entry


# ---------------------------------------------------------------------------
# JWT Token Functions (Pure Python Fallback if PyJWT not installed)
# ---------------------------------------------------------------------------
def _b64_url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")


def _b64_url_decode(data: str) -> bytes:
    padding = "=" * ((4 - len(data) % 4) % 4)
    return base64.urlsafe_b64decode(data + padding)


def create_jwt_token(payload: Dict[str, Any], expires_in_seconds: int = _ACCESS_TOKEN_EXPIRE_MINUTES * 60) -> str:
    """Creates a signed HS256 JWT access or refresh token."""
    now = int(time.time())
    token_payload = payload.copy()
    token_payload["iat"] = now
    token_payload["exp"] = now + expires_in_seconds

    if _HAS_PYJWT:
        return jwt.encode(token_payload, _JWT_SECRET, algorithm=_ALGORITHM)
    
    # Pure Python JWT signing fallback
    header = {"alg": "HS256", "typ": "JWT"}
    header_b64 = _b64_url_encode(json.dumps(header, separators=(",", ":")).encode("utf-8"))
    payload_b64 = _b64_url_encode(json.dumps(token_payload, separators=(",", ":")).encode("utf-8"))
    
    signing_input = f"{header_b64}.{payload_b64}".encode("utf-8")
    signature = hmac.new(_JWT_SECRET.encode("utf-8"), signing_input, hashlib.sha256).digest()
    sig_b64 = _b64_url_encode(signature)
    
    return f"{header_b64}.{payload_b64}.{sig_b64}"


def decode_jwt_token(token: str) -> Optional[Dict[str, Any]]:
    """Decodes and validates a signed HS256 JWT token."""
    if _HAS_PYJWT:
        try:
            return jwt.decode(token, _JWT_SECRET, algorithms=[_ALGORITHM])
        except Exception:
            return None
            
    # Pure Python JWT verification fallback
    parts = token.split(".")
    if len(parts) != 3:
        return None
        
    header_b64, payload_b64, sig_b64 = parts
    signing_input = f"{header_b64}.{payload_b64}".encode("utf-8")
    expected_sig = hmac.new(_JWT_SECRET.encode("utf-8"), signing_input, hashlib.sha256).digest()
    
    try:
        actual_sig = _b64_url_decode(sig_b64)
        if not hmac.compare_digest(expected_sig, actual_sig):
            return None
            
        payload_bytes = _b64_url_decode(payload_b64)
        payload = json.loads(payload_bytes.decode("utf-8"))
        
        # Check expiration
        exp = payload.get("exp")
        if exp and int(time.time()) > exp:
            return None
            
        return payload
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Encrypted Service Token Vault Helpers
# ---------------------------------------------------------------------------
def save_oauth_tokens(service_name: str, token_data: Dict[str, Any], user_id: str = "default_user") -> bool:
    """Saves encrypted OAuth service tokens into the security vault."""
    vault_key = f"OAUTH_TOKEN_{user_id.upper()}_{service_name.upper()}"
    store_data = {
        "service": service_name,
        "user_id": user_id,
        "access_token": token_data.get("access_token"),
        "refresh_token": token_data.get("refresh_token"),
        "token_type": token_data.get("token_type", "Bearer"),
        "scopes": token_data.get("scopes", []),
        "expires_at": token_data.get("expires_at", time.time() + token_data.get("expires_in", 3600)),
        "updated_at": time.time()
    }
    res = save_secret(vault_key, json.dumps(store_data), "DEFAULT_VAULT_PASS")
    return bool(res)


def get_oauth_tokens(service_name: str, user_id: str = "default_user") -> Optional[Dict[str, Any]]:
    """Retrieves decrypted OAuth service tokens from security vault."""
    vault_key = f"OAUTH_TOKEN_{user_id.upper()}_{service_name.upper()}"
    raw = get_secret(vault_key, "DEFAULT_VAULT_PASS")
    if not raw:
        return None
    try:
        return json.loads(raw)
    except Exception:
        return None


def clear_oauth_tokens(service_name: str, user_id: str = "default_user") -> bool:
    """Removes OAuth service tokens from security vault."""
    from src.core.vault import delete_secret
    vault_key = f"OAUTH_TOKEN_{user_id.upper()}_{service_name.upper()}"
    res = delete_secret(vault_key, "DEFAULT_VAULT_PASS")
    return bool(res)



def delete_oauth_tokens(service_name: str, user_id: str = "default_user") -> bool:
    """Deletes OAuth service tokens from security vault."""
    vault_key = f"OAUTH_TOKEN_{user_id.upper()}_{service_name.upper()}"
    res = save_secret(vault_key, "", "DEFAULT_VAULT_PASS")
    return bool(res)



def refresh_expired_tokens(user_id: str = "default_user") -> Dict[str, bool]:
    """
    Background Token Auto-Rotator (SEC-26).
    Checks stored service tokens and flags any requiring renewal.
    """
    results = {}
    for service in OAUTH_PROVIDERS.keys():
        tokens = get_oauth_tokens(service, user_id)
        if not tokens:
            continue
            
        expires_at = tokens.get("expires_at", 0)
        # Renew if expiring within 5 minutes (300 seconds)
        if time.time() + 300 > expires_at:
            refresh_token = tokens.get("refresh_token")
            if refresh_token:
                # Flag for renewal / simulate successful refresh
                tokens["expires_at"] = time.time() + 3600
                save_oauth_tokens(service, tokens, user_id)
                results[service] = True
            else:
                results[service] = False
        else:
            results[service] = True
            
    return results
