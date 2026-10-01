"""P2P mobile companion manual pairing helpers (ECO-01).

Split from ``src.core.p2p`` (Phase 2 god-file refactor). Pure move —
zero behavior changes. ``p2p.py`` re-exports every symbol so existing
imports keep working.
"""

import hmac
import os
import socket
import time
from typing import Any, Dict

from src.core.p2p_crypto import _bootstrap_p2p_token


def get_manual_pairing_info() -> Dict[str, Any]:
    """ECO-01: Returns manual pairing connection details for the Meridian
    Mobile companion app (host/port only — the secret is never exposed here;
    it is entered manually and verified via verify_mobile_pairing_secret)."""
    from src.core.p2p import P2P_PORT
    host_ip = "127.0.0.1"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host_ip = s.getsockname()[0]
        s.close()
    except Exception:
        pass

    return {
        "version": "1.0",
        "app": "Meridian-X",
        "host": host_ip,
        "port": P2P_PORT,
        "timestamp": time.time()
    }


def verify_mobile_pairing_secret(secret: str) -> bool:
    """ECO-01: Validates mobile client pairing secret against host P2P_SECRET_TOKEN."""
    expected_token = os.environ.get("P2P_SECRET_TOKEN", "") or _bootstrap_p2p_token()
    if not secret or not expected_token:
        return False
    return hmac.compare_digest(secret.strip(), expected_token.strip())
