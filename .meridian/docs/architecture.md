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
    N9["api.py [meridian_backend]"]
    N10["database.py [meridian_backend]"]
    N11["audit_logger.py [meridian_backend/src/core]"]
    N12["auth.py [meridian_backend/src/core]"]
    N13["bus.py [meridian_backend/src/core]"]
    N14["clipboard.py [meridian_backend/src/core]"]
    N15["code_graph.py [meridian_backend/src/core]"]
    N16["config.py [meridian_backend/src/core]"]
    N17["discord_bridge.py [meridian_backend/src/core]"]
    N18["doc_generator.py [meridian_backend/src/core]"]
    N19["doc_indexer.py [meridian_backend/src/core]"]
    N20["exporter.py [meridian_backend/src/core]"]
    N21["graph_sync.py [meridian_backend/src/core]"]
    N22["history_manager.py [meridian_backend/src/core]"]
    N23["llm_provider.py [meridian_backend/src/core]"]
    N24["logging_config.py [meridian_backend/src/core]"]
    N25["loop.py [meridian_backend/src/core]"]
    N26["lsp_client.py [meridian_backend/src/core]"]
    N27["mcp_client.py [meridian_backend/src/core]"]
    N28["mode.py [meridian_backend/src/core]"]
    N29["p2p.py [meridian_backend/src/core]"]
    N30["plugins.py [meridian_backend/src/core]"]
    N31["proactive.py [meridian_backend/src/core]"]
    N32["scheduler.py [meridian_backend/src/core]"]
    N33["speculative.py [meridian_backend/src/core]"]
    N34["telegram_bridge.py [meridian_backend/src/core]"]
    N35["vault.py [meridian_backend/src/core]"]
    N36["vision.py [meridian_backend/src/core]"]
    N37["watcher.py [meridian_backend/src/core]"]
    N38["clipboard.py [meridian_backend/src/tools]"]
    N39["communication.py [meridian_backend/src/tools]"]
    N40["db_query.py [meridian_backend/src/tools]"]
    N41["desktop.py [meridian_backend/src/tools]"]
    N42["developer.py [meridian_backend/src/tools]"]
    N43["dynamic_manager.py [meridian_backend/src/tools]"]
    N44["exporter.py [meridian_backend/src/tools]"]
    N45["filesystem.py [meridian_backend/src/tools]"]
    N46["knowledge.py [meridian_backend/src/tools]"]
    N47["ollama_manager.py [meridian_backend/src/tools]"]
    N48["recording.py [meridian_backend/src/tools]"]
    N49["registry.py [meridian_backend/src/tools]"]
    N50["review.py [meridian_backend/src/tools]"]
    N51["scheduler.py [meridian_backend/src/tools]"]
    N52["security_auditor.py [meridian_backend/src/tools]"]
    N53["shell.py [meridian_backend/src/tools]"]
    N54["system.py [meridian_backend/src/tools]"]
    N55["task_scheduler.py [meridian_backend/src/tools]"]
    N56["vault.py [meridian_backend/src/tools]"]
    N57["voice.py [meridian_backend/src/tools]"]
    N58["watcher.py [meridian_backend/src/tools]"]
    N59["web.py [meridian_backend/src/tools]"]
    N60["web_browser.py [meridian_backend/src/tools]"]
    N61["stt.py [meridian_backend/src/voice]"]
    N62["tts.py [meridian_backend/src/voice]"]
    N63["wakeword.py [meridian_backend/src/voice]"]
    N64["run_tests.py [meridian_backend/tests]"]
    N65["test_config.py [meridian_backend/tests]"]
    N66["test_database.py [meridian_backend/tests]"]
    N67["test_llm_provider.py [meridian_backend/tests]"]
    N68["test_logging.py [meridian_backend/tests]"]
    N69["test_tools.py [meridian_backend/tests]"]
    N70["vite.config.ts [meridian_frontend]"]
    N71["AppContext.tsx [meridian_frontend/src]"]
    N72["main.tsx [meridian_frontend/src]"]
    N73["Mascot.tsx [meridian_frontend/src]"]
    N74["NavRail.tsx [meridian_frontend/src/components]"]
    N75["RightDrawer.tsx [meridian_frontend/src/components]"]
    N76["Shell.tsx [meridian_frontend/src/components]"]
    N77["StatusBar.tsx [meridian_frontend/src/components]"]
    N78["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N79["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N80["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N81["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N82["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N83["BootSequence.tsx [meridian_frontend/src/startup]"]
    N84["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N85["Clipboard.tsx [meridian_frontend/src/views]"]
    N86["Jobs.tsx [meridian_frontend/src/views]"]
    N87["Productivity.tsx [meridian_frontend/src/views]"]
    N88["Settings.tsx [meridian_frontend/src/views]"]
    N89["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N90["Timeline.tsx [meridian_frontend/src/views]"]
    N91["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N92["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N93["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N94["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N95["get_system_platform_info.py [plugins]"]

    N5 --> N9
    N9 --> N10
    N14 --> N10
    N17 --> N10
    N19 --> N10
    N20 --> N10
    N23 --> N10
    N25 --> N10
    N28 --> N10
    N29 --> N10
    N31 --> N10
    N31 --> N9
    N32 --> N10
    N34 --> N10
    N36 --> N10
    N37 --> N10
    N38 --> N10
    N40 --> N10
    N41 --> N10
    N43 --> N10
    N44 --> N10
    N46 --> N10
    N47 --> N10
    N48 --> N10
    N49 --> N10
    N50 --> N10
    N53 --> N10
    N59 --> N10
    N60 --> N10
    N61 --> N10
    N62 --> N10
    N63 --> N10
    N66 --> N10
    N71 --> N94
    N72 --> N73
    N72 --> N83
    N72 --> N84
    N72 --> N76
    N72 --> N71
    N74 --> N71
    N75 --> N71
    N75 --> N81
    N75 --> N78
    N76 --> N71
    N76 --> N74
    N76 --> N77
    N76 --> N75
    N76 --> N90
    N76 --> N86
    N76 --> N85
    N76 --> N87
    N76 --> N89
    N76 --> N88
    N77 --> N71
    N77 --> N78
    N84 --> N80
    N85 --> N94
    N85 --> N80
    N86 --> N94
    N86 --> N80
    N86 --> N79
    N87 --> N94
    N87 --> N81
    N87 --> N80
    N87 --> N79
    N88 --> N94
    N88 --> N71
    N88 --> N81
    N88 --> N80
    N88 --> N79
    N89 --> N82
    N89 --> N80
    N90 --> N94
    N90 --> N80
    N90 --> N79
    N93 --> N94
    N94 --> N93
```

## Detailed File Index
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