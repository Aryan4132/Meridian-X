import os
import secrets
import hmac
from typing import Optional, Any
from fastapi import Header, HTTPException, status, Depends
from fastapi.security import APIKeyHeader

# API Key Header definition
API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)

def bootstrap_api_key():
  """
  Checks if MERIDIAN_API_KEY exists. If not, generates a 32-byte hex key,
  writes it to the root .env file (both MERIDIAN_API_KEY and VITE_API_KEY),
  and sets it in the environment.
  """
  # BUG-51 fix: replaced fragile 4-level dirname chain with find_workspace_root().
  # Chaining dirname N times is brittle if the file is ever moved to a sub-package.
  try:
    from src.core.history_manager import find_workspace_root
    env_path = os.path.join(find_workspace_root(), ".env")
  except Exception:
    # Fallback to dirname chain if history_manager is unavailable
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), ".env")
  
  api_key = os.getenv("MERIDIAN_API_KEY")
  if not api_key:
    # Try reading from .env manually
    if os.path.exists(env_path):
      with open(env_path, "r") as f:
        for line in f:
          if line.startswith("MERIDIAN_API_KEY="):
            api_key = line.split("=", 1)[1].strip()
            break
            
  if not api_key:
    # Generate new cryptographically secure key
    api_key = secrets.token_hex(32)
    # Ensure variables are written to .env
    mode = "a" if os.path.exists(env_path) else "w"
    try:
      with open(env_path, mode) as f:
        # Add newlines if adding to existing file
        if mode == "a":
          f.write("\n")
        f.write(f"MERIDIAN_API_KEY={api_key}\n")
        f.write(f"VITE_API_KEY={api_key}\n")
    except Exception as e:
      print(f"Error bootstrapping API key to .env: {e}")
      
    os.environ["MERIDIAN_API_KEY"] = api_key
    os.environ["VITE_API_KEY"] = api_key
  
  return api_key

def rotate_meridian_api_key(new_key: str):
    """Rotates MERIDIAN_API_KEY dynamically in environment and memory (SEC-22)."""
    global API_KEY
    API_KEY = new_key
    os.environ["MERIDIAN_API_KEY"] = new_key
    os.environ["VITE_API_KEY"] = new_key
    from src.core.audit_logger import log_sensitive_action
    log_sensitive_action("SECURITY_AUDIT", "api_key_rotated", {"new_key_prefix": new_key[:10] + "..."}, "SUCCESS")

def bootstrap_webhook_secret():
  """Ensures MERIDIAN_WEBHOOK_SECRET exists; generates + persists one if missing (SEC-FIX).

  Used to HMAC-sign /api/workflows/webhook ingress requests so unsigned callers
  can never trigger OAuth-backed workflow actions.
  """
  secret = os.getenv("MERIDIAN_WEBHOOK_SECRET")
  if secret:
    return secret
  try:
    from src.core.history_manager import find_workspace_root
    env_path = os.path.join(find_workspace_root(), ".env")
  except Exception:
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), ".env")
  if os.path.exists(env_path):
    with open(env_path, "r") as f:
      for line in f:
        if line.startswith("MERIDIAN_WEBHOOK_SECRET="):
          secret = line.split("=", 1)[1].strip()
          break
  if not secret:
    secret = secrets.token_hex(32)
    mode = "a" if os.path.exists(env_path) else "w"
    try:
      with open(env_path, mode) as f:
        if mode == "a":
          f.write("\n")
        f.write(f"MERIDIAN_WEBHOOK_SECRET={secret}\n")
    except Exception as e:
      print(f"Error bootstrapping webhook secret to .env: {e}")
    os.environ["MERIDIAN_WEBHOOK_SECRET"] = secret
  return secret

# Run bootstrap on module load
API_KEY = bootstrap_api_key()

from fastapi import Header, HTTPException, status, Depends, Request


def _is_loopback_request(request: Optional[Request]) -> bool:
    """Allow same-machine desktop app traffic only when the TCP peer is actually loopback.

    SEC-FIX: never trust the client-supplied ``Host`` or ``Origin`` headers for the
    auth decision — a LAN attacker (or a DNS-rebinding page) can set both freely.
    The physical source IP of the socket is the only trustworthy signal here.
    """
    if request is None:
        return False

    client_host = getattr(getattr(request, "client", None), "host", "") or ""
    if client_host in {"127.0.0.1", "::1", "localhost"}:
        # Loopback peer — additionally require a trusted Origin when one is
        # presented so browser-based DNS-rebinding requests are rejected.
        origin = (request.headers.get("origin") or "").strip().lower()
        if not origin or origin.startswith((
            "http://localhost", "http://127.0.0.1", "http://[::1]",
            "https://localhost", "https://127.0.0.1",
            "tauri://localhost", "http://tauri.localhost",
        )):
            return True
    return False


def require_api_key(
    request: Request,
    api_key_header: Optional[str] = Depends(API_KEY_HEADER)
):
    """
    FastAPI route dependency supporting Dual Auth:
    1. Authorization: Bearer <jwt_token>
    2. X-API-Key: <api_key>
    Uses constant-time comparison and JWT decoding to prevent side-channel timing attacks.
    Whitelists public endpoints (/api/health, /api/debug/log, /api/auth/oauth/*).
    """
    # Allow bypass if testing or environment explicitly disabled auth
    if os.getenv("DISABLE_AUTH") == "true":
        return True

    # Check path whitelist if request object is available
    if request is not None and hasattr(request, "url"):
        path = request.url.path
        if path in ("/api/health", "/docs", "/openapi.json") or path.startswith("/api/auth/oauth"):
            return True
        # SEC-FIX: /api/workflows/webhook and /api/debug/log removed from the
        # whitelist — webhooks verify their own HMAC signature (api.py) and the
        # debug log endpoint now requires auth to prevent log injection.

    if _is_loopback_request(request):
        return True

    client_ip = getattr(getattr(request, "client", None), "host", "unknown") if request else "unknown"

    # 1. Check for Authorization: Bearer <jwt_token>
    auth_header = request.headers.get("Authorization") if request else None
    if auth_header and auth_header.startswith("Bearer "):
        bearer_token = auth_header.split(" ", 1)[1].strip()
        from src.core.oauth_manager import decode_jwt_token
        decoded = decode_jwt_token(bearer_token)
        if decoded:
            return True

    # 2. Check X-API-Key header
    if api_key_header and hmac.compare_digest(api_key_header, API_KEY):
        return True

    # Auth failed
    try:
        from src.core.audit_logger import log_sensitive_action
        log_sensitive_action(
            category="AUTH_FAILURE",
            action="require_api_key",
            details={"reason": "Missing or invalid auth credential", "ip": client_ip, "path": getattr(request.url, "path", "unknown") if request else "unknown"},
            status="FAILED"
        )
    except Exception:
        pass

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorized: Valid X-API-Key or Bearer JWT token required."
    )


