import os
import json
import time
import re
import httpx
from selectolax.parser import HTMLParser
import ollama
from typing import List, Dict, Any, Optional
from database import get_ollama_client_host

# Global browser state
_playwright = None
_browser = None
_page = None
_viewport_w = 1280
_viewport_h = 800

def _get_active_model() -> str:
    from database import get_brain_model
    return get_brain_model()

def _get_vision_model() -> str:
    from database import get_vision_model
    return get_vision_model()


def browser_open(url: str) -> str:
    """Launch headless browser and navigate to a specified URL."""
    global _playwright, _browser, _page
    try:
        from playwright.sync_api import sync_playwright
        if not _playwright:
            _playwright = sync_playwright().start()
            _browser = _playwright.chromium.launch(headless=True)
            
        # Dynamically load viewport dimensions
        try:
            from database import get_user_profile
            vw = get_user_profile("browser_viewport_width")
            vh = get_user_profile("browser_viewport_height")
            viewport_w = int(vw) if vw else _viewport_w
            viewport_h = int(vh) if vh else _viewport_h
        except Exception:
            viewport_w = _viewport_w
            viewport_h = _viewport_h

        if not _page:
            _page = _browser.new_page(viewport={"width": viewport_w, "height": viewport_h})
            
        try:
            _page.goto(url)
            # Wait for network idle/load state
            _page.wait_for_load_state("load")
        except Exception as e:
            # BUG-34 fix: reset _page to None so the next call creates a fresh page
            # instead of reusing this broken/stale Playwright page.
            _page = None
            return f"Failed to navigate browser: {e}"
        return f"Successfully opened visual headless browser context and navigated to: {url}"
    except ImportError:
        return "Error: 'playwright' Python library is not installed or configured. Please install it."
    except Exception as e:
        return f"Failed to navigate browser: {e}"

def browser_screenshot(output_path: str = "browser.png") -> str:
    """Capture current browser viewport with visual outlines and indicators on interactable elements."""
    global _page
    if not _page:
        return "Error: Browser is not open. Call browser_open first."
    try:
        # Inject custom styles and overlays to number all buttons/inputs/links
        inject_script = """
        () => {
            const styles = document.createElement('style');
            styles.id = 'meridian-vision-styles';
            styles.innerHTML = `
                .meridian-outlined-el { border: 2px solid #ea580c !important; position: relative !important; }
                .meridian-label-span {
                    background: #ea580c !important;
                    color: black !important;
                    font-size: 10px !important;
                    font-weight: bold !important;
                    position: absolute !important;
                    top: 0 !important;
                    left: 0 !important;
                    z-index: 100000 !important;
                    padding: 1px 3px !important;
                    border-radius: 2px !important;
                    font-family: monospace !important;
                }
            `;
            document.head.appendChild(styles);
            const items = document.querySelectorAll('button, input, select, textarea, a');
            items.forEach((el, idx) => {
                el.classList.add('meridian-outlined-el');
                const span = document.createElement('span');
                span.className = 'meridian-label-span';
                span.innerText = '[' + idx + ']';
                try {
                    el.appendChild(span);
                } catch(e) {}
            });
        }
        """
        _page.evaluate(inject_script)
        
        # Take the screenshot
        _page.screenshot(path=output_path)
        
        # Clean up annotations immediately
        cleanup_script = """
        () => {
            document.querySelectorAll('.meridian-label-span').forEach(s => s.remove());
            document.querySelectorAll('.meridian-outlined-el').forEach(el => {
                el.classList.remove('meridian-outlined-el');
            });
            const styles = document.getElementById('meridian-vision-styles');
            if (styles) styles.remove();
        }
        """
        _page.evaluate(cleanup_script)
        
        return f"Captured annotated viewport screenshot and saved to '{output_path}'."
    except Exception as e:
        return f"Failed to capture browser screenshot: {e}"

def _locate_element_by_vision(description: str) -> Optional[tuple]:
    """Uses moondream:1.8b to visually locate coordinates on current screenshot."""
    global _page
    if not _page:
        return None
        
    temp_path = "temp_browser_click.png"
    try:
        _page.screenshot(path=temp_path)
        
        client = ollama.Client(host=get_ollama_client_host())
        prompt = (
            f"Locate the UI element described as '{description}' on this screenshot. "
            "Return ONLY the coordinate position in percentage format [X, Y] (from 0 to 100). "
            "For example: [50, 20]. Do not write markdown, code blocks, or explanations."
        )
        
        res = client.generate(
            model=_get_vision_model(),
            prompt=prompt,
            images=[temp_path]
        )
        coord_text = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
        print(f"[Vision Browser] Moondream coordinate prediction: {coord_text}")
        
        # BUG-33 fix: use [\d.]+ to match float coordinates returned by moondream (e.g. [50.5, 20.3])
        match = re.search(r"\[\s*([\d.]+)\s*,\s*([\d.]+)\s*\]", coord_text)
        if match:
            pct_x = float(match.group(1))
            pct_y = float(match.group(2))
            
            # Map percentages to pixel dimensions
            px_x = int((pct_x / 100.0) * _viewport_w)
            px_y = int((pct_y / 100.0) * _viewport_h)
            return (px_x, px_y)
    except Exception as e:
        print("[Vision Browser] Error in vision localization:", e)
    finally:
        try:
            os.remove(temp_path)
        except Exception:
            pass
    return None

def browser_find_and_click(description: str) -> str:
    """Vision-locate element matching the description on screen and click it."""
    global _page
    if not _page:
        return "Error: Browser is not open. Call browser_open first."
        
    coords = _locate_element_by_vision(description)
    if not coords:
        return f"Vision was unable to locate coordinates for: '{description}'."
        
    x, y = coords
    try:
        _page.mouse.click(x, y)
        return f"Visually clicked coordinate ({x}, {y}) corresponding to '{description}'."
    except Exception as e:
        return f"Failed to execute click: {e}"

def browser_type_in(description: str, text: str, delay: int = 50) -> str:
    """Vision-locate element matching description, click it, and type text with custom delay (ms)."""
    global _page
    if not _page:
        return "Error: Browser is not open. Call browser_open first."
        
    coords = _locate_element_by_vision(description)
    if not coords:
        return f"Vision was unable to locate coordinates for: '{description}'."
        
    x, y = coords
    try:
        _page.mouse.click(x, y)
        time.sleep(0.1)
        _page.keyboard.type(text, delay=delay)
        return f"Visually selected field '{description}' at ({x}, {y}) and typed key buffer (delay={delay}ms)."
    except Exception as e:
        return f"Failed to type in browser field: {e}"

def browser_get_text() -> str:
    """Extract all text contents from the current page viewport."""
    global _page
    if not _page:
        return "Error: Browser is not open. Call browser_open first."
    try:
        text = _page.evaluate("document.body.innerText")
        return text if text.strip() else "Page contains no readable text."
    except Exception as e:
        return f"Failed to extract browser text: {e}"

def browser_close() -> str:
    """Close the active headless browser session."""
    global _playwright, _browser, _page
    if not _browser:
        return "No active browser session to close."
    try:
        if _page:
            _page.close()
        _browser.close()
        _playwright.stop()
        
        _page = None
        _browser = None
        _playwright = None
        return "Closed headless browser environment safely."
    except Exception as e:
        return f"Failed to close browser: {e}"


# --- Scraping Tools ---

def scrape_urls(urls: List[str], extract_schema: str = "") -> str:
    """Scrape a list of URLs and extract fields specified in the schema."""
    results = []
    for url in urls:
        try:
            res = httpx.get(url, follow_redirects=True, timeout=10.0)
            if res.status_code != 200:
                results.append(f"URL: {url} -> Failed (Status Code: {res.status_code})")
                continue
                
            parser = HTMLParser(res.text)
            title = parser.css_first("title")
            title_text = title.text().strip() if title else "No Title"
            
            # Simple text extraction
            body_text = " ".join([p.text().strip() for p in parser.css("p")])
            
            # BUG-37 fix: unified truncation constant for consistency across schema and plain paths.
            SCRAPE_PREVIEW_CHARS = 1000
            # If a schema is specified, ask Ollama to extract structure
            if extract_schema:
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
        res = httpx.get(url, follow_redirects=True, timeout=10.0)
        if res.status_code != 200:
            return f"Failed to load URL (Status Code: {res.status_code})"
            
        parser = HTMLParser(res.text)
        tables = parser.css("table")
        if not tables or table_index >= len(tables):
            return f"Error: No table found at index {table_index}."
            
        table = tables[table_index]
        rows = []
        
        # Read header
        headers = [th.text().strip() for th in table.css("th")]
        
        # Read body rows
        for tr in table.css("tr"):
            cells = [td.text().strip() for td in tr.css("td")]
            if cells:
                rows.append(cells)
                
        if not headers and rows:
            # If no th elements, treat first row as header
            headers = rows.pop(0)
            
        if not headers:
            return "Table contains no headers or rows to format."
            
        # Format as Markdown
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
