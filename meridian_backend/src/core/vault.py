import os
import json
import base64
import time as _time
import hashlib
import threading
from typing import Dict, Optional
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# ---------------------------------------------------------------------------
# Key Derivation
# ---------------------------------------------------------------------------
def _derive_key(passphrase: str, salt: bytes) -> bytes:
    """Derive a 32-byte AES key from a passphrase + salt using PBKDF2-HMAC-SHA256."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    return kdf.derive(passphrase.encode())

# ---------------------------------------------------------------------------
# Passphrase Key Cache — 5-minute TTL, per-passphrase-hash, thread-safe
# Improvement: passphrase derivation (PBKDF2, 100k iterations) is expensive.
# Cache the derived key in memory for 5 minutes so repeated vault_get calls
# within a session don't re-derive on every request.
# ---------------------------------------------------------------------------
_cache_lock = threading.Lock()
# Stores: {pass_hash: (derived_key, expires_at)}
_key_cache: Dict[str, tuple] = {}
_CACHE_TTL = 300  # 5 minutes


def _get_or_derive_key(passphrase: str, salt: bytes) -> bytes:
    """Return the cached derived key for this passphrase if still valid, else re-derive."""
    pass_hash = hashlib.sha256(passphrase.encode()).hexdigest()
    with _cache_lock:
        entry = _key_cache.get(pass_hash)
        if entry is not None:
            dk, expires_at = entry
            if _time.time() < expires_at:
                return dk
        # Cache miss or expired — derive fresh key
        dk = _derive_key(passphrase, salt)
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

    # 2. Encrypt all secrets with a freshly generated salt
    data_bytes = json.dumps(secrets).encode("utf-8")
    salt = os.urandom(16)
    derived_key = _derive_key(passphrase, salt)  # always fresh on write

    aesgcm = AESGCM(derived_key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, data_bytes, None)

    # 3. Persist
    payload = {
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

    # Use the cache to avoid repeated PBKDF2 derivation in the same session
    derived_key = _get_or_derive_key(passphrase, salt)
    aesgcm = AESGCM(derived_key)

    decrypted_bytes = aesgcm.decrypt(nonce, ciphertext, None)
    return json.loads(decrypted_bytes.decode("utf-8"))
