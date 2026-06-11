import os
import platform
import time
from datetime import datetime
from typing import Dict, Any, List
import ollama

# Directives for each mode
MODE_DIRECTIVES = {
    "AUTO": "Reason and act balanced. Be helpful and direct. Use any tools required.",
    "ENGINEER": "You are a software developer. Be structured, write tests, inspect exit codes, check logs, and iterate on fixing errors. Prioritize developer tools (run_python, write_file, git_commit, search_codebase) and follow the write-test-fix loop.",
    "REVIEWER": "You are a code critic and auditor. Analyze files and diffs meticulously across correctness, security, performance, maintainability, and test coverage. Flag all bugs, warnings, and vulnerabilities.",
    "ANALYST": "You are a systems analyst. Focus on processes, CPU/memory performance metrics, networks, active sockets, logs, and database schemas. Prioritize parallel system analysis tool calls.",
    "OPERATOR": "You are a desktop automation operator. Execute actions swiftly using clicking, dragging, typing, screenshotting, and window control. Minimize thought length; act decisively.",
    "RESEARCHER": "You are an information researcher. Investigate local files, RAG knowledge bases, and web search results. Gather information comprehensively, cross-reference sources, and summarize facts clearly before answering."
}

# The static template for the system prompt
SYSTEM_PROMPT_TEMPLATE = """You are Meridian-X — a fully offline, autonomous desktop agent built by Aryan.
You were created by Aryan, not by Google, Anthropic, OpenAI, or any other company.
If asked who made you, who created you, or who built you, always answer: "I was built by Aryan."
You think, plan, act, observe results, and self-correct in a continuous loop.
Backend: {brain_model} via Ollama (local, offline).
Memory: Turbovec RAG + MongoDB Knowledge Graph. Vision: moondream:1.8b (on-demand).

════════════════════════════════════════════
COGNITIVE MODE DIRECTIVE: {mode}
{mode_directive}
════════════════════════════════════════════

════════════════════════════════════════════
AGENT LOOP PROTOCOL — MANDATORY
════════════════════════════════════════════
Every turn you MUST use this structure:

1. THINK FIRST & SELF-QUESTION — always open with:
   <thought>
     a. Query yourself: "Do I have verified information regarding the file paths, parameters, and environment dependencies? Or am I assuming?"
     b. If details are missing, prioritize exploratory search/observation commands (e.g. read_file, dir_list, grep_search) to resolve ambiguity first.
     c. Analyze current state, previous observations, and plan next action.
     d. If an observation has an error, debug it here and plan a fix.
   </thought>

2. CALL TOOLS — use zero or more calls per turn:
   <call:TOOL_NAME>{{"argument": "value"}}</call:TOOL_NAME>
   - Multiple calls in one turn run IN PARALLEL. Use this aggressively.
   - Args must be valid JSON inside the tags.

3. FINISH — when the goal is fully resolved:
   <finish>
     Your final response MUST be a raw JSON object containing exactly three keys:
     {{
       "chat": "Your final chat response to the user, in the user's preferred language/transliteration (e.g. Hinglish: 'Main theek hoon', English: 'I am fine')",
       "speech": "The spoken text. Write this in the exact same language and script used in the 'chat' response (unless directed otherwise by language directives).",
       "lang": "The 2-letter language code (e.g., 'en' for English, 'hi' for Hindi, 'ja' for Japanese, 'es' for Spanish, 'ru' for Russian)"
     }}
     Do NOT wrap this JSON block in markdown code blocks.
   </finish>

════════════════════════════════════════════
RULES
════════════════════════════════════════════
- NEVER ask the user a question mid-task. The system will automatically show a popup safety gate/confirmation box for any Tier-3 actions. Instruct the user to use the safety gate popup UI to approve or reject the action, rather than asking them to reply in chat.
- NEVER use placeholder logic or assume data — always call the tool to get real data.
- If a tool fails, self-correct in the next <thought> and retry (max 3 attempts).
- For Tier-3 actions (delete_file, kill_process, start_service, stop_service, run_command), describe the action and instruct the user to approve/deny it using the popup safety gate interface on their screen.
- To delete all files/contents inside a directory, use a wildcard path in `delete_file` (e.g. `path='C:\\path\\to\\dir\\*'`). This allows bulk deletion in a single call and avoids triggering multiple safety gate approvals.
- Never reveal credentials, private paths, or API keys in any response.
- Always respond to the user in the exact same language and script (e.g., Hindi/Devanagari, Spanish, English, or transliterated Hinglish) that they used in their latest input. When doing so, your final output inside <finish> tags MUST be the structured JSON block described above.
- If the user communicates in English, both the "chat" and "speech" keys MUST remain in English, and the "lang" key must be "en" or "na". Do NOT translate the voice output to Hindi unless specifically asked.

════════════════════════════════════════════
AVAILABLE TOOLS
════════════════════════════════════════════
{tools_doc}

════════════════════════════════════════════
CONTEXT
════════════════════════════════════════════
Workspace: {workspace}
Time: {current_time}
OS: {os_info}
Active Window: {active_window}
User Profile:
{user_profile}
RAG Context (relevant chunks):
{rag_context}
Knowledge Graph Facts:
{kg_facts}{rlef_feedback}
"""

def classify_mode(prompt: str) -> str:
    """Classify prompt into a cognitive mode based on keyword detection."""
    p = prompt.lower()

    # Engineer triggers
    if any(x in p for x in [
        "build", "write code", "implement", "fix a bug", "create script", "scaffold", "refactor",
        "debug", "optimize", "function", "class", "module", "error in", "fix the", "fix this",
        "write a", "create a", "update the", "add a", "remove a", "edit the", "change the",
        "unit test", "test case", "compile", "run script", "import", "syntax"
    ]):
        return "ENGINEER"
    # Reviewer triggers
    elif any(x in p for x in [
        "review", "audit", "lint", "check code", "code review", "git diff",
        "vulnerability", "security issue", "bad practice", "smell"
    ]):
        return "REVIEWER"
    # Analyst triggers
    elif any(x in p for x in [
        "cpu", "ram", "processes", "slow", "system health", "network", "socket", "port",
        "disk usage", "database", "sqlite", "query", "log", "analyse", "analyze",
        "monitor", "performance", "memory usage", "task manager", "benchmark"
    ]):
        return "ANALYST"
    # Operator triggers
    elif any(x in p for x in [
        "click", "open app", "type", "screenshot", "hotkey", "double click", "drag", "record",
        "move mouse", "press key", "automate", "macro"
    ]):
        return "OPERATOR"
    # Researcher triggers
    elif any(x in p for x in [
        "search web", "google", "find out", "research", "summarize page", "fetch url", "scrape",
        "look up", "wikipedia", "explain what", "what is", "who is", "tell me about"
    ]):
        return "RESEARCHER"

    return "AUTO"


import re

def lexical_context_compressor(text: str, query: str, ratio: float = 0.4) -> str:
    """Compresses text by ranking sentences based on lexical overlap with query words."""
    if not text or not query:
        return text
    
    sentences = re.split(r'(?<=[.!?])\s+', text)
    if len(sentences) <= 3:
        return text
        
    query_words = set(re.findall(r'\w+', query.lower()))
    if not query_words:
        return text
        
    scored_sentences = []
    for sent in sentences:
        words = re.findall(r'\w+', sent.lower())
        overlap = len(query_words.intersection(words))
        score = overlap / (len(words) + 1.0)
        scored_sentences.append((score, sent))
        
    scored_sentences.sort(key=lambda x: x[0], reverse=True)
    num_to_keep = max(3, int(len(sentences) * ratio))
    top_sentences = [sent for _, sent in scored_sentences[:num_to_keep]]
    
    final_sentences = [sent for sent in sentences if sent in top_sentences]
    return " ".join(final_sentences)

def detect_user_language(prompt: str) -> str:
    # 1. Check if prompt contains Devanagari characters (Hindi script)
    import re
    if re.search(r'[\u0900-\u097F]', prompt):
        return "HINDI"
    
    # 2. Check for common Hinglish words
    hinglish_keywords = {
        "aap", "kaise", "ho", "kya", "kar", "rhe", "rha", "hai", "hain", "hu", "hoon", 
        "mera", "meri", "mujhe", "tum", "apna", "apni", "nhi", "nahi", "thik", "theek",
        "karo", "batao", "samjhao", "likho", "dikhao", "chalao", "yaar", "ab", "kab",
        "sab", "se", "ko", "aur", "ki", "ka", "ke", "hi", "to", "toh"
    }
    words = [w.strip("?,.!:;\"'").lower() for w in prompt.split()]
    match_count = sum(1 for w in words if w in hinglish_keywords)
    
    if match_count >= 2 or (len(words) <= 3 and match_count >= 1):
        return "HINGLISH"
        
    return "ENGLISH"

def load_workspace_config() -> Dict[str, Any]:
    """Loads .meridian.json configuration file from the current working directory."""
    config_path = os.path.join(os.getcwd(), ".meridian.json")
    if os.path.exists(config_path):
        try:
            import json
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[Workspace Config] Error reading {config_path}: {e}")
    return {}

def build_system_prompt(prompt: str, brain_model: str, ollama_host: str, tools_doc: str) -> str:
    """Queries RAG, KG facts, user profile, and system specs to format the complete prompt."""
    mode = classify_mode(prompt)
    mode_directive = MODE_DIRECTIVES[mode]
    
    # Load workspace config overrides
    config = load_workspace_config()
    custom_directives = config.get("custom_directives")
    if custom_directives:
        mode_directive += f"\n- CUSTOM WORKSPACE DIRECTIVES: {custom_directives}"
    
    # Detect language of prompt and append appropriate language directive
    lang = detect_user_language(prompt)
    if lang == "ENGLISH":
        mode_directive += "\n- CRITICAL LANGUAGE DIRECTIVE: The user's input is in English. You MUST respond in English. Both your 'chat' and 'speech' keys MUST be in English. Set 'lang' to 'en'. Do NOT translate the voice output (speech key) to Hindi or any other language."
    else:
        mode_directive += "\n- CRITICAL LANGUAGE DIRECTIVE: The user's input is in Hindi/Hinglish. You MUST respond in Hindi. While your 'chat' response can be in Hinglish (Latin alphabet) or Hindi, your 'speech' response MUST be written in Devanagari Hindi script (e.g. 'आप कैसे हैं' instead of 'aap kaise hain') so the local TTS engine can speak it with correct pronunciation. Set 'lang' to 'hi'."
    # Check if whatsapp is mentioned in current prompt or recent history
    has_whatsapp_history = False
    try:
        from database import get_conversation_history
        records = get_conversation_history(limit=20)
        # Sort by timestamp to ensure chronological order
        records.sort(key=lambda x: x.get("timestamp", 0.0))
        # Look at last 6 turns (typically 3 user/assistant turns)
        recent_records = records[-6:]
        for r in recent_records:
            if "whatsapp" in r.get("content", "").lower():
                has_whatsapp_history = True
                break
    except Exception as e:
        print("[System Prompt] Error reading conversation history for WhatsApp check:", e)

    if "whatsapp" in prompt.lower() or has_whatsapp_history:
        mode_directive += "\n- CRITICAL DIRECTIVE: The user wants to send a WhatsApp message. You MUST use the `send_whatsapp_message` tool to search for the contact and send the message."
    
    # OS Info
    os_info = f"{platform.system()} {platform.release()} ({platform.machine()})"
    
    # Active Window
    active_window = "Unknown"
    try:
        from src.core.proactive import get_active_window_title
        active_window = get_active_window_title() or "None"
    except Exception:
        pass
    
    # Workspace
    workspace = os.getcwd()
    
    # Current Time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # RAG Context
    rag_context = "No relevant chunks retrieved."
    try:
        from database import search_knowledge_base
        results = search_knowledge_base(prompt, limit=2)
        if results:
            rag_context = ""
            for r in results:
                compressed_chunk = lexical_context_compressor(r['chunk_text'], prompt, ratio=0.4)
                rag_context += f"- [Source: {r['source']}] (Similarity: {r['similarity']:.3f})\n  Content: {compressed_chunk}\n"
    except Exception as e:
        print("[System Prompt] RAG search error:", e)
        
    # User Profile
    user_profile = "- Preferred response tone: concise\n- Coding preference: Python\n- Shell: PowerShell"
    try:
        from database import get_mongo_db
        db_conn = get_mongo_db()
        if db_conn is not None:
            col = db_conn["user_profile"]
            profile_data = list(col.find({}, {"_id": 0}))
            if profile_data:
                user_profile = ""
                for entry in profile_data:
                    user_profile += f"- {entry.get('key')}: {entry.get('value')}\n"
    except Exception as e:
        print("[System Prompt] User profile load error:", e)
        
    # KG Facts
    kg_facts = "No relevant relationships or facts loaded."
    try:
        from database import get_mongo_db
        db_conn = get_mongo_db()
        if db_conn is not None:
            words = [w.strip("?,.!:;\"'") for w in prompt.split() if len(w) > 3]
            query_filter = {"$or": [{"entity": {"$regex": w, "$options": "i"}} for w in words[:5]]} if words else {}
            if query_filter:
                col = db_conn["knowledge_graph"]
                facts_data = list(col.find(query_filter, {"_id": 0}).limit(5))
                if facts_data:
                    kg_facts = ""
                    for f in facts_data:
                        kg_facts += f"- {f.get('entity')} --({f.get('relation')})--> {f.get('target')}\n"
    except Exception as e:
        print("[System Prompt] KG facts load error:", e)
        
    # RLEF Environment Feedback
    rlef_feedback = ""
    try:
        from database import get_recent_failures
        failures = get_recent_failures(5)
        if failures:
            rlef_feedback = "\n\n════════════════════════════════════════════\nENVIRONMENT FEEDBACK (RLEF - Learned from recent tool execution failures):\n════════════════════════════════════════════\n"
            for f in failures:
                rlef_feedback += f"- Tool '{f['tool']}' recently failed with error: {f['error']}. Adapt your parameters or approach to avoid this.\n"
    except Exception as ree:
        print("[System Prompt] RLEF load error:", ree)

    return SYSTEM_PROMPT_TEMPLATE.format(
        brain_model=brain_model,
        mode=mode,
        mode_directive=mode_directive,
        tools_doc=tools_doc,
        workspace=workspace,
        current_time=current_time,
        os_info=os_info,
        active_window=active_window,
        user_profile=user_profile,
        rag_context=rag_context,
        kg_facts=kg_facts,
        rlef_feedback=rlef_feedback
    )
