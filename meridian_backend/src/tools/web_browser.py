import os
import json
import time
import re
import httpx
from urllib.parse import urlparse
try:
    from selectolax.parser import HTMLParser
except ImportError:
    HTMLParser = None
try:
    import ollama
except ImportError:
    ollama = None
from typing import List, Dict, Any, Optional
try:
    from database import get_ollama_client_host, get_vision_model, get_brain_model
except Exception:
    def get_ollama_client_host() -> str:  # type: ignore[misc]
        return "http://localhost:11434"
    def get_vision_model() -> str:  # type: ignore[misc]
        return ""
    def get_brain_model() -> str:  # type: ignore[misc]
        return ""


def _get_vision_model() -> str:
    """Return the configured vision model name (e.g. moondream:1.8b)."""
    return get_vision_model()

def _get_active_model() -> str:
    """Return the active brain/LLM model name."""
    return get_brain_model()

# Ensure Playwright finds system-installed browsers on Windows when running standalone/bundled
if "PLAYWRIGHT_BROWSERS_PATH" not in os.environ:
    _local_app = os.environ.get("LOCALAPPDATA", "")
    _pw_dir = os.path.join(_local_app, "ms-playwright") if _local_app else ""
    if _pw_dir and os.path.exists(_pw_dir):
        os.environ["PLAYWRIGHT_BROWSERS_PATH"] = _pw_dir

# Global browser state
_playwright: Any = None
_browser: Any = None
_page: Any = None
_viewport_w = 1280
_viewport_h = 800
# None = no session yet; otherwise tracks the flags of the live session so
# switching headless/visible/profile/engine transparently relaunches.
_session_headless: Optional[bool] = None
_session_profile: Optional[str] = None  # profile dir of live session, or None
_session_browser: Optional[str] = None  # engine id: chromium/chrome/edge/firefox/attached
_session_attached: bool = False  # True when driving the user's own browser via CDP
_page_ctx: Any = None  # BrowserContext used to mint pages for attached sessions

# Engine ids accepted by browser_open(browser=...).
BROWSER_ENGINES = ("chromium", "chrome", "edge", "firefox", "attached")
_session_cdp_url: Optional[str] = None  # CDP endpoint of an attached session


def _meridian_profile_dir() -> str:
    """Dedicated agent browser profile (logins persist here across sessions).

    Separate from your daily Chrome profile on purpose: Chrome locks a profile
    directory while running, so sharing yours would fail whenever Chrome is
    already open. Log in once in visible+profile mode and it sticks.
    """
    import tempfile
    base = os.path.join(os.getcwd(), "meridian_memory", "chrome_profile")
    try:
        os.makedirs(base, exist_ok=True)
        return base
    except Exception:
        fallback = os.path.join(tempfile.gettempdir(), "meridian_chrome_profile")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def _close_session() -> None:
    """Tears down the Playwright session without returning user text.

    Attached sessions (the user's own browser via CDP) only lose our tab —
    the user's browser is never closed.
    """
    global _playwright, _browser, _page, _page_ctx
    global _session_headless, _session_profile, _session_browser, _session_attached
    global _session_cdp_url
    try:
        if _page:
            _page.close()
    except Exception:
        pass
    if not _session_attached:
        try:
            if _browser:
                _browser.close()
        except Exception:
            pass
    try:
        if _playwright:
            _playwright.stop()
    except Exception:
        pass
    _page = None
    _page_ctx = None
    _browser = None
    _playwright = None
    _session_headless = None
    _session_profile = None
    _session_browser = None
    _session_attached = False
    _session_cdp_url = None


def _mint_page():
    """Creates a page on the live session (context-aware for CDP/persistent)."""
    global _page_ctx, _browser, _viewport_w, _viewport_h
    if _page_ctx is not None:
        return _page_ctx.new_page()
    if _session_profile:
        # Persistent contexts take viewport at launch, not per page.
        return _browser.new_page()
    return _browser.new_page(viewport={"width": _viewport_w, "height": _viewport_h})


def _launch_engine(pw, browser: str, headless: bool):
    """Launches a fresh engine-owned browser (chromium/chrome/edge/firefox) with graceful fallback."""
    slow_mo = 0 if headless else 300
    if browser == "firefox":
        return pw.firefox.launch(headless=headless, slow_mo=slow_mo)
    kwargs: Dict[str, Any] = {"headless": headless, "slow_mo": slow_mo}
    if browser in ("chrome", "edge"):
        kwargs["channel"] = "chrome" if browser == "chrome" else "msedge"
        return pw.chromium.launch(**kwargs)

    # Default browser is "chromium" - try standard launch then fallback to installed Chrome/Edge channels
    try:
        return pw.chromium.launch(**kwargs)
    except Exception as e:
        err_msg = str(e).lower()
        if "executable doesn't exist" in err_msg or "playwright install" in err_msg or "failed to find" in err_msg:
            # Fallback 1: System Chrome channel
            try:
                return pw.chromium.launch(headless=headless, slow_mo=slow_mo, channel="chrome")
            except Exception:
                pass
            # Fallback 2: System Edge channel
            try:
                return pw.chromium.launch(headless=headless, slow_mo=slow_mo, channel="msedge")
            except Exception:
                pass
            # Fallback 3: Explicit Chrome binary
            try:
                from src.tools.chrome_manager import find_chrome_executable
                chrome_exe = find_chrome_executable()
                if chrome_exe and os.path.exists(chrome_exe):
                    return pw.chromium.launch(headless=headless, slow_mo=slow_mo, executable_path=chrome_exe)
            except Exception:
                pass
        raise e


def browser_open(url: str, visible: bool = True, profile: bool = False,
                 profile_dir: Optional[str] = None, browser: str = "chromium",
                 cdp_url: Optional[str] = None) -> str:
    """Launch (or attach to) a browser and navigate to a URL.

    visible=True (default): opens a real, watchable window on the desktop
    (actions are executed visibly so you can follow along).
    visible=False: invisible headless browser, fastest.
    profile=True: use the persistent Meridian profile (logins/cookies stick
    across sessions) so the agent can act AS YOU on logged-in sites —
    YouTube Music playback, Google Forms, LinkedIn, etc. Log in once with
    visible=True + profile=True and later sessions reuse it. The profile is
    dedicated to the agent (not your daily Chrome profile) so it never
    clashes with an already-running Chrome. Real Google Chrome is preferred
    when installed (better media codecs); otherwise bundled Chromium is used.
    browser: "chromium" (default), "chrome" (installed Google Chrome),
    "edge" (installed Microsoft Edge), or "firefox".
    cdp_url: attach to YOUR already-running browser instead of launching one,
    e.g. "http://localhost:9222" after starting Chrome with
    --remote-debugging-port=9222. The agent then drives your real window with
    all your logins; closing the session only closes the agent's tab, never
    your browser. cdp_url overrides browser/profile/visible.
    """
    global _playwright, _browser, _page, _page_ctx, _viewport_w, _viewport_h
    global _session_headless, _session_profile, _session_browser, _session_attached
    global _session_cdp_url
    try:
        from playwright.sync_api import sync_playwright
        if cdp_url:
            want = ("attached", cdp_url)
        else:
            if browser not in ("chromium", "chrome", "edge", "firefox"):
                return (
                    f"Error: unknown browser '{browser}'. "
                    f"Choose one of: chromium, chrome, edge, firefox — or pass "
                    f"cdp_url to attach to a running browser."
                )
            want = (browser, None)
        headless = not visible
        want_profile = None if cdp_url else (profile_dir or (_meridian_profile_dir() if profile else None))
        if _session_headless is not None and (
            _session_headless != headless
            or _session_profile != want_profile
            or _session_browser != want[0]
            or (want[0] == "attached" and _session_cdp_url != cdp_url)
        ):
            # Mode/profile/engine/target switch requires a fresh session.
            _close_session()
        # Resolve viewport BEFORE launch: persistent contexts take it at
        # launch time, not per page.
        try:
            from database import get_user_profile
            vw = get_user_profile("browser_viewport_width")
            vh = get_user_profile("browser_viewport_height")
            viewport_w = int(vw) if vw else _viewport_w
            viewport_h = int(vh) if vh else _viewport_h
        except Exception:
            viewport_w = _viewport_w
            viewport_h = _viewport_h

        _viewport_w = viewport_w
        _viewport_h = viewport_h

        if not _playwright:
            _playwright = sync_playwright().start()
            if cdp_url:
                try:
                    _browser = _playwright.chromium.connect_over_cdp(cdp_url, timeout=15000)
                except Exception as e:
                    # Don't leak the driver process on a failed attach.
                    _close_session()
                    return (
                        "Failed to attach to browser at "
                        f"'{cdp_url}': {e}. Start Chrome/Edge with "
                        "--remote-debugging-port=9222 first, e.g.: "
                        "chrome.exe --remote-debugging-port=9222"
                    )
                ctxs = _browser.contexts
                _page_ctx = ctxs[0] if ctxs else _browser.new_context()
                _session_attached = True
                _session_browser = "attached"
                _session_cdp_url = cdp_url
                _session_profile = None
            elif want_profile:
                try:
                    from src.tools.chrome_manager import find_chrome_executable
                    chrome_path = find_chrome_executable()
                except Exception:
                    chrome_path = None
                import os as _os
                launch_kw = {
                    "user_data_dir": want_profile,
                    "headless": headless,
                    "slow_mo": 300 if not headless else 0,
                    "viewport": {"width": viewport_w, "height": viewport_h},
                    "args": [
                        "--no-sandbox",
                        "--disable-blink-features=AutomationControlled",
                        "--autoplay-policy=no-user-gesture-required",
                    ],
                }
                if chrome_path and _os.path.exists(chrome_path):
                    launch_kw["executable_path"] = chrome_path

                try:
                    _browser = _playwright.chromium.launch_persistent_context(**launch_kw)  # type: ignore
                except Exception as _pe:
                    _p_err = str(_pe).lower()
                    if "executable doesn't exist" in _p_err or "playwright install" in _p_err:
                        _launched = False
                        for _ch in ["chrome", "msedge"]:
                            try:
                                _fb_kw = dict(launch_kw)
                                _fb_kw.pop("executable_path", None)
                                _fb_kw["channel"] = _ch
                                _browser = _playwright.chromium.launch_persistent_context(**_fb_kw)  # type: ignore
                                _launched = True
                                break
                            except Exception:
                                continue
                        if not _launched:
                            raise _pe
                    else:
                        raise _pe
                except Exception as e:
                    err = str(e)
                    if "profile" in err.lower() and ("in use" in err.lower() or "already" in err.lower()):
                        # Don't leak the driver process on a locked profile.
                        _close_session()
                        return (
                            "Failed to open persistent profile: it is locked by another "
                            "running browser. Close Chrome windows using that profile, or "
                            f"pass a different profile_dir. Details: {e}"
                        )
                    raise
                _session_profile = want_profile
                _session_browser = browser
            else:
                _browser = _launch_engine(_playwright, browser, headless)
                _session_profile = None
                _session_browser = browser
            _session_headless = headless

        if not _page_alive():
            _page = _mint_page()
            
        try:
            _page.goto(url, wait_until="domcontentloaded", timeout=25000)
        except Exception as e:
            # BUG-34 fix: reset _page to None so the next call creates a fresh page
            # instead of reusing this broken/stale Playwright page.
            _page = None
            return f"Failed to navigate browser: {e}"

        if _session_attached:
            mode = "your running browser (attached tab)"
        elif want_profile:
            mode = (
                f"visible {browser} window with persistent Meridian profile"
                if visible else f"headless {browser} with persistent Meridian profile"
            )
        else:
            mode = f"visible desktop {browser} window" if visible else f"headless {browser} context"
        return f"Successfully opened {mode} and navigated to: {url}"
    except ImportError:
        return "Error: 'playwright' Python library is not installed or configured. Please install it."
    except Exception as e:
        # If launch itself failed (_session_headless never set), don't leak
        # the driver process. Navigation failures keep the session alive.
        if _session_headless is None and _playwright is not None:
            try:
                _close_session()
            except Exception:
                pass
        return f"Failed to navigate browser: {e}"

def browser_screenshot(output_path: str = "browser.png") -> str:
    """Capture current browser viewport with visual outlines and indicators on interactable elements."""
    global _page
    if not _page_alive():
        return _NOT_OPEN_MSG
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
    if not _page_alive() or not ollama:
        return None

    import tempfile
    temp_path = os.path.join(tempfile.gettempdir(), "meridian_browser_click.png")
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
    """Vision-locate element matching description, or fall back to DOM selector / text matching."""
    global _page
    if not _page_alive():
        return _NOT_OPEN_MSG
        
    coords = _locate_element_by_vision(description)
    if coords:
        x, y = coords
        try:
            _page.mouse.click(x, y)
            return f"Visually clicked coordinate ({x}, {y}) corresponding to '{description}'."
        except Exception as e:
            pass

    # DOM Selector / Text Matching Fallback
    dom_strategies = [
        description,
        f"text={description}",
        f"button:has-text('{description}')",
        f"a:has-text('{description}')",
        f"[aria-label='{description}']",
        f"[title='{description}']",
        f"[placeholder='{description}']"
    ]
    for strat in dom_strategies:
        try:
            if _page.is_visible(strat, timeout=500):
                _page.click(strat, timeout=3000)
                return f"Visually or via DOM clicked element matching '{description}' via DOM strategy '{strat}'."
        except Exception:
            continue


    return f"Failed to locate or click element matching '{description}' via vision or DOM."

def browser_type_in(description: str, text: str, delay: int = 50) -> str:
    """Vision-locate or DOM-locate element matching description, click it, and type text."""
    global _page
    if not _page_alive():
        return _NOT_OPEN_MSG
        
    coords = _locate_element_by_vision(description)
    if coords:
        x, y = coords
        try:
            _page.mouse.click(x, y)
            time.sleep(0.1)
            _page.keyboard.type(text, delay=delay)
            return f"Visually selected field '{description}' at ({x}, {y}) and typed key buffer (delay={delay}ms)."
        except Exception:
            pass

    # DOM Input Fill Fallback
    dom_strategies = [
        description,
        f"input[name='{description}']",
        f"input[placeholder*='{description}']",
        f"textarea[name='{description}']",
        f"[aria-label='{description}']",
        f"text={description}"
    ]
    for strat in dom_strategies:
        try:
            if _page.is_visible(strat, timeout=500):
                _page.fill(strat, text, timeout=3000)
                return f"Filled input field '{description}' via DOM strategy '{strat}'."
        except Exception:
            continue


    return f"Failed to locate or type into field matching '{description}' via vision or DOM."

def browser_get_text() -> str:
    """Extract all text contents from the current page viewport."""
    global _page
    if not _page_alive():
        return _NOT_OPEN_MSG
    try:
        text = _page.evaluate("document.body.innerText")
        return text if text.strip() else "Page contains no readable text."
    except Exception as e:
        return f"Failed to extract browser text: {e}"


def browser_press_key(key: str) -> str:
    """Presses a keyboard key on the active browser page (e.g. 'Enter', 'Escape', 'Tab', 'ArrowDown')."""
    global _page
    if not _page_alive():
        if not _ensure_active_page():
            return _NOT_OPEN_MSG
    try:
        _page.keyboard.press(key)
        return f"Pressed key '{key}' on active browser page."
    except Exception as e:
        return f"Failed to press key '{key}': {e}"


def browser_scroll(direction: str = "down", amount: int = 500) -> str:
    """Scrolls the active browser window up or down by a given pixel amount."""
    global _page
    if not _page_alive():
        if not _ensure_active_page():
            return _NOT_OPEN_MSG
    try:
        y_delta = amount if direction.lower() == "down" else -amount
        _page.evaluate(f"window.scrollBy(0, {y_delta});")
        return f"Scrolled {direction} by {amount}px."
    except Exception as e:
        return f"Failed to scroll browser: {e}"


def browser_wait(seconds: float = 2.0) -> str:
    """Waits for specified seconds for page content, network requests, or animations to settle."""
    global _page
    if not _page_alive():
        if not _ensure_active_page():
            return _NOT_OPEN_MSG
    try:
        _page.wait_for_timeout(float(seconds) * 1000.0)
        return f"Waited {seconds}s for browser state to settle."
    except Exception as e:
        return f"Failed waiting on browser: {e}"


def browser_get_interactive_elements() -> List[Dict[str, Any]]:
    """Extracts all clickable, input, link, and action elements visible in current viewport."""
    global _page
    if not _page_alive():
        if not _ensure_active_page():
            return []
    script = """
    () => {
        const items = [];
        const elements = document.querySelectorAll('button, a[href], input, textarea, select, [role="button"], [role="link"], [role="textbox"], [onclick]');
        let idx = 1;
        elements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.width > 2 && rect.height > 2 &&
                rect.bottom >= 0 && rect.top <= window.innerHeight &&
                rect.right >= 0 && rect.left <= window.innerWidth) {
                const style = window.getComputedStyle(el);
                if (style.display !== 'none' && style.visibility !== 'hidden' && style.opacity !== '0') {
                    let text = (el.innerText || el.value || el.placeholder || el.getAttribute('aria-label') || el.title || '').trim().replace(/\\s+/g, ' ');
                    text = text.substring(0, 100);
                    
                    let sel = '';
                    if (el.id) {
                        sel = '#' + CSS.escape(el.id);
                    } else if (el.name) {
                        sel = `${el.tagName.toLowerCase()}[name="${CSS.escape(el.name)}"]`;
                    } else if (el.placeholder) {
                        sel = `${el.tagName.toLowerCase()}[placeholder*="${CSS.escape(el.placeholder)}"]`;
                    } else if (el.getAttribute('aria-label')) {
                        sel = `[aria-label="${CSS.escape(el.getAttribute('aria-label'))}"]`;
                    } else {
                        sel = el.tagName.toLowerCase();
                    }
                    
                    items.push({
                        index: idx,
                        tag: el.tagName.toLowerCase(),
                        text: text,
                        selector: sel,
                        x: Math.round(rect.left + rect.width / 2),
                        y: Math.round(rect.top + rect.height / 2),
                        type: el.type || ''
                    });
                    idx++;
                }
            }
        });
        return items;
    }
    """
    try:
        res = _page.evaluate(script)
        return res if isinstance(res, list) else []
    except Exception as e:
        print("[Browser Use] Failed to extract interactive elements:", e)
        return []


def browser_highlight_elements() -> str:
    """Overlays visual Set-of-Marks badges [1], [2], [3] directly over elements on active screen."""
    global _page
    if not _page_alive():
        if not _ensure_active_page():
            return _NOT_OPEN_MSG
    script = """
    () => {
        document.querySelectorAll('.meridian-mark-badge').forEach(b => b.remove());
        document.querySelectorAll('.meridian-mark-outline').forEach(o => o.classList.remove('meridian-mark-outline'));
        
        let style = document.getElementById('meridian-mark-style');
        if (!style) {
            style = document.createElement('style');
            style.id = 'meridian-mark-style';
            style.innerHTML = `
                .meridian-mark-outline { outline: 2px solid #ff5722 !important; outline-offset: 1px !important; }
                .meridian-mark-badge {
                    background: #ff5722 !important;
                    color: #ffffff !important;
                    font-size: 11px !important;
                    font-weight: 900 !important;
                    font-family: monospace !important;
                    padding: 1px 4px !important;
                    border-radius: 3px !important;
                    position: absolute !important;
                    z-index: 2147483647 !important;
                    pointer-events: none !important;
                    box-shadow: 0 1px 4px rgba(0,0,0,0.5) !important;
                }
            `;
            document.head.appendChild(style);
        }
        
        const elements = document.querySelectorAll('button, a[href], input, textarea, select, [role="button"], [role="link"], [role="textbox"], [onclick]');
        let idx = 1;
        elements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.width > 2 && rect.height > 2 &&
                rect.bottom >= 0 && rect.top <= window.innerHeight &&
                rect.right >= 0 && rect.left <= window.innerWidth) {
                const style = window.getComputedStyle(el);
                if (style.display !== 'none' && style.visibility !== 'hidden' && style.opacity !== '0') {
                    el.classList.add('meridian-mark-outline');
                    el.setAttribute('data-meridian-index', String(idx));
                    const badge = document.createElement('span');
                    badge.className = 'meridian-mark-badge';
                    badge.innerText = `[${idx}]`;
                    badge.style.top = `${rect.top + window.scrollY}px`;
                    badge.style.left = `${rect.left + window.scrollX}px`;
                    document.body.appendChild(badge);
                    idx++;
                }
            }
        });
        return idx - 1;
    }
    """
    try:
        count = _page.evaluate(script)
        return f"Highlighted {count} interactive elements on active screen."
    except Exception as e:
        return f"Failed to highlight elements: {e}"


def browser_click_element(index_or_selector: str) -> str:
    """Clicks an element by numerical index '[1]', '1', or CSS / text selector."""
    global _page
    if not _page_alive():
        if not _ensure_active_page():
            return _NOT_OPEN_MSG

    clean = index_or_selector.strip().strip("[]")
    if clean.isdigit():
        target_idx = int(clean)
        elements = browser_get_interactive_elements()
        match = next((el for el in elements if el.get("index") == target_idx), None)
        if match:
            sel = match.get("selector")
            if sel:
                try:
                    if _page.is_visible(sel, timeout=500):
                        _page.click(sel, timeout=3000)
                        return f"Clicked element [{target_idx}] ({match.get('text', '')}) via selector '{sel}'."
                except Exception:
                    pass
            try:
                x, y = match.get("x", 0), match.get("y", 0)
                if x > 0 and y > 0:
                    _page.mouse.click(x, y)
                    return f"Clicked element [{target_idx}] ({match.get('text', '')}) at coordinates ({x}, {y})."
            except Exception as e:
                return f"Failed clicking element [{target_idx}]: {e}"

    return browser_find_and_click(index_or_selector)


def browser_type_element(index_or_selector: str, text: str, press_enter: bool = False, delay: int = 30) -> str:
    """Types text into an element by numerical index '[1]', '1', or CSS / text selector, optionally pressing Enter."""
    global _page
    if not _page_alive():
        if not _ensure_active_page():
            return _NOT_OPEN_MSG

    clean = index_or_selector.strip().strip("[]")
    if clean.isdigit():
        target_idx = int(clean)
        elements = browser_get_interactive_elements()
        match = next((el for el in elements if el.get("index") == target_idx), None)
        if match:
            sel = match.get("selector")
            if sel:
                try:
                    if _page.is_visible(sel, timeout=500):
                        _page.fill(sel, text, timeout=3000)
                        if press_enter:
                            _page.keyboard.press("Enter")
                        return f"Typed into element [{target_idx}] ({match.get('text', '')}) via selector '{sel}'."
                except Exception:
                    pass
            try:
                x, y = match.get("x", 0), match.get("y", 0)
                if x > 0 and y > 0:
                    _page.mouse.click(x, y)
                    _page.wait_for_timeout(100)
                    _page.keyboard.type(text, delay=delay)
                    if press_enter:
                        _page.keyboard.press("Enter")
                    return f"Typed into element [{target_idx}] at coordinates ({x}, {y})."
            except Exception as e:
                return f"Failed typing into element [{target_idx}]: {e}"

    res = browser_type_in(index_or_selector, text, delay=delay)
    if press_enter and _page:
        try:
            _page.keyboard.press("Enter")
        except Exception:
            pass
    return res


def browser_close() -> str:
    """Close the active browser session (headless or visible).

    Attached sessions only close the agent's tab — your own browser stays open.
    """
    global _playwright, _browser, _page
    if not _browser:
        return "No active browser session to close."
    attached = _session_attached
    try:
        _close_session()
        if attached:
            return "Detached from your browser safely (your browser was left running)."
        return "Closed browser environment safely."
    except Exception as e:
        return f"Failed to close browser: {e}"


def _page_alive() -> bool:
    """True when a usable Playwright page exists (guards against stale pages)."""
    global _page
    if not _page:
        return False
    try:
        closed = _page.is_closed()
        if closed is True:
            _page = None
            return False
    except Exception:
        _page = None
        return False
    return True


def _ensure_active_page(default_url: str = "https://www.google.com") -> bool:
    """Auto-recovers and launches visible browser session if uninitialized or closed."""
    global _page
    if not _page_alive():
        browser_open(default_url, visible=True)
    return _page_alive()



_NOT_OPEN_MSG = "Error: Browser is not open (or the page went stale). Call browser_open first."



# --- Scraping tools live in web_scraper.py (re-exported here for compat) ---
from src.tools.web_scraper import (
    sanitize_web_content_injection,
    _BROWSER_UA,
    _fetch_arxiv_cards,
    _fetch_github_cards,
    generate_tech_market_digest,
    _is_public_http_url,
    parse_youtube_content,
    scrape_urls,
    scrape_table,
    schedule_scrape,
)  # noqa: F401
