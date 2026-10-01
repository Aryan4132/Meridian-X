"""Unified non-streaming LLM completion entry points.

Split from ``src.core.llm_provider`` (Phase 2 god-file refactor). Pure
move — zero behavior changes. ``llm_provider.py`` re-exports every symbol
so existing imports keep working.

Import discipline: this module imports ``llm_auth`` (leaf) at top level
and ``llm_provider`` lazily inside functions to avoid a circular import.
"""

import asyncio
import logging
import os
from typing import Dict, List, Optional

from src.core.llm_auth import get_api_key, scan_and_redact_secrets

logger = logging.getLogger("meridian_llm_provider")


async def call_llm(
    messages: List[Dict[str, str]],
    provider: Optional[str] = None,
    model: Optional[str] = None,
    temperature: float = 0.7
) -> str:
    """
    Unified non-streaming completion call for any provider.
    Automatically redacts sensitive secrets in messages.
    Resolves provider/model defaults from database if not supplied.
    Logs token spend and enforces budget caps & air-gap mode.
    """
    from src.core.llm_provider import estimate_llm_cost, generate_completion_stream

    sanitized_messages = []
    for msg in messages:
        content = msg.get("content", "")
        sanitized_messages.append({
            **msg,
            "content": scan_and_redact_secrets(content)
        })

    if not provider or not model:
        try:
            from database import get_brain_model, get_model_source, get_user_profile
            if not model:
                model = get_brain_model()
            if not provider:
                configured_prov = os.getenv("MERIDIAN_PROVIDER") or get_user_profile("meridian_provider")
                if configured_prov:
                    provider = configured_prov
                else:
                    source = get_model_source()
                    provider = "ollama" if source == "local" else "openrouter"
        except Exception:
            provider = provider or os.getenv("MERIDIAN_PROVIDER") or "ollama"
            model = model or ""

    # Validate provider has required API key or fallback to configured provider / ollama
    if provider in ["openrouter", "groq", "mistral", "together", "perplexity", "anthropic", "openai", "gemini", "deepseek"]:
        if not get_api_key(provider):
            if os.getenv("MERIDIAN_PROVIDER") and os.getenv("MERIDIAN_PROVIDER") != provider:
                provider = os.getenv("MERIDIAN_PROVIDER")
            else:
                provider = "ollama"

    # TRUST-03: Budget Cap Check & Auto-Fallback
    try:
        from database import check_budget_exceeded, record_token_spend
        if provider != "ollama" and check_budget_exceeded():
            logger.warning(f"Monthly budget cap exceeded. Falling back provider '{provider}' -> 'ollama'.")
            provider = "ollama"
    except Exception as e:
        logger.debug(f"Budget check error: {e}")

    # Guarantee non-null provider and model strictly resolved from user choice / profile
    active_provider: str = provider or "ollama"
    active_model: str = model or ""
    if not active_model:
        try:
            from database import get_brain_model
            active_model = get_brain_model()
        except Exception:
            pass

    # Estimate prompt tokens
    raw_prompt_text = " ".join([m.get("content", "") for m in sanitized_messages])
    prompt_tokens = max(1, len(raw_prompt_text) // 4)

    chunks = []
    async for chunk in generate_completion_stream(sanitized_messages, provider=active_provider, model=active_model, temperature=temperature):
        chunks.append(chunk)

    result_text = "".join(chunks)
    completion_tokens = max(1, len(result_text) // 4)
    cost_usd = estimate_llm_cost(active_provider, prompt_tokens, completion_tokens)

    # Record token spend into SQLite
    try:
        from database import record_token_spend
        record_token_spend(active_provider, active_model, prompt_tokens, completion_tokens, cost_usd)
    except Exception as e:
        logger.debug(f"Failed logging token spend: {e}")

    return result_text


def call_llm_sync(
    messages: List[Dict[str, str]],
    provider: Optional[str] = None,
    model: Optional[str] = None,
    temperature: float = 0.7
) -> str:
    """
    Synchronous wrapper for call_llm.
    """
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            return pool.submit(lambda: asyncio.run(call_llm(messages, provider, model, temperature))).result()
    else:
        return asyncio.run(call_llm(messages, provider, model, temperature))
