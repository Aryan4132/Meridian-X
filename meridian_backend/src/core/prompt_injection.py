"""
prompt_injection.py — Prompt Injection Detection & Sanitizer Engine (SEC-08)
Pre-processes user prompt strings and tool outputs through a signature & heuristic scanner
to detect and neutralize jailbreak attempts, system override directives, and hidden payloads.
"""

import re
import logging
from typing import Tuple, List, Dict, Any

logger = logging.getLogger("meridian_prompt_injection")

# Common jailbreak and prompt injection patterns
INJECTION_PATTERNS = [
    (re.compile(r"(?i)\bignore\s+(all\s+)?(previous|above|prior)\s+(instructions|prompts|directives|rules)\b"), "IGNORE_PREVIOUS_INSTRUCTIONS"),
    (re.compile(r"(?i)\bdisregard\s+(all\s+)?(previous|above|prior)\s+(instructions|prompts|directives|rules)\b"), "DISREGARD_PREVIOUS_INSTRUCTIONS"),
    (re.compile(r"(?i)\bforget\s+(all\s+)?(previous|above|prior)\s+(instructions|rules)\b"), "FORGET_PREVIOUS_INSTRUCTIONS"),
    (re.compile(r"(?i)\b(you\s+are\s+now|act\s+as|pretend\s+to\s+be)\s+DAN\b"), "DAN_JAILBREAK"),
    (re.compile(r"(?i)\b(jailbreak|developer\s+mode|unfiltered\s+mode|god\s+mode)\s+enabled?\b"), "JAILBREAK_MODE_KEYWORD"),
    (re.compile(r"(?i)<\s*system\s*>[^<]*ignore"), "SYSTEM_TAG_INJECTION"),
    (re.compile(r"(?i)\[\s*system\s*override\s*\]"), "SYSTEM_OVERRIDE_BRACKETS"),
    (re.compile(r"(?i)\bdo\s+anything\s+now\b"), "DAN_PHRASE"),
    (re.compile(r"[\u200B-\u200D\uFEFF]"), "ZERO_WIDTH_UNICODE"),  # Hidden invisible zero-width unicode characters
]


def detect_prompt_injection(prompt: str) -> Tuple[bool, List[str]]:
    """
    Scans prompt string for prompt injection / jailbreak signatures.
    Returns (is_detected, list_of_matched_categories).
    """
    if not prompt:
        return False, []

    detected_categories = []
    for pattern, category in INJECTION_PATTERNS:
        if pattern.search(prompt):
            detected_categories.append(category)

    is_detected = len(detected_categories) > 0
    return is_detected, detected_categories


def sanitize_prompt(prompt: str) -> Tuple[str, bool, List[str]]:
    """
    Sanitizes prompt string by stripping zero-width unicode characters
    and returning (cleaned_prompt, was_injection_detected, categories).
    """
    if not prompt:
        return prompt, False, []

    is_detected, categories = detect_prompt_injection(prompt)

    # Strip zero-width unicode characters
    cleaned = re.sub(r"[\u200B-\u200D\uFEFF]", "", prompt)

    if is_detected:
        logger.warning(
            f"[SECURITY] Prompt injection signatures detected: {categories}. "
            f"Prompt snippet: {prompt[:60]}..."
        )
        try:
            from src.core.audit_logger import log_sensitive_action
            log_sensitive_action(
                category="PROMPT_INJECTION",
                action="sanitize_prompt",
                details={"detected_signatures": categories, "snippet": prompt[:100]},
                status="BLOCKED" if any("JAILBREAK" in c for c in categories) else "FLAGGED"
            )
        except Exception:
            pass

    return cleaned, is_detected, categories
