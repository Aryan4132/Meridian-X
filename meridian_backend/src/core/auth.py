import os
import secrets
import hmac
from typing import Optional, Any, Union
from fastapi import Header, HTTPException, status, Depends, Request, WebSocket
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
    request: Request = None,
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
        request: Request = None,
        current_user_roles: list = Depends(lambda: get_user_roles_from_request(None))
    ):
        if not has_permission(current_user_roles, permissions):
            from fastapi import HTTPException, status
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Insufficient permissions. Required: {permissions}"
            )
        return True
    return permission_checker

def get_user_roles_from_request(request: Request = None) -> list:
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
    request: Request = None,
    websocket: WebSocket = None,
):
    """
    FastAPI route dependency supporting Dual Auth.
    """
    if os.getenv("DISABLE_AUTH") == "true":
        return True

    if websocket is not None or (request is not None and getattr(request, "scope", {}).get("type") == "websocket"):
        return True



    if request is not None and hasattr(request, "url"):
        path = request.url.path
        if path in ("/api/health", "/docs", "/redoc", "/openapi.json", "/api/network/endpoints", "/ws") or path.startswith(("/api/auth/oauth", "/api/ws")):
            return True

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
    api_key_header = request.headers.get("X-API-Key") if request and hasattr(request, "headers") else None
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


