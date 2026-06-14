# Workspace Architecture & Component Map
Generated automatically by Meridian-X.

## Component Dependency Graph
```mermaid
graph TD
    N1["cleanup.py ()"]
    N2["create_shortcut.py ()"]
    N3["main.py ()"]
    N4["setup_db.py ()"]
    N5["setup_startup.py ()"]
    N6["vite.config.ts (meridain_frontend)"]
    N7["App.tsx (meridain_frontend/src)"]
    N8["main.tsx (meridain_frontend/src)"]
    N9["Mascot.tsx (meridain_frontend/src)"]
    N10["api.py (meridian_backend)"]
    N11["database.py (meridian_backend)"]
    N12["discord_bridge.py (meridian_backend)"]
    N13["bus.py (meridian_backend/src/core)"]
    N14["clipboard.py (meridian_backend/src/core)"]
    N15["code_graph.py (meridian_backend/src/core)"]
    N16["doc_generator.py (meridian_backend/src/core)"]
    N17["doc_indexer.py (meridian_backend/src/core)"]
    N18["exporter.py (meridian_backend/src/core)"]
    N19["graph_sync.py (meridian_backend/src/core)"]
    N20["history_manager.py (meridian_backend/src/core)"]
    N21["loop.py (meridian_backend/src/core)"]
    N22["lsp_client.py (meridian_backend/src/core)"]
    N23["mode.py (meridian_backend/src/core)"]
    N24["p2p.py (meridian_backend/src/core)"]
    N25["plugins.py (meridian_backend/src/core)"]
    N26["proactive.py (meridian_backend/src/core)"]
    N27["scheduler.py (meridian_backend/src/core)"]
    N28["speculative.py (meridian_backend/src/core)"]
    N29["telegram_bridge.py (meridian_backend/src/core)"]
    N30["vault.py (meridian_backend/src/core)"]
    N31["watcher.py (meridian_backend/src/core)"]
    N32["whatsapp_bridge.py (meridian_backend/src/core)"]
    N33["clipboard.py (meridian_backend/src/tools)"]
    N34["communication.py (meridian_backend/src/tools)"]
    N35["db_query.py (meridian_backend/src/tools)"]
    N36["desktop.py (meridian_backend/src/tools)"]
    N37["developer.py (meridian_backend/src/tools)"]
    N38["dynamic_manager.py (meridian_backend/src/tools)"]
    N39["exporter.py (meridian_backend/src/tools)"]
    N40["filesystem.py (meridian_backend/src/tools)"]
    N41["knowledge.py (meridian_backend/src/tools)"]
    N42["ollama_manager.py (meridian_backend/src/tools)"]
    N43["recording.py (meridian_backend/src/tools)"]
    N44["registry.py (meridian_backend/src/tools)"]
    N45["review.py (meridian_backend/src/tools)"]
    N46["scheduler.py (meridian_backend/src/tools)"]
    N47["security_auditor.py (meridian_backend/src/tools)"]
    N48["shell.py (meridian_backend/src/tools)"]
    N49["system.py (meridian_backend/src/tools)"]
    N50["task_scheduler.py (meridian_backend/src/tools)"]
    N51["vault.py (meridian_backend/src/tools)"]
    N52["voice.py (meridian_backend/src/tools)"]
    N53["watcher.py (meridian_backend/src/tools)"]
    N54["web.py (meridian_backend/src/tools)"]
    N55["web_browser.py (meridian_backend/src/tools)"]
    N56["stt.py (meridian_backend/src/voice)"]
    N57["tts.py (meridian_backend/src/voice)"]
    N58["wakeword.py (meridian_backend/src/voice)"]
    N59["get_system_platform_info.py (plugins)"]

    N3 --> N10
    N7 --> N9
    N10 --> N11
    N11 --> N10
    N14 --> N11
    N17 --> N11
    N18 --> N11
    N21 --> N11
    N23 --> N11
    N24 --> N11
    N26 --> N11
    N26 --> N10
    N27 --> N11
    N27 --> N10
    N29 --> N10
    N29 --> N11
    N31 --> N11
    N32 --> N10
    N32 --> N11
    N33 --> N11
    N35 --> N11
    N36 --> N11
    N39 --> N11
    N41 --> N11
    N42 --> N11
    N43 --> N11
    N44 --> N11
    N45 --> N11
    N48 --> N11
    N54 --> N11
    N55 --> N11
```

## Detailed File Index
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
- **meridain_frontend/src/App.tsx**
  - Imports: `Mascot`
  - Imports: `core`
  - Imports: `event`
  - Imports: `marked`
  - Imports: `react`
  - Imports: `types`
  - Imports: `webviewWindow`
  - Imports: `window`
- **meridain_frontend/src/Mascot.tsx**
  - Imports: `core`
  - Imports: `event`
  - Imports: `react`
  - Imports: `webviewWindow`
  - Imports: `window`
- **meridain_frontend/src/main.tsx**
  - Imports: `Appx`
  - Imports: `Mascotx`
  - Imports: `client`
  - Imports: `index.css`
  - Imports: `react`
  - Imports: `window`
- **meridain_frontend/vite.config.ts**
  - Imports: `path`
  - Imports: `plugin-react`
  - Imports: `vite`
- **meridian_backend/api.py**
  - Imports: `ast`
  - Imports: `base64`
  - Imports: `contextlib`
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `pydantic`
  - Imports: `random`
  - Imports: `re`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `uvicorn`
- **meridian_backend/database.py**
  - Imports: `api`
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
- **meridian_backend/discord_bridge.py**
  - Imports: `discord`
  - Imports: `os`
  - Imports: `requests`
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
  - Imports: `time`
  - Imports: `typing`
  - Imports: `uuid`
- **meridian_backend/src/core/lsp_client.py**
  - Imports: `asyncio`
  - Imports: `json`
  - Imports: `os`
  - Imports: `sys`
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
  - Imports: `database`
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
  - Imports: `api`
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
  - Imports: `api`
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
  - Imports: `typing`
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
- **meridian_backend/src/core/whatsapp_bridge.py**
  - Imports: `api`
  - Imports: `database`
  - Imports: `os`
  - Imports: `playwright`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
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
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/db_query.py**
  - Imports: `database`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `psycopg2`
  - Imports: `pymysql`
  - Imports: `sqlite3`
  - Imports: `typing`
- **meridian_backend/src/tools/desktop.py**
  - Imports: `PIL`
  - Imports: `database`
  - Imports: `mss`
  - Imports: `os`
  - Imports: `pyautogui`
  - Imports: `typing`
- **meridian_backend/src/tools/developer.py**
  - Imports: `asyncio`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `tempfile`
  - Imports: `time`
- **meridian_backend/src/tools/dynamic_manager.py**
  - Imports: `ast`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `re`
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
  - Imports: `os`
  - Imports: `queue`
  - Imports: `random`
  - Imports: `re`
  - Imports: `sounddevice`
  - Imports: `soundfile`
  - Imports: `supertonic`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `typing`
- **meridian_backend/src/voice/wakeword.py**
  - Imports: `numpy`
  - Imports: `openwakeword`
  - Imports: `os`
  - Imports: `sounddevice`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
- **plugins/get_system_platform_info.py**
  - Imports: `platform`
- **setup_db.py**
  - Imports: `os`
  - Imports: `sqlite3`
- **setup_startup.py**
  - Imports: `os`
  - Imports: `subprocess`
  - Imports: `sys`