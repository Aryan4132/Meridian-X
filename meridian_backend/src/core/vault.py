import os
import json
import base64
import time as _time
import hashlib
import threading
from typing import Dict, Optional, List, Any
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# ---------------------------------------------------------------------------
# Key Derivation
# ---------------------------------------------------------------------------
def _derive_key(passphrase: str, salt: bytes, kdf_type: str = "argon2id") -> bytes:
    """Derive a 32-byte AES key using Argon2id (with legacy PBKDF2 fallback)."""
    if kdf_type == "pbkdf2":
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        return kdf.derive(passphrase.encode())

    try:
        from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
        kdf = Argon2id(
            salt=salt,
            length=32,
            iterations=2,
            memory_cost=65536,
            lanes=4
        )
        return kdf.derive(passphrase.encode())
    except Exception:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        return kdf.derive(passphrase.encode())

# ---------------------------------------------------------------------------
# Passphrase Key Cache — 5-minute TTL, per-passphrase-hash, thread-safe
# Cache derived key in memory for 5 minutes so repeated vault_get calls
# within a session don't re-derive on every request.
# ---------------------------------------------------------------------------
_cache_lock = threading.Lock()
# Stores: {cache_key: (derived_key, expires_at)}
_key_cache: Dict[str, tuple] = {}
_CACHE_TTL = 300  # 5 minutes


def _get_or_derive_key(passphrase: str, salt: bytes, kdf_type: str = "argon2id") -> bytes:
    """Return the cached derived key for this passphrase if still valid, else re-derive."""
    pass_hash = hashlib.sha256(f"{passphrase}:{kdf_type}:{salt.hex()}".encode()).hexdigest()
    with _cache_lock:
        entry = _key_cache.get(pass_hash)
        if entry is not None:
            dk, expires_at = entry
            if _time.time() < expires_at:
                return dk
        # Cache miss or expired — derive fresh key
        dk = _derive_key(passphrase, salt, kdf_type=kdf_type)
        _key_cache[pass_hash] = (dk, _time.time() + _CACHE_TTL)
        return dk


def _invalidate_key_cache() -> None:
    """Evict all cached keys (called on vault write since a new salt is generated)."""
    with _cache_lock:
        _key_cache.clear()


# ---------------------------------------------------------------------------
# Audit Logging
# ---------------------------------------------------------------------------
def _audit(action: str, key_name: str, status: str = "SUCCESS") -> None:
    """Write vault access event to audit log without blocking the caller."""
    try:
        from src.core.audit_logger import log_sensitive_action
        log_sensitive_action(
            category="VAULT_ACCESS",
            action=action,
            details={"key_name": key_name},
            status=status,
        )
    except Exception:
        pass


# ---------------------------------------------------------------------------
# Vault File Path
# ---------------------------------------------------------------------------
from src.core.config import VAULT_FILE


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
def save_secret(key: str, value: str, passphrase: str) -> str:
    """Encrypt and persist a secret into the vault."""
    # 1. Load existing secrets if vault file exists
    secrets: Dict[str, str] = {}
    if os.path.exists(VAULT_FILE):
        is_valid_json = False
        try:
            with open(VAULT_FILE, "r", encoding="utf-8") as f:
                payload = json.load(f)
            if isinstance(payload, dict) and "salt" in payload and "nonce" in payload and "ciphertext" in payload:
                is_valid_json = True
        except Exception:
            pass

        if is_valid_json:
            try:
                secrets = load_all_secrets(passphrase)
            except Exception as e:
                _audit("vault_set", key, "FAILED")
                raise ValueError("Decryption failed. The master passphrase may be incorrect or the vault is corrupted.") from e

    secrets[key] = value

    # 2. Encrypt all secrets with a freshly generated salt and Argon2id KDF
    data_bytes = json.dumps(secrets).encode("utf-8")
    salt = os.urandom(16)
    kdf_type = "argon2id"
    derived_key = _derive_key(passphrase, salt, kdf_type=kdf_type)  # always fresh on write

    aesgcm = AESGCM(derived_key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, data_bytes, None)

    # 3. Persist
    payload = {
        "kdf": kdf_type,
        "salt": base64.b64encode(salt).decode("utf-8"),
        "nonce": base64.b64encode(nonce).decode("utf-8"),
        "ciphertext": base64.b64encode(ciphertext).decode("utf-8"),
    }
    with open(VAULT_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f)

    # Invalidate cache — salt changed, old derived keys are useless
    _invalidate_key_cache()
    _audit("vault_set", key)
    return f"Successfully saved secret key '{key}' in encrypted vault."


def get_secret(key: str, passphrase: str) -> Optional[str]:
    """Decrypt vault and return the value for `key`, or None if missing."""
    _audit("vault_get", key)
    try:
        secrets = load_all_secrets(passphrase)
        return secrets.get(key)
    except Exception:
        return None


def load_all_secrets(passphrase: str) -> Dict[str, str]:
    """Decrypt and return all secrets from the vault file."""
    if not os.path.exists(VAULT_FILE):
        return {}

    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        payload = json.load(f)

    salt = base64.b64decode(payload["salt"])
    nonce = base64.b64decode(payload["nonce"])
    ciphertext = base64.b64decode(payload["ciphertext"])
    kdf_type = payload.get("kdf", "pbkdf2")

    # Use the cache to avoid repeated key derivation in the same session
    derived_key = _get_or_derive_key(passphrase, salt, kdf_type=kdf_type)
    aesgcm = AESGCM(derived_key)

    decrypted_bytes = aesgcm.decrypt(nonce, ciphertext, None)
    return json.loads(decrypted_bytes.decode("utf-8"))


# ---------------------------------------------------------------------------
# Dynamic Custom API Key Vault Metadata Manager
# ---------------------------------------------------------------------------
def save_custom_key(
    name: str,
    env_var: str,
    api_key: str,
    base_url: str = "",
    category: str = "LLM Provider",
    passphrase: str = "DEFAULT_VAULT_PASS"
) -> Dict[str, Any]:
    """Saves a structured custom API key entry into the encrypted vault."""
    env_var_clean = env_var.strip().upper()
    keys_metadata = get_custom_keys_dict(passphrase)
    
    keys_metadata[env_var_clean] = {
        "name": name.strip(),
        "env_var": env_var_clean,
        "api_key": api_key.strip(),
        "base_url": base_url.strip(),
        "category": category.strip(),
        "updated_at": _time.time()
    }
    
    save_secret("__CUSTOM_KEYS_METADATA__", json.dumps(keys_metadata), passphrase)
    # Automatically inject into active environment
    os.environ[env_var_clean] = api_key.strip()
    if base_url.strip():
        os.environ[f"{env_var_clean}_BASE_URL"] = base_url.strip()
        
    return {"status": "success", "env_var": env_var_clean, "name": name}


def get_custom_keys_dict(passphrase: str = "DEFAULT_VAULT_PASS") -> Dict[str, Dict[str, Any]]:
    """Returns the internal dictionary of custom API key entries."""
    raw_json = get_secret("__CUSTOM_KEYS_METADATA__", passphrase)
    if not raw_json:
        return {}
    try:
        return json.loads(raw_json)
    except Exception:
        return {}


def list_custom_keys(passphrase: str = "DEFAULT_VAULT_PASS", include_secrets: bool = False) -> List[Dict[str, Any]]:
    """Lists registered custom API key entries, optionally masking raw key strings."""
    keys_dict = get_custom_keys_dict(passphrase)
    result = []
    for env_var, meta in keys_dict.items():
        raw_key = meta.get("api_key", "")
        masked_key = (raw_key[:4] + "••••••••" + raw_key[-4:]) if len(raw_key) > 8 else "••••••••"
        result.append({
            "name": meta.get("name", env_var),
            "env_var": env_var,
            "api_key": raw_key if include_secrets else masked_key,
            "base_url": meta.get("base_url", ""),
            "category": meta.get("category", "LLM Provider"),
            "updated_at": meta.get("updated_at", 0)
        })
    return result


def delete_custom_key(env_var: str, passphrase: str = "DEFAULT_VAULT_PASS") -> bool:
    """Deletes a custom key entry from the encrypted vault."""
    env_var_clean = env_var.strip().upper()
    keys_dict = get_custom_keys_dict(passphrase)
    if env_var_clean in keys_dict:
        keys_dict.pop(env_var_clean, None)
        save_secret("__CUSTOM_KEYS_METADATA__", json.dumps(keys_dict), passphrase)
        os.environ.pop(env_var_clean, None)
        os.environ.pop(f"{env_var_clean}_BASE_URL", None)
        return True
    return False


def inject_vault_keys_to_env(passphrase: str = "DEFAULT_VAULT_PASS") -> None:
    """Injects all vault-saved API keys into os.environ on backend startup."""
    try:
        keys_dict = get_custom_keys_dict(passphrase)
        for env_var, meta in keys_dict.items():
            if meta.get("api_key"):
                os.environ[env_var] = meta["api_key"]
            if meta.get("base_url"):
                os.environ[f"{env_var}_BASE_URL"] = meta["base_url"]
    except Exception as e:
        _audit("inject_vault_keys", "FAILED")

