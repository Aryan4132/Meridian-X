import os
from typing import List, Dict, Any
from src.core.vault import save_secret, get_secret, load_all_secrets, VAULT_FILE

def _get_master_passphrase() -> str:
    key = os.environ.get("MERIDIAN_VAULT_KEY")
    if not key:
        raise EnvironmentError("MERIDIAN_VAULT_KEY environment variable is not set. Cannot access vault in secure mode.")
    return key

def vault_set(name: str, value: str) -> str:
    """Encrypt and store a secret in the vault."""
    passphrase = _get_master_passphrase()
    try:
        return save_secret(name, value, passphrase)
    except Exception as e:
        return f"Failed to store secret: {e}"

def vault_get(name: str) -> str:
    """Decrypt and return a secret value from the vault (for internal tool usage only)."""
    passphrase = _get_master_passphrase()
    val = get_secret(name, passphrase)
    if val is None:
        return f"Secret '{name}' not found."
    return val

def vault_list() -> str:
    """List all secret names in the vault (values are hidden)."""
    passphrase = _get_master_passphrase()
    if not os.path.exists(VAULT_FILE):
        return "Secrets vault is empty (no file found)."
    try:
        secrets = load_all_secrets(passphrase)
        if not secrets:
            return "Secrets vault is empty."
        return "Stored secrets in vault:\n" + "\n".join(f"- {k}" for k in secrets.keys())
    except Exception as e:
        return f"Failed to list secrets (possible wrong master key or corrupted vault): {e}"

def vault_delete(name: str) -> str:
    """Remove a secret from the vault."""
    passphrase = _get_master_passphrase()
    if not os.path.exists(VAULT_FILE):
        return "Secrets vault is empty."
    try:
        secrets = load_all_secrets(passphrase)
        if name in secrets:
            del secrets[name]
            # Re-save the remaining secrets
            import json
            import base64
            from cryptography.hazmat.primitives.ciphers.aead import AESGCM
            from src.core.vault import _derive_key
            
            data_bytes = json.dumps(secrets).encode('utf-8')
            salt = os.urandom(16)
            derived_key = _derive_key(passphrase, salt)
            
            aesgcm = AESGCM(derived_key)
            nonce = os.urandom(12)
            ciphertext = aesgcm.encrypt(nonce, data_bytes, None)
            
            payload = {
                "salt": base64.b64encode(salt).decode('utf-8'),
                "nonce": base64.b64encode(nonce).decode('utf-8'),
                "ciphertext": base64.b64encode(ciphertext).decode('utf-8')
            }
            with open(VAULT_FILE, "w", encoding="utf-8") as f:
                json.dump(payload, f)
            return f"Successfully deleted secret '{name}'."
        else:
            return f"Secret '{name}' not found in vault."
    except Exception as e:
        return f"Failed to delete secret: {e}"
