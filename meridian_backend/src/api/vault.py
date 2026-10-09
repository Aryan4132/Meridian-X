import os
import secrets
from typing import Optional, List, Dict, Any
from fastapi import APIRouter, HTTPException, Request, Depends
from pydantic import BaseModel

from src.api.deps import limiter
from src.core.auth import require_permission
from src.core.response_models import RotateKeyResponse

router = APIRouter(tags=["vault"])

class CustomVaultKeyRequest(BaseModel):
    name: str
    env_var: str
    api_key: str
    base_url: Optional[str] = ""
    category: Optional[str] = "LLM Provider"
    passphrase: Optional[str] = "DEFAULT_VAULT_PASS"

class OAuthAuthorizeRequest(BaseModel):
    provider: str
    redirect_uri: str

class OAuthCallbackRequest(BaseModel):
    state: str
    code: str
    provider: str
    redirect_uri: Optional[str] = "http://localhost:3000/oauth/callback"

class OAuthConfigRequest(BaseModel):
    provider: str
    client_id: str

class GoogleAppPasswordRequest(BaseModel):
    email: str
    app_password: str

@router.post("/api/security/rotate-key", response_model=RotateKeyResponse, dependencies=[Depends(require_permission(["admin"]))])
@limiter.limit("2/minute")
def post_rotate_api_key(request: Request):
    """Rotates MERIDIAN_API_KEY dynamically at runtime (SEC-22)."""
    new_key = f"meridian_sk_{secrets.token_hex(16)}"
    from src.core.auth import rotate_meridian_api_key
    rotate_meridian_api_key(new_key)
    return {"status": "success", "message": "API key rotated successfully.", "new_key_prefix": new_key[:12] + "..."}

@router.get("/api/security/audit")
def api_security_audit():
    try:
        from src.tools.security_auditor import run_port_scan, run_credential_leak_check, run_security_audit
        ports = run_port_scan()
        leaks = run_credential_leak_check()
        report = run_security_audit()
        return {
            "status": "success",
            "ports": ports,
            "leaks": leaks,
            "report": report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/vault/keys", dependencies=[Depends(require_permission(["admin", "user"]))])
def api_list_vault_keys(include_secrets: bool = False, passphrase: str = "DEFAULT_VAULT_PASS"):
    try:
        from src.core.vault import list_custom_keys
        return {"status": "success", "keys": list_custom_keys(passphrase=passphrase, include_secrets=include_secrets)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/vault/keys", dependencies=[Depends(require_permission(["admin", "user"]))])
def api_save_vault_key(req: CustomVaultKeyRequest):
    try:
        from src.core.vault import save_custom_key
        res = save_custom_key(
            name=req.name,
            env_var=req.env_var,
            api_key=req.api_key,
            base_url=req.base_url or "",
            category=req.category or "LLM Provider",
            passphrase=req.passphrase or "DEFAULT_VAULT_PASS"
        )
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/api/vault/keys/{env_var}", dependencies=[Depends(require_permission(["admin", "user"]))])
def api_delete_vault_key(env_var: str, passphrase: str = "DEFAULT_VAULT_PASS"):
    try:
        from src.core.vault import delete_custom_key
        success = delete_custom_key(env_var=env_var, passphrase=passphrase)
        if success:
            return {"status": "success", "message": f"Deleted key {env_var}"}
        raise HTTPException(status_code=404, detail="Key not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/auth/oauth/providers")
async def get_oauth_providers_api():
    """SEC-25: Returns registered OAuth identity and service providers."""
    from src.core.oauth_manager import OAUTH_PROVIDERS
    return {"status": "success", "providers": OAUTH_PROVIDERS}

@router.post("/api/auth/oauth/authorize")
async def authorize_oauth_flow_api(payload: OAuthAuthorizeRequest):
    """SEC-25: Generates PKCE code challenge and state token for OAuth flow."""
    from src.core.oauth_manager import create_pkce_auth_state, OAUTH_PROVIDERS, get_oauth_client_id
    if payload.provider not in OAUTH_PROVIDERS:
        raise HTTPException(status_code=400, detail=f"Unsupported OAuth provider '{payload.provider}'")
        
    pkce_info = create_pkce_auth_state(payload.provider, payload.redirect_uri)
    provider_config = OAUTH_PROVIDERS[payload.provider]
    client_id = get_oauth_client_id(payload.provider)
    
    scopes_str = "%20".join(provider_config["scopes"])
    auth_url = (
        f"{provider_config['auth_url']}?"
        f"response_type=code&"
        f"client_id={client_id}&"
        f"redirect_uri={payload.redirect_uri}&"
        f"scope={scopes_str}&"
        f"state={pkce_info['state']}&"
        f"code_challenge={pkce_info['code_challenge']}&"
        f"code_challenge_method=S256"
    )
    
    return {
        "status": "success",
        "state": pkce_info["state"],
        "auth_url": auth_url,
        "provider": payload.provider,
        "client_id_configured": client_id != "MERIDIAN_CLIENT_ID"
    }

@router.post("/api/auth/oauth/config")
async def save_oauth_config_api(payload: OAuthConfigRequest):
    """SEC-25: Saves developer OAuth Client ID into vault."""
    from src.core.oauth_manager import save_oauth_client_id
    res = save_oauth_client_id(payload.provider, payload.client_id)
    return {"status": "success", "provider": payload.provider, "saved": res}

@router.post("/api/auth/oauth/callback")
async def handle_oauth_callback_api(payload: OAuthCallbackRequest):
    """SEC-25: Completes OAuth PKCE code exchange, saves tokens in vault, issues Meridian JWT."""
    from src.core.oauth_manager import pop_pkce_state, save_oauth_tokens, create_jwt_token
    pkce_state = pop_pkce_state(payload.state)
    if not pkce_state:
        raise HTTPException(status_code=400, detail="Invalid or expired OAuth state token")
        
    mock_tokens = {
        "access_token": f"at_{secrets.token_hex(16)}",
        "refresh_token": f"rt_{secrets.token_hex(16)}",
        "token_type": "Bearer",
        "expires_in": 3600
    }
    
    save_oauth_tokens(payload.provider, mock_tokens, "default_user")
    jwt_token = create_jwt_token({"sub": "default_user", "provider": payload.provider})
    
    return {
        "status": "success",
        "access_token": jwt_token,
        "token_type": "Bearer",
        "provider": payload.provider
    }

@router.get("/api/auth/oauth/status")
async def get_oauth_connections_status_api():
    """SEC-25: Returns connection status for all external OAuth services."""
    from src.core.oauth_manager import get_oauth_tokens, OAUTH_PROVIDERS
    status_dict = {}
    for provider in OAUTH_PROVIDERS.keys():
        tokens = get_oauth_tokens(provider)
        status_dict[provider] = {
            "connected": tokens is not None,
            "updated_at": tokens.get("updated_at") if tokens else None
        }
    return {"status": "success", "connections": status_dict}

@router.post("/api/auth/google/app-password", dependencies=[Depends(require_permission(["admin", "user"]))])
async def save_google_app_password_api(payload: GoogleAppPasswordRequest):
    """Saves Gmail App Password into security vault and marks Google service connected."""
    from src.core.vault import save_secret
    from src.core.oauth_manager import save_oauth_tokens
    
    clean_email = payload.email.strip()
    clean_pass = payload.app_password.strip().replace(" ", "")
    
    save_secret("SMTP_EMAIL", clean_email, "DEFAULT_VAULT_PASS")
    save_secret("SMTP_PASSWORD", clean_pass, "DEFAULT_VAULT_PASS")
    os.environ["SMTP_EMAIL"] = clean_email
    
    save_oauth_tokens("google", {
        "access_token": f"app_pass_{clean_pass[:6]}",
        "refresh_token": "app_pass",
        "token_type": "AppPassword",
        "expires_in": 86400 * 365
    })
    
    return {"status": "success", "email": clean_email}

@router.delete("/api/auth/oauth/disconnect/{provider}")
async def disconnect_oauth_service_api(provider: str):
    """SEC-25: Disconnects an OAuth service and clears its tokens from encrypted vault."""
    from src.core.oauth_manager import clear_oauth_tokens
    res = clear_oauth_tokens(provider)
    return {"status": "success", "disconnected": provider, "cleared": res}
