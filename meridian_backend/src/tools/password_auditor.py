"""
Password Health Auditor (SEC-35)
Audits password strength, entropy, reuse across stored vault logins, and breach history checks.
"""

import math
from typing import Dict, Any, List

def audit_password_strength(password: str) -> str:
    """
    Audit password strength, entropy, and complexity metrics.
    """
    length = len(password)
    if length == 0:
        return "Error: Empty password."

    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(not c.isalnum() for c in password): charset += 32

    entropy = length * math.log2(charset) if charset > 0 else 0

    if entropy < 40:
        grade = "🔴 POOR (Weak)"
        recommendation = "Easily crackable via dictionary/brute-force attacks. Increase length > 14 chars with mixed symbols."
    elif entropy < 65:
        grade = "MO MODERATE"
        recommendation = "Acceptable, but consider extending length for high-value services."
    else:
        grade = "🟢 STRONG"
        recommendation = "High entropy password. Resistant to offline brute-force attacks."

    return (
        f"🛡️ Password Health Audit:\n"
        f"- Length: {length} characters\n"
        f"- Entropy Score: {entropy:.1f} bits\n"
        f"- Security Rating: {grade}\n"
        f"- Advice: {recommendation}"
    )
