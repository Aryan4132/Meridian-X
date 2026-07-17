from src.core.mcp_client import mcp_manager
import os
import inspect
import asyncio
from typing import Dict, Any

# Import existing core tool functions
from src.tools.filesystem import read_file, write_file, list_directory, search_files, move_file, delete_file
from src.tools.web import search_web, fetch_page, parse_page, download_file, autonomous_research
from src.tools.desktop import (
    screenshot, screenshot_region, ocr_screen, vision_analyze, find_on_screen,
    gui_click, gui_right_click, gui_double_click, gui_drag, gui_type, gui_hotkey, gui_scroll, get_mouse_position,
    segment_screen, gui_click_badge
)
from src.tools.system import (
    list_windows, focus_window, resize_window, move_window, minimize_window, maximize_window, close_window,
    open_app, open_file, open_url_in_browser, close_app, get_active_window, wait_for_window,
    get_system_info, get_hardware_info, get_disk_info, get_battery_status, get_temperature,
    list_processes, get_process_detail, kill_process, list_startup_items, list_installed_apps,
    list_services, start_service, stop_service, get_network_connections, get_wifi_networks, ping_host,
    clipboard_get, clipboard_set
)
from src.tools.developer import (
    run_python, open_editor, git_status, git_commit, git_diff, search_codebase,
    scaffold_project, run_tests, install_package, lint_file, format_file,
    lsp_get_definition, lsp_get_references, lsp_get_hover_info, lsp_diagnose_file
)
from src.tools.communication import send_notification, send_email, read_emails, send_whatsapp_message

# Import newly implemented advanced capability tools
from src.tools.vault import vault_set, vault_get, vault_list, vault_delete
from src.tools.knowledge import kg_add_entity, kg_add_relation, kg_query, kg_search, kg_add_fact, kg_get_facts, kg_traverse, suggest_cross_project_patterns
from src.tools.scheduler import schedule_task, schedule_once, list_scheduled, cancel_task
from src.tools.watcher import watch_log, unwatch_log, list_log_watchers, tail_log, search_log, log_stats, watch_folder, unwatch_folder, list_watchers
from src.tools.review import review_file, review_diff, review_directory, export_review
from src.tools.shell import nl_to_shell, nl_run, shell_history
from src.tools.db_query import db_connect, db_query, db_execute, db_schema, db_nl_query, db_disconnect
from src.tools.exporter import export_session, export_goal, list_sessions, export_finetune_data, finetune_stats, mark_correction
from src.tools.web_browser import browser_open, browser_screenshot, browser_find_and_click, browser_type_in, browser_get_text, browser_close, scrape_urls, scrape_table, schedule_scrape
from src.tools.recording import record_screen, stop_recording, analyze_recording, save_workflow, replay_workflow, list_workflows
from src.tools.clipboard import clipboard_history, clipboard_search, clipboard_pin, clipboard_restore
from src.tools.voice import voice_record_and_transcribe, voice_speak
from src.tools.dynamic_manager import generate_dynamic_tool

# Advanced desktop tools imports
from src.tools.ollama_manager import ollama_list_models, ollama_pull_model, ollama_delete_model
from src.tools.task_scheduler import win_schedule_daily, win_schedule_once, win_list_tasks, win_delete_task
from src.tools.security_auditor import run_security_audit
from src.tools.documents import (
    read_document_text, create_word_document, edit_word_document,
    create_excel_document, edit_excel_document, create_powerpoint_presentation,
    edit_powerpoint_presentation, create_pdf_document, edit_pdf_document
)

# Dynamic imports to avoid circular database referencing
def _ingest_file(path: str) -> str:
    from database import ingest_into_knowledge_base
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    ingest_into_knowledge_base(path, content)
    return f"Successfully ingested {path} into Turbovec."

def _search_knowledge(query: str) -> str:
    from database import search_knowledge_base
    results = search_knowledge_base(query, limit=2)
    lines = []
    for r in results:
        lines.append(f"[Source: {r['source']} (similarity: {r['similarity']:.4f})]\n{r['chunk_text']}")
    return "\n---\n".join(lines) if lines else "No similar context discovered in database."

def _save_note(text: str) -> str:
    from database import ingest_into_knowledge_base
    ingest_into_knowledge_base("user_note", text, {"type": "note"})
    return "Saved note to episodic database memory."

def _search_offline_docs(query: str) -> str:
    from src.core.doc_indexer import search_offline_docs
    results = search_offline_docs(query, limit=3)
    lines = []
    for r in results:
        lines.append(f"[File: {r['file_path']} | Section: {r['section']} (score: {r['score']:.4f})]\n{r['content']}")
    return "\n---\n".join(lines) if lines else "No similar documentation discovered."

# Main Tool Configuration Registry
TOOL_REGISTRY: Dict[str, Dict[str, Any]] = {
    # Filesystem
    "read_file": {"tier": 0, "func": read_file},
    "write_file": {"tier": 1, "func": write_file},
    "list_directory": {"tier": 0, "func": list_directory},
    "search_files": {"tier": 0, "func": search_files},
    "move_file": {"tier": 1, "func": move_file},
    "delete_file": {"tier": 3, "func": delete_file},
    
    # Document Processing
    "read_document_text": {"tier": 0, "func": read_document_text},
    "create_word_document": {"tier": 1, "func": create_word_document},
    "edit_word_document": {"tier": 1, "func": edit_word_document},
    "create_excel_document": {"tier": 1, "func": create_excel_document},
    "edit_excel_document": {"tier": 1, "func": edit_excel_document},
    "create_powerpoint_presentation": {"tier": 1, "func": create_powerpoint_presentation},
    "edit_powerpoint_presentation": {"tier": 1, "func": edit_powerpoint_presentation},
    "create_pdf_document": {"tier": 1, "func": create_pdf_document},
    "edit_pdf_document": {"tier": 1, "func": edit_pdf_document},
    
    # Web & Network
    "search_web": {"tier": 0, "func": search_web},
    "fetch_page": {"tier": 0, "func": fetch_page},
    "parse_page": {"tier": 0, "func": parse_page},
    "download_file": {"tier": 1, "func": download_file},
    "autonomous_research": {"tier": 1, "func": autonomous_research},
    
    # Desktop Automation
    "screenshot": {"tier": 0, "func": screenshot},
    "screenshot_region": {"tier": 0, "func": screenshot_region},
    "ocr_screen": {"tier": 0, "func": ocr_screen},
    "vision_analyze": {"tier": 0, "func": vision_analyze},
    "find_on_screen": {"tier": 0, "func": find_on_screen},
    "gui_click": {"tier": 2, "func": gui_click},
    "gui_right_click": {"tier": 2, "func": gui_right_click},
    "gui_double_click": {"tier": 2, "func": gui_double_click},
    "gui_drag": {"tier": 2, "func": gui_drag},
    "gui_type": {"tier": 1, "func": gui_type},
    "gui_hotkey": {"tier": 1, "func": gui_hotkey},
    "gui_scroll": {"tier": 1, "func": gui_scroll},
    "get_mouse_position": {"tier": 0, "func": get_mouse_position},
    
    # Window management
    "list_windows": {"tier": 0, "func": list_windows},
    "focus_window": {"tier": 1, "func": focus_window},
    "resize_window": {"tier": 1, "func": resize_window},
    "move_window": {"tier": 1, "func": move_window},
    "minimize_window": {"tier": 1, "func": minimize_window},
    "maximize_window": {"tier": 1, "func": maximize_window},
    "close_window": {"tier": 2, "func": close_window},
    "open_app": {"tier": 1, "func": open_app},
    "open_file": {"tier": 1, "func": open_file},
    "open_url_in_browser": {"tier": 1, "func": open_url_in_browser},
    "close_app": {"tier": 2, "func": close_app},
    "get_active_window": {"tier": 0, "func": get_active_window},
    "wait_for_window": {"tier": 0, "func": wait_for_window},
    
    # System metrics
    "get_system_info": {"tier": 0, "func": get_system_info},
    "get_hardware_info": {"tier": 0, "func": get_hardware_info},
    "get_disk_info": {"tier": 0, "func": get_disk_info},
    "get_battery_status": {"tier": 0, "func": get_battery_status},
    "get_temperature": {"tier": 0, "func": get_temperature},
    "list_processes": {"tier": 0, "func": list_processes},
    "get_process_detail": {"tier": 0, "func": get_process_detail},
    "kill_process": {"tier": 3, "func": kill_process},
    "list_startup_items": {"tier": 0, "func": list_startup_items},
    "list_installed_apps": {"tier": 0, "func": list_installed_apps},
    "list_services": {"tier": 0, "func": list_services},
    "start_service": {"tier": 3, "func": start_service},
    "stop_service": {"tier": 3, "func": stop_service},
    "get_network_connections": {"tier": 0, "func": get_network_connections},
    "get_wifi_networks": {"tier": 0, "func": get_wifi_networks},
    "ping_host": {"tier": 0, "func": ping_host},
    "clipboard_get": {"tier": 0, "func": clipboard_get},
    "clipboard_set": {"tier": 1, "func": clipboard_set},
    
    # RAG & Memory
    "ingest_file": {"tier": 1, "func": _ingest_file},
    "search_knowledge": {"tier": 0, "func": _search_knowledge},
    "save_note": {"tier": 1, "func": _save_note},
    "search_offline_docs": {"tier": 0, "func": _search_offline_docs},
    
    # Developer & SWE Tools
    "run_python": {"tier": 2, "func": run_python},
    "open_editor": {"tier": 1, "func": open_editor},
    "git_status": {"tier": 0, "func": git_status},
    "git_commit": {"tier": 2, "func": git_commit},
    "git_diff": {"tier": 0, "func": git_diff},
    "search_codebase": {"tier": 0, "func": search_codebase},
    "scaffold_project": {"tier": 1, "func": scaffold_project},
    "run_tests": {"tier": 2, "func": run_tests},
    "install_package": {"tier": 2, "func": install_package},
    "lint_file": {"tier": 0, "func": lint_file},
    "format_file": {"tier": 1, "func": format_file},
    "lsp_get_definition": {"tier": 0, "func": lsp_get_definition},
    "lsp_get_references": {"tier": 0, "func": lsp_get_references},
    "lsp_get_hover_info": {"tier": 0, "func": lsp_get_hover_info},
    "lsp_diagnose_file": {"tier": 0, "func": lsp_diagnose_file},
    
    # Communication
    "send_notification": {"tier": 1, "func": send_notification},
    "send_email": {"tier": 2, "func": send_email},
    "read_emails": {"tier": 0, "func": read_emails},
    "send_whatsapp_message": {"tier": 2, "func": send_whatsapp_message},

    # --- ADVANCED CAPABILITY REGISTRATIONS ---
    # Secrets Vault
    "vault_set": {"tier": 2, "func": vault_set},
    "vault_get": {"tier": 1, "func": vault_get},
    "vault_list": {"tier": 0, "func": vault_list},
    "vault_delete": {"tier": 3, "func": vault_delete},

    # Knowledge Graph
    "kg_add_entity": {"tier": 1, "func": kg_add_entity},
    "kg_add_relation": {"tier": 1, "func": kg_add_relation},
    "kg_query": {"tier": 0, "func": kg_query},
    "kg_search": {"tier": 0, "func": kg_search},
    "kg_add_fact": {"tier": 1, "func": kg_add_fact},
    "kg_get_facts": {"tier": 0, "func": kg_get_facts},
    "kg_traverse": {"tier": 0, "func": kg_traverse},
    "suggest_cross_project_patterns": {"tier": 0, "func": suggest_cross_project_patterns},

    # Scheduler
    "schedule_task": {"tier": 1, "func": schedule_task},
    "schedule_once": {"tier": 1, "func": schedule_once},
    "list_scheduled": {"tier": 0, "func": list_scheduled},
    "cancel_task": {"tier": 2, "func": cancel_task},

    # Watchers / Event-driven
    "watch_log": {"tier": 1, "func": watch_log},
    "unwatch_log": {"tier": 1, "func": unwatch_log},
    "list_log_watchers": {"tier": 0, "func": list_log_watchers},
    "tail_log": {"tier": 0, "func": tail_log},
    "search_log": {"tier": 0, "func": search_log},
    "log_stats": {"tier": 0, "func": log_stats},
    "watch_folder": {"tier": 1, "func": watch_folder},
    "unwatch_folder": {"tier": 1, "func": unwatch_folder},
    "list_watchers": {"tier": 0, "func": list_watchers},

    # Code Review
    "review_file": {"tier": 0, "func": review_file},
    "review_diff": {"tier": 0, "func": review_diff},
    "review_directory": {"tier": 0, "func": review_directory},
    "export_review": {"tier": 1, "func": export_review},

    # NL Shell
    "nl_to_shell": {"tier": 0, "func": nl_to_shell},
    "nl_run": {"tier": 2, "func": nl_run},
    "shell_history": {"tier": 0, "func": shell_history},

    # Local DB query
    "db_connect": {"tier": 1, "func": db_connect},
    "db_query": {"tier": 1, "func": db_query},
    "db_execute": {"tier": 2, "func": db_execute},
    "db_schema": {"tier": 0, "func": db_schema},
    "db_nl_query": {"tier": 1, "func": db_nl_query},
    "db_disconnect": {"tier": 1, "func": db_disconnect},

    # Session Export & Fine-tuning
    "export_session": {"tier": 1, "func": export_session},
    "export_goal": {"tier": 1, "func": export_goal},
    "list_sessions": {"tier": 0, "func": list_sessions},
    "export_finetune_data": {"tier": 0, "func": export_finetune_data},
    "finetune_stats": {"tier": 0, "func": finetune_stats},
    "mark_correction": {"tier": 1, "func": mark_correction},

    # Playwright Browser Automation & Scraper
    "browser_open": {"tier": 1, "func": browser_open},
    "browser_screenshot": {"tier": 0, "func": browser_screenshot},
    "browser_find_and_click": {"tier": 2, "func": browser_find_and_click},
    "browser_type_in": {"tier": 2, "func": browser_type_in},
    "browser_get_text": {"tier": 0, "func": browser_get_text},
    "browser_close": {"tier": 1, "func": browser_close},
    "scrape_urls": {"tier": 1, "func": scrape_urls},
    "scrape_table": {"tier": 0, "func": scrape_table},
    "schedule_scrape": {"tier": 1, "func": schedule_scrape},

    # Screen Recording & Workflow Replay
    "record_screen": {"tier": 1, "func": record_screen},
    "stop_recording": {"tier": 1, "func": stop_recording},
    "analyze_recording": {"tier": 0, "func": analyze_recording},
    "save_workflow": {"tier": 1, "func": save_workflow},
    "replay_workflow": {"tier": 2, "func": replay_workflow},
    "list_workflows": {"tier": 0, "func": list_workflows},

    # Clipboard manager
    "clipboard_history": {"tier": 0, "func": clipboard_history},
    "clipboard_search": {"tier": 0, "func": clipboard_search},
    "clipboard_pin": {"tier": 1, "func": clipboard_pin},
    "clipboard_restore": {"tier": 1, "func": clipboard_restore},

    # Voice control
    "voice_record_and_transcribe": {"tier": 1, "func": voice_record_and_transcribe},
    "voice_speak": {"tier": 1, "func": voice_speak},
    "generate_dynamic_tool": {"tier": 2, "func": generate_dynamic_tool},

    # Ollama Model Manager
    "ollama_list_models": {"tier": 0, "func": ollama_list_models},
    "ollama_pull_model": {"tier": 1, "func": ollama_pull_model},
    "ollama_delete_model": {"tier": 2, "func": ollama_delete_model},
    
    # Windows Task Scheduler
    "win_schedule_daily": {"tier": 1, "func": win_schedule_daily},
    "win_schedule_once": {"tier": 1, "func": win_schedule_once},
    "win_list_tasks": {"tier": 0, "func": win_list_tasks},
    "win_delete_task": {"tier": 2, "func": win_delete_task},
    
    # Security Diagnostics
    "run_security_audit": {"tier": 1, "func": run_security_audit},

    # Meta-Learning reload plugins tool
    "reload_plugins": {"tier": 1, "func": lambda: reload_plugins_wrapper()},
    "segment_screen": {"tier": 0, "func": segment_screen},
    "gui_click_badge": {"tier": 2, "func": gui_click_badge},
    "p2p_sync": {"tier": 1, "func": lambda: p2p_sync_wrapper()},
    "create_dynamic_tool": {"tier": 3, "func": lambda name, code: create_dynamic_tool_wrapper(name, code)}
}

def p2p_sync_wrapper() -> str:
    from src.core.p2p import p2p_node
    return p2p_node.sync_now()

def create_dynamic_tool_wrapper(name: str, code: str) -> str:
    try:
        compile(code, "<string>", "exec")
    except Exception as e:
        return f"Tool compilation check failed: {e}"
        
    try:
        # BUG-63 fix: use find_workspace_root() instead of fragile dirname chain.
        try:
            from src.core.history_manager import find_workspace_root
            plugins_dir = os.path.join(find_workspace_root(), "plugins")
        except Exception:
            backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            root_dir = os.path.dirname(backend_dir)
            plugins_dir = os.path.join(root_dir, "plugins")
        
        os.makedirs(plugins_dir, exist_ok=True)
        plugin_path = os.path.join(plugins_dir, f"{name}.py")
        
        # Write with TIER = 3 (Manual User Approval required)
        with open(plugin_path, "w", encoding="utf-8") as f:
            f.write(f"TIER = 3\n\n{code}\n")
            
        res = reload_plugins_wrapper()
        return f"Successfully created dynamic tool '{name}' and reloaded registry: {res}"
    except Exception as e:
        return f"Failed to create dynamic tool: {e}"

def reload_plugins_wrapper() -> str:
    from src.core.plugins import reload_dynamic_plugins
    return reload_dynamic_plugins(TOOL_REGISTRY)

# Auto-discover plugins at runtime
try:
    from src.core.plugins import load_plugins
    load_plugins(TOOL_REGISTRY)
except Exception as e:
    print("[Plugins] Auto-discovery activation failed:", e)

async def call_tool(name: str, args: Dict[str, Any]) -> str:
    if name not in TOOL_REGISTRY:
        raise ValueError(f"Unknown tool: '{name}'")
        
    tool_info = TOOL_REGISTRY[name]
    func = tool_info["func"]
    
    try:
        # Support both synchronous and asynchronous tool functions
        if inspect.iscoroutinefunction(func):
            res = str(await func(**args))
        else:
            res = str(await asyncio.to_thread(func, **args))
            
        # Global output truncation guard
        MAX_TOOL_OUTPUT = 30000
        if len(res) > MAX_TOOL_OUTPUT:
            res = res[:MAX_TOOL_OUTPUT] + f"\n\n[Warning: Output truncated at {MAX_TOOL_OUTPUT} characters to prevent context window overflow]"
        return res
    except Exception as e:
        return f"Error executing {name}: {str(e)}"
