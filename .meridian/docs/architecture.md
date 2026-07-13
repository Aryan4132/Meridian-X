# Workspace Architecture & Component Map
Generated automatically by Meridian-X.

## Component Dependency Graph
```mermaid
graph TD
    N1["build_standalone.py []"]
    N2["cleanup.py []"]
    N3["create_shortcut.py []"]
    N4["main.py []"]
    N5["setup_db.py []"]
    N6["setup_startup.py []"]
    N7["verify_system.py []"]
    N8["api.py [meridian_backend]"]
    N9["database.py [meridian_backend]"]
    N10["audit_logger.py [meridian_backend/src/core]"]
    N11["auth.py [meridian_backend/src/core]"]
    N12["bus.py [meridian_backend/src/core]"]
    N13["clipboard.py [meridian_backend/src/core]"]
    N14["code_graph.py [meridian_backend/src/core]"]
    N15["config.py [meridian_backend/src/core]"]
    N16["discord_bridge.py [meridian_backend/src/core]"]
    N17["doc_generator.py [meridian_backend/src/core]"]
    N18["doc_indexer.py [meridian_backend/src/core]"]
    N19["exporter.py [meridian_backend/src/core]"]
    N20["graph_sync.py [meridian_backend/src/core]"]
    N21["history_manager.py [meridian_backend/src/core]"]
    N22["llm_provider.py [meridian_backend/src/core]"]
    N23["logging_config.py [meridian_backend/src/core]"]
    N24["loop.py [meridian_backend/src/core]"]
    N25["lsp_client.py [meridian_backend/src/core]"]
    N26["mcp_client.py [meridian_backend/src/core]"]
    N27["mode.py [meridian_backend/src/core]"]
    N28["p2p.py [meridian_backend/src/core]"]
    N29["plugins.py [meridian_backend/src/core]"]
    N30["proactive.py [meridian_backend/src/core]"]
    N31["scheduler.py [meridian_backend/src/core]"]
    N32["speculative.py [meridian_backend/src/core]"]
    N33["telegram_bridge.py [meridian_backend/src/core]"]
    N34["vault.py [meridian_backend/src/core]"]
    N35["vision.py [meridian_backend/src/core]"]
    N36["watcher.py [meridian_backend/src/core]"]
    N37["clipboard.py [meridian_backend/src/tools]"]
    N38["communication.py [meridian_backend/src/tools]"]
    N39["db_query.py [meridian_backend/src/tools]"]
    N40["desktop.py [meridian_backend/src/tools]"]
    N41["developer.py [meridian_backend/src/tools]"]
    N42["dynamic_manager.py [meridian_backend/src/tools]"]
    N43["exporter.py [meridian_backend/src/tools]"]
    N44["filesystem.py [meridian_backend/src/tools]"]
    N45["knowledge.py [meridian_backend/src/tools]"]
    N46["ollama_manager.py [meridian_backend/src/tools]"]
    N47["recording.py [meridian_backend/src/tools]"]
    N48["registry.py [meridian_backend/src/tools]"]
    N49["review.py [meridian_backend/src/tools]"]
    N50["scheduler.py [meridian_backend/src/tools]"]
    N51["security_auditor.py [meridian_backend/src/tools]"]
    N52["shell.py [meridian_backend/src/tools]"]
    N53["system.py [meridian_backend/src/tools]"]
    N54["task_scheduler.py [meridian_backend/src/tools]"]
    N55["vault.py [meridian_backend/src/tools]"]
    N56["voice.py [meridian_backend/src/tools]"]
    N57["watcher.py [meridian_backend/src/tools]"]
    N58["web.py [meridian_backend/src/tools]"]
    N59["web_browser.py [meridian_backend/src/tools]"]
    N60["stt.py [meridian_backend/src/voice]"]
    N61["tts.py [meridian_backend/src/voice]"]
    N62["wakeword.py [meridian_backend/src/voice]"]
    N63["run_tests.py [meridian_backend/tests]"]
    N64["test_config.py [meridian_backend/tests]"]
    N65["test_database.py [meridian_backend/tests]"]
    N66["test_llm_provider.py [meridian_backend/tests]"]
    N67["test_logging.py [meridian_backend/tests]"]
    N68["test_tools.py [meridian_backend/tests]"]
    N69["vite.config.ts [meridian_frontend]"]
    N70["AppContext.tsx [meridian_frontend/src]"]
    N71["main.tsx [meridian_frontend/src]"]
    N72["Mascot.tsx [meridian_frontend/src]"]
    N73["NavRail.tsx [meridian_frontend/src/components]"]
    N74["RightDrawer.tsx [meridian_frontend/src/components]"]
    N75["Shell.tsx [meridian_frontend/src/components]"]
    N76["StatusBar.tsx [meridian_frontend/src/components]"]
    N77["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N78["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N79["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N80["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N81["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N82["BootSequence.tsx [meridian_frontend/src/startup]"]
    N83["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N84["Clipboard.tsx [meridian_frontend/src/views]"]
    N85["Jobs.tsx [meridian_frontend/src/views]"]
    N86["Productivity.tsx [meridian_frontend/src/views]"]
    N87["Settings.tsx [meridian_frontend/src/views]"]
    N88["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N89["Timeline.tsx [meridian_frontend/src/views]"]
    N90["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N91["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N92["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N93["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N94["get_system_platform_info.py [plugins]"]

    N4 --> N8
    N8 --> N9
    N13 --> N9
    N16 --> N9
    N18 --> N9
    N19 --> N9
    N22 --> N9
    N24 --> N9
    N27 --> N9
    N28 --> N9
    N30 --> N9
    N30 --> N8
    N31 --> N9
    N33 --> N9
    N35 --> N9
    N36 --> N9
    N37 --> N9
    N39 --> N9
    N40 --> N9
    N42 --> N9
    N43 --> N9
    N45 --> N9
    N46 --> N9
    N47 --> N9
    N48 --> N9
    N49 --> N9
    N52 --> N9
    N58 --> N9
    N59 --> N9
    N60 --> N9
    N61 --> N9
    N62 --> N9
    N65 --> N9
    N70 --> N93
    N71 --> N72
    N71 --> N82
    N71 --> N83
    N71 --> N75
    N71 --> N70
    N73 --> N70
    N74 --> N70
    N74 --> N80
    N74 --> N77
    N75 --> N70
    N75 --> N73
    N75 --> N76
    N75 --> N74
    N75 --> N89
    N75 --> N85
    N75 --> N84
    N75 --> N86
    N75 --> N88
    N75 --> N87
    N76 --> N70
    N76 --> N77
    N83 --> N79
    N84 --> N93
    N84 --> N79
    N85 --> N93
    N85 --> N79
    N85 --> N78
    N86 --> N93
    N86 --> N80
    N86 --> N79
    N86 --> N78
    N87 --> N93
    N87 --> N70
    N87 --> N80
    N87 --> N79
    N87 --> N78
    N88 --> N81
    N88 --> N79
    N89 --> N93
    N89 --> N79
    N89 --> N78
    N92 --> N93
    N93 --> N92
```

## Detailed File Index
- **build_standalone.py**
  - Imports: `os`
  - Imports: `platform`
  - Imports: `shutil`
  - Imports: `subprocess`
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
  - Imports: `ast`
  - Imports: `base64`
  - Imports: `contextlib`
  - Imports: `database`
  - Imports: `fastapi`
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
  - Imports: `shutil`
  - Imports: `signal`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `uuid`
  - Imports: `uvicorn`
- **meridian_backend/database.py**
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
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `src`
  - Imports: `time`
- **meridian_backend/src/core/auth.py**
  - Imports: `fastapi`
  - Imports: `hmac`
  - Imports: `os`
  - Imports: `secrets`
  - Imports: `src`
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
  - Imports: `os`
  - Imports: `src`
  - Imports: `threading`
- **meridian_backend/src/core/doc_generator.py**
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
- **meridian_backend/src/core/doc_indexer.py**
  - Imports: `database`
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
  - Imports: `os`
  - Imports: `typing`
- **meridian_backend/src/core/logging_config.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/src/core/loop.py**
  - Imports: `anthropic`
  - Imports: `ast`
  - Imports: `asyncio`
  - Imports: `database`
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
  - Imports: `json`
  - Imports: `os`
  - Imports: `socket`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/plugins.py**
  - Imports: `importlib`
  - Imports: `inspect`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `typing`
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
- **meridian_backend/src/core/scheduler.py**
  - Imports: `apscheduler`
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `src`
  - Imports: `time`
- **meridian_backend/src/core/speculative.py**
  - Imports: `asyncio`
  - Imports: `json`
  - Imports: `os`
  - Imports: `re`
  - Imports: `socket`
  - Imports: `typing`
  - Imports: `urllib`
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
- **meridian_backend/src/core/vault.py**
  - Imports: `base64`
  - Imports: `cryptography`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
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
  - Imports: `ast`
  - Imports: `database`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `watchdog`
- **meridian_backend/src/tools/clipboard.py**
  - Imports: `bson`
  - Imports: `database`
  - Imports: `pyperclip`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/communication.py**
  - Imports: `email`
  - Imports: `imaplib`
  - Imports: `os`
  - Imports: `plyer`
  - Imports: `pyautogui`
  - Imports: `smtplib`
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
- **meridian_backend/src/tools/dynamic_manager.py**
  - Imports: `ast`
  - Imports: `database`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `time`
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
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/system.py**
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `pygetwindow`
  - Imports: `pyperclip`
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
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `re`
  - Imports: `selectolax`
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
  - Imports: `os`
  - Imports: `queue`
  - Imports: `random`
  - Imports: `re`
  - Imports: `sounddevice`
  - Imports: `soundfile`
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
- **meridian_backend/tests/test_config.py**
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_database.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `sys`
  - Imports: `unittest`
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
- **meridian_backend/tests/test_tools.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
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
  - Imports: `core`
  - Imports: `event`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/Mascot.tsx**
  - Imports: `core`
  - Imports: `event`
  - Imports: `react`
  - Imports: `window`
- **meridian_frontend/src/components/NavRail.tsx**
  - Imports: `AppContext`
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
  - Imports: `index.css`
  - Imports: `react`
- **meridian_frontend/src/startup/BootSequence.tsx**
  - Imports: `react`
- **meridian_frontend/src/startup/SetupWizard.tsx**
  - Imports: `HoloButton`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/Clipboard.tsx**
  - Imports: `HoloButton`
  - Imports: `lucide-react`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/views/Jobs.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `lucide-react`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/views/Productivity.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `ProgressArc`
  - Imports: `lucide-react`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/views/Settings.tsx**
  - Imports: `AppContext`
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `ProgressArc`
  - Imports: `event`
  - Imports: `lucide-react`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/views/SwarmDebate.tsx**
  - Imports: `HoloButton`
  - Imports: `TerminalLine`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/Timeline.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
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