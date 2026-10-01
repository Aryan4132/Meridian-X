"""HTTP scraping, digests & SSRF-guarded fetch tools.

Split from ``src.tools.web_browser`` (Phase 2 god-file refactor). Pure
move — zero behavior changes. ``web_browser.py`` re-exports every symbol
so existing imports keep working.

Import discipline: session helpers (``_get_active_model``) are imported
lazily inside functions to avoid a circular import with ``web_browser``.
"""

import re
import time
from typing import Any, Dict, List
from urllib.parse import urlparse

import httpx

try:
    from selectolax.parser import HTMLParser
except ImportError:
    HTMLParser = None


def sanitize_web_content_injection(content: str) -> tuple[str, bool]:
    """Strips HTML comments, zero-width chars, and indirect prompt injection signatures from scraped web content (SEC-24)."""
    if not content:
        return content, False
    # Strip HTML comments
    clean_text = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    # Strip zero-width unicode
    clean_text = re.sub(r"[​-‍﻿]", "", clean_text)

    from src.core.prompt_injection import sanitize_prompt
    sanitized, is_detected, _ = sanitize_prompt(clean_text)
    if is_detected:
        from src.core.audit_logger import log_sensitive_action
        log_sensitive_action("SECURITY_VIOLATION", "web_injection_attempt", {"snippet": content[:100]}, "FAILED")
    return sanitized, is_detected


_BROWSER_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Meridian-X/1.0 (research digest bot)"


def _fetch_arxiv_cards(query: str, max_results: int = 3) -> List[Dict[str, str]]:
    """Live arXiv API query (no key required). Returns [] on any failure."""
    import urllib.parse
    import xml.etree.ElementTree as ET
    try:
        # NOTE: sortBy/sortOrder params make some arXiv frontends answer
        # 406 — default relevance ordering is used instead.
        params = urllib.parse.urlencode({
            "search_query": f"all:{query}",
            "start": 0,
            "max_results": max_results,
        })
        res = httpx.get(
            f"https://export.arxiv.org/api/query?{params}",
            timeout=12.0,
            headers={"User-Agent": _BROWSER_UA},
        )
        if res.status_code != 200:
            # arXiv throttles aggressively — one polite retry before giving up.
            time.sleep(4.0)
            res = httpx.get(
                f"https://export.arxiv.org/api/query?{params}",
                timeout=12.0,
                headers={"User-Agent": _BROWSER_UA},
            )
            if res.status_code != 200:
                return []
        ns = {"a": "http://www.w3.org/2005/Atom"}
        cards = []
        for entry in ET.fromstring(res.text).findall("a:entry", ns)[:max_results]:
            title_el = entry.find("a:title", ns)
            summary_el = entry.find("a:summary", ns)
            id_el = entry.find("a:id", ns)
            title = " ".join((title_el.text or "").split()) if title_el is not None else "Untitled"
            summary = " ".join((summary_el.text or "").split()) if summary_el is not None else ""
            cards.append({
                "source": "arXiv",
                "title": title,
                "summary": summary[:300],
                "url": (id_el.text or "").strip() if id_el is not None else "",
            })
        return cards
    except Exception:
        return []


def _fetch_github_cards(query: str, max_results: int = 3) -> List[Dict[str, str]]:
    """Live GitHub repository search (unauthenticated, low rate limit). [] on failure."""
    import urllib.parse
    try:
        params = urllib.parse.urlencode({"q": query, "sort": "stars", "order": "desc", "per_page": max_results})
        res = httpx.get(
            f"https://api.github.com/search/repositories?{params}",
            timeout=12.0,
            headers={"User-Agent": _BROWSER_UA, "Accept": "application/vnd.github+json"},
        )
        if res.status_code != 200:
            return []
        cards = []
        for item in (res.json().get("items") or [])[:max_results]:
            cards.append({
                "source": "GitHub",
                "title": item.get("full_name", "Unknown repo"),
                "summary": (item.get("description") or "")[:300],
                "url": item.get("html_url", ""),
            })
        return cards
    except Exception:
        return []


def generate_tech_market_digest(topic: str = "AI Tech & Market News") -> Dict[str, Any]:
    """Builds briefing cards from LIVE arXiv + GitHub queries (FIN-02).

    Both sources are keyless. If a source is unreachable its cards are simply
    absent and the digest says so — never fabricated placeholder entries.
    """
    cards = _fetch_arxiv_cards(topic) + _fetch_github_cards(topic)
    digest = {
        "topic": topic,
        "briefing_cards": cards,
        "sources_live": {
            "arxiv": any(c["source"] == "arXiv" for c in cards),
            "github": any(c["source"] == "GitHub" for c in cards),
        },
        "generated_at": time.time(),
    }
    from src.core.audit_logger import log_sensitive_action
    log_sensitive_action(
        "RESEARCH_DIGEST", "generate_tech_market_digest",
        {"topic": topic, "cards": len(cards)}, "SUCCESS",
    )
    return digest


def _is_public_http_url(url: str) -> bool:
    """SSRF guard: only http(s) URLs resolving to public hosts are allowed (SEC-FIX).

    Blocks file://, and localhost/private/link-local/metadata targets so an
    agent-steered scraper cannot read internal services (Ollama, LAN, cloud
    metadata endpoints) from inside the user's machine.
    """
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return False
        hostname = (parsed.hostname or "").lower().rstrip(".")
        import ipaddress
        try:
            ip = ipaddress.ip_address(hostname)
            # Literal IP — check directly
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
                return False
            return True
        except ValueError:
            pass
        # Hostname — block obvious local names; public DNS names resolve at
        # request time (DNS-rebinding by remote servers is out of scope here).
        blocked_names = {"localhost", "*.local", "*.internal", "metadata.google.internal"}
        for pattern in blocked_names:
            if pattern.startswith("*."):
                if hostname.endswith(pattern[1:]):
                    return False
            elif hostname == pattern:
                return False
        return True
    except Exception:
        return False


def parse_youtube_content(url: str) -> Dict[str, Any]:
    """Extract metadata from YouTube video/playlist URLs using oEmbed API fallback."""
    try:
        oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
        res = httpx.get(oembed_url, timeout=8.0, headers={"User-Agent": _BROWSER_UA})
        if res.status_code == 200:
            data = res.json()
            return {
                "title": data.get("title", "YouTube Content"),
                "author": data.get("author_name", "Unknown Channel"),
                "provider": data.get("provider_name", "YouTube"),
                "thumbnail": data.get("thumbnail_url", ""),
                "url": url
            }
    except Exception:
        pass
    return {"title": "YouTube Video", "url": url}


def scrape_urls(urls: List[str], extract_schema: str = "") -> str:
    """Scrape a list of URLs and extract fields specified in the schema."""
    try:
        import ollama
    except ImportError:
        ollama = None
    try:
        from database import get_ollama_client_host
    except Exception:
        def get_ollama_client_host() -> str:  # type: ignore[misc]
            return "http://localhost:11434"
    from src.tools.web_browser import _get_active_model

    results = []
    for url in urls:
        try:
            if not _is_public_http_url(url):
                results.append(f"URL: {url} -> Blocked by SSRF guard (non-public or non-http target).")
                continue
            res = httpx.get(url, follow_redirects=True, timeout=10.0)
            if res.status_code != 200:
                results.append(f"URL: {url} (Failed with status code {res.status_code})")
                continue
            if not HTMLParser:
                results.append(f"URL: {url} -> Error: 'selectolax' library is not installed.")
                continue

            parser = HTMLParser(res.text)
            title = parser.css_first("title")
            title_text = title.text().strip() if title else "No Title"
            body_text = " ".join([p.text().strip() for p in parser.css("p")])
            SCRAPE_PREVIEW_CHARS = 1000
            if extract_schema and ollama:
                client = ollama.Client(host=get_ollama_client_host())
                prompt = (
                    f"Extract fields conforming to this schema: {extract_schema}\n\n"
                    f"From this text content scraped from URL '{url}':\n{body_text[:SCRAPE_PREVIEW_CHARS]}\n\n"
                    "Respond with a valid JSON block of fields. No other text."
                )
                ollama_res = client.generate(model=_get_active_model(), prompt=prompt)
                extracted_data = (ollama_res.response if hasattr(ollama_res, "response") else ollama_res.get("response", "{}")).strip()
                results.append(f"URL: {url} (Title: {title_text})\nExtracted Data:\n{extracted_data}")
            else:
                results.append(f"URL: {url} (Title: {title_text})\nText snippet:\n{body_text[:SCRAPE_PREVIEW_CHARS]}...")
        except Exception as e:
            results.append(f"URL: {url} -> Error: {e}")

    return "\n\n---\n\n".join(results)


def scrape_table(url: str, table_index: int = 0) -> str:
    """Extract an HTML table from a webpage URL and return it as markdown."""
    try:
        if not _is_public_http_url(url):
            return "Blocked by SSRF guard (non-public or non-http target)."
        if not HTMLParser:
            return "Error: 'selectolax' library is not installed."
        res = httpx.get(url, follow_redirects=True, timeout=10.0)
        if res.status_code != 200:
            return f"Failed to load URL (Status Code: {res.status_code})"

        parser = HTMLParser(res.text)
        tables = parser.css("table")
        if not tables or table_index >= len(tables):
            return f"Error: No table found at index {table_index}."

        table = tables[table_index]
        rows = []
        headers = [th.text().strip() for th in table.css("th")]
        for tr in table.css("tr"):
            cells = [td.text().strip() for td in tr.css("td")]
            if cells:
                rows.append(cells)

        if not headers and rows:
            headers = rows.pop(0)

        if not headers:
            return "Table contains no headers or rows to format."

        lines = []
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
        for row in rows:
            if len(row) < len(headers):
                row = row + [""] * (len(headers) - len(row))
            elif len(row) > len(headers):
                row = row[:len(headers)]
            lines.append("| " + " | ".join(row) + " |")

        return "\n".join(lines)
    except Exception as e:
        return f"Failed to scrape table: {e}"


def schedule_scrape(urls: List[str], cron_expr: str) -> str:
    """Schedule a recurring scrape job of URLs using the cron scheduler."""
    from src.tools.scheduler import schedule_task
    goal = f"Scrape URLs: {', '.join(urls)}, extract findings, and save note to memory."
    return schedule_task(goal, cron_expr)
