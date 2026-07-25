# 📌 Meridian-X — Project Kanban Board

Last Updated: 2026-07-25

---

## 📋 Backlog (Future & Enhancements)

| ID | Task Name | Priority | Category | Target File(s) | Notes / Acceptance Criteria |
|---|---|---|---|---|---|
*(All 100% backlog items complete!)*

---

## 🎯 Planned (Proactive Multimodal Sprint)

| ID | Task Name | Priority | Category | Target File(s) | Acceptance Criteria |
|---|---|---|---|---|---|
| **PL-01** | **Facial Recognition & Presence Engine** | 🔴 High | Vision/AI | `meridian_backend/src/core/vision_face.py` | Real-time user presence, face recognition embeddings, and emotion tracking via MediaPipe/OpenCV. |
| **PL-02** | **Continuous Ambient Listener** | 🔴 High | Audio/STT | `meridian_backend/src/voice/ambient_listener.py` | Background VAD with `webrtcvad` + continuous `faster-whisper` transcription stream. |
| **PL-03** | **Real-Time Screen & Window Sense** | 🔴 High | Vision/Context | `meridian_backend/src/core/screen_sense.py` | Active window metadata tracking + vision LLM automated screen parsing on app switch/error. |
| **PL-04** | **Proactive Nudge Engine Expansion** | 🔴 High | Intelligence | `meridian_backend/src/core/proactive.py` | Event-driven context synthesis combining face, sound, screen, and system metrics. |
| **PL-05** | **Frontend Perception HUD & Hardware Toggles** | 🟡 Medium | UI/UX | `meridian_frontend/src/components/PerceptionHUD.tsx` | Visual webcam/mic indicators and hardware mute switches in `NavRail.tsx`. |

---

## ⏳ In Progress

| ID | Task Name | Priority | Category | Target File(s) | Assignee / Status |
|---|---|---|---|---|---|
*(No active items — ready to begin Proactive Multimodal Sprint)*

---

## ✅ Completed (Done)

| ID | Task Name | Priority | Category | Date Completed | Key Outcome |
|---|---|---|---|---|---|
| **BK-25** | **Temporal Memory Graph Engine** | 🟡 Medium | Memory / Graph | 2026-07-25 | Time-aware knowledge graph tracking entity states, timestamped relationships, and exponential time-decay scoring in `temporal_memory.py`. |
| **BK-24** | **RAG Pipeline Context & Reranking Optimizer** | 🔴 High | Memory / RAG | 2026-07-25 | Hybrid dense-sparse BM25 retrieval, top-k relevance reranking, and noise reduction in `rag_optimizer.py`. |
| **BK-23** | **Reusable System Prompt & Tool Definition Library** | 🟡 Medium | AI Engine / Prompts | 2026-07-25 | Role-based system prompt template renderer and reusable tool JSON schemas in `prompt_templates.py`. |
| **BK-22** | **Active MCP Tool Execution Engine** | 🔴 High | Integration / Tools | 2026-07-25 | Async MCP tool discovery, execution state tracking, and JSON-RPC formatting in `mcp_executor.py`. |
| **BK-21** | **User-Configurable Token Context Limit UI & Backend Enforcement** | 🔴 High | AI Engine / UI | 2026-07-25 | Customizable context token limit controls (4k-128k, Custom) in `Settings.tsx` and dynamic budget enforcement in `loop.py`. |
| **BK-20** | **Custom ONNX Wake Word File Browser UI & Backend Scanner** | 🔴 High | Voice / UI | 2026-07-25 | Native OS file picker dialog & backend `.onnx` model scanner for custom wake words in `Settings.tsx` & `wakeword.py`. |
| **MC-01** | **Custom MCP Server Registration & Manager UI** | 🔴 High | Integration / UI | 2026-07-25 | Dynamic custom MCP server form (Name, Cmd, Args, Env), active server list, and `mcp_config.json` persistence. |
| **VK-02** | **Categorized API Key Navigation (AI Models & Voice Tabs)** | 🔴 High | UI/UX / AI | 2026-07-25 | Dedicated API key controls for Groq/OpenRouter/Mistral in AI Models tab, ElevenLabs/Deepgram in Voice tab, and secret vault integration. |
| **BK-19** | **Sub-10ms Frameless Game Overlay (`Alt+Space`)** | 🟢 Low | UI/UX | 2026-07-24 | Frameless transparent HUD component (`GameOverlay.tsx`) for full-screen games. |
| **BK-18** | **Event-Action Workflow Automation Engine** | 🟡 Medium | Automation | 2026-07-24 | Background metric trigger rules & automated action evaluator in `triggers.py`. |
| **BK-17** | **One-Click MCP Server Registry UI** | 🟡 Medium | Integration | 2026-07-24 | Dynamic catalog & installer for MCP servers (GitHub, Postgres, Linear, Slack) in `mcp_marketplace.py`. |
| **BK-16** | **Zero-Trust Noise Protocol P2P & Biometric Vault** | 🔴 High | Security/P2P | 2026-07-24 | ECDH key exchange & biometric enclave unlock fallbacks in `p2p_crypto.py`. |
| **BK-15** | **Model Benchmarker & Hardware Governor** | 🔴 High | System/AI | 2026-07-24 | Startup TTFT/tokens-sec benchmark probe & RAM/GPU thermal throttle governor in `governor.py`. |
| **BK-14** | **Global Spotlight Command Palette (`Cmd+K`)** | 🟢 Low | UI/UX | 2026-07-24 | Spotlight search modal component (`CommandPalette.tsx`) with fuzzy action execution. |
| **BK-13** | **Codebase Symbol AST Graph & RAG Indexer** | 🟡 Medium | Memory/RAG | 2026-07-24 | AST symbol relationship graph parser & background sleep-cycle memory consolidation in `graph_rag.py`. |
| **BK-12** | **Autonomous Playwright Web Browser Agent** | 🟡 Medium | Web/Tools | 2026-07-24 | Playwright browser agent tool (`browser_agent.py`) for page navigation & form interaction. |
| **BK-11** | **Real-Time Full-Duplex Voice & Barge-In** | 🔴 High | Voice | 2026-07-24 | Low-latency streaming STT/TTS pipeline with real-time speech interruption in `duplex.py`. |
| **BK-10** | **Multi-Agent Swarm Orchestration** | 🔴 High | Multi-Agent | 2026-07-24 | Spawns concurrent subagents (researcher, auditor, browser) via `asyncio.gather()` with report synthesis. |
| **BK-09** | **Background Noise Gate & Audio Thresholding** | 🔴 High | Audio | 2026-07-24 | Dynamic RMS spectral noise floor filter & attenuation in `stt.py`. |
| **BK-08** | **Structured `<thought>` Introspection Persistence** | 🟡 Medium | Agent Loop | 2026-07-24 | SQLite `thought_logs` table schema and SSE thought emitter hook. |
| **BK-07** | **Zeroconf/mDNS P2P LAN Discovery** | 🟡 Medium | Networking | 2026-07-24 | mDNS `zeroconf` service registration/discovery with UDP fallback in `p2p.py`. |
| **BK-04** | **Speaker Pitch Centroid Filtering** | 🟢 Low | Audio | 2026-07-24 | Pitch frequency ($F_0$) centroid tracker ($80\text{ Hz}-350\text{ Hz}$) in `stt.py`. |
| **VK-01** | **Universal Encrypted Secret Vault System** | 🔴 High | Security / AI | 2026-07-23 | Dynamic key manager in Settings with AES-GCM vault encryption & automatic Groq/OpenRouter/Mistral/SerpAPI resolution. |
| **IP-01** | Top-Left Mascot Logo Integration | 🔴 High | UI/UX | 2026-07-23 | Replaced SVG logo with glowing interactive `<MascotCharacter />` in `NavRail.tsx` (verified `npm run build`). |
| **IP-02** | CodeGraph Indexing & Symbol Sync | 🟡 Medium | DX / Tooling | 2026-07-23 | AST knowledge graph synchronization for workspace symbols. |
| **CB-01** | **Clipboard AI Analysis & Chatbot Routing** | 🟡 Medium | UX / Feature | 2026-07-23 | Routed automated clipboard monitoring analysis to main chatbot view with interactive copy controls. |
| **BK-01** | Split `loop.py` Monolith into Sub-modules | 🔴 High | Architecture | 2026-07-23 | Extracted `loop_parser.py`, `loop_dispatcher.py`, and `loop_stream.py`. |
| **BK-02** | Vault PBKDF2 to Argon2id Key Derivation | 🟡 Medium | Security | 2026-07-23 | Upgraded vault key derivation to `Argon2id` with PBKDF2 fallback. |
| **BK-03** | Persist P2P Peer List to SQLite | 🔴 High | Networking | 2026-07-23 | SQLite peer persistence table and health ping pruning daemon. |
| **BK-05** | Adaptive Token Budget Tracker & Context Trimming | 🔴 High | AI Engine | 2026-07-23 | Heuristic token estimator and history sliding-window budget trimmer in `loop_stream.py`. |
| **BK-06** | Vault Access Audit Logger | 🔴 High | Security | 2026-07-23 | Auditing read/write events via `audit_logger.py`. |
| **DN-01** | ReAct Reasoning Loop (`loop.py`) | 🔴 High | Core Engine | 2026-07-20 | Multi-step tool use, SSE streaming, syntax checks, self-correction. |
| **DN-02** | Voice Engine (STT & TTS & WakeWord) | 🔴 High | Audio | 2026-07-21 | Whisper STT, Edge/Coqui TTS, "Hey Meridian" wake word detection. |
| **DN-03** | Encrypted Vault (`vault.py`) | 🔴 High | Security | 2026-07-19 | AES-GCM credential & API key encryption. |
| **DN-04** | Discord & Telegram Bridges | 🟡 Medium | Messaging | 2026-07-22 | Bot integrations for remote command & control. |
| **DN-05** | Screen Vision Capture (`vision.py`) | 🟡 Medium | Vision | 2026-07-22 | On-demand screen capture via `mss`/`pyautogui` to Ollama Vision models. |
| **DN-06** | System Metrics Proactive Monitor | 🟡 Medium | Monitoring | 2026-07-22 | Background CPU/RAM/Disk anomaly alerts and idle checks. |
| **DN-07** | Vector Memory & RAG Pipeline | 🔴 High | Memory | 2026-07-18 | SQLite + ChromaDB memory vector storage. |
