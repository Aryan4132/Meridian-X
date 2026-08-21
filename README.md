<div align="center">

<img src="logo.png" alt="Meridian-X Logo" width="220" />

# 🪐 Meridian-X

### Intelligent Agentic Desktop Workspace Companion

[![Version](https://img.shields.io/badge/version-0.5.2-blueviolet)](https://github.com/Aryan4132/Meridian-X/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-blue?logo=tauri&logoColor=white)](https://tauri.app)
[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![Tauri](https://img.shields.io/badge/Tauri-v2-FFC131?logo=tauri&logoColor=white)](https://tauri.app)
[![FastAPI](https://img.shields.io/badge/FastAPI-async-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Meridian-X** is an offline-first, agentic desktop AI assistant built on **Tauri v2 + React**, **FastAPI**, and **user-configurable AI models (Local or Cloud)**. It runs autonomous ReAct reasoning loops, secures your workspace with multi-tier safety gates, parses documents into a local vector store, and ships an interactive 3D mascot companion with full cloud API vault and MCP server integration.

[🌐 Website](https://meridian-x.pages.dev) · [⬇ Download](https://github.com/Aryan4132/Meridian-X/releases) · [📖 Installation](#️-getting-started--installation) · [🛠 Contributing](#-contributing)

</div>

---

## ✨ Key Features

### 🧠 ReAct Reasoning Agent

Asynchronous **Reason → Act → Observe** loop powered by user-selected local or cloud models (Ollama, OpenAI, Anthropic, Gemini, Groq, OpenRouter, DeepSeek), streaming live reasoning timelines to the UI via SSE.

- **Self-Correction**: Intercepts tool calls and heals parameter mismatches against the `TOOL_REGISTRY`.
- **Syntax & Logic Validation**: Validates Python/JSON before execution; an auditor model catches logic bugs before they run.

### 🔐 Encrypted Secret Vault

AES-GCM encrypted credential store for all third-party secrets:

- **LLM Providers**: Groq, OpenRouter, Mistral, OpenAI, Anthropic, Gemini, DeepSeek.
- **Voice**: ElevenLabs, Deepgram. **Search**: Tavily.
- Machine-bound HMAC-SHA256 passphrase derivation tied to `hostname + username`.

### 🔌 MCP Server Registry

- **1-Click Marketplace**: Install and register MCP servers (GitHub, PostgreSQL, Slack, Linear).
- **Direct Tool Injection**: Connected MCP servers inject tools directly into the agent reasoning loop.

### 🦊 Interactive Mascot & Dynamic Island

A 3D orbital-ring companion floating over your desktop that reflects cognitive state in real time.

- **State Colors** (locked, never changes with theme): Blue = Idle · Amber = Working · Red = Failed · Green = Success.
- **Ring Dynamics**: Slow spin (idle) → Fast spin (working) → Frozen (failed).
- **Island Mode**: Closing the dashboard compresses Meridian-X into a sleek floating island.
- **6 Anchor Positions**: Top/Bottom × Left/Center/Right.

### 🎮 Frameless Overlay & Global Hotkeys

Sub-10ms frameless HUD and global hotkey engine — toggle workspace, mascot island, or voice input without leaving full-screen games or apps.

| Global Hotkey | Action Target | Description |
| :--- | :--- | :--- |
| **`Alt + M`** | 💬 Main Workspace Window | Hides/shows the main desktop workspace shell |
| **`Alt + Shift + M`** | 🦊 Mascot / Frameless Overlay | Toggles between full dashboard and compact floating mascot HUD |
| **`Alt + V`** | 🎙️ Push-to-Talk Voice Input | Triggers instant voice dictation from anywhere |

### ⚡ Speculative Concurrency Filtering

Dual-lane tool execution for maximum throughput with safety guarantees:

- **Tier 0 (Read-Only)**: `read_file`, `list_directory`, `search_web` — concurrent via `asyncio.gather()`.
- **Tier ≥ 1 (Mutating)**: `write_file`, `run_python`, `gui_click` — sequential transaction enforcement.

### 🛡️ Enterprise Security (`SEC-01`–`SEC-26`)

- Global `X-API-Key` auth middleware with explicit public whitelist.
- Per-endpoint rate limiting via `slowapi` (20/min chat, 10/min vault).
- Prompt injection sanitizer stripping jailbreak directives and zero-width unicode attacks.
- `MERIDIAN_ALLOW_HOST_CODE_EXEC` sandbox gate blocking un-sandboxed execution.

### 🛡️ Focus Distraction Blocker

Block distracting websites (`YouTube`, `Reddit`, `Twitter/X`, `Twitch`) and background processes (`discord.exe`, `steam.exe`) during Pomodoro focus blocks with active shield status.

### 📋 50-Slot Clipboard Surveillance & Multi-Column Grid

Real-time pastebuffer monitoring with 50 persistent slots, automatic URL/Code classification, 1-click prompt analysis, and SQLite WAL database persistence fallback.

### 🔊 Supertonic Speech & Voice Engine

Local text-to-speech engine featuring 10 distinct speaker voices (Male M1–M5, Female F1–F5), dynamic speech volume control, and audio state-change sound FX.

### 📈 Developer Productivity & Real Stats Engine

Queries live SQLite task logs and Git repository commits to calculate real metrics: `Success Rate`, `Heals Applied`, `Git Commits/Snapshots`, and `Pomodoros Completed`.

### 🌌 Ambient Particle Canvas & Low RAM Optimizer

Dynamic background particle renderer (`AmbientParticles.tsx`) with floating nodes & accent connections, featuring a 1-click **Low RAM Mode** toggle in Settings to conserve memory.

### ⚡ On-Device Turbovec Vector RAG & Knowledge Graph

Local semantic vector store (`Turbovec`) combined with entity-relationship knowledge graph memory for instant sub-millisecond retrieval without sending context to third parties.

### 🎨 11 Selectable Design Styles

Switch themes in **Settings → Mascot & Style** with live visual swatch previews & category filters (`All`, `Dark`, `Light`):

| Theme | Type | Key Accent | Typography |
| --- | --- | --- | --- |
| 🪐 Classic Cyber Slate | Dark | Solar Amber `#E8A020` | IBM Plex Mono |
| 🏛️ Art Deco Luxury | Dark | Metallic Gold `#D4AF37` | Playfair Display (Serif) |
| ⚡ Neobrutalism | **Light** | Canary Yellow `#FFDE59` | Space Grotesk |
| 🌆 Cyberpunk Neon | Dark | Neon Magenta `#FF0055` | Orbitron |
| 👾 Retro Synthwave | Dark | Hot Pink `#FF71CE` | VT323 (Pixel Mono) |
| 🖋️ Ink & Slate | Dark | Muted Indigo `#818CF8` | Inter |
| ❄️ Nordic Frost | Dark | Sky Blue `#38BDF8` | DM Sans |
| 🌈 Maximalism | Dark | Vibrant Pink `#FF007A` | Syne |
| 📜 Paper & Ink | **Light** | Terracotta Coral `#D95338` | Lora (Serif) |
| 🌸 Sakura Blossom | **Light** | Rose Quartz `#E85D75` | Outfit |
| ☀️ Solaris Light | **Light** | Cobalt Blue `#2563EB` | DM Sans |

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    subgraph Trigger["1️⃣ Trigger Layer"]
        direction LR
        U_UI["💬 Workspace Chat UI"]
        U_HUD["🎮 Overlay<br/>(Alt+Shift+M)"]
        U_VOICE["🎙️ Voice<br/>(Alt+V / Wake Word)"]
        U_CLIP["📋 Clipboard & File<br/>Watcher"]
    end

    subgraph Security["2️⃣ Security Gate"]
        AUTH["🛡️ Auth & Rate Limit<br/>(X-API-Key)"]
        SAN["🧹 Prompt Injection<br/>Sanitizer"]
        AUTH --> SAN
    end

    subgraph Context["3️⃣ Context Assembly"]
        subgraph CtxPar["Fetched in parallel"]
            direction LR
            VEC["⚡ Turbovec<br/>Vector RAG"]
            GRAPH["🕸️ Knowledge<br/>Graph"]
            HIST["📜 Conversation<br/>History"]
        end
        CTX["📦 Unified Prompt Context"]
        VEC --> CTX
        GRAPH --> CTX
        HIST --> CTX
    end

    subgraph Core["4️⃣ ReAct Reasoning"]
        LLM["🧠 Reason<br/>(User-Selected Local or Cloud Agent)"]
        CHECK{"❓ Schema & Syntax Valid?"}
        HEAL["🩹 Self-Heal<br/>Fixes Tool Signature Mismatch"]
        LLM --> CHECK
        CHECK -- "Invalid" --> HEAL --> LLM
    end

    subgraph Execution["5️⃣ Act — Tiered Execution"]
        ROUTER{"⚡ Concurrency Router"}
        subgraph Tier0["Tier 0 — Read-Only (parallel)"]
            direction LR
            T0a["read_file"]
            T0b["search_web"]
            T0c["fetch_url"]
        end
        subgraph Tier1["Tier 1+ — Mutating (sequential)"]
            direction LR
            T1a["write_file"] --> T1b["run_command"] --> T1c["gui_click"]
        end
        MCPX["🔌 MCP Servers<br/>(GitHub, Slack, Postgres, Linear)"]
        ROUTER --> Tier0
        ROUTER --> Tier1
        ROUTER -.->|"as needed"| MCPX
    end

    subgraph Output["6️⃣ Observe, Respond & Persist"]
        OBS["👁️ Observe<br/>merge tool results"]
        RESP["📝 Final Response"]
        TTS["🔊 Supertonic TTS<br/>(10 voices)"]
        VAULT[("🔐 AES-GCM Vault")]
        STORE[("💾 SQLite WAL + Turbovec")]
        SSE["📡 SSE Telemetry"]
        MASCOT["🦊 Mascot & Island<br/>(color + spin state)"]
    end

    U_UI & U_HUD & U_VOICE & U_CLIP --> AUTH
    SAN --> VEC
    SAN --> GRAPH
    SAN --> HIST
    CTX --> LLM
    CHECK -- "Valid" --> ROUTER

    Tier0 --> OBS
    Tier1 --> OBS
    MCPX --> OBS
    Tier1 -.->|"fetch creds"| VAULT
    OBS -->|"persist"| STORE
    OBS -->|"loop until task complete"| LLM
    OBS -->|"task complete"| RESP
    RESP --> TTS
    RESP --> U_UI

    LLM -.->|"live state"| SSE
    ROUTER -.->|"live state"| SSE
    OBS -.->|"live state"| SSE
    SSE --> MASCOT
    SSE --> U_UI
    SSE --> U_HUD

    classDef trigStyle fill:#818CF8,stroke:#4F46E5,color:#1E1B4B,stroke-width:1px
    classDef secStyle fill:#38BDF8,stroke:#0284C7,color:#0C1E2E,stroke-width:1px
    classDef ctxStyle fill:#67E8F9,stroke:#0891B2,color:#083344,stroke-width:1px
    classDef coreStyle fill:#A78BFA,stroke:#7C3AED,color:#1E1235,stroke-width:1px
    classDef parallelStyle fill:#4ADE80,stroke:#15803D,color:#052E16,stroke-width:1px
    classDef sequentialStyle fill:#FB923C,stroke:#C2410C,color:#2E1300,stroke-width:1px
    classDef outStyle fill:#FF71CE,stroke:#DB2777,color:#2E0A1A,stroke-width:1px
    classDef dbStyle fill:#FFDE59,stroke:#CA8A04,color:#1F1300,stroke-width:1px

    class U_UI,U_HUD,U_VOICE,U_CLIP trigStyle
    class AUTH,SAN secStyle
    class VEC,GRAPH,HIST,CTX ctxStyle
    class LLM,CHECK,HEAL,ROUTER,OBS,RESP coreStyle
    class T0a,T0b,T0c parallelStyle
    class T1a,T1b,T1c sequentialStyle
    class MCPX,TTS,SSE,MASCOT outStyle
    class VAULT,STORE dbStyle
```

### Architectural Layer Breakdown

| Layer | Technologies | Core Responsibility |
| :--- | :--- | :--- |
| **Presentation** | Tauri v2, React 18, Three.js, Lucide, Anime.js | Multi-window shell, 11-style theme switcher, responsive card grids, floating mascot island & HUD |
| **Orchestration** | FastAPI, asyncio, Pydantic v2 | ReAct agent loop, tool parameter auto-correction, speculative concurrency, SSE streaming |
| **Surveillance & Productivity** | Pyperclip, Watchdog, Distraction Shield | 50-slot persistent pastebuffer surveillance, website/process distraction blocker, Pomodoro HUD |
| **Security & Vault** | AES-256-GCM, Cryptography, SlowAPI | Machine-bound passphrase derivation, prompt injection sanitizer (SEC-16), rate limiting, host execution gates |
| **Storage & Memory** | Turbovec, SQLite WAL, MongoDB | On-device vector embeddings, persistent task histories, entity-relationship memory graph |
| **Inference & Voice** | Local / Cloud LLMs, Supertonic TTS | User-selected AI agents (Ollama, OpenAI, Anthropic, Gemini, Groq, OpenRouter) + local 10-voice speech synthesizer |

### 🚀 Non-Techie Onboarding Wizard

Plug-and-play guided setup for users with zero technical or LLM knowledge:

- **Hardware Spec Detection**: Automatically checks system RAM, CPU cores, and GPU VRAM to recommend the optimal offline model size (`Llama 3.2 1B`, `3B`, or `8B`).
- **Ollama Auto-Discovery & Port Probe**: Probes default `11434` port, alternative ports (`11435`, `8080`, `5000`), and process trees without manual user configuration.
- **1-Click Model Downloader**: Streams real-time download percentage and progress via SSE directly inside the setup modal.

### 🌐 Self-Hosting & Remote Backend Support

Deploy Meridian-X backend on a remote VPS or home server while running the desktop/web client anywhere:

- **Docker Compose Stack**: 1-command server spinup (`docker-compose up -d`) with isolated backend and Ollama containers.
- **Remote Server Switcher**: Configure custom API endpoint (e.g., `https://api.my-server.com`) and secure API Key in frontend settings.

---

### 🌐 Website Project Context

The official landing page and documentation portal for Meridian-X is maintained in the sister directory [`../meridian_website`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/meridian_website):

- Built with **React + Vite + Tailwind CSS**.
- Showcases interactive feature demos, documentation, downloadable binaries, and self-hosting guides.

---

## 💻 System Requirements

| Component | Minimum | Recommended |
| :--- | :--- | :--- |
| **CPU** | Intel i5 / Ryzen 5 (AVX2) | Intel i7 / Ryzen 7+ (8+ cores) |
| **RAM** | 8 GB | 16–32 GB DDR5 |
| **GPU / VRAM** | Intel Iris Xe / Radeon Vega | NVIDIA RTX 3060+ (8 GB+ VRAM) |
| **Storage** | 10 GB SSD | 30 GB+ NVMe |

> [!TIP]
> **No GPU?** Add a cloud API key (Gemini, OpenAI, Groq, etc.) in Settings to offload inference. Only audio preprocessing, DB indexing, and orchestration run locally — making even CPU-only hardware sufficient.

| OS | Status |
| :--- | :--- |
| **Windows 11** (64-bit) | ✅ Fully Supported |
| **macOS** (12+ Apple Silicon / Intel) | ✅ Fully Supported |
| **Linux** (Ubuntu / Debian / Arch / Fedora) | ✅ Fully Supported |

---

## 🛠️ Getting Started & Installation

### ⚡ One-Line Quick Install

#### 🪟 Windows (PowerShell)

```powershell
powershell -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/Aryan4132/Meridian-X/main/install.ps1 | iex"
```

#### 🐧 Linux & 🍎 macOS (Terminal)

```bash
curl -fsSL https://raw.githubusercontent.com/Aryan4132/Meridian-X/main/install.sh | bash
```

Or download pre-compiled installers directly from [GitHub Releases](https://github.com/Aryan4132/Meridian-X/releases):

- **Windows**: `meridian-x_0.4.0_x64-setup.exe` / `.msi`
- **Linux**: `meridian-x_0.4.0_amd64.AppImage` / `.deb`

> [!NOTE]
> **macOS Gatekeeper Warning ("App is damaged and can't be opened"):**
> Unsigned macOS builds downloaded from browsers trigger Apple Gatekeeper security. Fix with one command:
> ```bash
> sudo xattr -r -d com.apple.quarantine /Applications/meridian-x.app
> ```
> *(Or if installed in Downloads: `sudo xattr -r -d com.apple.quarantine ~/Downloads/meridian-x.app`)*

---

### Run from Source

**Prerequisites:** Python 3.10+, Node.js, Rust toolchain, Ollama.

#### 1. Pull Ollama Models

```bash
# Minimum (8 GB RAM / CPU-only)
ollama pull qwen2.5-coder:1.5b-instruct
ollama pull moondream:1.8b
ollama pull nomic-embed-text

# Recommended (16 GB+ / Dedicated GPU)
ollama pull qwen2.5-coder:7b-instruct-q4_K_M
ollama pull llama3.2-vision:11b
ollama pull nomic-embed-text
```

#### 2. Configure `.env`

Create `meridian_backend/.env`:

```env
OLLAMA_HOST=http://127.0.0.1:11434
MERIDIAN_MODEL=qwen2.5-coder:7b-instruct-q4_K_M
P2P_SECRET_TOKEN=your-secure-token

# Optional Cloud Keys (Hybrid Mode)
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=AIzaSy...
GROQ_API_KEY=gsk_...
```

#### 3. Launch

```bash
# Windows — one command
start_meridian.bat

# Or separately
# Backend
cd meridian_backend && python api.py

# Frontend
cd meridian_frontend && npm install && npm run tauri dev
```

---

## 🔍 Troubleshooting

<details>
<summary><b>Ollama Unreachable</b></summary>

Verify Ollama is running: open `http://127.0.0.1:11434` — should return `"Ollama is running"`.
Update `OLLAMA_HOST` in `.env` if using a non-default port.

```bash
ollama pull nomic-embed-text
ollama pull qwen2.5-coder:7b-instruct-q4_K_M
```

</details>

<details>
<summary><b>SQLite Database Locked</b></summary>

WAL mode is enabled automatically. If `sqlite3.OperationalError: database is locked` persists, kill ghost processes:

```powershell
Get-Process -Name python | Stop-Process -Force
```

</details>

<details>
<summary><b>High RAM/CPU & Lag</b></summary>

Switch to a smaller model in **Settings** or `.env`:

| Hardware | Brain Model | Vision Model |
| :--- | :--- | :--- |
| 8 GB / No GPU | `qwen2.5-coder:1.5b` | `moondream:1.8b` |
| 16 GB / 6 GB VRAM | `qwen2.5-coder:7b-q4` | `moondream:1.8b` |
| 32 GB+ / 12 GB+ VRAM | `qwen2.5-coder:14b` | `llama3.2-vision:11b` |

</details>

<details>
<summary><b>Microphone / Wake Word Not Working</b></summary>

1. Check OS mic permissions: **Settings → Privacy → Microphone**.
2. Run `python verify_system.py` to inspect audio devices.
3. Set input to `1 channel, 16-bit, 16000 Hz` in OS audio settings.

</details>

<details>
<summary><b>MongoDB Offline</b></summary>

Meridian-X gracefully degrades — core functions continue without MongoDB; only knowledge graph sync is skipped.

- **Windows**: `services.msc` → Start `MongoDB Server`
- **Linux/macOS**: `sudo systemctl start mongod`

</details>

---

## 🎗️ Credits

- **[Turbovec](https://github.com/RyanCodrai/turbovec)** — High-performance local vector database.
- **[Ollama](https://github.com/ollama/ollama)** — Offline local model deployments and embeddings.
- **[Tauri](https://github.com/tauri-apps/tauri)** — Secure, lightweight desktop frontend wrapper.
- **[FastAPI](https://github.com/fastapi/fastapi)** — Async Python backend, scheduler, and SSE telemetry.
- **[Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)** — Fast on-device voice transcription.
- **[Tavily](https://tavily.com)** — LLM-optimized web search engine.

---

## 🤝 Contributing

1. Fork the repository
2. Create your branch: `git checkout -b feature/my-feature`
3. Commit: `git commit -m 'feat: add my feature'`
4. Push & open a Pull Request

---

<div align="center">

© 2026 Built by **Aryan** · Meridian-X

</div>
