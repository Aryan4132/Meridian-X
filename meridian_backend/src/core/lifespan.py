"""Lifespan background service lifecycle manager for Meridian-X."""

import os
import asyncio
import logging
import platform
import threading
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.core.mcp_client import mcp_manager
from src.api.deps import ENV_KEY_MAP


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Orchestrates initialization and graceful shutdown of Meridian-X background daemons."""
    if "PYTEST_CURRENT_TEST" in os.environ or os.environ.get("TESTING") == "true":
        yield
        return
    # 1. Environment & Profiles
    try:
        from database import get_user_profile
        for profile_key, env_key in ENV_KEY_MAP.items():
            if not os.environ.get(env_key):
                val = get_user_profile(profile_key)
                if val is not None and val != "":
                    os.environ[env_key] = str(val)
                    print(f"[Startup] Loaded {env_key} from database profile.")
    except Exception as e:
        print("[Startup] Failed to load database profile keys into env:", e)

    # 2. Encrypted Vault Custom Keys
    try:
        from src.core.vault import inject_vault_keys_to_env
        inject_vault_keys_to_env()
        print("[Startup] Loaded encrypted Vault custom API keys into environment.")
    except Exception as e:
        print("[Startup] Failed to inject Vault keys:", e)

    # 3. System Logger Setup
    try:
        from src.core.logging_config import setup_logger
        log_file = setup_logger()
        logging.info("=========================================")
        logging.info("Starting Meridian-X Backend Service")
        logging.info(f"Process PID: {os.getpid()}")
        logging.info(f"System OS: {platform.system()} {platform.release()}")
        logging.info(f"Python Version: {platform.python_version()}")
        logging.info(f"Log File Location: {log_file}")
        logging.info("=========================================")
    except Exception as e:
        print("Failed to initialize logging:", e)

    # 4. Proactive Event Loop Binding
    try:
        from src.core.proactive import set_main_event_loop
        set_main_event_loop(asyncio.get_running_loop())
        print("[Startup] Bound main FastAPI event loop to proactive publisher.")
    except Exception as e:
        print("Failed to bind proactive event loop:", e)

    # 5. Smart Clipboard Monitoring
    try:
        from database import get_user_profile
        clip_pref = get_user_profile("smart_clipboard_enabled")
        if str(clip_pref).lower() != "false":
            from src.core.clipboard import start_clipboard_monitoring
            start_clipboard_monitoring()
        else:
            print("[Startup] Clipboard monitoring idle (smart_clipboard_enabled is false).")
    except Exception as e:
        print("Failed to start clipboard monitoring:", e)

    # 6. Task Scheduler
    try:
        from src.core.scheduler import start_scheduler
        start_scheduler()
    except Exception as e:
        print("Failed to start scheduler:", e)

    # 7. Plugins Autodiscovery
    try:
        from src.tools.registry import ensure_plugins_loaded
        ensure_plugins_loaded()
    except Exception as e:
        print("Failed to auto-discover plugins:", e)

    # 8. Workspace Knowledge Graph Scan
    try:
        from src.core.graph_sync import scan_workspaces
        try:
            from src.core.history_manager import find_workspace_root
            parent_dir = os.path.dirname(find_workspace_root())
        except Exception:
            parent_dir = os.getcwd()
        threading.Thread(target=scan_workspaces, args=(parent_dir,), daemon=True).start()
        print("Triggered initial workspace Knowledge Graph scan.")
    except Exception as e:
        print("Failed to trigger initial workspace scan:", e)

    # 9. MCP Servers Connection
    try:
        await mcp_manager.initialize()
        print("Initialized MCP servers connection.")
    except Exception as e:
        print("Failed to initialize MCP servers:", e)

    # 10. P2P Mesh Sync
    try:
        if os.environ.get("P2P_ENABLED", "false").lower() in ("true", "1", "yes"):
            from src.core.p2p import p2p_node
            msg = p2p_node.start()
            print(msg)
        else:
            print("[Startup] P2P mesh sync idle (enable with P2P_ENABLED=true).")
    except Exception as e:
        print("Failed to start P2P sync node:", e)

    # 11. Filesystem Watcher
    try:
        from src.core.watcher import start_workspace_watcher
        start_workspace_watcher(".")
    except Exception as e:
        print("Failed to start workspace watcher:", e)

    # 12. Wake Word Monitoring
    try:
        from database import get_user_profile
        wakeword_pref = get_user_profile("wakeword_enabled")
        wakeword_env = os.environ.get("WAKEWORD_ENABLED", "false")
        is_wakeword_on = str(wakeword_pref if wakeword_pref is not None else wakeword_env).lower() in ("true", "1", "yes")
        if is_wakeword_on:
            from src.voice.wakeword import start_wakeword_monitoring
            start_wakeword_monitoring()
            print("[Startup] Wake word monitoring active.")
        else:
            print("[Startup] Wake word monitoring idle (enable in Settings).")
    except Exception as e:
        print("Failed to start wake word monitoring:", e)

    # 13. External Bot Bridges (Telegram, Discord)
    if not os.environ.get("TELEGRAM_BOT_TOKEN"):
        print("[Startup] Telegram bridge disabled: TELEGRAM_BOT_TOKEN not set.")
    elif not (os.environ.get("MERIDIAN_ALLOWED_TELEGRAM_IDS", "").strip()
              or os.environ.get("TELEGRAM_AUTHORIZED_CHAT_ID", "").strip()):
        print("[Startup] Telegram bridge will deny all chats: set "
              "MERIDIAN_ALLOWED_TELEGRAM_IDS or TELEGRAM_AUTHORIZED_CHAT_ID.")
    if not os.environ.get("DISCORD_BOT_TOKEN"):
        print("[Startup] Discord bridge disabled: DISCORD_BOT_TOKEN not set.")
    elif not os.environ.get("MERIDIAN_ALLOWED_DISCORD_IDS", "").strip():
        print("[Startup] Discord bridge will deny all users: set "
              "MERIDIAN_ALLOWED_DISCORD_IDS.")
    try:
        from src.core.telegram_bridge import start_telegram_bridge
        start_telegram_bridge()
    except Exception as e:
        print("Failed to start Telegram bridge:", e)

    try:
        from src.core.discord_bridge import start_discord_bridge
        start_discord_bridge()
    except Exception as e:
        print("Failed to start Discord bridge:", e)

    # 14. Offline Docs Indexer Scan
    try:
        from src.core.doc_indexer import index_docs_directory
        from src.core.history_manager import find_workspace_root
        workspace_dir = find_workspace_root()
        docs_dir = os.path.join(workspace_dir, ".meridian", "docs")
        if os.path.exists(docs_dir):
            threading.Thread(target=index_docs_directory, args=(docs_dir,), daemon=True).start()
            print("Triggered initial offline docs indexer scan.")
        else:
            print(f"[Docs Indexer] No offline docs folder found at: {docs_dir}")
    except Exception as e:
        print("Failed to trigger doc indexer:", e)

    # 15. Pre-warm Models (TTS & STT in background thread)
    try:
        def prewarm_models():
            print("[Pre-Warming] Waking up local TTS and Whisper STT models in the background...")
            try:
                from src.voice.tts import get_tts_engine
                get_tts_engine()
                print("[Pre-Warming] Local TTS engine ready.")
            except Exception as tts_err:
                print("[Pre-Warming] Failed to pre-warm local TTS engine:", tts_err)
            try:
                from src.voice.stt import get_whisper_model
                get_whisper_model()
                print("[Pre-Warming] Local Whisper STT model ready.")
            except Exception as stt_err:
                print("[Pre-Warming] Failed to pre-warm local Whisper model:", stt_err)

        threading.Thread(target=prewarm_models, daemon=True).start()
    except Exception as e:
        print("[Pre-Warming] Failed to start pre-warming thread:", e)

    yield

    # ================= SHUTDOWN =================
    try:
        await mcp_manager.shutdown()
        print("Stopped all MCP servers.")
    except Exception as e:
        print("Failed to shutdown MCP manager:", e)
    try:
        from src.core.telegram_bridge import stop_telegram_bridge
        stop_telegram_bridge()
    except Exception as e:
        print("Failed to stop Telegram bridge:", e)
    try:
        from src.core.discord_bridge import stop_discord_bridge
        stop_discord_bridge()
    except Exception as e:
        print("Failed to stop Discord bridge:", e)
    try:
        from src.voice.wakeword import stop_wakeword_monitoring
        stop_wakeword_monitoring()
    except Exception as e:
        print("Failed to stop wake word monitoring:", e)
    try:
        from src.core.watcher import stop_workspace_watcher
        stop_workspace_watcher()
    except Exception as e:
        print("Failed to stop workspace watcher:", e)
    try:
        from src.core.clipboard import stop_clipboard_monitoring
        stop_clipboard_monitoring()
    except Exception as e:
        print("Failed to stop clipboard monitoring:", e)
    try:
        from src.core.scheduler import stop_scheduler
        stop_scheduler()
    except Exception as e:
        print("Failed to stop scheduler:", e)
    try:
        from src.core.p2p import p2p_node
        msg = p2p_node.stop()
        print(msg)
    except Exception as e:
        print("Failed to stop P2P sync node:", e)
    try:
        from src.core.watcher import stop_all_watchers
        stop_all_watchers()
        print("Stopped all filesystem watchers.")
    except Exception as e:
        print("Failed to stop filesystem watchers:", e)
    try:
        from src.core.logging_config import shutdown_logger
        shutdown_logger()
    except Exception as e:
        print("Failed to shut down logging:", e)
