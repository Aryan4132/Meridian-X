"""
browser_use_agent.py — Autonomous Browser-Use Agent for Meridian-X
Executes multi-step browser tasks on live, visible desktop browser sessions
using Set-of-Marks visual overlay badges, accessibility tree indexing, and
interactive Playwright actions.
"""

import os
import re
import json
import time
from typing import Dict, Any, Optional, List

from src.tools.web_browser import (
    browser_open,
    browser_get_text,
    browser_press_key,
    browser_scroll,
    browser_wait,
    browser_get_interactive_elements,
    browser_highlight_elements,
    browser_click_element,
    browser_type_element,
    _page_alive,
)


def _get_page_url() -> str:
    """Returns current page URL safely."""
    try:
        from src.tools import web_browser
        if web_browser._page and not web_browser._page.is_closed():
            return web_browser._page.url or ""
    except Exception:
        pass
    return ""


def _get_page_title() -> str:
    """Returns current page title safely."""
    try:
        from src.tools import web_browser
        if web_browser._page and not web_browser._page.is_closed():
            return web_browser._page.title() or ""
    except Exception:
        pass
    return ""


def _infer_start_url(task: str) -> str:
    """Extracts or infers a sensible start URL from user's natural language goal."""
    lower = task.lower()
    
    # 1. Match explicit URLs in task
    url_match = re.search(r'https?://[^\s\'"<>]+', task)
    if url_match:
        return url_match.group(0)

    # 2. Match domain-like patterns (e.g. youtube.com, github.com, reddit.com)
    domain_match = re.search(r'\b([a-zA-Z0-9-]+\.(?:com|org|io|net|edu|ai|co|gov))\b', task)
    if domain_match:
        return f"https://{domain_match.group(1)}"

    # 3. Known keywords
    if "youtube" in lower:
        return "https://www.youtube.com"
    if "github" in lower:
        return "https://www.github.com"
    if "wikipedia" in lower:
        return "https://www.wikipedia.org"
    if "reddit" in lower:
        return "https://www.reddit.com"
    if "amazon" in lower:
        return "https://www.amazon.com"
    if "twitter" in lower or " x.com" in lower:
        return "https://www.x.com"

    # Default to Google for general queries/searches
    return "https://www.google.com"


class BrowserUseAgent:
    """Autonomous agent driving Playwright browser sessions with Set-of-Marks perception."""

    def __init__(self, max_steps: int = 10):
        self.max_steps = max(1, min(max_steps, 25))

    def _plan_with_llm(self, task: str, url: str, title: str, elements: List[Dict[str, Any]], page_text: str) -> Optional[Dict[str, Any]]:
        """Invokes configured LLM (via call_llm or local Ollama) with structured Set-of-Marks prompt to decide next step."""
        elements_summary = []
        for el in elements[:30]:
            tag = el.get("tag", "")
            text = el.get("text", "")
            idx = el.get("index")
            elements_summary.append(f"[{idx}] <{tag}>: {text}")

        prompt = f"""You are the Browser-Use Agent. Your goal is: "{task}".
Current Page URL: {url}
Current Page Title: {title}

Visible Interactive Elements:
{chr(10).join(elements_summary) if elements_summary else "No interactable elements found."}

Visible Page Text Snippet:
{page_text[:1200]}

Decide the SINGLE next best browser action to make progress toward the goal.
Respond ONLY with a JSON object in one of the following formats:
- Type text into field: {{"action": "type", "target": "1", "text": "search query", "press_enter": true}}
- Click element: {{"action": "click", "target": "2"}}
- Press key: {{"action": "press_key", "key": "Enter"}}
- Scroll page: {{"action": "scroll", "direction": "down", "amount": 500}}
- Wait: {{"action": "wait", "seconds": 2}}
- Finished: {{"action": "finish", "result": "Detailed answer/summary of what was achieved"}}

Do NOT include markdown formatting or explanations. JSON only:"""

        raw = ""
        # 1. Try unified LLM provider first (supports OpenAI, Anthropic, Gemini, Groq, Ollama)
        try:
            import asyncio
            import concurrent.futures
            from src.core.llm_provider import call_llm

            async def _invoke():
                return await call_llm([{"role": "user", "content": prompt}], temperature=0.1)

            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = None

            if loop and loop.is_running():
                with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
                    raw = pool.submit(asyncio.run, _invoke()).result(timeout=15.0)
            else:
                raw = asyncio.run(_invoke())
        except Exception as e:
            # 2. Resilient fallback to direct local Ollama with 15s timeout
            try:
                import ollama
                from database import get_ollama_client_host, get_brain_model

                client = ollama.Client(host=get_ollama_client_host(), timeout=15.0)
                model = get_brain_model()
                res = client.generate(model=model, prompt=prompt)
                raw = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
            except Exception as ex:
                print(f"[BrowserUseAgent] LLM planning failed: {e}; Ollama fallback failed: {ex}")
                return None

        if raw:
            try:
                clean = re.sub(r"^```(?:json)?", "", raw.strip()).rstrip("`").strip()
                match = re.search(r'\{.*\}', clean, re.DOTALL)
                if match:
                    return json.loads(match.group(0))
            except Exception as pe:
                print(f"[BrowserUseAgent] JSON parse error: {pe}")

        return None

    def _plan_heuristic(self, task: str, url: str, elements: List[Dict[str, Any]], page_text: str, step: int) -> Dict[str, Any]:
        """Deterministic heuristic fallback when LLM planner is unavailable."""
        lower_task = task.lower()
        
        # Step 1: On search engine homepage, find search input and type query
        if step == 1 and ("google.com" in url or "youtube.com" in url or "wikipedia.org" in url or "github.com" in url):
            input_el = next((el for el in elements if el.get("tag") in ("input", "textarea") and el.get("type") not in ("hidden", "submit")), None)
            if input_el:
                # Extract clean search query
                clean_q = re.sub(r'^(?:search\s+(?:for\s+)?|find\s+|look\s+up\s+|go\s+to\s+)', '', task, flags=re.I).strip()
                clean_q = re.sub(r'\s+(?:on|in)\s+(?:google|youtube|wikipedia|github|web).*$', '', clean_q, flags=re.I).strip()
                return {
                    "action": "type",
                    "target": str(input_el.get("index")),
                    "text": clean_q or task,
                    "press_enter": True
                }

        # Step 2: Click first relevant result link
        if step == 2 and ("search" in url or "results" in url):
            link = next((el for el in elements if el.get("tag") == "a" and len(el.get("text", "")) > 10), None)
            if link:
                return {"action": "click", "target": str(link.get("index"))}

        # Step 3 or later: Finish with extracted content
        snippet = page_text[:800] if page_text else "Page loaded successfully."
        return {
            "action": "finish",
            "result": f"Successfully completed browser navigation for task '{task}'. Extracted summary: {snippet}"
        }

    def run(self, task: str, start_url: Optional[str] = None, visible: bool = True) -> Dict[str, Any]:
        """Executes autonomous multi-step browser loop."""
        initial_url = start_url or _infer_start_url(task)
        
        # Launch/attach browser visibly with fallback resilience
        open_res = browser_open(initial_url, visible=visible)
        if isinstance(open_res, str) and (open_res.startswith("Error:") or open_res.startswith("Failed")):
            for fb in ["chrome", "edge"]:
                open_res = browser_open(initial_url, visible=visible, browser=fb)
                if not (isinstance(open_res, str) and (open_res.startswith("Error:") or open_res.startswith("Failed"))):
                    break
        browser_wait(1.5)

        history: List[Dict[str, Any]] = []
        final_result = ""

        for step in range(1, self.max_steps + 1):
            try:
                from src.core.loop import _interrupt_event
                if _interrupt_event.is_set():
                    final_result = "Browser navigation interrupted by user."
                    break
            except Exception:
                pass

            curr_url = _get_page_url()
            curr_title = _get_page_title()

            # 1. Inject visual Set-of-Marks badges onto active screen
            browser_highlight_elements()
            browser_wait(0.3)

            # 2. Extract DOM interactive element tree & text
            elements = browser_get_interactive_elements()
            page_text = browser_get_text()

            # 3. Decide action (LLM with heuristic fallback)
            decision = self._plan_with_llm(task, curr_url, curr_title, elements, page_text)
            if not decision or not isinstance(decision, dict) or "action" not in decision:
                decision = self._plan_heuristic(task, curr_url, elements, page_text, step)

            action = decision.get("action", "finish")
            step_record = {
                "step": step,
                "url": curr_url,
                "title": curr_title,
                "decision": decision,
                "timestamp": time.time(),
            }

            if action == "finish":
                final_result = decision.get("result", page_text[:1000])
                step_record["status"] = "finished"
                history.append(step_record)
                break

            elif action == "click":
                target = decision.get("target", "1")
                res = browser_click_element(target)
                step_record["execution"] = res
                browser_wait(1.5)

            elif action == "type":
                target = decision.get("target", "1")
                text = decision.get("text", "")
                press_enter = decision.get("press_enter", False)
                res = browser_type_element(target, text, press_enter=press_enter)
                step_record["execution"] = res
                browser_wait(2.0)

            elif action == "press_key":
                key = decision.get("key", "Enter")
                res = browser_press_key(key)
                step_record["execution"] = res
                browser_wait(1.5)

            elif action == "scroll":
                direction = decision.get("direction", "down")
                amount = int(decision.get("amount", 500))
                res = browser_scroll(direction=direction, amount=amount)
                step_record["execution"] = res
                browser_wait(1.0)

            elif action == "wait":
                secs = float(decision.get("seconds", 2.0))
                res = browser_wait(secs)
                step_record["execution"] = res

            history.append(step_record)

        if not final_result:
            final_result = browser_get_text()[:1000]

        return {
            "status": "success",
            "task": task,
            "steps_taken": len(history),
            "final_url": _get_page_url(),
            "page_title": _get_page_title(),
            "result": final_result,
            "steps_log": history,
        }


def browser_use_task(task: str, start_url: Optional[str] = None, max_steps: int = 10, visible: bool = True) -> str:
    """Autonomous Browser-Use tool: executes high-level web instructions live in browser."""
    agent = BrowserUseAgent(max_steps=max_steps)
    res = agent.run(task, start_url=start_url, visible=visible)
    return json.dumps(res, indent=2)
