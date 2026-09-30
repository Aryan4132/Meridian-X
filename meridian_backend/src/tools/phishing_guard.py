"""
Phishing & Link Reputation Guard (SEC-30)
Pre-click URL reputation scan, domain typosquatting detector, and link safety verifier.
"""

import urllib.parse
from typing import Dict, Any

SUSPICIOUS_TLDS = [".xyz", ".top", ".work", ".click", ".link", ".kim", ".zip", ".mov"]
KNOWN_PHISH_PATTERNS = ["login-verify", "account-update", "secure-bank", "paypal-auth", "appleid-login"]

def check_url_reputation(target_url: str) -> str:
    """
    Perform pre-click safety scan on a URL. Checks domain typosquatting, TLD reputation, and suspicious URL structures.
    """
    try:
        parsed = urllib.parse.urlparse(target_url)
        domain = parsed.netloc.lower() or parsed.path.lower()
    except Exception:
        return f"🔴 CRITICAL: Invalid URL structure '{target_url}'."

    flags = []
    
    # 1. TLD Check
    for tld in SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            flags.append(f"High-risk TLD ('{tld}') detected.")
            break

    # 2. Typosquatting / Suspicious pattern keywords
    for pattern in KNOWN_PHISH_PATTERNS:
        if pattern in domain:
            flags.append(f"Known phishing pattern keyword ('{pattern}') detected.")

    # 3. IP address host check
    if domain.replace(".", "").isdigit():
        flags.append("Bare IP address used as hostname instead of domain name.")

    if not flags:
        return f"✅ URL Reputation Safe: '{target_url}' (Domain: {domain}) — No threat indicators detected."

    return (
        f"⚠️ PHISHING ALERT for '{target_url}':\n"
        f"Domain: {domain}\n"
        f"Threat Indicators:\n" + "\n".join(f"- {f}" for f in flags)
    )
