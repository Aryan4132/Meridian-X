"""P2P encrypted payload + challenge-response authentication.

Split from ``src.core.p2p`` (Phase 2 god-file refactor). Pure move —
zero behavior changes. ``p2p.py`` re-exports every symbol so existing
imports (``from src.core.p2p import ...``) keep working.
"""

import hashlib
import os
import socket


def _encrypt_payload(data_str: str, token: str) -> bytes:
    if not token:
        return data_str.encode('utf-8')
    import base64
    import hashlib
    from cryptography.fernet import Fernet
    h = hashlib.sha256(token.encode('utf-8')).digest()
    key = base64.urlsafe_b64encode(h)
    f = Fernet(key)
    return f.encrypt(data_str.encode('utf-8'))


def _bootstrap_p2p_token() -> str:
    """Ensure P2P_SECRET_TOKEN exists; generate + persist one if missing (SEC-FIX).

    Previously an empty token silently disabled payload encryption, making all
    P2P sync plaintext and unauthenticated. Tokens now always exist so the
    Fernet path is active by default (fail closed).
    """
    token = os.environ.get("P2P_SECRET_TOKEN", "")
    if token:
        return token
    try:
        from src.core.history_manager import find_workspace_root
        env_path = os.path.join(find_workspace_root(), ".env")
    except Exception:
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        root_dir = os.path.dirname(backend_dir)
        env_path = os.path.join(root_dir, ".env")

    if os.path.exists(env_path):
        try:
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("P2P_SECRET_TOKEN="):
                        token = line.split("=", 1)[1].strip()
                        break
        except Exception as e:
            print(f"[P2P Sync] Failed reading .env for P2P_SECRET_TOKEN: {e}")

    if not token:
        import secrets as _secrets
        token = _secrets.token_hex(32)
        try:
            mode = "a" if os.path.exists(env_path) else "w"
            with open(env_path, mode, encoding="utf-8") as f:
                if mode == "a":
                    f.write("\n")
                f.write(f"P2P_SECRET_TOKEN={token}\n")
            print("[P2P Sync] Generated new P2P_SECRET_TOKEN and persisted it to .env")
        except Exception as e:
            print(f"[P2P Sync] Failed to persist generated P2P_SECRET_TOKEN: {e}")

    os.environ["P2P_SECRET_TOKEN"] = token
    return token


def authenticate_p2p_peer_challenge(peer_ip: str, peer_port: int, shared_secret: str = "", timeout: float = 4.0) -> bool:
    """Real HMAC challenge-response handshake for P2P peer authentication (SEC-12).

    SEC-FIX: the previous implementation logged and returned True unconditionally,
    providing zero authentication. This version opens a TCP connection to the peer,
    sends a random nonce, and requires the peer to respond with
    ``MERIDIAN_AUTH:<hex hmac>`` computed over the nonce using the shared secret.
    Verification uses a constant-time comparison.
    """
    import hmac as hmac_mod
    import secrets as _secrets

    secret = shared_secret or os.environ.get("P2P_SECRET_TOKEN", "") or _bootstrap_p2p_token()
    if not secret:
        # Fail closed: no shared secret means no authentication is possible.
        return False

    nonce = _secrets.token_hex(16)
    expected = hmac_mod.new(secret.encode("utf-8"), nonce.encode("utf-8"), hashlib.sha256).hexdigest()

    sock = None
    try:
        from src.core.audit_logger import log_sensitive_action
        sock = socket.create_connection((peer_ip, peer_port), timeout=timeout)
        sock.settimeout(timeout)

        sock.sendall(f"MERIDIAN_CHALLENGE:{nonce}".encode("utf-8"))

        chunks = []
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)
            if b"\n" in chunk or sum(len(c) for c in chunks) > 4096:
                break
        response = b"".join(chunks).decode("utf-8", errors="replace").strip()
        if not response.startswith("MERIDIAN_AUTH:"):
            log_sensitive_action("P2P_AUTH", "peer_challenge", {"peer_ip": peer_ip, "peer_port": peer_port}, "FAILED")
            return False
        provided = response.split(":", 1)[1].strip().lower()
        ok = hmac_mod.compare_digest(provided, expected)
        log_sensitive_action(
            "P2P_AUTH", "peer_challenge",
            {"peer_ip": peer_ip, "peer_port": peer_port},
            "SUCCESS" if ok else "FAILED",
        )
        return ok
    except Exception as e:
        print(f"[P2P Auth] Challenge handshake with {peer_ip}:{peer_port} failed: {e}")
        try:
            from src.core.audit_logger import log_sensitive_action
            log_sensitive_action("P2P_AUTH", "peer_challenge", {"peer_ip": peer_ip, "peer_port": peer_port}, "FAILED")
        except Exception:
            pass
        return False
    finally:
        if sock:
            try:
                sock.close()
            except Exception:
                pass


def respond_p2p_peer_challenge(nonce: str, shared_secret: str = "") -> str:
    """Compute the HMAC response proving knowledge of the shared secret."""
    import hmac as hmac_mod
    secret = shared_secret or os.environ.get("P2P_SECRET_TOKEN", "") or _bootstrap_p2p_token()
    return hmac_mod.new(secret.encode("utf-8"), nonce.encode("utf-8"), hashlib.sha256).hexdigest()


def _decrypt_payload(data_bytes: bytes, token: str) -> str:
    if not token:
        return data_bytes.decode('utf-8')
    import base64
    import hashlib
    from cryptography.fernet import Fernet
    h = hashlib.sha256(token.encode('utf-8')).digest()
    key = base64.urlsafe_b64encode(h)
    f = Fernet(key)
    return f.decrypt(data_bytes).decode('utf-8')
