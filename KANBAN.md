# 📌 Meridian-X — Project Kanban Board

Last Updated: 2026-07-23

---

## 📋 Backlog (Future & Enhancements)

| ID | Task Name | Priority | Category | Target File(s) | Notes / Acceptance Criteria |
|---|---|---|---|---|---|
| **BK-04** | Speaker Diarization in Voice Engine | 🟢 Low | Audio | `meridian_backend/src/voice/` | Distinguish user voice from background voices/audio. |
| **BK-07** | Zeroconf/mDNS P2P LAN Discovery | 🟡 Medium | Networking | `meridian_backend/src/core/p2p.py` | Replace raw UDP broadcasts with `zeroconf` service discovery. |

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
| **VK-01** | **Universal Encrypted Secret Vault System** | 🔴 High | Security / AI | 2026-07-23 | Dynamic key manager in Settings with AES-GCM vault encryption & automatic Groq/OpenRouter/Mistral/SerpAPI resolution. |
| **IP-01** | Top-Left Mascot Logo Integration | 🔴 High | UI/UX | 2026-07-23 | Replaced SVG logo with glowing interactive `<MascotCharacter />` in `NavRail.tsx` (verified `npm run build`). |
| **IP-02** | CodeGraph Indexing & Symbol Sync | 🟡 Medium | DX / Tooling | 2026-07-23 | AST knowledge graph synchronization for workspace symbols. |
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
