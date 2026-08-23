# 📌 Meridian-X — Project Kanban Board

Last Updated: 2026-08-23

> **Status legend:** 🔴 High · 🟡 Medium · 🟢 Low — items move **Planned → In Progress → Completed** only after test-verified implementation.

---

## 📋 Backlog (Unscheduled Ideas)

*Butler ideas captured but **not yet scheduled** — promote to Planned when a sprint frees up. All verified missing on 2026-08-23.*

| ID | Idea | Priority | Category |
|---|---|---|---|
| **BUTLER-15** | Medication & Refill Sentinel (dose schedules, refill countdowns, local-only) | 🔴 High | Butler / Health |
| **BUTLER-22** | Screen Time & Deep Work Report (weekly focus analytics from PL-03) | 🟡 Medium | Butler / Attention |
| **BUTLER-16** | Meal Planner & Recipe Butler (pantry-aware, one-tap grocery add) | 🟡 Medium | Butler / Home |
| **BUTLER-18** | Habit Streaks & Goal Tracker (weekly reviews from journal/task data) | 🟡 Medium | Butler / Habits |
| **BUTLER-17** | Sleep & Bedtime Coach (wind-down preset, consistency score) | 🟢 Low | Butler / Health |
| **BUTLER-19** | Tax Document Collector (year-round categorized bucket → January export pack) | 🟢 Low | Butler / Finance |
| **BUTLER-21** | Package Delivery Tracker (shipping-email parse → delivery-day alert + doorbell cam check) | 🟢 Low | Butler / Logistics |
| **BUTLER-28** | Multi-Profile & Guest Mode (isolated personas, auto-wipe guest sessions) | 🟢 Low | Platform |

> *SEC-42/43 were promoted from this Backlog to Planned → Day 22 on 2026-08-23.*

---

## 🎯 Planned (Active Sprint Roadmap & Core Architecture)

*Only genuinely unimplemented work remains here — all Day 1–6 deliverables have been verified on disk/tested and moved to Completed.*

| ID | Task Name | Priority | Category | Target File(s) | Acceptance Criteria |
|---|---|---|---|---|---|
| **PL-08** | **Multi-Provider RAG Vector Embeddings Pipeline** | 🔴 High | Memory/RAG | `meridian_backend/database.py` | OpenAI `text-embedding-3-small` and in-memory CPU fallback (`fastembed`) when local Ollama `nomic-embed-text` is offline. |
| **PL-09** | **Multi-Cloud Vault Fallback Chain** | 🟡 Medium | AI Engine | `meridian_backend/src/core/llm_provider.py` | Automated failover across vault API keys (Primary Cloud → Secondary Cloud → Local Ollama). |
| **PL-11** | **Hybrid Sparse-Dense RAG & AST Code Chunking** | 🔴 High | RAG/Memory | `meridian_backend/src/core/doc_indexer.py` | BM25 keyword matching + Turbovec dense vectors + AST function/class boundary chunking. |
| **PL-17** | **Native Pure-Python PDF Layout & Table Extractor** | 🔴 High | RAG/Memory | `meridian_backend/src/tools/documents.py`, `doc_indexer.py` | Pure-Python XY-Cut reading-order sort and bounding-box table parser for RAG indexing without Java. |
| **PL-01** | **Facial Recognition & Presence Engine** | 🔴 High | Vision/AI | `meridian_backend/src/core/vision_face.py` | Real-time presence, face-recognition embeddings, emotion tracking via MediaPipe/OpenCV. |
| **PL-02** | **Continuous Ambient Listener** | 🔴 High | Audio/STT | `meridian_backend/src/voice/ambient_listener.py` | Background VAD (`webrtcvad`) + continuous `faster-whisper` transcription stream. |
| **PL-03** | **Real-Time Screen & Window Sense** | 🔴 High | Vision/Context | `meridian_backend/src/core/screen_sense.py` | Active-window metadata tracking + vision-LLM screen parsing on app switch/error. |
| **PL-04** | **Proactive Nudge Engine Expansion** | 🔴 High | Intelligence | `meridian_backend/src/core/proactive.py` | Event-driven context synthesis combining face, sound, screen, and system metrics. |
| **PL-05** | **Frontend Perception HUD & Hardware Toggles** | 🟡 Medium | UI/UX | `meridian_frontend/src/components/PerceptionHUD.tsx`, `NavRail.tsx` | Webcam/mic indicators and hardware mute switches. |
| **PL-06** | **Provider-Aware Multimodal Screen Vision** | 🔴 High | Vision/AI | `meridian_backend/src/core/vision.py` | Route screen captures to GPT-4o / Gemini Flash / Claude Sonnet when API keys are active. |
| **PL-29** | **Vision Motion & Hand Gesture Control Sentinel** | 🔴 High | Vision/AI | `meridian_backend/src/core/vision_gesture.py` | Hand-gesture recognizer (thumbs-up approve, open-palm stop, wave/swipes) + desk motion tracker. |
| **JARVIS-02** | **Eye-Tracking & Spatial Gaze Control Sentinel** | 🔴 High | Vision/Perception | `meridian_backend/src/core/gaze_tracker.py` | MediaPipe Iris gaze tracker for hands-free window selection & gaze-based dimming. |
| **JARVIS-04** | **Predictive Action Pre-Execution & Context Pre-Warmer** *(partial: habit model groundwork exists in `perception.py`)* | 🔴 High | Intelligence | `meridian_backend/src/core/predictive_engine.py` | Habit model pre-warms LLM context, opens dev tools, pre-scaffolds git diffs. |
| **JARVIS-05** | **Smart Camera & RTSP Security Vision Sentinel** | 🟡 Medium | Vision/Security | `meridian_backend/src/core/camera_sentinel.py` | RTSP object detector notifying room entry, deliveries, or unknown visitors. |
| **JARVIS-06** | **Room Arrival Auto-Briefing & Voice Synthesizer** | 🟡 Medium | Voice/Assistant | `meridian_backend/src/core/presence_briefing.py` | Presence-triggered 15-second executive voice report upon entering workspace. |
| **JARVIS-08** | **Dynamic AR Smart Glasses & Headset Mirroring Bridge** | 🟡 Medium | AR/Hardware | `meridian_backend/src/core/ar_bridge.py` | WebSocket HUD streaming for XREAL, Meta Ray-Ban, Apple Vision Pro. |
| **ECO-01** | **Mobile Companion App & QR P2P Sync** | 🔴 High | Cross-Device | `meridian_backend/src/core/p2p.py` | QR pairing, mobile voice-command relay, phone camera video ingestion. |
| **FIN-03** | **Real-Time Financial News Sentiment & Stock Sentinel** | 🔴 High | Personal Finance | `meridian_backend/src/core/finance_sentinel.py` | News sentiment classifier + hybrid stock trend forecasting engine. |
| **PL-10** | **Heterogeneous Subagent Model Binding** | 🟡 Medium | Multi-Agent | `meridian_backend/src/core/swarm.py` | Role-based subagent model binding (DeepSeek Coder → Auditor, Gemini Flash → Researcher). |
| **SYS-01** | **Smart Workspace Window Auto-Organizer** | 🟡 Medium | System Automation | `meridian_backend/src/core/workspace_layout.py` | Auto-arrange editor/terminal/browser/HUD windows into Dev, Research, Review presets. |
| **JARVIS-10** | **Multi-Lingual Whisper & Real-Time Code Polyglot** | 🟡 Medium | Voice | `meridian_backend/src/voice/polyglot.py` | 50+ language real-time speech-to-code translator. |
| **PL-13** | **Mascot Visor Expressions & Micro-Emotions** | 🟡 Medium | UI/Mascot | `meridian_frontend/src/Mascot.tsx` | Dynamic SVG visor eyes (`^ _ ^`, `> _ <`, `- _ -`) + sleeping Zzz particles. |
| **PL-14** | **Mascot Real-Time Voice Audio Visualizer** | 🟡 Medium | UI/Audio | `meridian_frontend/src/Mascot.tsx` | Circular 8-bar equalizer reacting to STT/TTS frequencies. |
| **PL-15** | **Agent Loop Action Auras for Mascot** | 🟡 Medium | UI/Agent | `meridian_frontend/src/Mascot.tsx` | Action-specific auras (browsing particles, vision sonar, auditing shield). |
| **PL-16** | **Desktop Floating Pet Edge-Snapping & Drag Physics** | 🟢 Low | UI/Desktop | `meridian_frontend/src/Mascot.tsx` | Edge-snapping, drag physics, click reactions for floating pet mode. |
| **PL-19** | **Collapsible Timeline Step Accordions & Diff Preview** | 🟡 Medium | UI/UX | `meridian_frontend/src/views/Timeline.tsx` | Collapsible agent step accordions + syntax-highlighted diff previews. |
| **PL-20** | **Active Brain Model & Execution Mode Header Pill** | 🟡 Medium | UI/UX | `StatusBar.tsx`, `NavRail.tsx` | Persistent badge showing loaded model + Local vs Cloud/API mode. |
| **PL-21** | **Command Palette View Navigation & Action Toggles** | 🟢 Low | UI/UX | `CommandPalette.tsx` | Ctrl+K palette view switching, mode toggles, shortcut hints. |
| **PL-22** | **Inline Connection & API Key Health Checks** | 🟡 Medium | UI/UX | `Settings.tsx` | Live status badges for Ollama ping + vault key validation in Settings. |
| **PL-27** | **Anime.js UI Animation Integration** | 🟡 Medium | UI/UX | `meridian_website/package.json`, `src/` | Anime.js timelines, SVG morphing, staggered transitions across website components. |

### 🎯 Planned — Butler, Cyber-Defense & Calling Expansion *(priority-ordered)*

#### 🔴 High

| ID | Task Name | Category | Target File(s) | Acceptance Criteria |
|---|---|---|---|---|
| **SEC-36** | **Local Malware Scanner & Download Inspector** | Security/Malware | `malware_scanner.py`, `tools/filesystem.py` | Signature + heuristic engine (YARA-style rules, ClamAV fallback) scanning downloads/files/USB on insertion; encrypted quarantine; hash-reputation lookup. |
| **SEC-37** | **Real-Time Process Behavior Monitor (EDR-Lite)** | Security/System | `behavior_monitor.py`, `system_defense.py` | Detect process-injection patterns, crypto-miner signatures, mass file-handle access, suspicious child chains → auto-quarantine via JARVIS-07. |
| **SEC-38** | **Persistence & Autoruns Sentinel** | Security/System | `persistence_sentinel.py`, `watcher.py` | Baseline registry Run keys / scheduled tasks / services / startup folders / browser extensions; alert + one-click rollback on new persistence entries. |
| **SEC-34** | **Emergency Lockdown Mode** | Security/System | `emergency_lockdown.py`, `system_defense.py` | One voice/command trigger: lock workstation, mute mic, disable cameras, isolate network adapters, freeze vault; PIN/biometric unlock; audit-logged. |
| **TRUST-01** | **Memory Editor UI ("What do you remember?")** | Trust/AI | `memory_editor.py`, `MemoryEditor.tsx`, `temporal_memory.py` | Searchable window into everything Meridian remembers; edit/delete/"forget this"; JSON export — GDPR-style brain transparency. |
| **TRUST-02** | **Tool-Use Regression Suite** | Trust/CI | `tests/tool_scenarios.yaml`, `.github/workflows/ci.yml` | Scripted NL scenarios asserting correct tool selection + args through `loop.py`; CI gate pre-release so refactors can't break routing. |
| **OPS-01** | **Self-Updater with Safe Swap & Changelog** | Platform/Reliability | `updater.py`, `.github/workflows/release.yml` | Version check → download → verify signature → swap binaries → restart with rollback on failed health probe; in-app changelog. |
| **KNOW-01** | **Downloads Janitor** | Files/Automation | `file_janitor.py`, `tools/filesystem.py` | Auto-sort downloads by type/date, duplicate hash finder, age-out rules with review-before-delete; nightly summary nudge. |
| **FIT-01** | **Wearable Health Data Ingestion** | Health/Integration | `health_ingest.py`, `proactive.py` | Google Fit / Apple Health / smartwatch steps + sleep feeding wellness score and morning-briefing "readiness" line. |
| **SEC-31** | **Ransomware Canary & File Integrity Watcher** | Security/Files | `fim_sentinel.py`, `watcher.py` | Honeypot files + hash baselines on Documents/Desktop; mass-modify tripwire → process quarantine (JARVIS-07 hook), emergency snapshot, toast alert. |
| **CALL-01** | **VoIP Phone Agent Bridge** | Communication/Voice | `tools/phone_agent.py`, `voice/duplex.py` | Twilio/SIP trunk bridging live calls through duplex STT/TTS loop; `make_phone_call` tool with goal-driven conversation loop and hang-up detection. |
| **CALL-02** | **AI Call Screener & Receptionist** | Communication/Voice | `tools/phone_agent.py` | Answers unknown numbers; spam/human/priority classification; message taking; starred-caller passthrough; live transcript to UI. |
| **BUTLER-11** | **Routine Composer** | Butler/Automation | `routine_composer.py`, `WorkflowBuilder.tsx` | "Record this" demo capture chaining existing tools/presets into named routines; NL editing; voice triggers ("start my morning routine"). |
| **BUTLER-13** | **Quiet Hours & DND Governor** | Butler/Notifications | `proactive.py`, `database.py` | Sleep schedule, calendar-aware auto-DND, critical-only breakthrough rules, per-channel silencing. |
| **SEC-30** | **Phishing & Link Reputation Guard** | Security/Web | `tools/web_browser.py`, `external_connectors.py` | Pre-click URL reputation + heuristics scan; Gmail connector link scanning; sandboxed screenshot preview of suspicious pages. |
| **SEC-28** | **Breach & Leak Sentinel** | Security/Identity | `breach_sentinel.py` | HIBP k-anonymity email checks, periodic re-scan, exposed-credential rotation prompts, dark-web keyword watch. |
| **CALL-03** | **Post-Call Intelligence** | Communication/AI | `voice/duplex.py`, `database.py` | Auto-transcription → speaker-labeled summary → action items → optional calendar follow-up (extends AST-14 to phone calls). |
| **BUTLER-02** | **Personal CRM & Occasion Sentinel** | Butler/Memory | `personal_crm.py`, `proactive.py` | People graph (birthdays, anniversaries, last-contact); occasion nudges + LLM gift ideas 3 days ahead; silent-VIP follow-up alerts. |
| **BUTLER-04** | **Travel Butler & Leave-By Briefing** | Butler/Travel | `travel_butler.py`, `tools/web.py` | NL trip creation, itinerary from Gmail confirmations, leave-by commute calc via `geo_location.py`, travel-day voice briefing. |
| **BUTLER-06** | **Document Expiry Vault Sentinel** | Butler/Security | `expiry_sentinel.py`, `tools/documents.py` | Passport/ID/insurance/warranty/domain registry with 30/14/7/1-day escalation via proactive notifications. |

#### 🟡 Medium

| ID | Task Name | Category | Target File(s) | Acceptance Criteria |
|---|---|---|---|---|
| **SEC-32** | **Built-in TOTP 2FA Generator** | Security/Vault | `tools/vault.py`, `Settings.tsx` | Vault-stored RFC-6238 seeds, one-tap code copy, expiry countdown UI. |
| **SEC-35** | **Password Health Auditor** | Security/Vault | `tools/vault.py`, `security_auditor.py` | Strength/reuse/age audit with breach-corpus cross-check; weak-password report card. |
| **SEC-29** | **Network Guardian** | Security/Network | `network_guardian.py` | New-LAN-device alerts, ARP-spoof detection, per-process outbound monitor, open-port sweep feeding JARVIS-07. |
| **CALL-04** | **Emergency SOS Voice Protocol** | Voice/Safety | `sos_protocol.py`, `geo_location.py` | Wake-phrase SOS: location share via WhatsApp/Telegram, siren, fake-call decoy. |
| **BUTLER-26** | **Memory Time Machine** | Trust/Data | `memory_backup.py`, `vault.py` | Encrypted scheduled snapshots of DB + vault + memory graphs; diffable restore points; one-click rollback. |
| **BUTLER-24** | **Email Zero Triage** | Productivity/Email | `external_connectors.py`, `api.py` | Needs-reply/FYI/noise classifier, reply drafts in user's voice, unsubscribe suggestions, batch UI. |
| **BUTLER-23** | **Meeting Prep Briefing** | Assistant/Calendar | `proactive.py`, `oauth_manager.py` | T-minus-10-min cards: attendee CRM profile, last-thread summary, talking points. |
| **BUTLER-25** | **Voice Thought Bucket** | Capture/Memory | `voice/wakeword.py`, `temporal_memory.py` | "Note: …" instant capture anywhere, auto-tagging, contextual resurfacing via RAG. |
| **CALL-05** | **WhatsApp Voice Call Bridge** | Communication | `whatsapp_manager.py` | Playwright session extended for WhatsApp voice calls: dial by alias, live transcript. |
| **BUTLER-14** | **Undo & Action Journal** | Trust/UX | `loop_dispatcher.py`, `Timeline.tsx` | Every tool call journaled with reversible flag; "undo that" executes inverse for supported actions. |
| **SEC-33** | **USB & Peripheral Watchdog** | Security/Hardware | `usb_watchdog.py` | New USB device alerts, HID keystroke-burst (BadUSB) detection, trusted-device allowlist. |
| **SEC-39** | **DNS Filter & Web Shield** | Security/Network | `dns_shield.py`, `tools/web_browser.py` | Malicious-domain blocklist with auto-updates, DNS-over-HTTPS enforcement, hosts-file hijack detection, per-app domain blocking. |
| **SEC-40** | **Webcam & Mic Access Guard** | Security/Privacy | `cam_guard.py`, `PerceptionHUD.tsx` | Per-process camera/mic access monitoring, unknown-process block + toast alert, indicator sync with PL-05 HUD. |
| **SEC-41** | **Email Attachment Detonation Sandbox** | Security/Email | `external_connectors.py`, `sandbox_runner.py` | Detonate inbound attachments in SEC-27 sandbox pre-delivery; behavioral verdict (persistence? encryption? C2 callback?) attached to email. |
| **TRUST-03** | **Cloud Spend & Token Meter** | Trust/Cost | `llm_provider.py`, `Settings.tsx` | Per-provider token/cost dashboard, monthly budget caps, auto-downgrade to local Ollama on overspend. |
| **KNOW-02** | **Screenshot Memory** | Knowledge/RAG | `screenshot_memory.py`, `doc_indexer.py` | Auto-captured screenshots OCR-indexed into RAG ("that error I saw Tuesday"), retention window, instant recall. |
| **KNOW-03** | **Universal Search Hub** | Knowledge/Search | `search_hub.py`, `CommandPalette.tsx` | One query fusing RAG docs, code-graph symbols, chat history, screenshots, clipboard history, and files; keyboard-first UI. |
| **OPS-04** | **Local-Only Mode Switch** | Platform/Privacy | `mode.py`, `security_middleware.py` | Single audited toggle blocking every outbound cloud/API call; Settings shows live proof-of-enforcement badge. |
| **FIN-04** | **Wishlist Price Watcher** | Finance/Shopping | `price_watcher.py`, `tools/web_browser.py` | Track product pages for drops with price-history sparklines; proactive alert + buy deep link. |
| **CAR-01** | **Car Logbook & Service Predictor** | Butler/Vehicle | `car_logbook.py`, `documents.py` | Fuel/service/expense entries, mileage-based service predictions, insurance tie-in with BUTLER-06 expiry ladder. |
| **FAM-01** | **Shared Family Board** | Butler/Family | `family_board.py`, `database.py` | Role-based shared lists/calendar/shopping (BUTLER-05 beyond solo), WhatsApp broadcast updates. |
| **OPS-02** | **Multi-Machine State Sync** | Platform/Sync | `p2p.py`, `memory_backup.py` | Encrypted delta-sync of settings + memory graphs between desktops over existing P2P (ECO-01 is phone-only). |
| **OPS-03** | **Butler Skill Plugin SDK** | Platform/Extensibility | `plugins.py`, `docs/PLUGIN_SDK.md` | Signed third-party butler-skill packages: manifest, permission tiers, sandboxed install via marketplace. |
| **MED-01** | **Photo Organizer & Memories** | Media/AI | `photo_organizer.py`, `vision_face.py` | Dedupe, face-tagged albums (PL-01 embeddings), auto-albums, "on this day" resurfacing. |
| **BUTLER-03** | **Wellness & Ergonomics Butler** | Butler/Health | `wellness.py`, `proactive.py` | Hydration/posture/eye-strain/stretch micro-breaks respecting Focus Guard + throttling; daily wellness score. |
| **BUTLER-05** | **Household Ops: Grocery, Pantry & Chore Tracker** | Butler/Home | `household.py`, `database.py` | NL list capture, low-stock pantry suggestions, chore rotations, WhatsApp-shared shopping lists. |
| **BUTLER-07** | **Evening Wind-Down & Daily Review** | Butler/Reflection | `proactive.py`, `database.py` | End-of-day digest, journal reflection prompt, shutdown-ritual workspace preset. |
| **BUTLER-10** | **Bill-Due Radar & Cashflow Calendar** | Butler/Finance | `bill_radar.py`, `documents.py` | Recurring-bill register from FIN-01 parsing, pre-debit reminders, missing/anomalous bill flags. |

#### 🟢 Low

| ID | Task Name | Category | Target File(s) | Acceptance Criteria |
|---|---|---|---|---|
| **BUTLER-12** | **Butler Persona & Mood Engine** | UI/Personality | `llm_provider.py`, `Mascot.tsx` | Personality slider, context-driven mood, TTS tone adaptation via AST-07 params. |
| **BUTLER-27** | **Weekly Review Generator** | Reflection | `proactive.py`, `database.py` | Sunday auto-review: wins/misses/metrics/next-week plan; voice-readable. |
| **BUTLER-08** | **Learning Queue & Spaced Reading Digest** | Butler/Learning | `learning_queue.py`, `web_browser.py` | Save-for-later queue, scheduled digest slot, SM-2 flashcards with chat recall quizzes. |
| **BUTLER-09** | **Weather-Aware Day Planner & Outfit Advisor** | Butler/Context | `day_planner.py`, `geo_location.py` | Morning plan timeline merging weather/calendar/habits; outfit suggestions; rain-alert replans. |
| **SEC-42** | **Wi-Fi Security Assessor** | Security/Network | `wifi_assessor.py`, `proactive.py` | Warn on open/WEP/WPA2-weak networks at join, auto-tighten firewall + sharing rules on public Wi-Fi, network trust profiles. |
| **SEC-43** | **Secure File Shredder & Sensitive Vault** | Security/Files | `secure_shredder.py`, `tools/filesystem.py` | DoD 5220.20-M multi-pass wipe with verification, encrypted sensitive-file vault, wipe certificates for audit. |
| **TRUST-04** | **Citation Guardrails** | Trust/AI | `loop_stream.py`, `prompt_templates.py` | Web/RAG-sourced answers must carry citations; uncited factual claims flagged inline. |
| **KNOW-04** | **Smart Bookmark Manager** | Knowledge/Web | `bookmark_manager.py`, `tools/web_browser.py` | Deduped, auto-tagged bookmarks with dead-link pruning and full-text page recall. |
| **FIN-05** | **Group Expense Settlement** | Finance/Social | `expense_pool.py`, `whatsapp_manager.py` | Splitwise-style pools, minimal-settlement calc, WhatsApp settlement reminders. |
| **FIN-06** | **Net Worth Snapshot** | Finance/Insight | `networth_tracker.py`, `documents.py` | Weekly assets-vs-liabilities card in morning briefing with trend arrow. |
| **CAR-02** | **Parking Locator** | Butler/Vehicle | `geo_location.py` | Auto-save parked location on arrival, "where's my car?" recall with walking directions. |
| **FAM-02** | **Kids Mode & Screen Limits** | Butler/Family | `parental_controls.py` | Per-profile app time budgets, bedtime lock, parent activity report. |
| **ACC-01** | **Accessibility & Voice-Only Control Pass** | UI/Accessibility | `meridian_frontend/src/*` | Full keyboard nav + screen-reader labels, high-contrast theme, font scaling, voice-only control audit. |
| **MED-02** | **Journal Prompts & Gratitude Mode** | Reflection | `proactive.py`, `database.py` | Nightly reflection prompts inside BUTLER-07 wind-down; gratitude streak tracking. |

---

## ⏳ In Progress

| ID | Task Name | Priority | Category | Target File(s) | Assignee / Status |
|---|---|---|---|---|---|
| *(empty — pick from Planned or Butler Backlog)* | | | | | |

---

## ✅ Completed (Code Implemented & Test-Verified)

### Sprint: Foundation → Full-Duplex Voice → AST Graph (Days 1–6)

| ID | Task Name | Date Completed | Key Outcome |
|---|---|---|---|
| **OPT-01** | Ultra-Lightweight Frontend RAM & Performance Engine | 2026-08-10 | Tab unmounting, virtualization, blob GC, Low-RAM CSS toggle (<45MB target). |
| **PL-30** | Geo-Location & Spatial Context Engine | 2026-08-10 | IP/OS location resolver, spatial query bias, localized weather briefings (`tools/geo_location.py`). |
| **SEC-25** | OAuth 2.0 Hybrid Auth & External Connector Engine | 2026-08-12 | PKCE flow, JWT validation, encrypted token vault; Gmail/Calendar/Contacts/GitHub/Cloudflare connectors; `/api/auth/oauth/*`. |
| **WKF-01** | n8n-Style Node Workflow & Automation Engine | 2026-08-12 | DAG engine (`workflow_engine.py`), variable interpolation, webhook gateway, `/api/workflows/*`, `WorkflowBuilder.tsx`. |
| **WAP-01** | Local WhatsApp Contact Directory & Auto-Resolver | 2026-08-13 | MongoDB contact store, alias resolution ("Mom" → number), `manage_whatsapp_contacts`. |
| **WAP-02** | Playwright WhatsApp Web Session & Message Puller | 2026-08-13 | Persistent session profile, `read_whatsapp_messages`, `list_whatsapp_chats`. |
| **WAP-03** | Cross-Platform Smart WhatsApp Sender | 2026-08-13 | Auto-resolving sender with Desktop/Web fallbacks on Windows/macOS/Linux. |
| **PL-12** | Interactive Approval Gates for Destructive Actions | 2026-08-13 | HITL gate interceptor (`check_approval_gate`) in `loop.py`. |
| **SEC-27** | Ephemeral Sandboxed Code Execution Runner | 2026-08-13 | Process sandbox wrapper (`run_sandboxed_command`) with resource bounds. |
| **JARVIS-07** | Self-Healing System Defense & Thermal Governor | 2026-08-13 | Cache purger, health monitoring, rogue-process isolation in `system_defense.py`. |
| **PL-18** | Native OS System Toast Notification Integration | 2026-08-13 | Native toast runner (`send_native_toast_notification`) in `communication.py`. |
| **PL-07** | Unified LLM Provider Code Auditor | 2026-08-14 | Code review tools routed via `llm_provider.py` instead of hardcoded Ollama. |
| **PL-23** | User-Selected Model for Task Decomposition & Loop Helpers | 2026-08-14 | Loop helpers bound to user's `brain_model`. |
| **PL-24** | Frontend Dynamic Model Source Lookup & LocalStorage Setter | 2026-08-14 | Execution mode resolved from `MERIDIAN_MODEL_SOURCE` localStorage. |
| **PL-25** | Settings Page Execution Mode Toggle (Local vs Cloud/API) | 2026-08-14 | Explicit execution-mode switch in Settings. |
| **PL-26** | Backend API Settings & Model Source Synchronization | 2026-08-14 | `MERIDIAN_MODEL_SOURCE` persisted in profile DB and synced to stream handler. |
| **JARVIS-11** | Autonomous PR Reviewer & Automated Unit Test Generator | 2026-08-14 | pytest/jest generation for unstaged diffs + pre-commit review in `auto_reviewer.py`. |
| **AST-15** | Full-Duplex Voice & Live Voice Interrupt | 2026-08-15 | WebSocket audio streaming with instant barge-in. |
| **AST-08** | Continuous Conversation Window | 2026-08-15 | 10-second follow-up listening window without wake word. |
| **JARVIS-03** | Voice Biometric Identity & Speaker Verification | 2026-08-15 | Voiceprint matcher blocking unauthorized background commands. |
| **DEV-05** | Tree-Sitter Offline Codebase AST Graph | 2026-08-16 | Dependency graph visualizer, symbol search, caller/callee trace, impact analysis. |
| **JARVIS-09** | Subconscious Codebase Memory & Neural RAG Synthesizer | 2026-08-16 | Background AST semantic synthesizer in `neural_rag.py`. |
| **DEV-04** | Paper2Code (PaperCoder) Integration | 2026-08-16 | 3-stage paper-to-repo multi-agent generator in `papercoder.py`. |
| **BUTLER-01** | Persistent Butler Account & Chrome YouTube Music Automation | 2026-08-23 | Preference memory, Chrome profile launcher, YouTube Music autoplay, screenshot verification loop (`test_butler_media.py`). |

### Sprint: Core Platform (Jul 2026)

| ID | Task Name | Date Completed | Key Outcome |
|---|---|---|---|
| **DN-01** | ReAct Reasoning Loop (`loop.py`) | 2026-07-20 | Multi-step tool use, SSE streaming, self-correction. |
| **DN-02** | Voice Engine (STT/TTS/WakeWord) | 2026-07-21 | Whisper STT, Edge/Coqui TTS, "Hey Meridian" wake word. |
| **DN-03** | Encrypted Vault (`vault.py`) | 2026-07-19 | AES-GCM credential encryption. |
| **DN-04** | Discord & Telegram Bridges | 2026-07-22 | Remote command & control bots. |
| **DN-05** | Screen Vision Capture (`vision.py`) | 2026-07-22 | mss/pyautogui capture to vision models. |
| **DN-06** | System Metrics Proactive Monitor | 2026-07-22 | CPU/RAM/Disk anomaly alerts. |
| **DN-07** | Vector Memory & RAG Pipeline | 2026-07-18 | SQLite + ChromaDB memory storage. |
| **BK-01..BK-33** | Architecture, Vault, Voice, Packaging & UI hardening series | 2026-07-23 → 2026-07-26 | Loop split, Argon2id vault, P2P persistence, duplex voice, swarm orchestration, MCP server/client, benchmark governor, spotlight palette, Tauri cross-platform targets, transparency/clipboard fallbacks, etc. |
| **SEC-01..SEC-26** | Security hardening series | 2026-07-26 | API-key middleware, rate limiting, body-size caps, audit chain HMAC, machine-bound passphrase, injection sanitizer/denylists, path-traversal guard, SQL guard, secret redaction, clipboard poison detector, dependency CVE scanner, TLS, security headers. |
| **AST-01..AST-14** | Assistant intelligence series | 2026-07-26 | Preference graph, morning briefing, daily summarizer, workspace macros, ghost assistant, focus guard, emotion TTS, media control, calendar/email assistant, custom voice persona, meeting transcriber, dynamic tool creator, smart home control. |
| **DEV-01..DEV-03** | Developer tooling series | 2026-07-26 | Autonomous bug fixer, MCP-server exposure, tech-debt radar. |
| **GAM/CRT/FIN/ECO** | Gaming, creative, finance & device series | 2026-07-26 | Game coach overlay, power profiles, local visual studio, call translator, slide generator, receipt/subscription parser, market digest, clipboard sync. |
| **VK/MC/IP/CB** | Vault keys, MCP manager, mascot logo, clipboard router | 2026-07-25 → 2026-07-26 | Categorized API-key tabs, custom MCP registration, mascot logo integration, clipboard chatbot routing. |
| **PL-28** | Multi-Channel Proactive Event & Notification Engine | 2026-08-09 | Event bus dispatcher, crash hook, motion-return trigger, proactive notify tool + endpoint. |
