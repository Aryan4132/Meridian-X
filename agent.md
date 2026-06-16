# Meridian-X: Autonomous Offline Desktop Agent (GUI Only)

> **Meridian-X** is a fully offline, privacy-absolute autonomous desktop agent — one unified brain, infinite capability. It runs a continuous **Reasoning → Action → Observation** loop powered by local Ollama models and switches cognitive modes internally to become a software engineer, system analyst, code reviewer, or shell operator on demand. Every tool, every memory system, and every UI panel is orchestrated by a single agent that never sends a byte to the cloud.

**Stack:** `Qwen2.5-Coder:7B` via `Ollama` · `nomic-embed-text` (ONNX) · `minicpm-v:latest` (Vision) · `faster-whisper` · `Supertonic` · Python 3.11+ asyncio · LanceDB · MongoDB · **Tauri Desktop Shell** · `cryptography` · APScheduler

## 1.5 Configuration Overrides (`.env`)

Meridian-X supports user overrides via `.env` to customize which local Ollama and speech models are used at runtime.

| Variable | Example / Default | Notes |
|---|---|---|
| `MERIDIAN_MODEL` | `gemma4:31b-cloud` | Primary reasoning/coding brain override (defaults to `qwen2.5-coder:7b-instruct-q4_K_M`). |
| `MERIDIAN_VISION_MODEL` | `gemma4:31b-cloud` | Alternate vision/multimodal brain override (defaults to `minicpm-v:latest`). |
| `MERIDIAN_STT_MODEL` | `small` | Speech-to-text model selection for offline voice input. Options include `tiny`, `tiny.en`, `base`, `base.en`, `small`, `small.en`, `medium`, `medium.en`, `large-v3`. |
| `OLLAMA_HOST` | `http://localhost:11434` | Optional Ollama server endpoint override. If unset, Meridian-X probes local standard ports and environment settings at startup to discover the active Ollama server. |
| `MONGODB_URI` | `mongodb://localhost:27017/meridian_kg` | Local knowledge graph database connection string override. |

- `Supertonic` remains the default offline TTS model. Download it from https://github.com/supertone-inc/supertonic/
- `silero-vad` is used as the local voice activity detection (VAD) engine in the voice pipeline.

---

## 1.6 Runtime Modes & Launch Paths

Meridian-X is designed as a **desktop application** with a modern Tauri shell for native performance and seamless local integration.

| Mode | Command | Purpose |
|---|---|---|
| **Backend Only** | `python daemon.py` | Start the backend services only; dashboard remains closed until opened. |
| **Open Dashboard** | `cargo tauri dev` | Launch the native Tauri dashboard when the backend is already running. |
| Direct Goal | `python main.py --goal "Your goal here"` | Execute a single autonomous task without launching the desktop shell |
| Local API | `uvicorn api:app --host 127.0.0.1 --port 4132` | Programmatic access to Meridian-X for external apps |
| Windows launcher | `start_meridian.bat` | Quick menu for dashboard/API/daemon/autostart actions |

**Activation Hotkeys:**
- `Alt + M` toggles the Tauri dashboard when the backend is running: press once to open it, press again to hide it. If the backend is not running, start `python daemon.py` first.
- `Alt + Shift + M` toggles island mode: press once to open it, press again to hide it.

Additional maintenance utilities:
- `setup_startup.py` manages Windows startup autostart entries for launching both the backend and frontend automatically (and silently) on system boot.
- `create_shortcut.py` creates a Desktop shortcut for launching the Tauri dashboard when the backend is active.
- `cleanup.py` clears persistent storage, secrets, scheduler jobs, and sample databases.
- `setup_db.py` generates `sample_shop.db` for local SQL query testing.

---

## 1. Core Identity & Agent Profile

| Property | Value | Rationale |
|---|---|---|
| **Agent Type** | Autonomous ReAct Loop Agent | Multi-turn planning, not single-shot Q&A |
| **Interface** | **Native desktop shell** | Tauri-powered local app with native windowing |
| **Inference Backend** | `Ollama` (local, offline) | No internet required; GPU or CPU execution |
| **Primary Brain** | `qwen2.5-coder:7b-instruct-q4_K_M` | Best offline coding+reasoning model at 4.7 GB |
| **Fallback Brain** | `qwen2.5-coder:1.5b-instruct-q8_0` | 1.6 GB; instant cold-start when VRAM is tight |
| **Vision Brain** | `moondream:1.8b` (Ollama) | On-demand screen analysis and image understanding |
| **Embedding Model** | `nomic-embed-text` (ONNX, INT8) | ~500 MB; best with GPU/acceleration for local RAG |
| **Voice STT** | `faster-whisper tiny.en` (CTranslate2 INT8) | ~300ms for 5s audio, fully offline |
| **Voice TTS** | `Supertonic` (ONNX) | Professional-quality speech synthesis at 100ms TTFA |
| **Vector Database** | `LanceDB` (embedded, serverless) | Sub-5ms ANN queries; zero daemon process |
| **Knowledge Graph** | `MongoDB` (local, `mongod`) | Entity-relationship store for persistent world knowledge |
| **Tool Call Format** | XML tags (`<call:tool>`, `<thought>`, `<finish>`) | Highly reliable parsing on quantized 7B models |
| **Max Agent Turns** | Unlimited | Agent loops until `<finish>` is reached |
| **Safety Net** | 10-minute global timeout | Prevents runaway loops from infinite execution |
| **Cognitive Modes** | AUTO / ENGINEER / ANALYST / REVIEWER / OPERATOR | Single agent switches reasoning style per task |
| **Plugin System** | `plugins/` auto-discovery | Drop `.py` files to add new tools instantly |
| **API Mode** | `FastAPI` on `127.0.0.1:4132` | Other apps can call Meridian-X programmatically |
| **Secrets Vault** | AES-256 encrypted local store | Zero plaintext credentials anywhere |
| **Clipboard Memory** | MongoDB + semantic search | Searchable history of everything you've ever copied |
| **NL Shell** | Natural Language → shell command | Type commands in plain English |
| **Desktop Shell** | `Tauri` desktop shell | High-end native application experience with embedded backend |
| **Philosophy** | Offline-first · Privacy-absolute · Self-correcting | Every byte stays on your machine |

---

## 2. The Autonomous ReAct Loop — How Meridian-X Thinks

Unlike a simple chatbot, Meridian-X **does not answer in a single pass**. It plans, acts, observes the results, corrects mistakes, and loops until the goal is resolved — exactly like OpenClaw or Hermes.

```
  ╔══════════════════════════════════════════════════════════════╗
  ║                   USER GOAL / TASK INPUT                     ║
  ╚════════════════════════════╤═════════════════════════════════╝
                               │
                               ▼
               ┌───────────────────────────────┐
               │   SEMANTIC CACHE LOOKUP       │◄─── LanceDB cosine scan
               │   similarity > 0.96?          │     (< 5ms, no inference)
               └──────────┬────────────────────┘
              HIT ◄────────┘           │ MISS
               │                       ▼
               │         ┌─────────────────────────┐
               │         │  RAG CONTEXT RETRIEVAL  │◄─── LanceDB top-2 ANN
               │         │  knowledge_base search  │     nomic-embed-text embed
               │         └────────────┬────────────┘
               │                      │
               │                      ▼
               │    ╔═══════════════════════════════════╗
               │    ║       AGENT TURN (ReAct Loop)     ║
               │    ╠═══════════════════════════════════╣
               │    ║                                   ║
               │    ║  1. THOUGHT                       ║
               │    ║     <thought>                     ║
               │    ║       Analyze state, plan         ║
               │    ║       next logical action         ║
               │    ║     </thought>                    ║
               │    ║                                   ║
               │    ║  2. ACTION (0 or more calls)      ║
               │    ║     <call:tool_name>              ║
               │    ║       {"arg": "value"}            ║
               │    ║     </call:tool_name>             ║
               │    ║                                   ║
               │    ║  3. OBSERVATION (injected)        ║
               │    ║     <observation:tool_name>       ║
               │    ║       raw execution result        ║
               │    ║     </observation:tool_name>      ║
               │    ║                                   ║
               │    ║  4. SELF-CORRECTION HOOK          ║
               │    ║     Error in observation?         ║
               │    ║     YES → debug + re-call         ║
               │    ║     NO  → next subgoal            ║
               │    ║                                   ║
               │    ║  5. FINISH or LOOP?               ║
               │    ║     Goal reached?                 ║
               │    ║     YES → <finish>response</finish>║
               │    ║     NO  → loop back to THOUGHT   ║
               │    ╚═══════════════════════════════════╝
               │                      │
               │                      │ <finish> reached
               │                      ▼
               └──────────────►  FINAL RESPONSE
                                       │
                              ┌────────▼────────┐
                              │  MEMORY WRITE   │◄─── asyncio.create_task()
                              │  LanceDB store  │     non-blocking background
                              │  Cache update   │     never delays user
                              └─────────────────┘
```

---

## 3. XML Tool-Call Protocol

Meridian-X uses a **strict XML tag protocol** for its tool calls. This is a deliberate design choice — quantized 7B models on Ollama are significantly more reliable parsing flat XML tags than deeply nested JSON schemas. The runner parses tags using regex, injecting observations back into the conversation context for the next turn.

### 3.1 Tag Reference

| Tag | Direction | Purpose |
|---|---|---|
| `<thought>...</thought>` | Model → Runner | Internal reasoning; planning, debugging, strategy |
| `<call:TOOL_NAME>JSON_ARGS</call:TOOL_NAME>` | Model → Runner | Request tool execution |
| `<observation:TOOL_NAME>RESULT</observation:TOOL_NAME>` | Runner → Model | Raw output of the executed tool call |
| `<finish>FINAL_RESPONSE</finish>` | Model → User | Final answer; terminates the loop |

### 3.2 Multi-Tool Parallel Dispatch

When the model issues multiple `<call:...>` tags in a single turn, the runner dispatches them in **parallel via `asyncio.gather()`**. The combined observations are injected back in a single system turn before the next reasoning pass.

```
Turn N — Model Output:
  <thought>I need the file contents and git status simultaneously.</thought>
  <call:read_file>{"path": "src/main.py"}</call:read_file>
  <call:git_status>{"repo_path": "."}</call:git_status>

Turn N — Runner:
  [asyncio.gather(read_file(...), git_status(...))]  ← parallel execution
  Injects:
  <observation:read_file>...file contents...</observation:read_file>
  <observation:git_status>M  src/main.py</observation:git_status>

Turn N+1 — Model continues with full context...
```

### 3.3 Self-Correction Example

```
Turn 1 — Model:
  <thought>I'll run this Python script to process the CSV data.</thought>
  <call:run_python>{"code": "import pandas as pd\ndf = pd.read_csv('data.csv')\nprint(df.head())"}</call:run_python>

Turn 1 — Observation (error injected):
  <observation:run_python>ModuleNotFoundError: No module named 'pandas'</observation:run_python>

Turn 2 — Model self-corrects without asking the user:
  <thought>pandas is not installed. I'll use the built-in csv module instead.</thought>
  <call:run_python>{"code": "import csv\nwith open('data.csv') as f:\n    reader = csv.DictReader(f)\n    for i, row in enumerate(reader):\n        print(row)\n        if i >= 4: break"}</call:run_python>
```

---

## 4. Agent Capabilities & Tool Registry

### 4.1 Filesystem & I/O
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `read_file` | `path` | 0 | Async aiofiles; zero thread-block |
| `write_file` | `path, content` | 1 | Async write; overwrites atomically |
| `list_directory` | `path` | 0 | anyio-threaded scandir |
| `search_files` | `query, dir` | 0 | ripgrep binary; 1M files in <500ms |
| `move_file` | `src, dst` | 1 | shutil.move in thread pool |
| `delete_file` | `path` | 3 | Requires y/n confirmation |

### 4.2 Web & Network (Offline-First)
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `search_web` | `query` | 0 | Tavily primary search; DuckDuckGo fallback when Tavily is unavailable |
| `fetch_page` | `url` | 0 | httpx HTTP/2 async; connection reuse |
| `parse_page` | `html` | 0 | selectolax C engine; 10x vs BS4 |
| `browse_url` | `url` | 0 | Playwright headless; only when JS needed |
| `download_file` | `url, dest` | 1 | Streaming chunk-to-disk via httpx |

### 4.3 Desktop Automation & Vision (Full GUI Control)
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `screenshot` | `output` | 0 | mss DXGI capture; <15ms |
| `screenshot_region` | `x, y, w, h, output` | 0 | Crop capture for focused analysis |
| `ocr_screen` | `image_path` | 0 | rapidocr-onnxruntime offline OCR |
| `vision_analyze` | `image_path, prompt` | 0 | moondream:1.8b describes/queries image via Ollama |
| `find_on_screen` | `image_path, target_desc` | 0 | Screenshot + OCR + vision to locate UI element |
| `gui_click` | `x, y` | 2 | pyautogui native Win32 click |
| `gui_right_click` | `x, y` | 2 | Context menu trigger |
| `gui_double_click` | `x, y` | 2 | Open files, activate items |
| `gui_drag` | `x1, y1, x2, y2` | 2 | Drag-and-drop automation |
| `gui_type` | `text` | 1 | pyautogui keyboard injection |
| `gui_hotkey` | `*keys` | 1 | pyautogui.hotkey native SendInput |
| `gui_scroll` | `x, y, clicks` | 1 | Mouse wheel scroll |
| `get_mouse_position` | — | 0 | Returns current `(x, y)` cursor coords |

### 4.4 Window Management & App Control
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `list_windows` | — | 0 | pygetwindow; returns all open window titles + positions |
| `focus_window` | `title` | 1 | Bring window to foreground (Win32 SetForegroundWindow) |
| `resize_window` | `title, w, h` | 1 | Resize window to exact pixel dimensions |
| `move_window` | `title, x, y` | 1 | Move window to screen coordinate |
| `minimize_window` | `title` | 1 | Minimize to taskbar |
| `maximize_window` | `title` | 1 | Maximize to full screen |
| `close_window` | `title` | 2 | Send WM_CLOSE; graceful close |
| `open_app` | `name_or_path` | 1 | Launch any app by name or full path |
| `open_file` | `path` | 1 | `os.startfile` — opens with default handler |
| `open_url_in_browser` | `url` | 1 | Opens URL in default browser (offline) |
| `close_app` | `name` | 2 | psutil process tree kill by name |
| `get_active_window` | — | 0 | Returns title of currently focused window |
| `wait_for_window` | `title, timeout` | 0 | Polls until window appears; useful after app launch |

### 4.5 Deep System Analysis & Monitoring
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `get_system_info` | — | 0 | CPU %, RAM %, disk usage; TTL-cached 5s |
| `get_hardware_info` | — | 0 | CPU model, GPU, RAM modules, motherboard via wmic/dmidecode |
| `get_disk_info` | — | 0 | All partitions: total, used, free, filesystem type |
| `get_battery_status` | — | 0 | psutil.sensors_battery(); charge %, plugged state |
| `get_temperature` | — | 0 | psutil.sensors_temperatures() — CPU/GPU thermals |
| `list_processes` | — | 0 | pid, name, cpu%, mem%, status for all processes |
| `get_process_detail` | `pid_or_name` | 0 | Full detail: cmdline, open files, threads, net connections |
| `kill_process` | `pid` | 3 | SIGKILL; explicit confirmation required |
| `list_startup_items` | — | 0 | HKCU/HKLM Run keys + Startup folder (Windows) |
| `list_installed_apps` | — | 0 | Registry uninstall keys; returns name, version, install date |
| `list_services` | — | 0 | sc query / psutil.win_service_iter(); name + status |
| `start_service` | `name` | 3 | sc start; requires confirmation |
| `stop_service` | `name` | 3 | sc stop; requires confirmation |
| `get_network_connections` | — | 0 | All active sockets: PID, local/remote addr, state |
| `get_wifi_networks` | — | 0 | netsh wlan show networks — nearby SSIDs |
| `ping_host` | `host` | 0 | ICMP reachability check |
| `clipboard_get` | — | 0 | pyperclip read |
| `clipboard_set` | `text` | 1 | pyperclip write |
| `media_control` | `action` | 1 | pycaw Windows Core Audio COM interface |
| `run_command` | `cmd, cwd` | 2 | asyncio subprocess shell; piped stdout+stderr |
| `get_env` | `key` | 0 | os.environ direct lookup |
| `set_env` | `key, value` | 2 | os.environ + optional .env write |

### 4.5 Memory & RAG
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `ingest_file` | `path` | 1 | PDF/MD/TXT/PY → LanceDB chunks |
| `search_knowledge` | `query` | 0 | ANN search on knowledge_base |
| `save_note` | `text` | 1 | Appends to episodic memory |

### 4.6 Code & Developer Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `run_python` | `code, timeout` | 2 | Isolated subprocess sandbox |
| `open_editor` | `file` | 1 | VS Code fire-and-forget spawn |
| `git_status` | `repo_path` | 0 | git status --short; direct CLI |
| `git_commit` | `message, repo_path` | 2 | git commit -am; direct CLI |
| `git_diff` | `repo_path` | 0 | git diff HEAD; piped to model |
| `search_codebase` | `query, path` | 0 | ripgrep; 500K LOC in <50ms |

### 4.7 Communication
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `send_notification` | `title, message` | 1 | win10toast / plyer toast |
| `send_email` | `to, subject, body` | 2 | aiosmtplib async SMTP |
| `read_emails` | `n` | 0 | aioimaplib async IMAP FETCH |
| `send_whatsapp_message` | `contact, message` | 2 | GUI automation (pyautogui) to send a WhatsApp message to contact by name |

### 4.8 Voice
| Component | Model | Latency |
|---|---|---|
| STT | `faster-whisper tiny.en` INT8 | ~300ms / 5s audio |
| TTS | `Supertonic` ONNX | ~100ms to first audio chunk |
| VAD | `silero-vad` ONNX | <10ms voice detection |

---



## 5. Deep System Analysis — What the Agent Can Do

Beyond answering questions, Meridian-X can **fully analyze, operate, and maintain your Windows system** autonomously. Below are the core analysis workflows with real example agent traces.

### 5.1 System Health Audit
Ask: *"Check my system health and tell me what's slowing it down."*

```
<thought>
  I'll gather CPU, RAM, disk, temperature, and process data in parallel
  to build a complete health picture before diagnosing.
</thought>
<call:get_system_info>{}</call:get_system_info>
<call:get_hardware_info>{}</call:get_hardware_info>
<call:get_disk_info>{}</call:get_disk_info>
<call:get_temperature>{}</call:get_temperature>
<call:list_processes>{}</call:list_processes>

<observation:get_system_info>CPU: 94% | RAM: 13.1/16 GB (82%) | Disk C: 87% full</observation:get_system_info>
<observation:list_processes>PID 4821 'electron.exe' CPU 38% | PID 1204 'msedge.exe' CPU 22%</observation:list_processes>
<observation:get_temperature>CPU Package: 91°C (CRITICAL)</observation:get_temperature>

<thought>
  CPU is throttling due to thermal stress. electron.exe and msedge are
  consuming 60% CPU. Disk is nearly full. I'll report all three issues.
</thought>
<finish>
  ⚠️ 3 Critical Issues Found:
  1. **CPU at 91°C** — thermal throttling active. Check fan/thermal paste.
  2. **electron.exe (38%) + msedge.exe (22%)** — killing 60% CPU. Close these if not needed.
  3. **Disk C: 87% full** — recommend running disk cleanup or moving large files.
</finish>
```

### 5.2 App & Process Control
Ask: *"Open Notepad, type 'Hello World', and save it as hello.txt on the Desktop."*

```
<thought>Launch Notepad, wait for it, type text, then save with Ctrl+S.</thought>
<call:open_app>{"name_or_path": "notepad.exe"}</call:open_app>

<call:wait_for_window>{"title": "Notepad", "timeout": 5}</call:wait_for_window>
<call:focus_window>{"title": "Notepad"}</call:focus_window>
<call:gui_type>{"text": "Hello World"}</call:gui_type>
<call:gui_hotkey>{"keys": ["ctrl", "shift", "s"]}</call:gui_hotkey>

<call:wait_for_window>{"title": "Save As", "timeout": 3}</call:wait_for_window>
<call:gui_type>{"text": "C:\\Users\\aryan\\Desktop\\hello.txt"}</call:gui_type>
<call:gui_hotkey>{"keys": ["enter"]}</call:gui_hotkey>
<finish>Done. Saved hello.txt to your Desktop via Notepad.</finish>
```

### 5.3 File System Deep Analysis
Ask: *"Find the 10 largest files on my C drive and list them."*

```
<thought>Run a Python script to walk the drive and sort by size. Faster than a tool chain.</thought>
<call:run_python>{
  "code": "import os\nfiles=[]\nfor r,d,fs in os.walk('C:\\\\'):\n  for f in fs:\n    try:\n      p=os.path.join(r,f); files.append((os.path.getsize(p),p))\n    except: pass\nfiles.sort(reverse=True)\nfor s,p in files[:10]: print(f'{s/1e9:.2f} GB  {p}')",
  "timeout": 30
}</call:run_python>

<observation:run_python>
  12.40 GB  C:\hiberfil.sys
  8.12 GB   C:\pagefile.sys
  4.71 GB   C:\Users\aryan\Downloads\ubuntu.iso
  ...
</observation:run_python>
<finish>
  Top 10 largest files on C:\\
  1. 12.4 GB — hiberfil.sys (hibernation file — safe to disable)
  2. 8.1 GB  — pagefile.sys (virtual memory — do not delete)
  3. 4.7 GB  — ubuntu.iso in Downloads (safe to delete if no longer needed)
  ...
</finish>
```

### 5.4 Network & Security Analysis
Ask: *"Show me all active network connections and flag any suspicious ones."*

```
<thought>Pull all active sockets and installed apps to cross-reference unknown PIDs.</thought>
<call:get_network_connections>{}</call:get_network_connections>
<call:list_installed_apps>{}</call:list_installed_apps>

<observation:get_network_connections>
  PID 3281 python.exe → 52.86.24.1:443 ESTABLISHED
  PID 5902 unknown.exe → 185.220.101.6:9001 ESTABLISHED
  ...
</observation:get_network_connections>

<thought>
  unknown.exe connecting to 185.220.101.6:9001 is suspicious — port 9001 is
  commonly used by Tor relays. Not in installed apps list. Flag for user.
</thought>
<finish>
  🚨 Suspicious Connection Detected:
  - PID 5902 `unknown.exe` → 185.220.101.6:9001 (possible Tor relay)
  - This process is not in your installed applications list.
  - Recommended action: kill PID 5902 and investigate the executable path.
  - Type: "kill process 5902" to terminate it (requires confirmation).
</finish>
```

### 5.5 Startup & Performance Cleanup
Ask: *"Analyze what's slowing down my startup and suggest what to disable."*

```
<thought>Pull startup items and services, then assess which are non-essential.</thought>
<call:list_startup_items>{}</call:list_startup_items>
<call:list_services>{}</call:list_services>

<observation:list_startup_items>
  Teams.exe (HKCU\Run) | Discord.exe (HKCU\Run) | Spotify.exe (Startup folder)
  OneDrive.exe (HKCU\Run) | AdobeUpdater.exe (HKLM\Run)
</observation:list_startup_items>

<finish>
  Startup items analysis (5 found):
  | App | Startup Type | Recommendation |
  |---|---|---|
  | Teams.exe | Registry | ⚠️ Disable — heavy; launch on demand |
  | Discord.exe | Registry | ⚠️ Disable — optional; launch on demand |
  | Spotify.exe | Startup Folder | ⚠️ Disable — not essential |
  | OneDrive.exe | Registry | ✅ Keep — needed for sync |
  | AdobeUpdater.exe | Registry | ⚠️ Disable — updater; runs silently |

  Disabling Teams, Discord, Spotify, AdobeUpdater could save ~8-12 seconds on boot.
  Say "disable Teams from startup" to proceed.
</finish>
```

---

## 6. Safety Tiers

| Tier | Label | Examples | Policy |
|---|---|---|---|
| **0** | Safe | File reads, screenshots, system info, web search | Execute immediately |
| **1** | Low Risk | File writes, clipboard, notifications, git status | Execute; background audit log |
| **2** | Medium | Code execution, email send, app launch, git commit | Announce intent; execute async |
| **3** | High | Delete files, kill processes, shell commands | `y/n` CLI confirmation required |
| **4** | Critical | Mass delete, exfiltration risk | Typed passphrase + dry-run preview |

---

## 6. LanceDB Memory Architecture

```
  ┌─────────────────────────────────────────────────────────────┐
  │                  meridian_memory/ (LanceDB)                  │
  ├───────────────────┬─────────────────────────────────────────┤
  │ conversations     │ id · timestamp · role · content ·        │
  │                   │ summary · embedding[384]                 │
  ├───────────────────┼─────────────────────────────────────────┤
  │ knowledge_base    │ id · source · chunk_text · embedding[384]│
  │                   │ · metadata                               │
  ├───────────────────┼─────────────────────────────────────────┤
  │ semantic_cache    │ id · query_text · query_embedding[384]   │
  │                   │ · response_text · expires_at             │
  ├───────────────────┼─────────────────────────────────────────┤
  │ task_log          │ id · timestamp · tool · tier · outcome   │
  │                   │ · error (append-only audit trail)        │
  └───────────────────┴─────────────────────────────────────────┘
```

- **Semantic Cache:** Cosine similarity >0.96 returns instantly (<5ms), skipping all inference.
- **Episodic Memory:** Past conversations searchable by embedding; recency-decay weighted scores.
- **Knowledge Base:** Ingested local files chunked into 200-word windows with 30-word overlap.
- **Audit Log:** Every Tier-2+ action written asynchronously via `asyncio.create_task()` — never delays user.

---

## 7. Self-Healing Error Recovery

```
Tool Fails or Returns Error
          │
          ├─► [Classify Error]
          │
          ├─► Code Error / Exception
          │        └─► Model reads stderr in <observation>
          │            Re-generates corrected code in next <thought>
          │            Auto-retries (up to 3 times per subgoal)
          │
          ├─► LLM OOM / Stalled
          │        └─► Evict moondream from Ollama
          │            Fall back to qwen2.5-coder:1.5b-instruct-q8_0
          │            Truncate context to 2048 tokens and retry
          │
          ├─► Permission / Tier-3 Block
          │        └─► Pause loop; request user confirmation
          │            Resume loop after confirmed
          │
          └─► Unrecoverable (3x retries exhausted)
                   └─► Return partial result to user
                       Append error to task_log (background)
                       Suggest next step in plain language
```

---

## 8. System Prompt — Autonomous Agent Mode

This is injected as the system message into every Ollama generation call. It is **static** (enabling Ollama KV-cache prefix reuse) and only the `{{PLACEHOLDERS}}` change per request.

```text
You are Meridian-X — a fully offline, autonomous desktop agent.
You think, plan, act, observe results, and self-correct in a continuous loop.
Backend: qwen2.5-coder:7b via Ollama (local, offline).
Memory: LanceDB RAG + MongoDB Knowledge Graph. Vision: moondream:1.8b (on-demand).

════════════════════════════════════════════
AGENT LOOP PROTOCOL — MANDATORY
════════════════════════════════════════════
Every turn you MUST use this structure:

1. THINK FIRST — always open with:
   <thought>
     Analyze current state, previous observations, and plan next action.
     If an observation has an error, debug it here and plan a fix.
   </thought>

2. CALL TOOLS — use zero or more calls per turn:
   <call:TOOL_NAME>{"argument": "value"}</call:TOOL_NAME>
   - Multiple calls in one turn run IN PARALLEL. Use this aggressively.
   - Args must be valid JSON inside the tags.

3. FINISH — when the goal is fully resolved:
   <finish>
     Your final response to the user. Be direct and clear.
     Include code blocks, tables, or structured output as needed.
   </finish>

════════════════════════════════════════════
RULES
════════════════════════════════════════════
- NEVER ask the user a question mid-task unless a Tier-3 confirmation is required.
- NEVER use placeholder logic or assume data — always call the tool to get real data.
- If a tool fails, self-correct in the next <thought> and retry (max 3 attempts).
- For Tier-3 actions (delete_file, kill_process), describe the action and pause for confirmation.
- Never reveal credentials, private paths, or API keys in any response.

════════════════════════════════════════════
CONTEXT
════════════════════════════════════════════
Workspace: {{WORKING_DIRECTORY}}
Time: {{CURRENT_DATETIME}}
OS: {{OS_INFO}}
RAG Context (top-2 relevant chunks):
{{RAG_CONTEXT}}
```

---

## 9. Full Stack Setup

### 9.1 Ollama — Pull Required Models

```bash
# Core reasoning brain (primary)
ollama pull qwen2.5-coder:7b-instruct-q4_K_M

# Fallback brain for low-RAM conditions
ollama pull qwen2.5-coder:1.5b-instruct-q8_0

# Vision model for screen analysis
ollama pull moondream:1.8b
```

### 9.2 Ollama Performance Environment Variables

```bash
# Windows (PowerShell) — set once, persistent
[System.Environment]::SetEnvironmentVariable('OLLAMA_FLASH_ATTENTION', '1', 'User')
[System.Environment]::SetEnvironmentVariable('OLLAMA_NUM_PARALLEL', '1', 'User')
[System.Environment]::SetEnvironmentVariable('OLLAMA_MAX_LOADED_MODELS', '1', 'User')
[System.Environment]::SetEnvironmentVariable('OLLAMA_KEEP_ALIVE', '300s', 'User')

# Linux / macOS
export OLLAMA_FLASH_ATTENTION=1       # KV-cache flash attention
export OLLAMA_NUM_PARALLEL=1          # One request at a time (edge hardware)
export OLLAMA_MAX_LOADED_MODELS=1     # Prevent VRAM OOM
export OLLAMA_KEEP_ALIVE=300s         # Keep model hot for 5 min
```

### 9.3 Python Dependencies (`requirements.txt`)

```txt
# === Inference & Embeddings ===
ollama                     # Ollama async Python client
sentence-transformers      # nomic-embed-text
optimum[onnxruntime]       # ONNX export for embeddings
onnxruntime                # CPU inference for embeddings, OCR, TTS, VAD

# === Vector Database ===
lancedb                    # Serverless embedded vector DB
pyarrow                    # Required by LanceDB

# === Knowledge Graph ===
pymongo                    # MongoDB Python driver (local mongod)

# === Scheduler & File Watcher ===
apscheduler                # Cron-style offline task scheduler (SQLite backend)
watchdog                   # Filesystem event monitoring

# === REST API Mode ===
fastapi                    # Local REST API server
uvicorn                    # ASGI server for FastAPI

# === Terminal Dashboard ===
textual                    # UI framework (replaces plain CLI)
rich                       # Markdown/syntax coloring in terminal

# === Voice Pipeline ===
faster-whisper             # INT8 offline STT
supertonic                # Supertonic TTS
sounddevice                # Audio capture & playback
silero-vad                 # Offline voice activity detection

# === Async Core ===
aiofiles                   # Async file I/O
anyio                      # Thread pool + structured concurrency
httpx[http2]               # Async HTTP client

# === Web & Parsing ===
tavily                     # Primary web search engine for fast query results
duckduckgo-search          # Privacy-first offline-capable fallback search
selectolax                 # Ultra-fast C HTML parser
playwright                 # Async headless browser (JS pages only)
pdfplumber                 # PDF text extraction

# === Desktop Automation ===
mss                        # Fast screenshot (<15ms)
rapidocr-onnxruntime       # Fully offline ONNX OCR
pyautogui                  # GUI keyboard/mouse automation
pygetwindow                # Window management
pyperclip                  # Clipboard
pycaw                      # Windows audio control
psutil                     # Process & system monitoring

# === Communication ===
aiosmtplib                 # Async SMTP
aioimaplib                 # Async IMAP
win10toast-reborn          # Windows toast notifications
plyer                      # Cross-platform notifications

# === Config ===
python-dotenv              # .env loading
```

### 9.4 Project Layout

```
meridian/
├── main.py                    # CLI entry point (or GUI)
├── api.py                     # FastAPI REST server (optional mode)
├── agent.md                   # This specification
├── requirements.txt
├── .env                       # Email creds, MongoDB URI, optional settings
├── plugins/                   # Drop .py files here to add new tools
│   └── example_plugin.py
├── src/
│   ├── core/
│   │   ├── loop.py            # Main ReAct orchestrator
│   │   ├── engine.py          # Ollama inference + embeddings
│   │   ├── memory.py          # LanceDB tables + cache
│   │   ├── knowledge.py       # MongoDB knowledge graph
│   │   ├── scheduler.py       # APScheduler cron task manager
│   │   ├── watcher.py         # Watchdog file system monitor
│   │   └── plugins.py         # Plugin auto-discovery loader
│   ├── tools/
│   │   ├── filesystem.py      # File read/write/search
│   │   ├── web.py             # Search, fetch, parse, scrape
│   │   ├── desktop.py         # Screenshot, OCR, vision, recording
│   │   ├── system.py          # Processes, clipboard, network, registry
│   │   ├── communication.py   # Email, notifications
│   │   ├── developer.py       # Python runner, git, ripgrep
│   │   └── rag.py             # File ingestion pipeline
├── ui/
│   └── app.py               # Tauri desktop shell entry module

│   └── voice/
│       ├── stt.py             # faster-whisper transcription
│       └── tts.py             # Supertonic synthesis
├── meridian_memory/           # LanceDB storage (auto-created)
└── meridian_kg/               # MongoDB data dir (local mongod)
```

---

## 10. Edge Performance Targets

| Operation | Target | Hardware |
|---|---|---|
| Semantic cache hit | < 5ms | Any |
| ONNX nomic-embed-text embed | < 1ms | CPU AVX2 |
| LanceDB ANN search | < 5ms | 8GB RAM + NVMe |
| Ollama TTFT (7B Q4, 512-tok ctx) | < 900ms | 8-core CPU |
| Ollama TTFT (1.5B Q8, 512-tok ctx) | < 200ms | 8-core CPU |
| Screenshot (mss) | < 15ms | Any OS |
| OCR (rapidocr-onnx) | < 100ms | CPU |
| STT (faster-whisper tiny) | < 300ms | CPU, 5s audio |
| TTS first audio (Supertonic) | < 100ms | CPU |
| ripgrep codebase search | < 50ms | SSD, 500K LOC |
| Per agent loop turn | < 1200ms | 8-core CPU |

---

## 11. Privacy & Security

- **Air-Gap Capable:** All inference, embedding, vector search, OCR, and TTS run entirely offline. Zero external API calls.
- **No Telemetry:** Ollama by default sends zero telemetry. All models run on `127.0.0.1:11434`.
- **Sandboxed Code:** `run_python` spawns an isolated subprocess. No direct file system access unless explicitly called via a Tier-1+ tool.
- **Tier-Gated Actions:** Destructive operations (Tier 3+) require explicit user confirmation before the agent proceeds.
- **Audit Trail:** Every Tier-2+ tool call is logged to `task_log` via `asyncio.create_task()` — non-blocking, never delays user.
- **Credential Safety:** The system prompt explicitly prohibits exposing any credentials, private paths, or keys in responses.

---

---

## 12. Advanced Capabilities

---

### 12.1 Persistent Knowledge Graph (MongoDB)

While LanceDB handles **vector similarity search**, MongoDB handles **structured world knowledge** — named entities, relationships, and facts the agent discovers from your conversations, files, and actions.

**Why MongoDB (local `mongod`) over NetworkX/SQLite:**
- Rich document model: each entity node is a flexible JSON document with arbitrary fields.
- Native `$graphLookup` for multi-hop relationship traversal.
- Full-text index + aggregation pipelines for complex queries.
- Persistent across sessions; survives context resets.

#### MongoDB Collections

```
mongodb://localhost:27017/meridian_kg
│
├── entities              — nodes in the knowledge graph
│   { _id, name, type, aliases[], attributes{}, embedding[384],
│     first_seen, last_seen, source }
│   Types: person · project · file · app · concept · place · event
│
├── relationships         — directed edges between entities
│   { _id, from_id, to_id, relation, strength(0-1),
│     created_at, evidence_text }
│   Relations: works_on · located_at · uses · depends_on ·
│              created_by · related_to · mentioned_with
│
└── facts                 — atomic key-value facts about the user/world
    { _id, subject, predicate, object, confidence,
      created_at, last_confirmed }
    Example: {subject:"Aryan", predicate:"uses", object:"Windows 11"}
```

#### Knowledge Graph Agent Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `kg_add_entity` | `name, type, attributes` | 1 | Upsert entity node into MongoDB |
| `kg_add_relation` | `from, to, relation, evidence` | 1 | Add directed edge with source evidence |
| `kg_query` | `entity_name` | 0 | Fetch entity + all connected nodes |
| `kg_search` | `query_text` | 0 | Full-text search across all entities |
| `kg_add_fact` | `subject, predicate, object` | 1 | Store atomic fact |
| `kg_get_facts` | `subject` | 0 | Retrieve all facts about an entity |
| `kg_traverse` | `start, depth` | 0 | `$graphLookup` multi-hop graph walk |

#### Example — Agent Learning About You
```
User: "My main project is Meridian, it lives at C:\Projects\meridian"

<thought>
  Extract entities and relationships from this statement and persist them.
</thought>
<call:kg_add_entity>{"name": "Meridian", "type": "project", "attributes": {"path": "C:\\Projects\\meridian"}}</call:kg_add_entity>
<call:kg_add_entity>{"name": "Aryan", "type": "person", "attributes": {"role": "owner"}}</call:kg_add_entity>
<call:kg_add_relation>{"from": "Aryan", "to": "Meridian", "relation": "works_on", "evidence": "User stated: my main project is Meridian"}</call:kg_add_relation>
<call:kg_add_fact>{"subject": "Meridian", "predicate": "located_at", "object": "C:\\Projects\\meridian"}</call:kg_add_fact>
<finish>Got it. I've saved Meridian as your main project at C:\Projects\meridian. I'll remember this permanently.</finish>
```

---

### 12.2 Agent Memory Summarization

A **background compression task** runs after every 20 conversation turns. It asks the model to distill the episodic conversation history into a compact set of facts, then writes those facts into the MongoDB `facts` collection and prunes the old LanceDB conversation entries.

```
[Background Task — every 20 turns]
        │
        ▼
[Fetch last 20 LanceDB conversation entries]
        │
        ▼
[Ollama: "Summarize these conversations into atomic facts"
  using qwen2.5-coder:1.5b (fast, cheap)]
        │
        ▼
[Write facts → MongoDB facts collection]
[Delete compressed entries from LanceDB]
        │
        ▼
[Memory stays lean; knowledge grows richer]
```

- Runs entirely via `asyncio.create_task()` — never blocks the user.
- Uses the 1.5B fallback model to minimize CPU cost during compression.
- MongoDB facts are included in every system prompt via the `{{KG_FACTS}}` placeholder.

---

### 12.3 Multi-Modal Input (Image-to-Task)

Users can paste or drag an image/screenshot directly into the desktop shell.
 The image is passed to `moondream:1.8b` via Ollama, and the description + raw path are injected into the agent's next turn as context.

```
User drops: error_screenshot.png

<thought>
  I received an image. I'll analyze it with moondream before planning.
</thought>
<call:vision_analyze>{"image_path": "error_screenshot.png", "prompt": "Describe all error messages and UI state visible in this image."}</call:vision_analyze>

<observation:vision_analyze>
  ModuleNotFoundError: No module named 'lancedb' visible in a PowerShell
  window. The traceback points to src/core/memory.py line 3.
</observation:vision_analyze>

<thought>The fix is simple — lancedb is not installed. I'll install it and check requirements.txt.</thought>
<call:run_command>{"cmd": "pip install lancedb"}</call:run_command>
<call:read_file>{"path": "requirements.txt"}</call:read_file>
```

**Supported input types:** PNG, JPEG, WEBP, BMP, GIF (first frame).

---

### 12.4 Cron-Style Task Scheduler (APScheduler + SQLite Backend)

Meridian-X can schedule any natural language task to run at a future time or on a recurring schedule — entirely offline, using `APScheduler` with a local SQLite job store.

#### Scheduler Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `schedule_task` | `goal, cron_expr` | 1 | Add recurring job (cron syntax) |
| `schedule_once` | `goal, run_at` | 1 | One-shot future task |
| `list_scheduled` | — | 0 | List all pending/recurring jobs |
| `cancel_task` | `job_id` | 2 | Remove scheduled job |

#### Example
```
User: "Every morning at 8AM, summarize my emails and notify me."

<call:schedule_task>{
  "goal": "Read the last 10 emails, write a 3-sentence summary, and send me a desktop notification with the summary.",
  "cron_expr": "0 8 * * *"
}</call:schedule_task>
<finish>Done. I'll run that every morning at 8:00 AM. Job ID: job_0042.</finish>
```

---

### 12.5 File Watcher / Event-Driven Agent (Watchdog)

Meridian-X can monitor any folder for changes and trigger autonomous agent tasks when events occur.

#### Watcher Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `watch_folder` | `path, on_create_goal, on_modify_goal` | 1 | Start watching a directory |
| `unwatch_folder` | `path` | 1 | Stop watching |
| `list_watchers` | — | 0 | List active watchers |

#### Example Automations
```
# Auto-ingest any PDF dropped into ~/Documents/inbox
watch_folder:
  path: "C:\Users\aryan\Documents\inbox"
  on_create_goal: "Ingest the new file at {{file_path}} into the RAG knowledge base and notify me."

# Auto-run tests when any .py file in src/ changes
watch_folder:
  path: "C:\Projects\meridian\src"
  on_modify_goal: "Run 'python -m pytest tests/' and report the results."
```

---

### 12.6 Vision-Guided Browser Automation

Combines `playwright` (headless Chromium) with `moondream:1.8b` for **visual browser control** — the agent takes a screenshot of the browser, uses vision to locate UI elements by natural language description, and clicks the correct coordinates. No CSS selectors needed.

#### Browser + Vision Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `browser_open` | `url` | 1 | Launch headless browser to URL |
| `browser_screenshot` | — | 0 | Capture current browser viewport |
| `browser_find_and_click` | `description` | 2 | Vision-locate element → click coordinates |
| `browser_type_in` | `description, text` | 2 | Vision-locate input → type text |
| `browser_get_text` | — | 0 | Extract all visible text from current page |
| `browser_close` | — | 1 | Close browser session |

#### Example — Fill a Web Form Without Selectors
```
<call:browser_open>{"url": "http://localhost:3000/login"}</call:browser_open>
<call:browser_screenshot>{}</call:browser_screenshot>
<call:vision_analyze>{"image_path": "browser.png", "prompt": "What are the (x,y) coordinates of the username input field and the password input field?"}</call:vision_analyze>

<observation:vision_analyze>Username field at approximately (640, 310). Password field at (640, 380).</observation:vision_analyze>

<call:gui_click>{"x": 640, "y": 310}</call:gui_click>
<call:gui_type>{"text": "aryan"}</call:gui_type>
<call:gui_click>{"x": 640, "y": 380}</call:gui_click>
<call:gui_type>{"text": "mypassword"}</call:gui_type>
<call:browser_find_and_click>{"description": "Login button"}</call:browser_find_and_click>
<finish>Logged in successfully using vision-guided coordinate mapping.</finish>
```

---

### 12.7 Offline Web Scraping Pipeline

Crawl a list of local or intranet URLs, extract structured data (tables, lists, prices), and persist it to LanceDB or MongoDB. Runs fully offline for local resources.

#### Scraper Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `scrape_urls` | `urls[], extract_schema` | 1 | Crawl list of URLs; extract fields per schema |
| `scrape_table` | `url, table_index` | 0 | Extract HTML table → Python list of dicts |
| `schedule_scrape` | `urls[], cron_expr` | 1 | Recurring automated scrape job |

#### Example
```
User: "Monitor my local inventory page every hour and alert me if stock drops below 10."

<call:schedule_scrape>{
  "urls": ["http://localhost:8080/inventory"],
  "cron_expr": "0 * * * *"
}</call:schedule_scrape>
# On each run, scrape → check values → if stock < 10, call send_notification
```

---

### 12.8 Plugin System

Any `.py` file dropped into the `plugins/` directory is **auto-discovered at startup**. Each public function in the file is registered as a new agent tool with its docstring as the tool description, its type hints as argument schema, and its tier from a `TIER` module-level constant.

#### Plugin Contract
```python
# plugins/my_custom_tool.py
TIER = 1  # execution tier for all tools in this file

async def send_slack_message(channel: str, message: str) -> str:
    """Send a message to a local Slack-compatible webhook."""
    # ... implementation
    return "Message sent."
```

At startup, `plugins.py` walks the `plugins/` directory, imports each module, and registers every `async def` as a callable tool in the agent's tool map. No code changes to core required.

---

### 12.9 Local REST API Mode (FastAPI on 127.0.0.1:4132)

Run `python api.py` or `uvicorn api:app --host 127.0.0.1 --port 4132` to expose Meridian-X as a local HTTP server. Other applications — VS Code extensions, Obsidian plugins, custom scripts, or another agent — can send tasks programmatically.

#### Endpoints
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/run` | Execute a goal synchronously and return the final result |
| `POST` | `/api/v1/run_background` | Start a goal in the background and return immediately |
| `GET` | `/api/v1/status` | Health status for the agent service |

```bash
# Start the API server
uvicorn api:app --host 127.0.0.1 --port 4132

# Submit a task to Meridian-X from another script
curl -X POST http://127.0.0.1:4132/api/v1/run \
  -H "Content-Type: application/json" \
  -d '{"goal": "Find the largest file in C:/Users/aryan/Downloads and tell me its size."}'
```

---

## 13. Unified Cognitive Mode System

Meridian-X is **one agent** — but it is not a flat, single-mode reasoner. When the task classifier detects the type of work required, it injects a **Cognitive Mode Directive** into the system prompt, changing how the agent reasons, which tools it prioritises, and how verbose its `<thought>` blocks are. There are no separate processes, no spawned subprocesses, and no inter-agent message buses. It is all one ReAct loop with a dynamically scoped reasoning persona.

### 13.1 Cognitive Mode Switcher

```
User Goal Arrives
       │
       ▼
[Mode Classifier — 32-token fast pass]
Analyzes keywords, intent, and entity types:
       │
       ├─► "build", "write", "fix", "test", "debug"   → ENGINEER mode
       ├─► "review", "audit", "check for bugs"        → REVIEWER mode
       ├─► "what's using CPU", "analyze system"       → ANALYST mode
       ├─► "click", "open", "type", "automate"        → OPERATOR mode
       ├─► "research", "find info", "summarize web"   → RESEARCHER mode
       └─► everything else                            → AUTO mode (default)
               │
               ▼
       [Mode Directive injected into system prompt]
       [ReAct loop proceeds with mode-specific reasoning]
```

### 13.2 Mode Behaviours

| Mode | Reasoning Style | Prioritised Tools | `<thought>` Depth |
|---|---|---|---|
| **AUTO** | Balanced; conversational | Any tool as needed | Minimal |
| **ENGINEER** | Code-first; test-driven; iterative | `run_python`, `write_file`, `git_*`, `search_codebase` | Deep |
| **REVIEWER** | Critic; structured analysis; finds edge cases | `read_file`, `git_diff`, `search_files`, `run_python` | Deep |
| **ANALYST** | Data-first; parallel data collection | `get_system_info`, `list_processes`, `get_disk_info`, `get_network_connections` | Medium |
| **OPERATOR** | Action-first; minimal reasoning delay | `screenshot`, `gui_click`, `open_app`, `focus_window` | Minimal |
| **RESEARCHER** | Explore-then-synthesize | `search_web`, `fetch_page`, `parse_page`, `ingest_file`, `search_knowledge` | Medium |

The mode is re-evaluated after every 3 turns — if the conversation pivots (e.g. research turns into coding), the agent seamlessly switches modes mid-task.

---

## 14. Remaining Advanced Capabilities

---

### 14.1 SWE-Agent Mode (Autonomous Software Engineer)

When in **ENGINEER** mode on a complex coding goal, the agent runs a specialised inner loop: **write → test → observe failures → fix → repeat** until all tests pass or the goal is explicitly marked done. This is the Meridian-X equivalent of SWE-agent / Devin, running entirely on local Qwen2.5-Coder.

#### SWE Loop
```
[ENGINEER Goal Received]
        │
        ▼
<thought> Scaffold project/file structure </thought>
<call:write_file> scaffold code </call:write_file>
        │
        ▼
<call:run_python> run tests </call:run_python>
        │
   ┌────▼────┐
   │ PASS?   │
   └────┬────┘
    YES │           NO
        │     ┌─────▼──────────────────────────────┐
        │     │ <thought> Read failure, locate bug  │
        │     │ Generate targeted fix </thought>    │
        │     │ <call:write_file> patch </call>      │
        │     │ [loop back to run tests]            │
        │     └────────────────────────────────────┘
        ▼
<finish> All tests pass. Here's the summary. </finish>
```

#### SWE-Mode Tools Added
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `scaffold_project` | `name, template` | 1 | Generate project skeleton from template (Python, FastAPI, React) |
| `run_tests` | `path, framework` | 2 | Run pytest / unittest; returns pass/fail + stdout |
| `install_package` | `package` | 2 | `pip install`; captured async |
| `lint_file` | `path` | 0 | Run `ruff` or `flake8`; returns issues list |
| `format_file` | `path` | 1 | Run `black` / `autopep8` in-place |

---

### 14.2 Screen Recording & Workflow Replay

The agent can record your screen while you perform a task, analyze it by sampling frames with `moondream:1.8b`, extract the sequence of actions, and replay them autonomously on demand.

#### How It Works
```
User: "Watch me fill in this form, then repeat it automatically."
        │
        ▼
[record_screen starts — mss captures frames at 2fps into temp dir]
[User performs the task manually]
[User says "stop"]
        │
        ▼
<call:analyze_recording> sample every 5th frame with moondream
 → "Frame 1: User opens Chrome"
 → "Frame 4: User clicks username field at ~(640,310)"
 → "Frame 7: User types 'aryan'"
 → "Frame 12: User clicks Login button at ~(640,450)"
</call:analyze_recording>
        │
        ▼
[Agent generates a replayable action plan stored in MongoDB]
        │
        ▼
[replay_workflow] executes the plan: open_app → gui_click → gui_type ...
```

#### Recording Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `record_screen` | `output_dir, fps` | 1 | Capture frames to temp folder using mss |
| `stop_recording` | — | 1 | Stop recording and return frame count |
| `analyze_recording` | `frame_dir` | 0 | Sample frames with moondream; extract action sequence |
| `save_workflow` | `name, action_plan` | 1 | Persist replay plan to MongoDB `workflows` collection |
| `replay_workflow` | `name` | 2 | Execute saved workflow action-by-action |
| `list_workflows` | — | 0 | List all saved replay workflows |

---

### 14.3 Adaptive User Profiling

Every interaction teaches the agent more about you. A background profiling task continuously extracts preference signals from conversations and tool usage, writing them into the MongoDB `user_profile` collection. Every system prompt injection includes the top-10 most relevant facts about you.

#### Profile Schema (MongoDB)
```javascript
// mongodb://localhost/meridian_kg.user_profile
{
  _id: "aryan",
  preferences: {
    coding_language: "Python",
    editor: "VS Code",
    shell: "PowerShell",
    response_tone: "concise",
    preferred_model_mode: "ENGINEER"
  },
  habits: {
    peak_hours: ["22:00", "23:00", "00:00"],   // inferred from timestamps
    frequent_tools: ["run_python", "git_commit", "search_codebase"],
    frequent_paths: ["C:\\Projects\\meridian", "C:\\Users\\aryan\\Downloads"]
  },
  corrections: 14,         // times user corrected the agent → fine-tuning signal
  last_updated: "2026-05-18T00:00:00Z"
}
```

**System Prompt Injection:**
```text
User Profile:
- Preferred language: Python · Editor: VS Code · Shell: PowerShell
- Peak hours: 10PM-12AM · Frequently works in: C:\Projects\meridian
- Prefers concise responses · Default mode: ENGINEER
```

---

### 14.4 Smart Clipboard Manager

Every clipboard write (user or agent) is intercepted, embedded with nomic-embed-text, and stored in MongoDB with a timestamp and source context. The entire history is semantically searchable.

#### Clipboard Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `clipboard_history` | `n` | 0 | List last N clipboard entries with timestamps |
| `clipboard_search` | `query` | 0 | Semantic search across all clipboard history |
| `clipboard_pin` | `entry_id` | 1 | Pin entry so it never expires |
| `clipboard_restore` | `entry_id` | 1 | Re-paste a historical clipboard entry |

#### Example
```
User: "find that async generator snippet I copied a few days ago"

<call:clipboard_search>{"query": "async generator Python"}</call:clipboard_search>

<observation:clipboard_search>
  [2026-05-14 23:41]  async def stream_tokens(...):\n    async for chunk in ...
  [2026-05-13 18:22]  async for item in aiter(collection): yield item
</observation:clipboard_search>

<finish>Found 2 matches. The most likely one is from May 14th — async generator
that streams tokens. Restoring it to your clipboard now.</finish>
```

---

### 14.5 Fine-Tuning Data Collection

Every time you correct the agent, the original (wrong) response and your correction are automatically logged as a JSONL training pair. Over time this builds a personal fine-tuning dataset aligned to your preferences.

#### Collection Logic
```
Agent gives response
        │
        ▼
User types a correction (e.g. "no, do it this way instead...")
        │
        ▼
[Correction detector — keyword match: "no", "wrong", "instead", "actually"]
        │
        ▼
[Write to finetune_data.jsonl]:
  {
    "instruction": "<original user goal>",
    "rejected":    "<agent's wrong response>",
    "chosen":      "<user's corrected version>",
    "timestamp":   "2026-05-18T00:00:00Z",
    "mode":        "ENGINEER"
  }
```

#### Fine-Tuning Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `export_finetune_data` | `output_path` | 0 | Export collected JSONL dataset |
| `finetune_stats` | — | 0 | Show correction count, breakdown by mode |
| `mark_correction` | `pair_id, quality` | 1 | Rate a collected pair (good/bad) for DPO training |

---

### 14.6 Encrypted Secrets Vault

A local AES-256-GCM encrypted vault stores all credentials (API keys, passwords, tokens). The agent retrieves secrets by **name only** — the raw value is decrypted in memory for the tool call and never appears in any response, log, or `<thought>` block.

#### Vault Design
```
vault.enc  (AES-256-GCM, key derived from master password via Argon2id)
├── SMTP_PASSWORD    → "hunter2"
├── GITHUB_TOKEN     → "ghp_xxxx"
└── OPENAI_KEY       → "sk-xxxx"   (for future optional use)
```

#### Vault Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `vault_set` | `name, value` | 2 | Encrypt and store a secret |
| `vault_get` | `name` | 1 | Decrypt and return secret value (in-memory only) |
| `vault_list` | — | 0 | List secret names only (never values) |
| `vault_delete` | `name` | 3 | Remove secret; confirmation required |

**System Prompt Rule:** The agent is prohibited from including any `vault_get` result in `<finish>` or `<thought>` output. Secrets flow only into tool call arguments via the runner.

---

### 14.7 Offline Code Review Agent (REVIEWER Mode)

Point the agent at any file, directory, or `git diff` and it switches into REVIEWER mode, performing a structured 5-pillar analysis entirely on `qwen2.5-coder:7b`.

#### Review Pillars
1. **Correctness** — Logic errors, off-by-one, wrong conditionals, data races
2. **Security** — Injection risks, hardcoded credentials, unsafe deserialization
3. **Performance** — N+1 loops, unnecessary I/O in hot paths, blocking calls in async code
4. **Maintainability** — Function length, naming, missing docstrings, dead code
5. **Test Coverage** — Missing edge cases, untested error paths

#### Review Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `review_file` | `path` | 0 | Full 5-pillar review of a single file |
| `review_diff` | `repo_path` | 0 | Review `git diff HEAD` output |
| `review_directory` | `path, glob` | 0 | Review all matching files; aggregate report |
| `export_review` | `output_path` | 1 | Write review report as markdown file |

#### Example Output
```
📋 Code Review — src/core/loop.py

🔴 SECURITY [line 47]  User input passed directly to asyncio subprocess — shell injection risk.
                       Fix: use shlex.split() or pass as list, not string.

🟡 PERFORMANCE [line 89]  tool.execute() called serially in a for-loop.
                           Fix: use asyncio.gather(*[execute(t) for t in tools])

🟢 CORRECTNESS  No logic errors detected.
🟢 MAINTAINABILITY  Functions well-scoped, docstrings present.
⚪ TEST COVERAGE  No tests found for MeridianLoop.parse_loop_response()
```

---

### 14.8 Natural Language Shell (NL Shell Mode)

A dedicated `/shell` mode where every input is treated as a plain-English command. The agent translates it to the correct shell command, previews it, runs it, and shows the output — without the user needing to remember syntax.

```
>>> /shell
NL Shell active. Type commands in plain English. Type /exit to leave.

shell> list all Python files over 1MB modified in the last 7 days
→ Translated: Get-ChildItem -Recurse -Filter *.py | Where-Object { $_.Length -gt 1MB -and $_.LastWriteTime -gt (Get-Date).AddDays(-7) }
→ Running...

C:\Projects\meridian\src\core\loop.py        1.3 MB   2026-05-17
C:\Projects\meridian\data\corpus.py          2.1 MB   2026-05-15

shell> kill everything using more than 20% CPU
→ Translated: Get-Process | Where-Object {$_.CPU -gt 20} | Stop-Process -Force
→ ⚠️ This is a Tier-3 action. Confirm? (y/N):
```

#### NL Shell Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `nl_to_shell` | `natural_language` | 0 | Translate NL to shell command (preview only) |
| `nl_run` | `natural_language` | 2 | Translate and execute; Tier-3 gated for destructive ops |
| `shell_history` | `n` | 0 | Last N NL shell entries with translations |

---

### 14.9 Conversation Export & Session Reports

Export any completed session — or a specific goal thread — as a formatted markdown or standalone HTML report. Useful for documentation, sharing workflows, or creating runbooks.

#### Export Formats
| Format | Description |
|---|---|
| **Markdown** | Clean `.md` with thought blocks collapsed, tool calls formatted as code, final answers highlighted |
| **HTML** | Self-contained `.html` with syntax highlighting, collapsible thought sections, copy buttons |
| **JSONL** | Raw structured log of all turns, tool calls, observations, and timings |
| **Runbook** | Markdown document describing only the actions taken — no thoughts, no observations — as a reproducible how-to guide |

#### Export Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `export_session` | `format, output_path` | 1 | Export current session |
| `export_goal` | `goal_id, format, output_path` | 1 | Export a specific past goal by ID |
| `list_sessions` | — | 0 | List past exportable sessions from LanceDB |

#### Example
```
User: "Export this session as a runbook so I can share it with my team."

<call:export_session>{"format": "runbook", "output_path": "C:\\Users\\aryan\\Desktop\\session_runbook.md"}</call:export_session>
<finish>Runbook exported to Desktop. It contains 7 reproducible steps
with all commands and file paths filled in from the actual run.</finish>
```

---

### 14.10 Local Database Query Tool (ANALYST Mode)

The agent can connect to any local database — SQLite, PostgreSQL, or MySQL — and run queries expressed in natural language or raw SQL. Useful for developers who want to inspect local dev databases without leaving the terminal.

#### Supported Backends
| Driver | Database | Lib |
|---|---|---|
| `aiosqlite` | SQLite (`.db` files) | Built-in async; zero setup |
| `asyncpg` | Local PostgreSQL | Async native driver |
| `aiomysql` | Local MySQL / MariaDB | Async native driver |

#### Database Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `db_connect` | `type, path_or_dsn` | 1 | Open connection to a local DB |
| `db_query` | `sql` | 1 | Execute a SELECT query; returns rows as list of dicts |
| `db_execute` | `sql` | 2 | Execute INSERT/UPDATE/DELETE; returns affected rows |
| `db_schema` | — | 0 | List all tables, columns, types, and row counts |
| `db_nl_query` | `natural_language` | 1 | Translate NL to SQL, preview, then execute |
| `db_disconnect` | — | 1 | Close active connection |

#### Example — Natural Language to SQL
```
User: "Connect to my dev SQLite database and show me the 5 most recent orders."

<call:db_connect>{"type": "sqlite", "path_or_dsn": "C:\\Projects\\shop\\dev.db"}</call:db_connect>
<call:db_schema>{}</call:db_schema>

<observation:db_schema>
  Tables: orders(id, user_id, total, created_at), users(id, name, email)
</observation:db_schema>

<call:db_nl_query>{"natural_language": "5 most recent orders"}</call:db_nl_query>

<observation:db_nl_query>
  SQL: SELECT * FROM orders ORDER BY created_at DESC LIMIT 5;
  Results: [{id:42, user_id:7, total:149.99, created_at:"2026-05-17"}, ...]
</observation:db_nl_query>

<finish>
  | id | user_id | total   | created_at |
  |----|---------|---------|------------|
  | 42 | 7       | £149.99 | 2026-05-17 |
  | 41 | 3       | £72.50  | 2026-05-16 |
  ...
</finish>
```

#### Example — Schema Analysis
```
User: "What's the total row count and size of each table in my SQLite DB?"

<call:db_nl_query>{"natural_language": "row count and estimated size per table"}</call:db_nl_query>
<finish>
  | Table    | Rows   | Est. Size |
  |----------|--------|-----------|
  | orders   | 12,847 | 4.2 MB    |
  | users    | 1,203  | 0.8 MB    |
  | products | 342    | 0.2 MB    |
</finish>
```

---

### 14.11 Log File Monitoring & Error Detection (ANALYST Mode)

The agent watches one or more log files in real time using `watchdog` + async file tailing. When it detects an error, exception, or anomaly pattern, it wakes up, diagnoses the problem using the LLM, and optionally triggers a self-healing action (restart a service, notify the user, or file a task in the scheduler).

#### How It Works
```
[watch_log activated on app.log]
        │
        ▼ (new line written to log)
[Pattern Matcher]
  │
  ├─► ERROR / EXCEPTION / CRITICAL / TRACEBACK detected?
  │        └─► YES: wake agent
  │
  └─► Anomaly threshold? (e.g. >10 errors/min)
           └─► YES: wake agent
        │
        ▼
<thought>
  Read the last 50 log lines for context.
  Identify root cause.
  Check if auto-fix is applicable.
</thought>
<call:read_file>{"path": "app.log"}</call:read_file>
        │
        ▼
[Auto-fix decision tree]
  Known error + fix available → apply fix silently, notify user
  Unknown error              → notify user with diagnosis + suggested next step
  Critical / Tier-3 action   → pause and request user confirmation
```

#### Log Monitor Tools
| Tool | Args | Tier | Notes |
|---|---|---|---|
| `watch_log` | `path, patterns[], on_match_goal` | 1 | Start real-time log watcher |
| `unwatch_log` | `path` | 1 | Stop watching a log file |
| `list_log_watchers` | — | 0 | List all active log watchers |
| `tail_log` | `path, n` | 0 | Read last N lines from a log file |
| `search_log` | `path, pattern, limit` | 0 | Regex/substring search through log file |
| `log_stats` | `path` | 0 | Count ERROR / WARN / INFO lines; errors-per-minute rate |

#### Example — Auto-Monitoring a FastAPI Service
```
User: "Watch my API server log and alert me if there are more than 5 errors per minute."

<call:watch_log>{
  "path": "C:\\Projects\\api\\server.log",
  "patterns": ["ERROR", "CRITICAL", "Traceback"],
  "on_match_goal": "Read the last 30 lines of server.log, diagnose the error, and send me a desktop notification with the root cause."
}</call:watch_log>
<finish>Log watcher active on server.log. You'll be alerted immediately on any ERROR or CRITICAL entry.</finish>

# --- Later, when an error appears ---

[WATCHER TRIGGERED]
<call:tail_log>{"path": "C:\\Projects\\api\\server.log", "n": 30}</call:tail_log>
<call:log_stats>{"path": "C:\\Projects\\api\\server.log"}</call:log_stats>

<observation:log_stats>ERROR count: 23 in last 60s (rate: 23/min)</observation:log_stats>
<observation:tail_log>...sqlalchemy.exc.OperationalError: database is locked...</observation:tail_log>

<thought>
  Root cause: SQLite database lock contention. This happens when multiple
  async workers try to write simultaneously. Fix: add WAL mode pragma.
</thought>
<call:send_notification>{
  "title": "🚨 API Server Error Spike",
  "message": "23 errors/min detected. Root cause: SQLite lock contention. Suggested fix: enable WAL mode."
}</call:send_notification>
```

#### Built-In Error Pattern Library
The watcher ships with a built-in pattern library that maps common error signatures to diagnostic hints:

| Pattern | Diagnosis | Auto-Action |
|---|---|---|
| `database is locked` | SQLite write contention | Suggest WAL mode |
| `Connection refused` | Service not running | Offer to restart via `run_command` |
| `MemoryError` | OOM condition | Report top memory processes |
| `PermissionError` | File access denied | Report file path + owner |
| `ModuleNotFoundError` | Missing dependency | Offer `pip install <module>` |

---

## 15. Updated Requirements & Project Layout

### 15.1 Additional Dependencies

```txt
# === SWE Mode ===
ruff                       # Fast Python linter (replaces flake8)
black                      # Code formatter
pytest                     # Test runner for run_tests tool

# === Screen Recording ===
opencv-python-headless     # Frame analysis and sampling from recordings

# === Secrets Vault ===
cryptography               # AES-256-GCM encryption + Argon2id key derivation

# === Clipboard Monitoring ===
pynput                     # Global keyboard/mouse hook for clipboard intercept

# === Database Query Tool ===
aiosqlite                  # Async SQLite driver
asyncpg                    # Async PostgreSQL driver (local postgres)
aiomysql                   # Async MySQL driver (local mysql)

# === Log Monitoring ===
aiofiles                   # Async log file tailing (already in core)
# watchdog already listed above — reused for log file watching

# === Fine-Tuning Data ===
# No new deps — writes to finetune_data.jsonl natively

# === NL Shell ===
# Uses existing run_command + Ollama generate — no new deps
```

### 15.2 Updated Project Layout

```
meridian/
├── main.py                      # Desktop entry point (GUI-first)
├── api.py                       # FastAPI REST server
├── agent.md                     # This specification
├── requirements.txt
├── .env                         # MongoDB URI, SMTP, optional settings
├── vault.enc                    # AES-256 encrypted secrets vault
├── finetune_data.jsonl          # Auto-collected fine-tuning pairs
├── plugins/                     # Drop .py files to add tools
│   └── example_plugin.py
├── src/
│   ├── core/
│   │   ├── loop.py              # Main ReAct orchestrator
│   │   ├── engine.py            # Ollama inference + embeddings
│   │   ├── memory.py            # LanceDB tables + semantic cache
│   │   ├── knowledge.py         # MongoDB knowledge graph + facts
│   │   ├── scheduler.py         # APScheduler cron task manager
│   │   ├── watcher.py           # Watchdog file system monitor
│   │   ├── plugins.py           # Plugin auto-discovery loader
│   │   ├── profiler.py          # Adaptive user profiling
│   │   ├── vault.py             # AES-256 secrets vault
│   │   ├── clipboard.py         # Smart clipboard history manager
│   │   ├── finetune.py          # Fine-tuning data collector
│   │   └── mode.py              # Cognitive mode classifier + injector
│   ├── tools/
│   │   ├── filesystem.py        # File read/write/search
│   │   ├── web.py               # Search, fetch, parse, scrape
│   │   ├── desktop.py           # Screenshot, OCR, vision, GUI, recording
│   │   ├── system.py            # Processes, clipboard, network, registry
│   │   ├── communication.py     # Email, notifications
│   │   ├── developer.py         # Python runner, git, ripgrep, linting
│   │   ├── review.py            # Code review (5-pillar REVIEWER mode)
│   │   ├── shell.py             # NL Shell translation + execution
│   │   └── rag.py               # File ingestion pipeline
├── ui/
│   └── app.py               # Tauri desktop shell entry module

│   └── voice/
│       ├── stt.py               # faster-whisper transcription
│       └── tts.py               # Supertonic synthesis
├── meridian_memory/             # LanceDB storage (auto-created)
├── meridian_kg/                 # MongoDB data directory
└── recordings/                  # Temporary screen recording frames
```

---

## 16. Full Capability Summary

| # | Capability | Mode | Key Tech |
|---|---|---|---|
| 1 | Autonomous ReAct Loop | ALL | Ollama + XML tags |
| 2 | Multi-turn self-correction | ALL | Error → `<thought>` → retry |
| 3 | Semantic cache (>0.96 cosine) | ALL | LanceDB |
| 4 | RAG knowledge base | ALL | LanceDB + nomic-embed-text |
| 5 | MongoDB knowledge graph | ALL | pymongo + `$graphLookup` |
| 6 | Memory summarization | ALL | Background task, 1.5B model |
| 7 | Adaptive user profiling | ALL | MongoDB `user_profile` |
| 8 | Cognitive mode switching | ALL | Mode classifier + prompt injection |
| 9 | Filesystem (read/write/search) | ALL | aiofiles + ripgrep |
| 10 | Web search & scraping | RESEARCHER | Tavily primary + DuckDuckGo fallback + selectolax |
| 11 | Vision-guided browser | OPERATOR | playwright + moondream |
| 12 | Full GUI automation | OPERATOR | pyautogui + mss |
| 13 | Window management | OPERATOR | pygetwindow + Win32 |
| 14 | Deep system analysis | ANALYST | psutil + wmic |
| 15 | Startup / registry audit | ANALYST | winreg + sc query |
| 16 | Network & security analysis | ANALYST | psutil net + process cross-ref |
| 17 | SWE-Agent mode (write→test→fix) | ENGINEER | run_python + pytest loop |
| 18 | Code scaffolding | ENGINEER | Templates + write_file |
| 19 | Linting & formatting | ENGINEER | ruff + black |
| 20 | Git integration | ENGINEER | Async git CLI |
| 21 | 5-pillar code review | REVIEWER | qwen2.5-coder:7b |
| 22 | Natural Language Shell | ALL | Ollama translate + run_command |
| 23 | Screen recording & replay | OPERATOR | mss + moondream + MongoDB |
| 24 | Smart clipboard manager | ALL | pynput + MongoDB + nomic-embed-text |
| 25 | APScheduler cron tasks | ALL | APScheduler + SQLite |
| 26 | File watcher automations | ALL | watchdog |
| 27 | Voice input (STT) | ALL | faster-whisper INT8 |
| 28 | Voice output (TTS) | ALL | Supertonic |
| 29 | Email send/read | ALL | aiosmtplib + aioimaplib |
| 30 | Desktop notifications | ALL | win10toast / plyer |
| 31 | Multi-modal image input | ALL | moondream:1.8b via Ollama |
| 32 | Encrypted secrets vault | ALL | AES-256-GCM + Argon2id |
| 33 | Fine-tuning data collection | ALL | JSONL auto-logging |
| 34 | Session export (MD/HTML/runbook) | ALL | Markdown + Jinja2 |
| 35 | Plugin auto-discovery | ALL | `plugins/` folder |
| 36 | REST API mode | ALL | FastAPI + 127.0.0.1:4132 |
| 37 | Tauri Desktop Shell | ALL | Tauri + native windowing |
| 38 | Self-healing fallback (1.5B) | ALL | Ollama model swap |
| 39 | Tier-gated safety system | ALL | 0-4 confirmation ladder |
| 40 | Full audit trail | ALL | LanceDB `task_log` |
| 41 | Local database query (SQL) | ANALYST | aiosqlite + asyncpg + aiomysql |
| 42 | Log monitoring & error detection | ANALYST | watchdog + regex + auto-fix loop |

---

*Meridian-X — One agent. Every capability. Fully yours. Fully offline.*

---

```
<!-- FILE_END: meridian-desktop/src-tauri/src/main.rs -->

