"""LLM credential resolution + secret redaction (SEC-11).

Split from ``src.core.llm_provider`` (Phase 2 god-file refactor). Leaf
module — imports nothing from sibling LLM modules, so it can be safely
imported anywhere. ``llm_provider.py`` re-exports every symbol so existing
imports keep working.
"""

import logging
import os
import re
from typing import Optional

logger = logging.getLogger("meridian_llm_provider")

SECRET_REGEX_PATTERNS = [
    re.compile(r"sk-[a-zA-Z0-9]{32,}"),
    re.compile(r"sk-ant-[a-zA-Z0-9_\-]{20,}"),
    re.compile(r"AIzaSy[a-zA-Z0-9_\-]{30,}"),
    re.compile(r"hf_[a-zA-Z0-9]{34,}"),
    re.compile(r"ghp_[a-zA-Z0-9]{36}"),
    re.compile(r"github_pat_[a-zA-Z0-9_]{80,}"),
    re.compile(r"eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}"),
]


def scan_and_redact_secrets(text: str) -> str:
    """Scans and redacts high-entropy API keys and tokens before sending to LLM APIs (SEC-11)."""
    if not text:
        return text

    try:
        from src.core.audit_logger import log_sensitive_action
    except ImportError:
        log_sensitive_action = None

    redacted_text = text
    redacted_count = 0
    for pattern in SECRET_REGEX_PATTERNS:
        matches = pattern.findall(redacted_text)
        for match in matches:
            redacted_text = redacted_text.replace(match, "[REDACTED_SECRET]")
            redacted_count += 1

    if redacted_count > 0 and log_sensitive_action:
        log_sensitive_action("SECURITY_AUDIT", "secret_redacted", {"secret_type": "high_entropy_token", "count": redacted_count}, "SUCCESS")

    return redacted_text


def get_ollama_host() -> str:
    """Retrieves the normalized Ollama host URL."""
    try:
        from database import get_ollama_client_host
        return get_ollama_client_host()
    except Exception:
        host = os.getenv("OLLAMA_HOST")
        if not host:
            host = "http://localhost:11434"
        if host == "0.0.0.0":
            return "http://127.0.0.1:11434"
        if host.startswith("0.0.0.0:"):
            return f"http://127.0.0.1:{host.split(':')[1]}"
        if "0.0.0.0" in host:
            return host.replace("0.0.0.0", "127.0.0.1")
        if not host.startswith("http://") and not host.startswith("https://"):
            return f"http://{host}"
        return host


def get_api_key(provider: str) -> Optional[str]:
    """Retrieves the API key for a provider."""
    try:
        from src.core.vault import vault_get
        key = vault_get(f"{provider.lower()}_key") or vault_get(f"{provider.upper()}_API_KEY")
        if key:
            return key
    except Exception:
        pass

    env_name = f"{provider.upper()}_API_KEY"
    key = os.getenv(env_name)
    if key:
        return key

    try:
        from database import get_user_profile
        profile_key = f"{provider.lower()}_key"
        val = get_user_profile(profile_key)
        if val is not None and val != "":
            return val
    except Exception as e:
        logger.debug(f"Failed to fetch {provider} key from database profile: {e}")

    return None
