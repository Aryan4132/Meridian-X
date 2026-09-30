"""
test_known_errors_remediation.py
Tests verifying fixes for known_errors.md & improvement_research.md issues:
- Generic Ollama <-> Cloud API model tag normalizer
- Ollama connection failure handling
- Hermes/OpenClaw elevated privilege checks
- OneDrive file lock retries
- YouTube oEmbed content scraping fallback
"""

import pytest
import os
import sys

from src.core.llm_provider import normalize_provider_and_model
from src.tools.filesystem import is_admin_process, retry_file_operation
from src.core.elevated_runner import is_admin, run_command_elevated
from src.tools.web_browser import parse_youtube_content, scrape_urls


def test_model_tag_normalization_groq():
    prov, mod = normalize_provider_and_model("groq", "gemma4:32b-cloud")
    assert prov == "groq"
    assert "gemma" in mod.lower()

    prov2, mod2 = normalize_provider_and_model("groq", "llama-3-8b")
    assert prov2 == "groq"
    assert "llama" in mod2.lower()


def test_model_tag_normalization_openrouter():
    prov, mod = normalize_provider_and_model("openrouter", "gemma4:31b")
    assert prov == "openrouter"
    assert "gemma" in mod.lower()

    prov2, mod2 = normalize_provider_and_model("openrouter", "deepseek-v4")
    assert prov2 == "openrouter"
    assert "deepseek" in mod2.lower()


def test_model_tag_normalization_deepseek():
    prov, mod = normalize_provider_and_model("deepseek", "deepseek-v4-pro")
    assert prov == "deepseek"
    assert "deepseek" in mod.lower()


def test_prefix_parsing_in_model_name():
    prov, mod = normalize_provider_and_model("ollama", "openrouter/anthropic/claude-3.5-sonnet")
    assert prov == "openrouter"
    assert "claude" in mod.lower() or "anthropic" in mod.lower()


def test_admin_privilege_detection():
    # Verify function runs without throwing exceptions
    admin_state_fs = is_admin_process()
    admin_state_runner = is_admin()
    assert isinstance(admin_state_fs, bool)
    assert isinstance(admin_state_runner, bool)
    assert admin_state_fs == admin_state_runner


def test_retry_file_operation_success():
    call_count = 0

    def flaky_func():
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise PermissionError("[WinError 13] Access is denied")
        return "success"

    res = retry_file_operation(flaky_func, retries=3, delay=0.01)
    assert res == "success"
    assert call_count == 2


def test_youtube_content_oembed_parsing():
    res = parse_youtube_content("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    assert isinstance(res, dict)
    assert "title" in res
    assert "url" in res


def test_scrape_urls_youtube_fallback():
    scraped = scrape_urls(["https://www.youtube.com/watch?v=dQw4w9WgXcQ"])
    assert "YouTube Content" in scraped or "Rick Astley" in scraped or "URL:" in scraped
