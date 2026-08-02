# Workspace Architecture & Component Map
Generated automatically by Meridian-X.

## Component Dependency Graph
```mermaid
graph TD
    N1["build_standalone.py []"]
    N2["bump_version.py []"]
    N3["cleanup.py []"]
    N4["create_shortcut.py []"]
    N5["main.py []"]
    N6["setup_db.py []"]
    N7["setup_startup.py []"]
    N8["verify_system.py []"]
    N9["temporal_consensus_guard.py [agent]"]
    N10["api.py [meridian_backend]"]
    N11["database.py [meridian_backend]"]
    N12["audit_logger.py [meridian_backend/src/core]"]
    N13["auth.py [meridian_backend/src/core]"]
    N14["bus.py [meridian_backend/src/core]"]
    N15["clipboard.py [meridian_backend/src/core]"]
    N16["code_graph.py [meridian_backend/src/core]"]
    N17["config.py [meridian_backend/src/core]"]
    N18["discord_bridge.py [meridian_backend/src/core]"]
    N19["doc_generator.py [meridian_backend/src/core]"]
    N20["doc_indexer.py [meridian_backend/src/core]"]
    N21["exporter.py [meridian_backend/src/core]"]
    N22["governor.py [meridian_backend/src/core]"]
    N23["graph_rag.py [meridian_backend/src/core]"]
    N24["graph_sync.py [meridian_backend/src/core]"]
    N25["history_manager.py [meridian_backend/src/core]"]
    N26["llm_provider.py [meridian_backend/src/core]"]
    N27["logging_config.py [meridian_backend/src/core]"]
    N28["loop.py [meridian_backend/src/core]"]
    N29["loop_dispatcher.py [meridian_backend/src/core]"]
    N30["loop_parser.py [meridian_backend/src/core]"]
    N31["loop_stream.py [meridian_backend/src/core]"]
    N32["lsp_client.py [meridian_backend/src/core]"]
    N33["mcp_client.py [meridian_backend/src/core]"]
    N34["mcp_executor.py [meridian_backend/src/core]"]
    N35["mode.py [meridian_backend/src/core]"]
    N36["p2p.py [meridian_backend/src/core]"]
    N37["p2p_crypto.py [meridian_backend/src/core]"]
    N38["plugins.py [meridian_backend/src/core]"]
    N39["proactive.py [meridian_backend/src/core]"]
    N40["prompt_injection.py [meridian_backend/src/core]"]
    N41["prompt_templates.py [meridian_backend/src/core]"]
    N42["rag_optimizer.py [meridian_backend/src/core]"]
    N43["scheduler.py [meridian_backend/src/core]"]
    N44["security_middleware.py [meridian_backend/src/core]"]
    N45["speculative.py [meridian_backend/src/core]"]
    N46["swarm.py [meridian_backend/src/core]"]
    N47["telegram_bridge.py [meridian_backend/src/core]"]
    N48["temporal_memory.py [meridian_backend/src/core]"]
    N49["triggers.py [meridian_backend/src/core]"]
    N50["vault.py [meridian_backend/src/core]"]
    N51["vision.py [meridian_backend/src/core]"]
    N52["watcher.py [meridian_backend/src/core]"]
    N53["browser_agent.py [meridian_backend/src/tools]"]
    N54["clipboard.py [meridian_backend/src/tools]"]
    N55["communication.py [meridian_backend/src/tools]"]
    N56["db_query.py [meridian_backend/src/tools]"]
    N57["desktop.py [meridian_backend/src/tools]"]
    N58["developer.py [meridian_backend/src/tools]"]
    N59["documents.py [meridian_backend/src/tools]"]
    N60["dynamic_manager.py [meridian_backend/src/tools]"]
    N61["exporter.py [meridian_backend/src/tools]"]
    N62["filesystem.py [meridian_backend/src/tools]"]
    N63["knowledge.py [meridian_backend/src/tools]"]
    N64["mcp_marketplace.py [meridian_backend/src/tools]"]
    N65["ollama_manager.py [meridian_backend/src/tools]"]
    N66["recording.py [meridian_backend/src/tools]"]
    N67["registry.py [meridian_backend/src/tools]"]
    N68["review.py [meridian_backend/src/tools]"]
    N69["scheduler.py [meridian_backend/src/tools]"]
    N70["security_auditor.py [meridian_backend/src/tools]"]
    N71["shell.py [meridian_backend/src/tools]"]
    N72["system.py [meridian_backend/src/tools]"]
    N73["task_scheduler.py [meridian_backend/src/tools]"]
    N74["vault.py [meridian_backend/src/tools]"]
    N75["voice.py [meridian_backend/src/tools]"]
    N76["watcher.py [meridian_backend/src/tools]"]
    N77["web.py [meridian_backend/src/tools]"]
    N78["web_browser.py [meridian_backend/src/tools]"]
    N79["duplex.py [meridian_backend/src/voice]"]
    N80["stt.py [meridian_backend/src/voice]"]
    N81["tts.py [meridian_backend/src/voice]"]
    N82["wakeword.py [meridian_backend/src/voice]"]
    N83["run_tests.py [meridian_backend/tests]"]
    N84["test_backlog_features.py [meridian_backend/tests]"]
    N85["test_backlog_sprint.py [meridian_backend/tests]"]
    N86["test_bridges.py [meridian_backend/tests]"]
    N87["test_config.py [meridian_backend/tests]"]
    N88["test_context_budget.py [meridian_backend/tests]"]
    N89["test_database.py [meridian_backend/tests]"]
    N90["test_document_tools.py [meridian_backend/tests]"]
    N91["test_llm_provider.py [meridian_backend/tests]"]
    N92["test_logging.py [meridian_backend/tests]"]
    N93["test_loop_parser.py [meridian_backend/tests]"]
    N94["test_loop_submodules.py [meridian_backend/tests]"]
    N95["test_model_source.py [meridian_backend/tests]"]
    N96["test_p2p.py [meridian_backend/tests]"]
    N97["test_proactive.py [meridian_backend/tests]"]
    N98["test_security_features.py [meridian_backend/tests]"]
    N99["test_sprint2_features.py [meridian_backend/tests]"]
    N100["test_swarm.py [meridian_backend/tests]"]
    N101["test_temporal_consensus.py [meridian_backend/tests]"]
    N102["test_tools.py [meridian_backend/tests]"]
    N103["test_vault.py [meridian_backend/tests]"]
    N104["test_wakeword_onnx.py [meridian_backend/tests]"]
    N105["vite.config.ts [meridian_frontend]"]
    N106["AppContext.tsx [meridian_frontend/src]"]
    N107["main.tsx [meridian_frontend/src]"]
    N108["Mascot.tsx [meridian_frontend/src]"]
    N109["CommandPalette.tsx [meridian_frontend/src/components]"]
    N110["NavRail.tsx [meridian_frontend/src/components]"]
    N111["RightDrawer.tsx [meridian_frontend/src/components]"]
    N112["Shell.tsx [meridian_frontend/src/components]"]
    N113["StatusBar.tsx [meridian_frontend/src/components]"]
    N114["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N115["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N116["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N117["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N118["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N119["BootSequence.tsx [meridian_frontend/src/startup]"]
    N120["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N121["Clipboard.tsx [meridian_frontend/src/views]"]
    N122["GameOverlay.tsx [meridian_frontend/src/views]"]
    N123["Jobs.tsx [meridian_frontend/src/views]"]
    N124["LocalStudio.tsx [meridian_frontend/src/views]"]
    N125["Productivity.tsx [meridian_frontend/src/views]"]
    N126["SecurityPanel.tsx [meridian_frontend/src/views]"]
    N127["Settings.tsx [meridian_frontend/src/views]"]
    N128["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N129["Timeline.tsx [meridian_frontend/src/views]"]
    N130["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N131["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N132["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N133["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N134["get_system_platform_info.py [plugins]"]

    N5 --> N10
    N10 --> N11
    N15 --> N11
    N18 --> N11
    N20 --> N11
    N21 --> N11
    N26 --> N11
    N28 --> N11
    N30 --> N11
    N31 --> N11
    N35 --> N11
    N36 --> N11
    N39 --> N11
    N39 --> N10
    N43 --> N11
    N47 --> N11
    N51 --> N11
    N54 --> N11
    N56 --> N11
    N57 --> N11
    N61 --> N11
    N63 --> N11
    N65 --> N11
    N66 --> N11
    N67 --> N11
    N68 --> N11
    N71 --> N11
    N77 --> N11
    N78 --> N11
    N80 --> N11
    N81 --> N11
    N82 --> N11
    N84 --> N11
    N85 --> N10
    N88 --> N11
    N89 --> N11
    N95 --> N11
    N96 --> N11
    N98 --> N10
    N99 --> N10
    N104 --> N10
    N106 --> N133
    N106 --> N17
    N107 --> N108
    N107 --> N119
    N107 --> N120
    N107 --> N112
    N107 --> N106
    N107 --> N17
    N110 --> N106
    N110 --> N108
    N111 --> N106
    N111 --> N117
    N111 --> N114
    N112 --> N106
    N112 --> N110
    N112 --> N113
    N112 --> N111
    N112 --> N129
    N112 --> N123
    N112 --> N121
    N112 --> N125
    N112 --> N128
    N112 --> N127
    N113 --> N106
    N113 --> N114
    N119 --> N17
    N120 --> N116
    N120 --> N17
    N121 --> N133
    N121 --> N106
    N121 --> N116
    N121 --> N17
    N123 --> N133
    N123 --> N116
    N123 --> N115
    N123 --> N17
    N125 --> N133
    N125 --> N117
    N125 --> N116
    N125 --> N115
    N125 --> N17
    N127 --> N17
    N127 --> N133
    N127 --> N106
    N127 --> N117
    N127 --> N116
    N127 --> N115
    N128 --> N118
    N128 --> N116
    N128 --> N17
    N129 --> N133
    N129 --> N116
    N129 --> N115
    N129 --> N17
    N132 --> N133
    N133 --> N132
```

## Detailed File Index
- **agent/temporal_consensus_guard.py**
  - Imports: `datetime`
  - Imports: `re`
- **build_standalone.py**
  - Imports: `glob`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `shutil`
  - Imports: `subprocess`
  - Imports: `sys`
- **bump_version.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `re`
  - Imports: `sys`
- **cleanup.py**
  - Imports: `os`
  - Imports: `shutil`
- **create_shortcut.py**
  - Imports: `os`
  - Imports: `subprocess`
- **main.py**
  - Imports: `api`
  - Imports: `argparse`
  - Imports: `asyncio`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `uvicorn`
- **meridian_backend/api.py**
  - Imports: `_thread`
  - Imports: `ast`
  - Imports: `asyncio`
  - Imports: `base64`
  - Imports: `contextlib`
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `pydantic`
  - Imports: `random`
  - Imports: `re`
  - Imports: `secrets`
  - Imports: `shutil`
  - Imports: `slowapi`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `trustme`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `uuid`
  - Imports: `uvicorn`
- **meridian_backend/database.py**
  - Imports: `datetime`
  - Imports: `docx`
  - Imports: `json`
  - Imports: `numpy`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `pymongo`
  - Imports: `pypdf`
  - Imports: `random`
  - Imports: `sqlite3`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `turbovec`
  - Imports: `typing`
- **meridian_backend/src/core/audit_logger.py**
  - Imports: `getpass`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
- **meridian_backend/src/core/auth.py**
  - Imports: `fastapi`
  - Imports: `hmac`
  - Imports: `os`
  - Imports: `secrets`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/bus.py**
  - Imports: `asyncio`
  - Imports: `typing`
- **meridian_backend/src/core/clipboard.py**
  - Imports: `database`
  - Imports: `pyperclip`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/code_graph.py**
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
- **meridian_backend/src/core/config.py**
  - Imports: `os`
- **meridian_backend/src/core/discord_bridge.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `discord`
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
- **meridian_backend/src/core/doc_generator.py**
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
- **meridian_backend/src/core/doc_indexer.py**
  - Imports: `database`
  - Imports: `hashlib`
  - Imports: `json`
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `sqlite3`
  - Imports: `time`
  - Imports: `turbovec`
- **meridian_backend/src/core/exporter.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/governor.py**
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/graph_rag.py**
  - Imports: `ast`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/graph_sync.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/history_manager.py**
  - Imports: `os`
  - Imports: `subprocess`
- **meridian_backend/src/core/llm_provider.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `math`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/logging_config.py**
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/src/core/loop.py**
  - Imports: `anthropic`
  - Imports: `ast`
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `inspect`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `openai`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `random`
  - Imports: `re`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `uuid`
- **meridian_backend/src/core/loop_dispatcher.py**
  - Imports: `asyncio`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/loop_parser.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/loop_stream.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `json`
  - Imports: `typing`
- **meridian_backend/src/core/lsp_client.py**
  - Imports: `asyncio`
  - Imports: `json`
  - Imports: `os`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_backend/src/core/mcp_client.py**
  - Imports: `asyncio`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `typing`
- **meridian_backend/src/core/mcp_executor.py**
  - Imports: `asyncio`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `meridian_backend`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/mode.py**
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/p2p.py**
  - Imports: `base64`
  - Imports: `cryptography`
  - Imports: `database`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `json`
  - Imports: `os`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `zeroconf`
- **meridian_backend/src/core/p2p_crypto.py**
  - Imports: `base64`
  - Imports: `hashlib`
  - Imports: `os`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/plugins.py**
  - Imports: `importlib`
  - Imports: `inspect`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `watchdog`
- **meridian_backend/src/core/proactive.py**
  - Imports: `api`
  - Imports: `asyncio`
  - Imports: `ctypes`
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `random`
  - Imports: `re`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/prompt_injection.py**
  - Imports: `logging`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/prompt_templates.py**
  - Imports: `json`
  - Imports: `typing`
- **meridian_backend/src/core/rag_optimizer.py**
  - Imports: `math`
  - Imports: `re`
  - Imports: `typing`
- **meridian_backend/src/core/scheduler.py**
  - Imports: `apscheduler`
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `pynvml`
  - Imports: `src`
  - Imports: `time`
- **meridian_backend/src/core/security_middleware.py**
  - Imports: `fastapi`
  - Imports: `logging`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_backend/src/core/speculative.py**
  - Imports: `asyncio`
  - Imports: `json`
  - Imports: `os`
  - Imports: `re`
  - Imports: `socket`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_backend/src/core/swarm.py**
  - Imports: `asyncio`
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/telegram_bridge.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `src`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/temporal_memory.py**
  - Imports: `math`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/triggers.py**
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/vault.py**
  - Imports: `base64`
  - Imports: `cryptography`
  - Imports: `getpass`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `json`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/vision.py**
  - Imports: `base64`
  - Imports: `database`
  - Imports: `httpx`
  - Imports: `logging`
  - Imports: `mss`
  - Imports: `os`
  - Imports: `pyautogui`
  - Imports: `src`
  - Imports: `tempfile`
- **meridian_backend/src/core/watcher.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/browser_agent.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/clipboard.py**
  - Imports: `bson`
  - Imports: `database`
  - Imports: `platform`
  - Imports: `pyperclip`
  - Imports: `shutil`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/communication.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `pyautogui`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/db_query.py**
  - Imports: `database`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `psycopg2`
  - Imports: `pymysql`
  - Imports: `sqlite3`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `typing`
- **meridian_backend/src/tools/desktop.py**
  - Imports: `PIL`
  - Imports: `database`
  - Imports: `mss`
  - Imports: `os`
  - Imports: `pyautogui`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/developer.py**
  - Imports: `asyncio`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `tempfile`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/documents.py**
  - Imports: `docx`
  - Imports: `openpyxl`
  - Imports: `os`
  - Imports: `pptx`
  - Imports: `pypdf`
  - Imports: `re`
  - Imports: `reportlab`
  - Imports: `src`
  - Imports: `typing`
  - Imports: `xlrd`
- **meridian_backend/src/tools/dynamic_manager.py**
  - Imports: `ast`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_backend/src/tools/exporter.py**
  - Imports: `database`
  - Imports: `json`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/filesystem.py**
  - Imports: `glob`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/knowledge.py**
  - Imports: `database`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/mcp_marketplace.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/ollama_manager.py**
  - Imports: `database`
  - Imports: `threading`
- **meridian_backend/src/tools/recording.py**
  - Imports: `database`
  - Imports: `glob`
  - Imports: `json`
  - Imports: `mss`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `pyautogui`
  - Imports: `pyperclip`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/registry.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `inspect`
  - Imports: `os`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/review.py**
  - Imports: `database`
  - Imports: `glob`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `subprocess`
  - Imports: `typing`
- **meridian_backend/src/tools/scheduler.py**
  - Imports: `apscheduler`
  - Imports: `datetime`
  - Imports: `src`
- **meridian_backend/src/tools/security_auditor.py**
  - Imports: `os`
  - Imports: `re`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `typing`
- **meridian_backend/src/tools/shell.py**
  - Imports: `database`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `select,`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/system.py**
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `pyautogui`
  - Imports: `pygetwindow`
  - Imports: `pyperclip`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `time`
  - Imports: `webbrowser`
  - Imports: `winreg`
- **meridian_backend/src/tools/task_scheduler.py**
  - Imports: `csv`
  - Imports: `os`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
- **meridian_backend/src/tools/vault.py**
  - Imports: `base64`
  - Imports: `cryptography`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/voice.py**
  - Imports: `src`
- **meridian_backend/src/tools/watcher.py**
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/web.py**
  - Imports: `concurrent`
  - Imports: `database`
  - Imports: `ddgs`
  - Imports: `duckduckgo_search`
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `re`
  - Imports: `selectolax`
  - Imports: `sqlite3,`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/web_browser.py**
  - Imports: `database`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `playwright`
  - Imports: `re`
  - Imports: `selectolax`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/voice/duplex.py**
  - Imports: `asyncio`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/voice/stt.py**
  - Imports: `database`
  - Imports: `faster_whisper`
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `scipy`
  - Imports: `sounddevice`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `torch`
  - Imports: `typing`
- **meridian_backend/src/voice/tts.py**
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `os`
  - Imports: `queue`
  - Imports: `random`
  - Imports: `re`
  - Imports: `sounddevice`
  - Imports: `soundfile`
  - Imports: `src`
  - Imports: `supertonic`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/voice/wakeword.py**
  - Imports: `database`
  - Imports: `numpy`
  - Imports: `openwakeword`
  - Imports: `os`
  - Imports: `sounddevice`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `threading`
  - Imports: `time`
- **meridian_backend/tests/run_tests.py**
  - Imports: `os`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_backlog_features.py**
  - Imports: `database`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_backlog_sprint.py**
  - Imports: `api`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_bridges.py**
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `time`
- **meridian_backend/tests/test_config.py**
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_context_budget.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `sys`
- **meridian_backend/tests/test_database.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_document_tools.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_llm_provider.py**
  - Imports: `asyncio`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_logging.py**
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_loop_parser.py**
  - Imports: `json`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_loop_submodules.py**
  - Imports: `asyncio`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_model_source.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_p2p.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `sqlite3`
  - Imports: `src`
- **meridian_backend/tests/test_proactive.py**
  - Imports: `asyncio`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_security_features.py**
  - Imports: `api`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_sprint2_features.py**
  - Imports: `api`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_swarm.py**
  - Imports: `asyncio`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_temporal_consensus.py**
  - Imports: `datetime`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_tools.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_vault.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `time`
- **meridian_backend/tests/test_wakeword_onnx.py**
  - Imports: `api`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib/coreBundle.js**
  - Imports: `test`
- **meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib/utilsBundle.js**
  - Imports: `ajv`
  - Imports: `ajv-formats`
- **meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types/structs.d.ts**
  - Imports: `types`
- **meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types/types.d.ts**
  - Imports: `child_process`
  - Imports: `fs`
  - Imports: `protocol`
  - Imports: `stream`
  - Imports: `structs`
  - Imports: `test`
  - Imports: `v3`
  - Imports: `zod`
- **meridian_frontend/src/AppContext.tsx**
  - Imports: `config`
  - Imports: `core`
  - Imports: `event`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/Mascot.tsx**
  - Imports: `core`
  - Imports: `event`
  - Imports: `react`
  - Imports: `window`
- **meridian_frontend/src/components/CommandPalette.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/NavRail.tsx**
  - Imports: `AppContext`
  - Imports: `Mascot`
  - Imports: `core`
  - Imports: `react`
  - Imports: `window`
- **meridian_frontend/src/components/RightDrawer.tsx**
  - Imports: `AppContext`
  - Imports: `DataBadge`
  - Imports: `ProgressArc`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/Shell.tsx**
  - Imports: `AppContext`
  - Imports: `Clipboard`
  - Imports: `Jobs`
  - Imports: `NavRail`
  - Imports: `Productivity`
  - Imports: `RightDrawer`
  - Imports: `Settings`
  - Imports: `StatusBar`
  - Imports: `SwarmDebate`
  - Imports: `Timeline`
  - Imports: `react`
- **meridian_frontend/src/components/StatusBar.tsx**
  - Imports: `AppContext`
  - Imports: `DataBadge`
  - Imports: `react`
- **meridian_frontend/src/components/ui/DataBadge.tsx**
  - Imports: `react`
- **meridian_frontend/src/components/ui/GlowCard.tsx**
  - Imports: `react`
- **meridian_frontend/src/components/ui/HoloButton.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/ui/ProgressArc.tsx**
  - Imports: `react`
- **meridian_frontend/src/components/ui/TerminalLine.tsx**
  - Imports: `react`
- **meridian_frontend/src/main.tsx**
  - Imports: `AppContext`
  - Imports: `BootSequence`
  - Imports: `Mascot`
  - Imports: `SetupWizard`
  - Imports: `Shell`
  - Imports: `client`
  - Imports: `config`
  - Imports: `index.css`
  - Imports: `react`
- **meridian_frontend/src/startup/BootSequence.tsx**
  - Imports: `config`
  - Imports: `react`
- **meridian_frontend/src/startup/SetupWizard.tsx**
  - Imports: `HoloButton`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/Clipboard.tsx**
  - Imports: `AppContext`
  - Imports: `HoloButton`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/views/GameOverlay.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/Jobs.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/views/LocalStudio.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/Productivity.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `ProgressArc`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/views/SecurityPanel.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/Settings.tsx**
  - Imports: `AppContext`
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `ProgressArc`
  - Imports: `config`
  - Imports: `core`
  - Imports: `event`
  - Imports: `lucide-react`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/views/SwarmDebate.tsx**
  - Imports: `HoloButton`
  - Imports: `TerminalLine`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/Timeline.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `config`
  - Imports: `core`
  - Imports: `dompurify`
  - Imports: `event`
  - Imports: `lucide-react`
  - Imports: `marked`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/vite.config.ts**
  - Imports: `path`
  - Imports: `plugin-react`
  - Imports: `vite`
- **plugins/get_system_platform_info.py**
  - Imports: `platform`
- **setup_db.py**
  - Imports: `os`
  - Imports: `sqlite3`
- **setup_startup.py**
  - Imports: `os`
  - Imports: `platform`
  - Imports: `subprocess`
  - Imports: `sys`
- **verify_system.py**
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `pyaudio`
  - Imports: `pymongo`
  - Imports: `socket`
  - Imports: `sounddevice`
  - Imports: `sqlite3`
  - Imports: `subprocess`
  - Imports: `sys`