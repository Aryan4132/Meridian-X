"""
Built-in TOTP 2FA Generator (SEC-32)
RFC-6238 time-based 2FA token generator integrated with encrypted vault storage.
"""

import time
import hmac
import hashlib
import struct
import base64
from typing import Dict, Any

def generate_totp_code(secret_b32: str, time_step: int = 30, digits: int = 6) -> str:
    """
    Generate an RFC-6238 TOTP 2FA passcode from a base32 encoded secret.
    """
    try:
        # Normalize and decode base32 secret
        secret_clean = secret_b32.strip().replace(" ", "").upper()
        # Add padding if required
        missing_padding = len(secret_clean) % 8
        if missing_padding:
            secret_clean += "=" * (8 - missing_padding)
        key = base64.b32decode(secret_clean, casefold=True)

        counter = int(time.time() // time_step)
        counter_bytes = struct.pack(">Q", counter)

        hmac_digest = hmac.new(key, counter_bytes, hashlib.sha1).digest()
        offset = hmac_digest[-1] & 0x0F
        binary_code = struct.unpack(">I", hmac_digest[offset:offset+4])[0] & 0x7FFFFFFF

        otp = str(binary_code % (10 ** digits)).zfill(digits)
        seconds_remaining = time_step - int(time.time() % time_step)
        
        return f"🔐 TOTP 2FA Code: {otp[:3]} {otp[3:]} (Expires in {seconds_remaining}s)"
    except Exception as e:
        return f"Error generating TOTP code: {e}"
