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
    N6["api.py (meridian_backend)"]
    N7["database.py (meridian_backend)"]
    N8["auth.py (meridian_backend/src/core)"]
    N9["bus.py (meridian_backend/src/core)"]
    N10["clipboard.py (meridian_backend/src/core)"]
    N11["code_graph.py (meridian_backend/src/core)"]
    N12["discord_bridge.py (meridian_backend/src/core)"]
    N13["doc_generator.py (meridian_backend/src/core)"]
    N14["doc_indexer.py (meridian_backend/src/core)"]
    N15["exporter.py (meridian_backend/src/core)"]
    N16["graph_sync.py (meridian_backend/src/core)"]
    N17["history_manager.py (meridian_backend/src/core)"]
    N18["llm_provider.py (meridian_backend/src/core)"]
    N19["loop.py (meridian_backend/src/core)"]
    N20["lsp_client.py (meridian_backend/src/core)"]
    N21["mcp_client.py (meridian_backend/src/core)"]
    N22["mode.py (meridian_backend/src/core)"]
    N23["p2p.py (meridian_backend/src/core)"]
    N24["plugins.py (meridian_backend/src/core)"]
    N25["proactive.py (meridian_backend/src/core)"]
    N26["scheduler.py (meridian_backend/src/core)"]
    N27["speculative.py (meridian_backend/src/core)"]
    N28["telegram_bridge.py (meridian_backend/src/core)"]
    N29["vault.py (meridian_backend/src/core)"]
    N30["vision.py (meridian_backend/src/core)"]
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
    N59["vite.config.ts (meridian_frontend)"]
    N60["AppContext.tsx (meridian_frontend/src)"]
    N61["main.tsx (meridian_frontend/src)"]
    N62["Mascot.tsx (meridian_frontend/src)"]
    N63["NavRail.tsx (meridian_frontend/src/components)"]
    N64["RightDrawer.tsx (meridian_frontend/src/components)"]
    N65["Shell.tsx (meridian_frontend/src/components)"]
    N66["StatusBar.tsx (meridian_frontend/src/components)"]
    N67["DataBadge.tsx (meridian_frontend/src/components/ui)"]
    N68["GlowCard.tsx (meridian_frontend/src/components/ui)"]
    N69["HoloButton.tsx (meridian_frontend/src/components/ui)"]
    N70["ProgressArc.tsx (meridian_frontend/src/components/ui)"]
    N71["TerminalLine.tsx (meridian_frontend/src/components/ui)"]
    N72["BootSequence.tsx (meridian_frontend/src/startup)"]
    N73["SetupWizard.tsx (meridian_frontend/src/startup)"]
    N74["Clipboard.tsx (meridian_frontend/src/views)"]
    N75["Jobs.tsx (meridian_frontend/src/views)"]
    N76["Productivity.tsx (meridian_frontend/src/views)"]
    N77["Settings.tsx (meridian_frontend/src/views)"]
    N78["SwarmDebate.tsx (meridian_frontend/src/views)"]
    N79["Timeline.tsx (meridian_frontend/src/views)"]
    N80["get_system_platform_info.py (plugins)"]

    N3 --> N6
    N6 --> N7
    N7 --> N6
    N10 --> N7
    N12 --> N7
    N14 --> N7
    N15 --> N7
    N18 --> N7
    N19 --> N7
    N22 --> N7
    N23 --> N7
    N25 --> N7
    N25 --> N6
    N26 --> N7
    N26 --> N6
    N28 --> N7
    N30 --> N7
    N31 --> N7
    N32 --> N7
    N33 --> N7
    N35 --> N7
    N36 --> N7
    N38 --> N7
    N39 --> N7
    N41 --> N7
    N42 --> N7
    N43 --> N7
    N44 --> N7
    N45 --> N7
    N48 --> N7
    N54 --> N7
    N55 --> N7
    N61 --> N62
    N61 --> N72
    N61 --> N73
    N61 --> N65
    N61 --> N60
    N63 --> N60
    N64 --> N60
    N64 --> N70
    N64 --> N67
    N65 --> N60
    N65 --> N63
    N65 --> N66
    N65 --> N64
    N65 --> N79
    N65 --> N75
    N65 --> N74
    N65 --> N76
    N65 --> N78
    N65 --> N77
    N66 --> N60
    N66 --> N67
    N73 --> N69
    N74 --> N69
    N75 --> N69
    N75 --> N68
    N76 --> N70
    N76 --> N69
    N76 --> N68
    N77 --> N60
    N77 --> N70
    N77 --> N69
    N77 --> N68
    N78 --> N71
    N78 --> N69
    N79 --> N69
    N79 --> N68
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
  - Imports: `sys`
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
- **meridian_backend/src/core/auth.py**
  - Imports: `fastapi`
  - Imports: `hmac`
  - Imports: `os`
  - Imports: `secrets`
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
  - Imports: `database`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `typing`
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
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `os`
  - Imports: `playwright`
  - Imports: `src`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
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
  - Imports: `typing`
- **meridian_backend/src/tools/dynamic_manager.py**
  - Imports: `ast`
  - Imports: `database`
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
- **meridian_frontend/src/AppContext.tsx**
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
  - Imports: `lucide-react`
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