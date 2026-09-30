"""
consensus_engine.py — Decoupled Intelligent Consensus Debate Engine
Orchestrates QA Reviewer vs Lead Coder consensus verification.
Applies smart gating to bypass debate for low-risk conversational queries,
preserving sub-500ms voice TTFA while maintaining rigorous checks on code mutations.
"""

import re
import time
import uuid
import json
import logging
from typing import Tuple, List, Dict, Any, Optional

logger = logging.getLogger("meridian.consensus")


def build_consensus_qa_prompt(response_text: str) -> str:
    """Builds QA Reviewer prompt with dynamic system date and live web search evidence rules."""
    from datetime import datetime
    current_date_str = datetime.now().strftime("%Y-%m-%d")
    return (
        f"Current System Date: {current_date_str}.\n"
        "You are the QA Reviewer Agent. Critique the proposed response below.\n"
        "TEMPORAL AND SEARCH EVIDENCE RULES:\n"
        f"- Dates up to and including {current_date_str} represent real-time current events.\n"
        f"- Do NOT flag dates on or before {current_date_str} as 'future dates' or 'temporal hallucinations'.\n"
        "- When tools like `search_news` or `search_web` return recent facts or real-time data dated up to the current date, treat those retrieved facts as verified truth.\n"
        "- Do NOT override live search tool evidence using pre-trained static knowledge cutoff assumptions.\n"
        "Do NOT write any introduction or conclusion, just write a bullet list of issues.\n\n"
        f"Proposed Response:\n{response_text}"
    )


def build_consensus_coder_prompt(response_text: str, critique: str) -> str:
    """Builds Lead Coder prompt with dynamic system date context."""
    from datetime import datetime
    current_date_str = datetime.now().strftime("%Y-%m-%d")
    return (
        f"Current System Date: {current_date_str}.\n"
        "You are the Lead Coder Agent. Refine the proposed response based on the QA Reviewer's critique.\n"
        f"Dates on or before {current_date_str} represent current real-time events. Do NOT revert real-time search facts into defensive refusal messages.\n"
        "Return ONLY the final JSON response block with keys 'chat', 'speech', and 'lang'. No explanation, no markdown.\n\n"
        f"Original Response:\n{response_text}\n\n"
        f"Critique:\n{critique}"
    )


def filter_temporal_false_positives(critique: str, current_date_str: str = "", executed_search_tool: bool = False) -> Tuple[str, bool]:
    """Detects and filters out false-positive temporal hallucination critiques
    when current search tool evidence was used or dates are on/before current system date.
    Returns (cleaned_critique, is_false_positive).
    """
    if not critique:
        return critique, False

    if not current_date_str:
        from datetime import datetime
        current_date_str = datetime.now().strftime("%Y-%m-%d")

    current_year = current_date_str.split("-")[0]
    critique_lower = critique.lower()

    temporal_keywords = [
        "temporal error", "future date", "fabricating \"current\" events",
        "fabricating current events", "temporal hallucination", "hallucination/temporal error",
        "future year", "is a future date"
    ]

    has_temporal_flag = any(kw in critique_lower for kw in temporal_keywords)
    mentions_current_year = current_year in critique

    if has_temporal_flag and (executed_search_tool or mentions_current_year):
        lines = critique.split("\n")
        remaining_lines = []
        for line in lines:
            line_l = line.lower()
            if any(kw in line_l for kw in temporal_keywords):
                continue
            remaining_lines.append(line)

        cleaned = "\n".join(remaining_lines).strip()
        return cleaned, True

    return critique, False


def should_run_debate(
    tool_calls: Optional[List[Any]] = None,
    goal: str = "",
    finish_text: str = "",
    is_voice: bool = False,
    mode: str = "DIRECT"
) -> bool:
    """Smart Gate: Determines whether consensus debate is strictly necessary.
    
    Returns False (bypasses debate, saving 2-6s latency) for:
    - Voice queries / voice mode (preserves sub-500ms TTFA)
    - Greetings / conversational chit-chat
    - Read-only status checks and simple Q&A without code
    
    Returns True ONLY for:
    - High-stakes mutating tools (file modifications, system execution)
    - Responses containing substantial code blocks (>150 chars)
    - Multi-step tool workflows (>=2 tool calls)
    - Explicit code review, audit, or security analysis requests
    """
    # 1. Voice queries bypass debate for speed
    if is_voice:
        return False

    # 2. Check for explicit code review or audit keywords in user goal
    goal_clean = (goal or "").strip().lower()
    audit_keywords = {"code review", "review this code", "audit", "find bugs", "security review", "verify code", "refactor"}
    if any(k in goal_clean for k in audit_keywords):
        return True

    # 3. Check tool calls for mutations or multi-step execution
    MUTATING_TOOLS = {
        "write_to_file", "replace_file_content", "multi_replace_file_content",
        "run_command", "git_commit", "git_push", "delete_file",
        "dev_automation", "format_code", "execute_terminal", "browser_use_task"
    }
    executed_names: List[str] = []
    if tool_calls:
        for tc in tool_calls:
            if isinstance(tc, str):
                executed_names.append(tc)
            elif isinstance(tc, dict):
                executed_names.append(tc.get("name") or tc.get("tool") or "")
            elif hasattr(tc, "name"):
                executed_names.append(getattr(tc, "name", ""))

    if any(t in MUTATING_TOOLS for t in executed_names):
        return True

    if len(executed_names) >= 2:
        return True

    # 4. Skip debate for greetings and chit-chat if no modifying tools were executed
    GREETINGS = {
        "hi", "hello", "hey", "hola", "namaste", "good morning", "good evening",
        "good afternoon", "thanks", "thank you", "bye", "goodbye", "who are you",
        "what can you do", "help"
    }
    if goal_clean in GREETINGS or any(goal_clean.startswith(g + " ") for g in GREETINGS):
        return False

    # 5. Skip debate for read-only status checks
    READ_ONLY_QUERIES = [
        "what time is it", "current time", "what day is it", "date today",
        "system status", "health check", "battery", "weather", "ping"
    ]
    if any(q in goal_clean for q in READ_ONLY_QUERIES):
        return False

    # 6. Check if response contains substantial code blocks
    if finish_text:
        has_code_block = bool(re.search(r'```(?:python|ts|tsx|js|javascript|json|html|css|bash|sh|rust|go|c|cpp)\b', finish_text, re.IGNORECASE))
        if has_code_block and len(finish_text) > 150:
            return True

    return False


# Legacy alias
should_trigger_consensus_debate = should_run_debate


async def run_debate(
    initial_finish: str,
    active_model: str,
    auditor_model: str,
    user_lang: str = "en",
    client: Any = None,
    has_search: bool = False,
    active_debates: Optional[Dict[str, Any]] = None,
    emit_thought: Optional[Any] = None
) -> Tuple[str, str, str]:
    """Runs Coder vs QA Reviewer consensus debate.
    Returns (debated_finish_text, critique, debate_key).
    """
    import asyncio
    from src.core.llm_provider import call_llm
    from src.core.loop_parser import process_final_response

    qa_prompt = build_consensus_qa_prompt(initial_finish)
    qa_task = call_llm([{"role": "user", "content": qa_prompt}], model=auditor_model, temperature=0.2)
    fmt_task = process_final_response(initial_finish, user_lang, client)

    corrected_finish, qa_res = await asyncio.gather(fmt_task, qa_task)
    critique = (qa_res or "").strip()
    if critique.startswith("Error:"):
        critique = ""

    # Filter false-positive temporal error critiques
    critique, is_false_pos = filter_temporal_false_positives(critique, executed_search_tool=has_search)

    if emit_thought:
        await emit_thought(f"[Consensus Debate - QA Reviewer]: Critique generated:\n{critique if critique else '(No relevant issues detected)'}")

    if critique:
        coder_prompt = build_consensus_coder_prompt(corrected_finish, critique)
        refined = await call_llm([{"role": "user", "content": coder_prompt}], model=active_model, temperature=0.5)
        refined = (refined or "").strip()
        if refined.startswith("```"):
            refined = refined.strip("`").replace("json\n", "").strip()

        try:
            json.loads(refined)
            if has_search and ("apologize" in refined.lower() or "do not have access" in refined.lower()) and not ("apologize" in corrected_finish.lower()):
                debated_finish = corrected_finish
            else:
                debated_finish = await process_final_response(refined, user_lang, client)
        except Exception:
            debated_finish = corrected_finish
    else:
        debated_finish = corrected_finish

    debate_key = f"debate-{uuid.uuid4()}"
    if active_debates is not None:
        active_debates[debate_key] = {
            "draft": corrected_finish,
            "critique": critique,
            "refined": debated_finish
        }

    return debated_finish, critique, debate_key

