"""
loop_planning.py — Hierarchical Task Planning, complexity routing, MCTS candidate scoring, and memory distillation.
"""

import os
import re
import json
import asyncio
import time
from typing import Dict, Any, List, Tuple, Optional, AsyncGenerator

from database import get_auditor_model
from src.core.llm_clients import get_cached_ollama_client


def detect_complex_prompt(prompt: str) -> bool:
    p = prompt.lower()
    complex_words = ["build", "setup", "implement", "deploy", "architecture", "design and create", "create a complete", "pipeline", "scaffold"]
    return len(prompt) > 200 or any(w in p for w in complex_words)


async def decompose_goal_to_checklist(prompt: str, client: Any = None, model: Optional[str] = None) -> List[Dict[str, Any]]:
    if model is None:
        try:
            from database import get_brain_model
            model = get_brain_model()
        except Exception:
            model = get_auditor_model()
    decomp_prompt = (
        "You are the Meridian Project Manager. Decompose the user's goal into a logical list of sub-tasks (maximum 4).\n"
        f"Goal: {prompt}\n\n"
        "Return ONLY a JSON list of tasks, where each task is an object with \"id\" (int) and \"description\" (str). "
        "Do NOT include markdown block wrapping. Example response: [{\"id\": 1, \"description\": \"Create file a.py\"}, {\"id\": 2, \"description\": \"Write tests\"}]"
    )
    try:
        from src.core.llm_provider import call_llm
        text = await asyncio.wait_for(
            call_llm([{"role": "user", "content": decomp_prompt}], model=model),
            timeout=10.0
        )
        text = text.strip()
        if text.startswith("```"):
            text = text.strip("`").replace("json\n", "").strip()
        tasks = json.loads(text)
        if isinstance(tasks, list):
            return tasks
    except Exception as e:
        print("[HTP] Failed to decompose goal, falling back to single loop:", e)
    return []


async def score_candidate_branch(tool_name: str, args_str: str, history: List[Dict[str, str]], client: Any = None, model: Optional[str] = None) -> float:
    if model is None:
        try:
            from database import get_brain_model
            model = get_brain_model()
        except Exception:
            model = get_auditor_model()
    prompt = (
        f"You are the Monte Carlo Tree Search evaluator. Score the proposed action from 0.0 (fails/dangerous/unlikely to succeed) to 1.0 (highly successful/safe/optimal).\n"
        f"Goal/History context length: {len(history)} turns.\n"
        f"Proposed Action: Call tool '{tool_name}' with args: {args_str}\n\n"
        f"Output ONLY the numeric score (e.g. 0.85). Do not include any text or commentary."
    )
    try:
        from src.core.llm_provider import call_llm
        val_str = await call_llm([{"role": "user", "content": prompt}], model=model)
        val_str = val_str.strip()
        score = float(re.findall(r"[-+]?\d*\.\d+|\d+", val_str)[0])
        return min(max(score, 0.0), 1.0)
    except Exception:
        return 0.5


async def run_self_question_check(goal: str, history: List[Dict[str, str]], client: Any = None, model: Optional[str] = None) -> Tuple[bool, str]:
    if model is None:
        try:
            from database import get_brain_model
            model = get_brain_model()
        except Exception:
            model = get_auditor_model()
    check_prompt = (
        f"Goal: {goal}\n"
        f"Recent History turns: {len(history)}.\n"
        "Are the exact paths, parameters, and environment dependencies verified? Or are you about to assume details?\n"
        "Answer ONLY 'YES' if they are verified, or 'NO' if they are not verified."
    )
    try:
        from src.core.llm_provider import call_llm
        ans = await call_llm([{"role": "user", "content": check_prompt}], model=model)
        ans = ans.strip().upper()
        if "NO" in ans:
            return False, "You do not have verified information. You MUST run search or observation commands first (e.g. read_file, dir_list, grep_search) to inspect paths and verify details before making assumptions."
        return True, ""
    except Exception:
        return True, ""


def route_model_by_complexity(prompt: str, brain_model: str, model_source: str = "local") -> str:
    """Assess task complexity and route to a lightweight model for simple requests, or standard brain model for complex reasoning."""
    if model_source == "cloud":
        return brain_model
    p = prompt.lower()
    
    complex_keywords = [
        "refactor", "architect", "design a", "write a full", "complex", "optimize", 
        "security audit", "vulnerability", "performance analysis", "benchmark"
    ]
    if any(k in p for k in complex_keywords) or len(p) > 300:
        print(f"[Model Router] Complex task detected. Routing to brain model: '{brain_model}'")
        return brain_model
        
    simple_keywords = [
        "what is", "current time", "date", "cpu", "ram", "disk", "battery", 
        "temperature", "process", "kill", "ping", "say", "hello", "hi", "clear"
    ]
    if any(k in p for k in simple_keywords):
        try:
            from database import get_user_profile
            sqlite_model = get_user_profile("meridian_auditor_model")
            if sqlite_model:
                print(f"[Model Router] Simple task detected. Routing to fast model: '{sqlite_model}'")
                return str(sqlite_model)
        except Exception:
            pass
        fallback_fast = os.environ.get("MERIDIAN_FAST_MODEL") or get_auditor_model()
        print(f"[Model Router] Simple task detected. Routing to fast fallback model: '{fallback_fast}'")
        return fallback_fast
        
    return brain_model


async def run_memory_summarization_background(ollama_host: str):
    """Distills episodic conversations into facts in the knowledge graph in the background."""
    try:
        from database import get_sqlite_conn
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT id, timestamp, role, content FROM conversations ORDER BY timestamp ASC")
        rows = cursor.fetchall()
        conn.close()
        
        valid_records = [dict(r) for r in rows]
        if len(valid_records) < 20:
            return
            
        distill_set = valid_records[:20]
        
        conversation_log = ""
        for item in distill_set:
            conversation_log += f"{item.get('role', 'user')}: {item.get('content', '')}\n"
            
        client = get_cached_ollama_client(ollama_host)
        prompt = (
            "Analyze the conversation log below. Extract key persistent facts about the user's "
            "preferences, workflows, or project details as a JSON list. "
            "Each item must be: {\"subject\": \"...\", \"predicate\": \"...\", \"object\": \"...\"}\n"
            "Keep facts simple and short. Return ONLY valid JSON array.\n\n"
            f"Log:\n{conversation_log}"
        )
        
        from database import get_brain_model
        fallback_model = get_auditor_model()
        try:
            res = client.generate(model=fallback_model, prompt=prompt)
        except Exception:
            model = get_brain_model()
            res = client.generate(model=model, prompt=prompt)

        text = (res.response if hasattr(res, "response") else res.get("response", "")).strip()

        if text.startswith("```"):
            text = text.strip("`").replace("json\n", "").strip()
            
        try:
            facts = json.loads(text)
            from src.tools.knowledge import kg_add_fact
            for f in facts:
                if f.get("subject") and f.get("predicate") and f.get("object"):
                    kg_add_fact(f["subject"], f["predicate"], f["object"])
            
            conn = get_sqlite_conn()
            cursor = conn.cursor()
            ids_to_delete = [r["id"] for r in distill_set]
            placeholders = ",".join("?" for _ in ids_to_delete)
            cursor.execute(f"DELETE FROM conversations WHERE id IN ({placeholders})", tuple(ids_to_delete))
            conn.commit()
            conn.close()
            print(f"[Memory Summarizer] Distilled {len(distill_set)} episodic turns into facts.")
        except Exception as je:
            print("[Memory Summarizer] JSON parse error on response:", je, text)
    except Exception as e:
        print("[Memory Summarizer] Summarization cycle execution error:", e)


async def run_htp_pipeline(
    prompt: str,
    client: Any,
    brain_model: str,
    ollama_host: str,
    model_source: str,
    api_provider: str,
    run_loop_fn: Any,
    sse_event_fn: Any,
) -> AsyncGenerator[str, None]:
    """Runs Hierarchical Task Planning decomposition, concurrent/sequential worker tasks, and synthesis."""
    yield sse_event_fn("thought", json.dumps({
        "id": f"htp-decomposing-{time.time()}",
        "type": "planning",
        "text": "[Hierarchical Task Planning] Decomposing complex prompt into sub-tasks...",
        "status": "running"
    }))
    checklist = await decompose_goal_to_checklist(prompt, client, model=brain_model)
    if not checklist:
        return

    yield sse_event_fn("thought", json.dumps({
        "id": f"htp-decomposed-{time.time()}",
        "type": "planning",
        "text": f"[Hierarchical Task Planning] Checklist generated:\n" + "\n".join(f"- Task {t['id']}: {t['description']}" for t in checklist),
        "status": "completed"
    }))

    SEQ_KEYWORDS = {"then", "after", "finally", "deploy", "commit", "push", "last"}

    def is_sequential(task_desc: str) -> bool:
        return any(kw in task_desc.lower() for kw in SEQ_KEYWORDS)

    parallel_tasks = [t for t in checklist if not is_sequential(t["description"])]
    sequential_tasks = [t for t in checklist if is_sequential(t["description"])]
    worker_outcomes = []

    async def _run_worker(sub_task: dict) -> tuple:
        task_desc = sub_task["description"]
        worker_prompt = (
            f"Your task is to execute sub-task: '{task_desc}' as part of the overall goal: '{prompt}'. "
            f"Focus only on completing this sub-task and report the results."
        )
        worker_text = ""
        async for event in run_loop_fn(
            prompt=worker_prompt,
            brain_model=brain_model,
            ollama_host=ollama_host,
            model_source=model_source,
            api_provider=api_provider,
            is_worker=True
        ):
            if event.startswith("event: text"):
                for line in event.splitlines():
                    if line.startswith("data: "):
                        worker_text += line[6:]
        return sub_task["id"], worker_text

    if parallel_tasks:
        yield sse_event_fn("thought", json.dumps({
            "id": f"htp-parallel-start-{time.time()}",
            "type": "planning",
            "text": f"[Hierarchical Task Planning] Running {len(parallel_tasks)} independent sub-tasks in parallel...",
            "status": "running"
        }))
        parallel_results = await asyncio.gather(*[_run_worker(t) for t in parallel_tasks])
        for task_id, worker_text in parallel_results:
            worker_outcomes.append(f"Sub-task {task_id} Result: {worker_text}")
            yield sse_event_fn("thought", json.dumps({
                "id": f"htp-task-complete-{task_id}-{time.time()}",
                "type": "planning",
                "text": f"[Hierarchical Task Planning] Sub-task {task_id} completed (parallel).",
                "status": "completed"
            }))

    for sub_task in sequential_tasks:
        task_desc = sub_task["description"]
        yield sse_event_fn("thought", json.dumps({
            "id": f"htp-task-start-{sub_task['id']}-{time.time()}",
            "type": "planning",
            "text": f"[Hierarchical Task Planning] Spawning sequential worker for Sub-task {sub_task['id']}: '{task_desc}'...",
            "status": "running"
        }))
        _, worker_text = await _run_worker(sub_task)
        worker_outcomes.append(f"Sub-task {sub_task['id']} Result: {worker_text}")
        yield sse_event_fn("thought", json.dumps({
            "id": f"htp-task-complete-{sub_task['id']}-{time.time()}",
            "type": "planning",
            "text": f"[Hierarchical Task Planning] Sub-task {sub_task['id']} completed (sequential).",
            "status": "completed"
        }))

    yield sse_event_fn("thought", json.dumps({
        "id": f"htp-synthesis-{time.time()}",
        "type": "planning",
        "text": "[Hierarchical Task Planning] Synthesis of all worker outcomes...",
        "status": "running"
    }))
    synthesis_prompt = (
        f"You are the Meridian Project Manager. Synthesize the following completed worker sub-tasks into a cohesive final update to the user.\n"
        f"Goal: {prompt}\n"
        f"Worker Outcomes:\n" + "\n".join(worker_outcomes) + "\n\n"
        "Return the final response in the required JSON format: {\"chat\": \"...\", \"speech\": \"...\", \"lang\": \"...\"}"
    )
    try:
        res_sys = await asyncio.to_thread(client.chat, model=brain_model, messages=[{"role": "user", "content": synthesis_prompt}])
        raw_content = (res_sys.message.content if hasattr(res_sys, "message") and hasattr(res_sys.message, "content") else (res_sys.get("message", {}).get("content", "") if isinstance(res_sys, dict) else ""))
        text_sys = (raw_content or "").strip()
        if text_sys.startswith("```"):
            text_sys = text_sys.strip("`").replace("json\n", "").strip()
        yield sse_event_fn("text", text_sys)
    except Exception:
        yield sse_event_fn("text", json.dumps({"chat": "All tasks completed.", "speech": "All tasks completed.", "lang": "en"}))


def enrich_system_prompt(
    system_prompt: str,
    prompt: str,
    session_id: str,
    near_miss_ctx: Optional[str] = None,
    temporal_graphs: Optional[Dict[str, Any]] = None,
) -> str:
    """Enriches base system prompt with TemporalMemory, Semantic Cache, and Cognitive Graph context."""
    if temporal_graphs is not None:
        try:
            from src.core.temporal_memory import TemporalMemoryGraph
            _tmg: TemporalMemoryGraph = temporal_graphs.setdefault(session_id, TemporalMemoryGraph())
            if _tmg.nodes:
                now = time.time()
                scored = [(nid, _tmg.calculate_temporal_relevance(nid, now), _tmg.nodes[nid]) for nid in _tmg.nodes]
                scored.sort(key=lambda x: x[1], reverse=True)
                top_facts = scored[:3]
                if top_facts:
                    facts_text = "\n".join(f"- [{n['type']}] {n['entity_id']}: {n['state']}" for _, _, n in top_facts)
                    system_prompt += f"\n\n[TEMPORAL MEMORY — Recent Project Context]\n{facts_text}"
        except Exception:
            pass

    if near_miss_ctx:
        system_prompt += f"\n\n[SEMANTIC MEMORY — Related Prior Response]\n{near_miss_ctx}"

    try:
        from src.core.cognitive_graph import get_cognitive_graph
        _cog_graph = get_cognitive_graph()
        _graph_ctx = _cog_graph.get_unified_context(prompt)
        if _graph_ctx:
            system_prompt += f"\n\n{_graph_ctx}"
    except Exception:
        pass

    return system_prompt


