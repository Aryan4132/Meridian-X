from src.core.mcp_client import mcp_manager
import os
import inspect
import asyncio
from typing import Dict, Any, Optional


# Import existing core tool functions
from src.tools.filesystem import read_file, write_file, list_directory, search_files, move_file, delete_file
from src.tools.web import search_web, search_news, fetch_page, parse_page, download_file, autonomous_research, ingest_url
from src.tools.search_hub import universal_search
from src.tools.geo_location import resolve_location, get_localized_weather, bias_query_spatially
from src.tools.desktop import (
    screenshot, screenshot_region, ocr_screen, vision_analyze, find_on_screen,
    gui_click, gui_right_click, gui_double_click, gui_drag, gui_type, gui_hotkey, gui_scroll, get_mouse_position,
    segment_screen, gui_click_badge, screenshot_to_code
)
from src.tools.system import (
    list_windows, focus_window, resize_window, move_window, minimize_window, maximize_window, close_window,
    open_app, open_file, open_url_in_browser, close_app, get_active_window, wait_for_window,
    get_system_info, get_hardware_info, get_disk_info, get_battery_status, get_temperature,
    list_processes, get_process_detail, kill_process, list_startup_items, list_installed_apps,
    list_services, start_service, stop_service, get_network_connections, get_wifi_networks, ping_host,
    clipboard_get, clipboard_set, control_media_playback
)
from src.tools.developer import (
    run_python, open_editor, git_status, git_commit, git_diff, git_create_snapshot, git_rollback, search_codebase,
    scaffold_project, run_tests, install_package, lint_file, format_file,
    lsp_get_definition, lsp_get_references, lsp_get_hover_info, lsp_diagnose_file
)
from src.tools.communication import send_notification, send_email, read_emails, send_whatsapp_message, triage_and_read_emails, send_native_toast_notification, send_discord_message, read_discord_messages, add_discord_reaction, list_discord_channels
from src.tools.whatsapp_manager import manage_whatsapp_contacts, read_whatsapp_messages, list_whatsapp_chats, login_whatsapp_session, bridge_whatsapp_voice_call
from src.tools.health_ingest import sync_wearable_health_data, get_health_metrics_summary
from src.tools.wellness import track_hydration, trigger_ergonomic_break, calculate_daily_wellness_score

# Import newly implemented advanced capability tools
from src.tools.vault import vault_set, vault_get, vault_list, vault_delete
from src.tools.knowledge import kg_add_entity, kg_add_relation, kg_query, kg_search, kg_add_fact, kg_get_facts, kg_traverse, suggest_cross_project_patterns
from src.tools.scheduler import schedule_task, schedule_once, list_scheduled, cancel_task
from src.tools.watcher import watch_log, unwatch_log, list_log_watchers, tail_log, search_log, log_stats, watch_folder, unwatch_folder, list_watchers
from src.tools.review import review_file, review_diff, review_directory, export_review
from src.tools.auto_reviewer import generate_unit_tests, review_git_changes

from src.tools.shell import nl_to_shell, nl_run, shell_history, monitor_process
from src.tools.db_query import db_connect, db_query, db_execute, db_schema, db_nl_query, db_disconnect
from src.tools.exporter import export_session, export_goal, list_sessions, export_finetune_data, finetune_stats, mark_correction
from src.tools.web_browser import (
    browser_open, browser_screenshot, browser_find_and_click, browser_type_in,
    browser_get_text, browser_close, scrape_urls, scrape_table, schedule_scrape,
    browser_press_key, browser_scroll, browser_wait, browser_click_element,
    browser_type_element, browser_highlight_elements, browser_get_interactive_elements
)
from src.tools.browser_use_agent import browser_use_task
from src.tools.browser_agent import browser_navigate_tool, browser_interact_tool
from src.tools.recording import record_screen, stop_recording, analyze_recording, save_workflow, replay_workflow, list_workflows, export_video_mp4, record_webcam_video
from src.tools.video_editor import trim_video, concat_videos, change_video_speed, add_text_watermark, convert_video_to_gif, add_auto_subtitles


from src.tools.clipboard import clipboard_history, clipboard_search, clipboard_pin, clipboard_restore
from src.tools.voice import voice_record_and_transcribe, voice_speak
from src.tools.dynamic_manager import generate_dynamic_tool
from src.tools.papercoder import generate_paper2code
from src.tools.chrome_manager import launch_chrome_with_profile, get_chrome_profile_status
from database import save_user_preference, get_user_preference

from src.tools.ollama_manager import ollama_list_models, ollama_pull_model, ollama_delete_model
from src.tools.task_scheduler import win_schedule_daily, win_schedule_once, win_list_tasks, win_delete_task
from src.tools.security_auditor import run_security_audit
from src.tools.documents import (
    read_document_text, create_word_document, edit_word_document,
    create_excel_document, edit_excel_document, create_powerpoint_presentation,
    edit_powerpoint_presentation, create_pdf_document, edit_pdf_document
)

# JARVIS Perception & Intelligence Tools
from src.core.perception import (
    start_gaze_tracking, stop_gaze_tracking, get_current_gaze,
    list_camera_feeds, get_recent_alerts,
    list_ar_headsets, push_ar_hud_payload,
    predict_next_action, prewarm_context_for_intent,
    generate_presence_briefing
)
from src.voice.polyglot import translate_speech_to_code
from src.core.vision import analyze_screen_multimodal
from src.core.screen_sense import get_active_window_sense
from src.core.vision_face import get_presence_state
from src.voice.ambient_listener import get_recent_ambient_transcripts
from src.core.proactive import synthesize_ambient_nudge, generate_meeting_prep_briefing



from src.tools.phone_agent import make_outbound_call, screen_incoming_call, process_post_call_intelligence
from src.core.sos_protocol import trigger_emergency_sos
from src.tools.external_connectors import triage_inbox_emails, generate_draft_reply, manage_unsubscribes
from src.core.personal_crm import add_crm_contact, check_crm_occasions, list_crm_contacts

# Day 12 & Day 13 Butler, Knowledge, Finance & Security Tools
from src.tools.expiry_sentinel import add_expiry_document, check_document_expiries, list_expiry_documents
from src.tools.travel_butler import create_trip, calculate_leave_by_time, get_upcoming_trips
from src.tools.bill_radar import register_recurring_bill, get_bill_due_radar
from src.tools.finance_sentinel import analyze_stock_sentiment, get_market_watchlist
from src.tools.file_janitor import scan_downloads_folder, organize_downloads
from src.tools.search_hub import universal_search
from src.tools.screenshot_memory import capture_screenshot_memory, query_screenshot_memory
from src.tools.household import add_grocery_item, add_household_chore, get_household_summary
from src.tools.phishing_guard import check_url_reputation
from src.tools.totp_generator import generate_totp_code
from src.tools.password_auditor import audit_password_strength
from src.tools.network_guardian import audit_network_boundary
from src.tools.usb_watchdog import audit_usb_peripherals
from src.tools.dns_shield import audit_dns_health
from src.tools.cam_guard import audit_camera_mic_access
from src.tools.detonation_sandbox import detonate_attachment_sample





# Dynamic imports to avoid circular database referencing
def _ingest_file(path: str) -> str:
    from database import extract_text_from_file, ingest_into_knowledge_base
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    content = extract_text_from_file(path)
    ingest_into_knowledge_base(os.path.basename(path), content)
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


def query_cognitive_graph(query: str = "", start_node: str = "", max_hops: int = 2) -> str:
    """Traverse and query the Unified Cognitive Graph linking code, APIs, views, memories, and workflows."""
    from src.core.cognitive_graph import get_cognitive_graph
    cg = get_cognitive_graph()

    if start_node:
        subgraph = cg.traverse(start_node, max_hops=max_hops)
        if not subgraph.get("nodes"):
            return f"No related graph nodes found starting from '{start_node}'."
        lines = [f"Cognitive Graph neighborhood for '{start_node}' (hops <= {max_hops}):"]
        lines.append(f"Discovered {subgraph['total_nodes']} nodes, {subgraph['total_edges']} edges:")
        for n in subgraph["nodes"]:
            lines.append(f"  • [hop {n.get('hop', 0)}] ({n['type']}) {n['name']} (ID: {n['id']})")
        for e in subgraph["edges"]:
            lines.append(f"    └── [{e['source']}] --({e['relation']})--> [{e['target']}]")
        return "\n".join(lines)

    if query:
        nodes = cg.find_nodes(query, limit=5)
        if not nodes:
            return f"No cognitive graph nodes found matching query: '{query}'."
        lines = [f"Cognitive Graph search matches for '{query}':"]
        for n in nodes:
            lines.append(f"• [{n['type']}] {n['name']} (ID: {n['id']})")
            neighbors = cg.get_neighbors(n["id"], direction="both")
            for nb in neighbors[:3]:
                arrow = "-->" if nb["direction"] == "out" else "<--"
                lines.append(f"    └── {arrow} ({nb['relation']}) [{nb['node']['type']}] {nb['node']['name']}")
        return "\n".join(lines)

    return "Please specify either a 'query' to search nodes or 'start_node' to traverse relations."

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
    "universal_search": {"tier": 0, "func": universal_search, "description": "Unified cross-system search across AST code symbols, RAG knowledge docs, conversation memories, and workspace files."},
    "query_cognitive_graph": {"tier": 0, "func": query_cognitive_graph, "description": "Multi-hop relational search across the Unified Cognitive Graph linking code AST, frontend views, backend routes, and episodic memories."},
    "search_web": {"tier": 0, "func": search_web},
    "search_news": {"tier": 0, "func": search_news},
    "fetch_page": {"tier": 0, "func": fetch_page},
    "parse_page": {"tier": 0, "func": parse_page},
    "download_file": {"tier": 1, "func": download_file},
    "autonomous_research": {"tier": 1, "func": autonomous_research},
    "ingest_url": {"tier": 0, "func": ingest_url},
    
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
    "screenshot_to_code": {"tier": 1, "func": screenshot_to_code},
    
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
    "launch_chrome_with_profile": {"tier": 1, "func": launch_chrome_with_profile},
    "get_chrome_profile_status": {"tier": 0, "func": get_chrome_profile_status},
    "control_media_playback": {"tier": 1, "func": control_media_playback},
    "save_user_preference": {"tier": 1, "func": save_user_preference},
    "get_user_preference": {"tier": 0, "func": get_user_preference},
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
    "git_create_snapshot": {"tier": 0, "func": git_create_snapshot},
    "git_rollback": {"tier": 2, "func": git_rollback},
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
    "send_native_toast_notification": {"tier": 1, "func": send_native_toast_notification},
    "send_proactive_notification": {
        "tier": 1,
        "func": lambda title, message, priority="medium", category="general": __import__("src.core.proactive", fromlist=["dispatch_notification"]).dispatch_notification(title, message, priority, category)
    },
    "send_email": {"tier": 2, "func": send_email},
    "read_emails": {"tier": 0, "func": read_emails},
    "send_whatsapp_message": {"tier": 2, "func": send_whatsapp_message},
    "send_discord_message": {"tier": 2, "func": send_discord_message},
    "read_discord_messages": {"tier": 0, "func": read_discord_messages},
    "add_discord_reaction": {"tier": 1, "func": add_discord_reaction},
    "list_discord_channels": {"tier": 0, "func": list_discord_channels},
    "manage_whatsapp_contacts": {"tier": 1, "func": manage_whatsapp_contacts},
    "read_whatsapp_messages": {"tier": 0, "func": read_whatsapp_messages},
    "list_whatsapp_chats": {"tier": 0, "func": list_whatsapp_chats},
    "login_whatsapp_session": {"tier": 1, "func": login_whatsapp_session},
    "bridge_whatsapp_voice_call": {"tier": 2, "func": bridge_whatsapp_voice_call},
    "triage_and_read_emails": {"tier": 1, "func": triage_and_read_emails},
    "sync_wearable_health_data": {"tier": 1, "func": sync_wearable_health_data},
    "get_health_metrics_summary": {"tier": 0, "func": get_health_metrics_summary},
    "track_hydration": {"tier": 0, "func": track_hydration},
    "trigger_ergonomic_break": {"tier": 0, "func": trigger_ergonomic_break},
    "calculate_daily_wellness_score": {"tier": 0, "func": calculate_daily_wellness_score},



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
    "generate_unit_tests": {"tier": 1, "func": generate_unit_tests},
    "review_git_changes": {"tier": 0, "func": review_git_changes},

    # Day 10 Multimodal & Ambient Perception Tools
    "analyze_active_screen": {"tier": 0, "func": analyze_screen_multimodal},
    "get_active_window_sense": {"tier": 0, "func": get_active_window_sense},
    "get_presence_state": {"tier": 0, "func": get_presence_state},
    "get_ambient_speech_context": {"tier": 0, "func": get_recent_ambient_transcripts},
    "synthesize_ambient_nudge": {"tier": 0, "func": synthesize_ambient_nudge},

    # Day 11 Telephony, Emergency SOS, Email Triage & Personal CRM Tools
    "make_outbound_call": {"tier": 2, "func": make_outbound_call},
    "screen_incoming_call": {"tier": 0, "func": screen_incoming_call},
    "process_post_call_intelligence": {"tier": 0, "func": process_post_call_intelligence},
    "trigger_emergency_sos": {"tier": 2, "func": trigger_emergency_sos},
    "triage_inbox_emails": {"tier": 0, "func": triage_inbox_emails},
    "generate_draft_reply": {"tier": 1, "func": generate_draft_reply},
    "manage_unsubscribes": {"tier": 1, "func": manage_unsubscribes},
    "add_crm_contact": {"tier": 1, "func": add_crm_contact},
    "check_crm_occasions": {"tier": 0, "func": check_crm_occasions},
    "list_crm_contacts": {"tier": 0, "func": list_crm_contacts},
    "generate_meeting_prep_briefing": {"tier": 0, "func": generate_meeting_prep_briefing},




    # NL Shell
    "nl_to_shell": {"tier": 0, "func": nl_to_shell},
    "nl_run": {"tier": 2, "func": nl_run},
    "shell_history": {"tier": 0, "func": shell_history},
    "monitor_process": {"tier": 1, "func": monitor_process},

    # Geo-Location & Spatial Context Engine
    "resolve_location": {"tier": 0, "func": resolve_location},
    "get_localized_weather": {"tier": 0, "func": get_localized_weather},
    "bias_query_spatially": {"tier": 0, "func": bias_query_spatially},


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
    "browser_use_task": {"tier": 1, "func": browser_use_task, "description": "Primary default autonomous browser agent. Executes complex multi-step web tasks (search, navigate, click, fill forms, extract) live on screen with Set-of-Marks perception."},
    "browser_open": {"tier": 1, "func": browser_open, "description": "Open visible or headless browser window and navigate to URL."},
    "browser_navigate": {"tier": 1, "func": browser_navigate_tool, "description": "Navigate active browser to target URL."},
    "browser_click_element": {"tier": 2, "func": browser_click_element, "description": "Click element by Set-of-Marks numerical index '[1]' or selector."},
    "browser_type_element": {"tier": 2, "func": browser_type_element, "description": "Type text into element by index '[1]' or selector, with optional press_enter."},
    "browser_press_key": {"tier": 1, "func": browser_press_key, "description": "Press a keyboard key in the browser ('Enter', 'Escape', 'Tab', etc.)."},
    "browser_scroll": {"tier": 0, "func": browser_scroll, "description": "Scroll the active browser window up or down."},
    "browser_wait": {"tier": 0, "func": browser_wait, "description": "Wait for browser page to settle or animations to complete."},
    "browser_interact": {"tier": 2, "func": browser_interact_tool, "description": "Interact with browser element (action='click' or 'type')."},
    "browser_screenshot": {"tier": 0, "func": browser_screenshot, "description": "Capture screenshot of current browser viewport."},
    "browser_find_and_click": {"tier": 2, "func": browser_find_and_click, "description": "Find and click element by visual description or text."},
    "browser_type_in": {"tier": 2, "func": browser_type_in, "description": "Type into input field matching description."},
    "browser_get_text": {"tier": 0, "func": browser_get_text, "description": "Extract all readable text from current browser viewport."},
    "browser_close": {"tier": 1, "func": browser_close, "description": "Close active browser session."},
    "scrape_urls": {"tier": 1, "func": scrape_urls},
    "scrape_table": {"tier": 0, "func": scrape_table},
    "schedule_scrape": {"tier": 1, "func": schedule_scrape},

    # Screen Recording, Video Editing & Workflow Replay
    "record_screen": {"tier": 1, "func": record_screen},
    "stop_recording": {"tier": 1, "func": stop_recording},
    "analyze_recording": {"tier": 0, "func": analyze_recording},
    "save_workflow": {"tier": 1, "func": save_workflow},
    "replay_workflow": {"tier": 2, "func": replay_workflow},
    "list_workflows": {"tier": 0, "func": list_workflows},
    "export_video_mp4": {"tier": 1, "func": export_video_mp4},
    "record_webcam_video": {"tier": 1, "func": record_webcam_video},
    "trim_video": {"tier": 1, "func": trim_video},
    "concat_videos": {"tier": 1, "func": concat_videos},
    "change_video_speed": {"tier": 1, "func": change_video_speed},
    "add_text_watermark": {"tier": 1, "func": add_text_watermark},
    "convert_video_to_gif": {"tier": 1, "func": convert_video_to_gif},
    "add_auto_subtitles": {"tier": 1, "func": add_auto_subtitles},



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
    "create_dynamic_tool": {"tier": 3, "func": lambda name, code: create_dynamic_tool_wrapper(name, code)},
    "run_agent_swarm": {"tier": 2, "func": lambda goal, roles="researcher,auditor": run_agent_swarm_wrapper(goal, roles)},
    "mcp_list_servers": {"tier": 0, "func": lambda: mcp_list_servers_wrapper()},
    "run_autonomous_bug_fixer": {"tier": 2, "func": lambda target_path=None: run_autonomous_bug_fixer_wrapper(target_path)},

    # JARVIS Intelligence & Perception Tools
    "get_current_gaze": {"tier": 0, "func": get_current_gaze},
    "start_gaze_tracking": {"tier": 0, "func": start_gaze_tracking},
    "stop_gaze_tracking": {"tier": 0, "func": stop_gaze_tracking},
    "list_camera_feeds": {"tier": 0, "func": list_camera_feeds},
    "list_ar_headsets": {"tier": 0, "func": list_ar_headsets},
    "translate_speech_to_code": {"tier": 0, "func": translate_speech_to_code},
    "predict_next_action": {"tier": 0, "func": predict_next_action},
    "generate_presence_briefing": {"tier": 0, "func": generate_presence_briefing},

    # Day 12 & Day 13 Butler, Knowledge, Finance & Security Tools
    "add_expiry_document": {"tier": 1, "func": add_expiry_document},
    "check_document_expiries": {"tier": 0, "func": check_document_expiries},
    "list_expiry_documents": {"tier": 0, "func": list_expiry_documents},
    "create_trip": {"tier": 1, "func": create_trip},
    "calculate_leave_by_time": {"tier": 0, "func": calculate_leave_by_time},
    "get_upcoming_trips": {"tier": 0, "func": get_upcoming_trips},
    "register_recurring_bill": {"tier": 1, "func": register_recurring_bill},
    "get_bill_due_radar": {"tier": 0, "func": get_bill_due_radar},
    "analyze_stock_sentiment": {"tier": 0, "func": analyze_stock_sentiment},
    "get_market_watchlist": {"tier": 0, "func": get_market_watchlist},
    "scan_downloads_folder": {"tier": 0, "func": scan_downloads_folder},
    "organize_downloads": {"tier": 2, "func": organize_downloads},
    "universal_search": {"tier": 0, "func": universal_search},
    "capture_screenshot_memory": {"tier": 1, "func": capture_screenshot_memory},
    "query_screenshot_memory": {"tier": 0, "func": query_screenshot_memory},
    "add_grocery_item": {"tier": 1, "func": add_grocery_item},
    "add_household_chore": {"tier": 1, "func": add_household_chore},
    "get_household_summary": {"tier": 0, "func": get_household_summary},
    "check_url_reputation": {"tier": 0, "func": check_url_reputation},
    "generate_totp_code": {"tier": 0, "func": generate_totp_code},
    "audit_password_strength": {"tier": 0, "func": audit_password_strength},
    "audit_network_boundary": {"tier": 0, "func": audit_network_boundary},
    "audit_usb_peripherals": {"tier": 0, "func": audit_usb_peripherals},
    "audit_dns_health": {"tier": 0, "func": audit_dns_health},
    "audit_camera_mic_access": {"tier": 0, "func": audit_camera_mic_access},
    "detonate_attachment_sample": {"tier": 2, "func": detonate_attachment_sample}
}

def mcp_list_servers_wrapper() -> str:
    from src.tools.mcp_marketplace import mcp_list_servers_tool
    return mcp_list_servers_tool()

def mcp_install_server_wrapper(server_id: str) -> str:
    from src.tools.mcp_marketplace import mcp_install_server_tool
    return mcp_install_server_tool(server_id)


def _run_coro_safe(coro):
    """Executes a coroutine safely, supporting execution inside an active event loop."""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            return pool.submit(lambda: asyncio.run(coro)).result()
    else:
        return asyncio.run(coro)


def run_agent_swarm_wrapper(goal: str, roles: str = "researcher,auditor") -> str:
    """BK-10: Spawns parallel specialized subagents to work on a goal concurrently."""
    try:
        from src.core.swarm import SwarmOrchestrator
        role_list = [r.strip() for r in roles.split(",") if r.strip()]
        res = _run_coro_safe(SwarmOrchestrator().run_swarm(goal, role_list))
        return res.get("synthesis", "Swarm execution complete.")
    except Exception as e:
        return f"Swarm execution failed: {e}"


def run_autonomous_bug_fixer_wrapper(target_path: Optional[str] = None) -> str:
    """DEV-01: Autonomous Background Bug Fixer & Auto-PR Agent."""
    import json
    try:
        from src.core.swarm import AutonomousBugFixer
        fixer = AutonomousBugFixer()
        res = _run_coro_safe(fixer.auto_fix_pipeline(target_path=target_path))
        return json.dumps(res, indent=2)
    except Exception as e:
        return f"Autonomous bug fixer execution failed: {e}"



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

# Auto-discover plugins at runtime — LAZY by design. Importing this module must
# not spawn threads or print: use ensure_plugins_loaded() at explicit entry
# points (API startup, call_tool, ToolRegistry accessors).
_plugins_loaded = False


def ensure_plugins_loaded() -> None:
    """Idempotent plugin auto-discovery (imports plugin tools + starts the
    hot-reload watcher). Safe to call from any entry point."""
    global _plugins_loaded
    if _plugins_loaded:
        return
    _plugins_loaded = True
    try:
        from src.core.plugins import load_plugins
        load_plugins(TOOL_REGISTRY)
    except Exception as e:
        print("[Plugins] Auto-discovery activation failed:", e)

# Register Day 16, 17, 18 Tools
try:
    from src.tools.workspace_layout import arrange_workspace_grid
    from src.tools.learning_queue import add_to_learning_queue, generate_reading_digest
    from src.tools.price_watcher import add_watched_product, check_price_drops
    from src.tools.networth_tracker import get_networth_summary
    from src.tools.wifi_assessor import assess_wifi_security
    from src.tools.bookmark_manager import add_bookmark, list_bookmarks

    TOOL_REGISTRY["arrange_workspace_grid"] = {"func": arrange_workspace_grid, "description": "Arrange active desktop windows into 2x2 grid", "tier": 1}
    TOOL_REGISTRY["add_to_learning_queue"] = {"func": add_to_learning_queue, "description": "Save article or link for later reading", "tier": 1}
    TOOL_REGISTRY["generate_reading_digest"] = {"func": generate_reading_digest, "description": "Generate SM-2 reading digest summary", "tier": 1}
    TOOL_REGISTRY["add_watched_product"] = {"func": add_watched_product, "description": "Track e-commerce product price drops", "tier": 1}
    TOOL_REGISTRY["get_networth_summary"] = {"func": get_networth_summary, "description": "Get total assets vs liabilities snapshot", "tier": 1}
    TOOL_REGISTRY["assess_wifi_security"] = {"func": assess_wifi_security, "description": "Assess Wi-Fi security and firewall status", "tier": 1}
    TOOL_REGISTRY["add_bookmark"] = {"func": add_bookmark, "description": "Add auto-tagged smart bookmark", "tier": 1}
except Exception as _tool_err:
    print("[Registry] Day 16-18 tool registration warning:", _tool_err)


async def call_tool(name: str, args: Dict[str, Any]) -> str:
    ensure_plugins_loaded()
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

def register_dynamic_tool(name: str, func: Any, description: str = "", tier: int = 1):
    """Registers a dynamically generated tool at runtime (AST-13)."""
    TOOL_REGISTRY[name] = {
        "func": func,
        "description": description,
        "tier": tier
    }


def register_tool(name: str, metadata: Dict[str, Any]) -> bool:
    """Register a new tool with full metadata."""
    try:
        # Validate required fields
        if not name or not isinstance(name, str):
            return False
            
        # Create tool entry
        TOOL_REGISTRY[name] = {
            "func": None,  # Will be set dynamically when needed
            "description": metadata.get("description", ""),
            "tier": metadata.get("tier", 1),
            "inputSchema": metadata.get("inputSchema", {"type": "object", "properties": {}}),
            "outputSchema": metadata.get("outputSchema", {"type": "object", "properties": {}}),
            "supportsStreaming": metadata.get("supportsStreaming", False),
            "handlerModule": metadata.get("handlerModule", ""),
            "handlerFunction": metadata.get("handlerFunction", ""),
            "metadata": metadata  # Store full metadata for reference
        }
        return True
    except Exception:
        return False


def unregister_tool(name: str) -> bool:
    """Unregister a tool by name."""
    try:
        if name in TOOL_REGISTRY:
            del TOOL_REGISTRY[name]
            return True
        return False
    except Exception:
        return False


class ToolRegistry:
    """Class wrapper for tool registry operations."""
    def list_tools(self) -> list:
        ensure_plugins_loaded()
        return [{"name": k, "description": v.get("description", ""), "tier": v.get("tier", 1)} for k, v in TOOL_REGISTRY.items()]

    def get_tool(self, name: str) -> Optional[Any]:
        ensure_plugins_loaded()
        info = TOOL_REGISTRY.get(name)
        return info["func"] if info else None

registry = ToolRegistry()


