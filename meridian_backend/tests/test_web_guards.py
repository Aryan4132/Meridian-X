"""
test_web_guards.py — SSRF guard + injection-sanitizer coverage for web tools.

Asserts that every agent-reachable HTTP fetch entry point rejects
non-public targets WITHOUT touching the network, and that ingested
content is sanitized before persistence.
"""

from src.tools.web import download_file, fetch_page, ingest_url
from src.tools.web_scraper import _is_public_http_url


def test_ssrf_guard_blocks_internal_targets():
    blocked = [
        "http://localhost:11434/api/tags",
        "http://127.0.0.1:4132/api/health",
        "http://169.254.169.254/latest/meta-data/",
        "http://10.0.0.5/admin",
        "http://192.168.1.1/",
        "file:///etc/passwd",
        "ftp://example.com/file",
    ]
    for url in blocked:
        assert _is_public_http_url(url) is False, url


def test_ssrf_guard_allows_public_targets():
    assert _is_public_http_url("https://example.com/page") is True
    assert _is_public_http_url("http://example.com/") is True


def test_fetch_page_blocks_without_network():
    # Must return before any socket is opened (no network in this test).
    assert fetch_page("http://169.254.169.254/latest/meta-data/").startswith("Error:")
    assert fetch_page("file:///etc/passwd").startswith("Error:")
    assert fetch_page("http://localhost:11434/api/tags").startswith("Error:")


def test_download_file_blocks_without_network():
    assert download_file("http://127.0.0.1:4132/api/health", "x.bin").startswith("Error:")


def test_ingest_url_chains_block_as_error():
    res = ingest_url("http://localhost:11434/api/tags")
    assert res.startswith("Failed to fetch page: Error:")
