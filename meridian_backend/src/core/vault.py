import os
import json
import base64
from typing import Dict, Any, Optional
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# Key derivation
def _derive_key(passphrase: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    return kdf.derive(passphrase.encode())

# Path mapping for vault file in root
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_dir = os.path.dirname(backend_dir)
VAULT_FILE = os.path.join(root_dir, "vault.enc")

def save_secret(key: str, value: str, passphrase: str) -> str:
    # 1. Load existing secrets if vault file exists
    secrets = {}
    if os.path.exists(VAULT_FILE):
        try:
            secrets = load_all_secrets(passphrase)
        except Exception:
            # If wrong password or corrupt, initialize new
            pass
            
    secrets[key] = value
    
    # 2. Encrypt all secrets
    data_bytes = json.dumps(secrets).encode('utf-8')
    salt = os.urandom(16)
    derived_key = _derive_key(passphrase, salt)
    
    aesgcm = AESGCM(derived_key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, data_bytes, None)
    
    # 3. Store payload: salt + nonce + ciphertext
    payload = {
        "salt": base64.b64encode(salt).decode('utf-8'),
        "nonce": base64.b64encode(nonce).decode('utf-8'),
        "ciphertext": base64.b64encode(ciphertext).decode('utf-8')
    }
    
    with open(VAULT_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f)
        
    return f"Successfully saved secret key '{key}' in encrypted vault."

def get_secret(key: str, passphrase: str) -> Optional[str]:
    try:
        secrets = load_all_secrets(passphrase)
        return secrets.get(key)
    except Exception:
        return None

def load_all_secrets(passphrase: str) -> Dict[str, str]:
    if not os.path.exists(VAULT_FILE):
        return {}
        
    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        payload = json.load(f)
        
    salt = base64.b64decode(payload["salt"])
    nonce = base64.b64decode(payload["nonce"])
    ciphertext = base64.b64decode(payload["ciphertext"])
    
    derived_key = _derive_key(passphrase, salt)
    aesgcm = AESGCM(derived_key)
    
    decrypted_bytes = aesgcm.decrypt(nonce, ciphertext, None)
    return json.loads(decrypted_bytes.decode('utf-8'))
