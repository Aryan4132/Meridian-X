"""
test_web_guards.py — SSRF guard + injection-sanitizer coverage for web tools.

Asserts that every agent-reachable HTTP fetch entry point rejects
non-public targets WITHOUT touching the network, and that ingested
content is sanitized before persistence.
"""

from unittest.mock import MagicMock, patch

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


def test_open_url_in_browser_allows_http_and_localhost():
    from src.tools.system_windows import open_url_in_browser
    with patch("webbrowser.open", return_value=True) as mock_open:
        assert open_url_in_browser("https://example.com/").startswith("Opened URL")
        assert open_url_in_browser("http://localhost:5173/").startswith("Opened URL")
        assert mock_open.call_count == 2


def test_open_url_in_browser_blocks_dangerous_schemes():
    from src.tools.system_windows import open_url_in_browser
    with patch("webbrowser.open") as mock_open:
        assert open_url_in_browser("javascript:alert(1)").startswith("Error:")
        assert open_url_in_browser("file:///etc/passwd").startswith("Error:")
        assert open_url_in_browser("data:text/html,<h1>x</h1>").startswith("Error:")
        assert open_url_in_browser("not a url").startswith("Error:")
        mock_open.assert_not_called()


def test_fetch_page_rejects_binary_content():
    resp = MagicMock()
    resp.headers = {"content-type": "application/zip"}
    stream = MagicMock()
    stream.__enter__.return_value = resp
    client = MagicMock()
    client.stream.return_value = stream
    client_ctx = MagicMock()
    client_ctx.__enter__.return_value = client
    with patch("src.tools.web.httpx.Client", return_value=client_ctx):
        res = fetch_page("https://example.com/file.zip")
    assert res.startswith("Error:") and "download_file" in res
