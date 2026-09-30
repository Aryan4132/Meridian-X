import os
import secrets
import hmac
import hashlib
from typing import Optional, Any, Union
from fastapi import Header, HTTPException, status, Depends, Request, WebSocket
from fastapi.security import APIKeyHeader

def compute_sha256(text: str) -> str:
    """Computes hex SHA-256 hash of a string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def verify_provided_token(provided_token: Optional[str]) -> bool:
    """
    Verifies an incoming auth token or API key against configured secrets.
    Supports matching raw MERIDIAN_API_KEY, custom passwords, or SHA-256 derived hashes.
    """
    if not provided_token:
        return False
    
    # 1. Match against primary API_KEY
    if hmac.compare_digest(provided_token, API_KEY):
        return True
    
    # 2. Match against SHA-256 hash of primary API_KEY
    if hmac.compare_digest(provided_token.lower(), compute_sha256(API_KEY).lower()):
        return True

    # 3. Check custom password env vars (MERIDIAN_PAIRING_PASSWORD / MERIDIAN_CUSTOM_PASSWORD)
    for env_var in ("MERIDIAN_PAIRING_PASSWORD", "MERIDIAN_CUSTOM_PASSWORD"):
        custom_pwd = os.getenv(env_var)
        if custom_pwd:
            if hmac.compare_digest(provided_token, custom_pwd):
                return True
            if hmac.compare_digest(provided_token.lower(), compute_sha256(custom_pwd).lower()):
                return True

    return False



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
from starlette.requests import HTTPConnection


def _is_loopback_request(request: Optional[HTTPConnection]) -> bool:
    """Allow same-machine desktop app traffic only when the TCP peer is actually loopback."""
    if request is None:
        return False

    client_host = getattr(getattr(request, "client", None), "host", "") or ""
    if client_host in {"127.0.0.1", "::1", "localhost", "testclient"}:
        origin = (request.headers.get("origin") or "").strip().lower()
        if not origin or origin.startswith((
            "http://localhost", "http://127.0.0.1", "http://[::1]",
            "https://localhost", "https://127.0.0.1",
            "tauri://localhost", "http://tauri.localhost",
            "testclient"
        )):
            return True
    return False


# --- Admin guard -------------------------------------------------------------
from fastapi import Header, HTTPException, Depends
import os

def require_admin(
    request: Request,
    admin_key: Optional[str] = Header(None, convert_underscores=False),
) -> bool:
    """Simple admin protection for privileged endpoints.
    Checks the optional ``X-Admin-Key`` (or ``admin_key`` header) against the
    ``MERIDIAN_ADMIN_KEY`` environment variable.  If the env var is not set the
    endpoint is considered unsecured (fallback to normal API‑key auth).
    """
    expected = os.getenv("MERIDIAN_ADMIN_KEY")
    if not expected:
        return True  # no admin key configured – allow
    if admin_key and admin_key == expected:
        return True
    raise HTTPException(status_code=403, detail="Admin credentials required")


# Role-based access control system
ROLES = {
    "admin": ["read", "write", "delete", "admin"],
    "user": ["read", "write"],
    "viewer": ["read"],
    "api": ["read", "write"]  # For service-to-service communication
}

# Permission mapping for endpoints
ENDPOINT_PERMISSIONS = {
    # Health and system endpoints (public)
    "/api/health": [],
    "/api/version": [],
    "/metrics": [],
    "/docs": [],
    "/redoc": [],
    "/openapi.json": [],
    
    # Auth endpoints (public or special handling)
    "/api/auth/oauth/": [],
    
    # Admin endpoints
    "/api/security/rotate-key": ["admin"],
    "/api/system/shutdown": ["admin"],
    "/api/system/trigger-update": ["admin"],
    
    # Chat endpoints
    "/api/chat": ["user", "api"],
    "/api/chat/stream": ["user", "api"],
    "/api/chat/clear": ["user", "api"],
    "/api/chat/history": ["user", "api"],
    "/api/chat/abort": ["user", "api"],
    "/api/chat/stop": ["user", "api"],
    
    # Voice endpoints
    "/api/voice/record": ["user", "api"],
    "/api/voice/interrupt": ["user", "api"],
    
    # RAG endpoints
    "/api/rag/ingest": ["user", "api"],
    "/api/rag/ingest-file": ["user", "api"],
    "/api/rag/ingest-files": ["user", "api"],
    "/api/rag/search": ["user", "api"],
    
    # System endpoints
    "/api/system-usage": ["user", "api"],
    "/api/onboarding/*": ["user", "api"],
    "/api/profile/*": ["user", "api"],
    
    # Default: require authentication for all other endpoints
}

def get_required_permission(path: str, method: str = "GET") -> list:
    """Determine required permission for an endpoint based on path and method."""
    # Check for exact match first
    if path in ENDPOINT_PERMISSIONS:
        return ENDPOINT_PERMISSIONS[path]
    
    # Check for wildcard matches
    for pattern, perms in ENDPOINT_PERMISSIONS.items():
        if "*" in pattern:
            # Simple wildcard matching (can be enhanced)
            prefix = pattern.replace("*", "")
            if path.startswith(prefix):
                return perms
    
    # Default to requiring authenticated user for protected endpoints
    if path.startswith("/api/"):
        return ["user"]
    
    return []  # Public endpoint

def has_permission(user_roles: list, required_permissions: list) -> bool:
    """Check if user roles have the required permissions."""
    if not required_permissions:  # No permissions required (public endpoint)
        return True
    
    # Flatten user permissions
    user_permissions = set()
    for role in user_roles:
        if role in ROLES:
            user_permissions.update(ROLES[role])
    
    # Check if user has at least one of the required permissions
    return bool(user_permissions.intersection(set(required_permissions)))

def require_permission(permissions: list):
    """Dependency factory for requiring specific permissions."""
    def permission_checker(
        request: Request,
        current_user_roles: list = Depends(get_user_roles_from_request)
    ):
        if not has_permission(current_user_roles, permissions):
            from fastapi import HTTPException, status
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Insufficient permissions. Required: {permissions}"
            )
        return True
    return permission_checker

def get_user_roles_from_request(request: Request) -> list:
    """Extract user roles from request (simplified implementation)."""
    # In a real implementation, this would decode JWT token or session
    # For now, we'll check headers or fall back to default
    if request is None:
        return ["viewer"]  # Default role
    
    # Try to get roles from header (for demo/testing)
    roles_header = request.headers.get("X-User-Roles")
    if roles_header:
        try:
            import json
            roles = json.loads(roles_header)
            if isinstance(roles, list):
                return roles
        except Exception:
            pass
    
    # Fallback to checking user profile or default
    # In reality, this would come from authenticated user data
    return ["viewer"]  # Default role


async def require_api_key(
    request: HTTPConnection,
):
    """
    FastAPI route dependency supporting Dual Auth.
    """
    req = request
    if os.getenv("DISABLE_AUTH") == "true":
        return True

    if req is not None and getattr(req, "scope", {}).get("type") == "websocket":
        return True

    if req is not None and hasattr(req, "url"):
        path = req.url.path
        if path in ("/api/health", "/docs", "/redoc", "/openapi.json", "/api/network/endpoints", "/ws") or path.startswith(("/api/auth/oauth", "/api/ws")):
            return True

    if req is not None and _is_loopback_request(req):
        return True

    client_ip = getattr(getattr(req, "client", None), "host", "unknown") if req else "unknown"

    # 1. Check for Authorization: Bearer <jwt_token>
    auth_header = req.headers.get("Authorization") if req and hasattr(req, "headers") else None
    if auth_header and auth_header.startswith("Bearer "):
        bearer_token = auth_header.split(" ", 1)[1].strip()
        from src.core.oauth_manager import decode_jwt_token
        decoded = decode_jwt_token(bearer_token)
        if decoded:
            return True

    # 2. Check X-API-Key header or query parameter
    api_key_header = req.headers.get("X-API-Key") if req and hasattr(req, "headers") else None
    if not api_key_header and req and hasattr(req, "query_params"):
        api_key_header = req.query_params.get("token") or req.query_params.get("apiKey")
    if api_key_header and verify_provided_token(api_key_header):
        return True

    # Auth failed
    try:
        from src.core.audit_logger import log_sensitive_action
        log_sensitive_action(
            category="AUTH_FAILURE",
            action="require_api_key",
            details={"reason": "Missing or invalid auth credential", "ip": client_ip, "path": getattr(req.url, "path", "unknown") if req and hasattr(req, "url") else "unknown"},
            status="FAILED"
        )
    except Exception:
        pass

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorized: Valid X-API-Key or Bearer JWT token required."
    )


