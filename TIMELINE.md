# ⏳ Meridian-X — Day-by-Day Implementation Timeline

Daily schedule sequenced strictly by **priority/importance**, **security impact**, and **architectural dependency**.

> **Legend:** ✅ Completed & test-verified · 🔜 Scheduled next · ⬜ Not started · 🔶 Partial (groundwork exists)
> Progress mirror: see `KANBAN.md`. Last reconciled: 2026-08-23.

---

## 📅 Day 1 — Foundation & Performance Boost (✅ Completed 2026-08-10)
- **`OPT-01` — Ultra-Lightweight Frontend RAM & Performance Engine**
  - *Target*: `useMemoryOptimizer.ts`, `Settings.tsx`
  - *Deliverable*: Inactive tab unmounting, list virtualization, blob GC, and Low-RAM CSS toggle (<45MB RAM target).
- **`PL-30` — Geo-Location & Spatial Context Engine**
  - *Target*: `geo_location.py`, `web.py`
  - *Deliverable*: IP/OS location resolver, local spatial query bias, localized weather briefings.

---

## 📅 Day 2 — OAuth 2.0, External Connectors & Workflow Automation Engine (✅ Completed 2026-08-12)
- [x] **`SEC-25` — OAuth 2.0 Hybrid Auth & External Connector Engine**
  - *Target*: `oauth_manager.py`, `external_connectors.py`
  - *Deliverable*: Dual API key + Bearer JWT auth, PKCE login flow, encrypted OAuth token vault for Gmail, Calendar, Contacts, GitHub, and Cloudflare.
- [x] **`WKF-01` — Meridian-X Node Workflow & Automation Engine**
  - *Target*: `workflow_engine.py`, `WorkflowBuilder.tsx`
  - *Deliverable*: Trigger/Action visual workflow runner (Webhook/Schedule/Email trigger $\rightarrow$ Filter $\rightarrow$ External Service Node $\rightarrow$ LLM step) executing multi-step automation pipelines.


---

## 📅 Day 3 — WhatsApp Integration, Security Approval Gates & Sandbox (✅ Completed 2026-08-13)
- **`WAP-01` — Local WhatsApp Contact Directory & Auto-Resolver**
  - *Target*: `whatsapp_manager.py`, `database.py`
  - *Deliverable*: Local MongoDB contact store (`whatsapp_contacts`), contact resolution engine ("Mom" $\rightarrow$ `+1234567890`).
- **`WAP-02` — Playwright WhatsApp Web Session & Message Puller**
  - *Target*: `whatsapp_manager.py`, `registry.py`
  - *Deliverable*: Persistent WhatsApp Web session (`/meridian_memory/whatsapp_session`), message pulling (`read_whatsapp_messages`), and unread chat list (`list_whatsapp_chats`).
- **`WAP-03` — Cross-Platform Smart WhatsApp Sender**
  - *Target*: `communication.py`
  - *Deliverable*: Upgrade `send_whatsapp_message()` with contact resolution, multiline text, and web URL/Desktop app fallbacks across Windows, macOS, and Linux.
- **`PL-12` — Interactive Approval Gates for Destructive Actions**
  - *Target*: `loop.py`
  - *Deliverable*: HITL UI approval modal for dangerous shell and database operations.
- **`SEC-27` — Ephemeral Sandboxed Code Execution Runner**
  - *Target*: `sandbox_runner.py`
  - *Deliverable*: Ephemeral Docker/WASM container sandbox with memory, CPU, and network bounds for unsafe code execution.
- **`JARVIS-07` — Self-Healing System Defense & Thermal Governor**
  - *Target*: `system_defense.py`
  - *Deliverable*: Real-time RAM/CPU cache purging, rogue process killer, and threat port isolation.
- **`PL-18` — Native OS System Toast Notification Integration**
  - *Target*: `communication.py`
  - *Deliverable*: Windows OS Balloon/Toast popups for background AI task completions.

---

## 📅 Day 4 — Execution Controls, Model Auditor & Auto PR Reviewer (✅ Completed 2026-08-14)

- **`PL-07` — Unified LLM Provider Code Auditor**
  - *Target*: `review.py`
  - *Deliverable*: Route code review tools dynamically via `llm_provider.py` instead of hardcoded Ollama.
- **`PL-23` — User-Selected Model for Task Decomposition & Loop Helpers**
  - *Target*: `loop.py`
  - *Deliverable*: Bind internal loop helpers to user's selected `brain_model`.
- **`PL-24` — Frontend Dynamic Model Source Lookup & LocalStorage Setter**
  - *Target*: `Timeline.tsx`, `Mascot.tsx`
  - *Deliverable*: Dynamic execution mode resolution from `localStorage`.
- **`PL-25` — Settings Page Execution Mode Toggle (Local vs Cloud/API)**
  - *Target*: `Settings.tsx`
  - *Deliverable*: Explicit UI switch for `Local` vs `Cloud/API` model execution mode.
- **`PL-26` — Backend API Settings & Model Source Synchronization**
  - *Target*: `api.py`
  - *Deliverable*: Persist `MERIDIAN_MODEL_SOURCE` in profile DB and sync with ReAct stream handler.
- **`JARVIS-11` — Autonomous PR Reviewer & Automated Unit Test Generator**
  - *Target*: `auto_reviewer.py`
  - *Deliverable*: Writes pytest/jest unit tests for unstaged git diffs & generates pre-commit code review feedback.

---

## 📅 Day 5 — Full-Duplex Voice, Biometrics & Conversation Window (✅ Completed 2026-08-15)
- [x] **`AST-15` — Full-Duplex Voice & Live Voice Interrupt**
  - *Target*: `duplex.py`
  - *Deliverable*: Full-duplex WebSocket audio streaming engine supporting instant barge-in voice interruption mid-sentence.
- [x] **`AST-08` — Continuous Conversation Window**
  - *Target*: `wakeword.py`
  - *Deliverable*: 10-second active listening window following responses for follow-up speech without wake word.
- [x] **`JARVIS-03` — Voice Biometric Identity & Speaker Verification**
  - *Target*: `voice_biometrics.py`
  - *Deliverable*: Voiceprint embedding matcher blocking unauthorized background voice commands.

---

## 📅 Day 6 — Codebase AST Graph, Neural RAG & PaperCoder (✅ Completed 2026-08-16)
- [x] **`DEV-05` — Tree-Sitter Offline Codebase AST Graph**
  - *Target*: `code_graph.py`
  - *Deliverable*: AST dependency graph visualizer, symbol search, caller/callee tracing, & instant impact analysis.
- [x] **`JARVIS-09` — Subconscious Codebase Memory & Neural RAG Synthesizer**
  - *Target*: `neural_rag.py`
  - *Deliverable*: Background AST semantic synthesizer building real-time project intent knowledge graphs.
- [x] **`DEV-04` — Paper2Code (PaperCoder) Integration**
  - *Target*: `papercoder.py`, `registry.py`
  - *Deliverable*: 3-stage paper-to-repository multi-agent generator converting arXiv/PDFs into runnable code repos.


---

## 📅 Day 7 — Multi-Provider RAG, PDF Extractor & Vault Fallback (🔴 High Priority · ✅ Complete)
- **`PL-08`** ✅ — Multi-Provider RAG Vector Embeddings Pipeline
  - *Target*: `database.py`
  - *Deliverable*: OpenAI `text-embedding-3-small` and in-memory `fastembed` fallback when local Ollama is offline.
- **`PL-11`** ✅ — Hybrid Sparse-Dense RAG & AST Code Chunking
  - *Target*: `doc_indexer.py`
  - *Deliverable*: BM25 keyword matching + Turbovec dense vectors + AST function/class boundary chunking.
- **`PL-17`** ✅ — Native Pure-Python PDF Layout & Table Extractor
  - *Target*: `documents.py`, `doc_indexer.py`
  - *Deliverable*: Pure-Python XY-Cut reading order sorting and bounding box table parser.
- **`PL-09`** ✅ — Multi-Cloud Vault Fallback Chain
  - *Target*: `llm_provider.py`
  - *Deliverable*: Automated failover chain across vault API keys (Primary Cloud $\rightarrow$ Secondary Cloud $\rightarrow$ Ollama).

---

## 📅 Day 8 — Ambient Perception, Vision Sense & Gesture Control (🔴 High Priority · ⬜ Not started)
- **`PL-01`** ⬜ — Facial Recognition & Presence Engine
  - *Target*: `vision_face.py`
  - *Deliverable*: Real-time face recognition embeddings, emotion tracking, and workspace user presence.
- **`PL-02`** ⬜ — Continuous Ambient Listener
  - *Target*: `ambient_listener.py`
  - *Deliverable*: Background VAD with `webrtcvad` + continuous `faster-whisper` transcription stream.
- **`PL-03`** ⬜ — Real-Time Screen & Window Sense
  - *Target*: `screen_sense.py`
  - *Deliverable*: Active window metadata tracking + vision LLM screen parsing on app switches.
- **`PL-04`** ⬜ — Proactive Nudge Engine Expansion
  - *Target*: `proactive.py`
  - *Deliverable*: Event-driven context synthesis combining face, audio, screen, and system metrics.
- **`PL-06`** ⬜ — Provider-Aware Multimodal Screen Vision
  - *Target*: `vision.py`
  - *Deliverable*: Direct screen capture routing to OpenAI `gpt-4o`, Gemini `gemini-1.5-flash`, or Claude `claude-3-5-sonnet`.
- **`PL-29`** ⬜ — Vision Motion & Hand Gesture Control Sentinel
  - *Target*: `vision_gesture.py`
  - *Deliverable*: MediaPipe/OpenCV hand gesture recognizer (thumbs up for HITL, open palm stop, wave) + desk motion tracker.
- **`JARVIS-02`** ⬜ — Eye-Tracking & Spatial Gaze Control Sentinel
  - *Target*: `gaze_tracker.py`
  - *Deliverable*: MediaPipe Iris gaze tracker for hands-free window selection & gaze-based screen dimming.

---

## 📅 Day 9 — Predictive AI, Financial Sentinel & Mobile Sync (🔴 High Priority · ⬜ Not started)
- **`JARVIS-04`** 🔶 Partial — Predictive Action Pre-Execution & Context Pre-Warmer
  - *Target*: `predictive_engine.py` *(habit-model groundwork currently lives in `perception.py`; dedicated engine file not yet created)*
  - *Deliverable*: Habit model pre-warming LLM context, opening dev tools, and pre-scaffolding git diffs.
- **`FIN-03`** ⬜ — Real-Time Financial News Sentiment & Stock Sentinel
  - *Target*: `finance_sentinel.py`
  - *Deliverable*: Financial news sentiment classifier & hybrid stock trend forecasting engine.
- **`ECO-01`** ⬜ — Mobile Companion App & QR P2P Sync
  - *Target*: `p2p.py`
  - *Deliverable*: Mobile QR pairing, remote voice command relay, and phone camera video stream ingestion.

---

---


## 📅 Day 10 — Personal Butler Expansion I: Memory, Travel & Expiry (🔴 High Priority · ⬜ Not started)

*Everything below was verified as **missing from the codebase** on 2026-08-23. Each item reuses existing infrastructure (proactive event bus, preference memory, WhatsApp/OAuth connectors, geo engine, scheduler).*

- **`BUTLER-02`** 🔜 — Personal CRM & Occasion Sentinel
  - *Target*: `personal_crm.py`, `database.py`, `proactive.py`
  - *Deliverable*: People graph with birthdays/anniversaries/last-contact; LLM gift ideas + follow-up nudges for silent VIP contacts.
- **`BUTLER-04`** 🔜 — Travel Butler & Leave-By Briefing
  - *Target*: `travel_butler.py`, `tools/web.py`
  - *Deliverable*: NL trip creation, itinerary assembly from Gmail confirmations, leave-by commute calc via `geo_location.py`, travel-day voice briefing.
- **`BUTLER-06`** 🔜 — Document Expiry Vault Sentinel
  - *Target*: `expiry_sentinel.py`, `tools/documents.py`
  - *Deliverable*: Passport/ID/insurance/warranty/domain registry with 30/14/7/1-day escalation via proactive notifications.

---

## 📅 Day 11 — Cyber Defense Sprint I: Emergency & Data Protection (🔴 High Priority · ⬜ Not started)

*Verified missing on 2026-08-23: no ransomware detection, network monitoring, breach watch, or lockdown mode exists (`system_defense.py` covers only CPU/RAM/process hygiene).*

- **`SEC-34`** 🔜 — Emergency Lockdown Mode
  - *Target*: `emergency_lockdown.py`, `system_defense.py`
  - *Deliverable*: One voice/command trigger that locks the workstation, mutes mic, disables cameras, isolates network adapters, and freezes vault sessions; PIN/biometric unlock; fully audit-logged.
- **`SEC-31`** 🔜 — Ransomware Canary & File Integrity Watcher
  - *Target*: `fim_sentinel.py`, `watcher.py`
  - *Deliverable*: Honeypot files + baseline hashes on Documents/Desktop; mass modify/rename tripwire → instant process quarantine via JARVIS-07 hook, emergency snapshot backup trigger, toast alert.
- **`SEC-30`** 🔜 — Phishing & Link Reputation Guard
  - *Target*: `tools/web_browser.py`, `external_connectors.py`
  - *Deliverable*: Pre-click URL reputation scan + heuristics, email link scanning in the Gmail connector, sandboxed screenshot preview of suspicious pages before the user opens them.
- **`SEC-28`** 🔜 — Breach & Leak Sentinel
  - *Target*: `breach_sentinel.py`
  - *Deliverable*: HaveIBeenPwned k-anonymity checks for registered emails, periodic re-scan, exposed-credential rotation prompts, dark-web keyword watch for personal identity terms.

---

## 📅 Day 12 — Voice Calling Engine (🔴 High Priority · ⬜ Not started)

*Verified missing on 2026-08-23: `duplex.py` only transcribes/translates supplied audio — there is no real telephony bridge or call agent anywhere.*

- **`CALL-01`** 🔜 — VoIP Phone Agent Bridge
  - *Target*: `tools/phone_agent.py`, `voice/duplex.py`
  - *Deliverable*: Twilio/SIP trunk bridge routing live calls through the duplex STT/TTS loop; outbound dialing tool (`make_phone_call`) with goal-driven conversation loop and hang-up detection.
- **`CALL-02`** 🔜 — AI Call Screener & Receptionist
  - *Target*: `tools/phone_agent.py`
  - *Deliverable*: Answers unknown numbers, classifies spam vs. human vs. priority, takes messages, passes through starred callers, streams live transcript to the UI.
- **`CALL-03`** 🔜 — Post-Call Intelligence
  - *Target*: `voice/duplex.py`, `database.py`
  - *Deliverable*: Auto-transcription → speaker-labeled summary → action items → optional calendar follow-up; extends AST-14 meeting transcriber to phone calls.
- **`CALL-04`** 🔜 — Emergency SOS Voice Protocol
  - *Target*: `sos_protocol.py`, `geo_location.py`
  - *Deliverable*: Wake-phrase SOS: shares live location via WhatsApp/Telegram with trusted contacts, triggers siren, optional fake-incoming-call decoy.

---

## 📅 Day 13 — Cyber Defense Sprint II: Malware & System Protection (🔴 High Priority · ⬜ Not started)

*Verified missing on 2026-08-23: no malware scanning, behavioral detection, or persistence auditing exists (`security_auditor.py` covers only port scans + leak checks).*

- **`SEC-36`** 🔜 — Local Malware Scanner & Download Inspector
  - *Target*: `malware_scanner.py`, `tools/filesystem.py`
  - *Deliverable*: Signature + heuristic engine (YARA-style rules, ClamAV engine fallback) for downloads, files, and USB drives on insertion; encrypted quarantine folder; hash-reputation lookup.
- **`SEC-37`** 🔜 — Real-Time Process Behavior Monitor (EDR-Lite)
  - *Target*: `behavior_monitor.py`, `system_defense.py`
  - *Deliverable*: Behavioral detections — process injection patterns, crypto-miner CPU signatures, mass file-handle access, suspicious child-process chains → auto-quarantine via JARVIS-07 isolation.
- **`SEC-38`** 🔜 — Persistence & Autoruns Sentinel
  - *Target*: `persistence_sentinel.py`, `watcher.py`
  - *Deliverable*: Baseline of registry Run keys, scheduled tasks, services, startup folders, and browser extensions; alert + one-click rollback on any new persistence entry.

---

## 📅 Day 14 — Trust & Reliability Sprint (🔴 High Priority · ⬜ Not started)

*Verified missing on 2026-08-23: no way to inspect/edit agent memory, no tool-routing regression tests, no updater, no cost meter.*

- **`TRUST-01`** 🔜 — Memory Editor UI ("What do you remember?")
  - *Target*: `memory_editor.py` API, `MemoryEditor.tsx`, `temporal_memory.py`
  - *Deliverable*: Searchable window into everything Meridian remembers (preferences, facts, journal); edit/delete/"forget this" commands; export as JSON — GDPR-style brain transparency.
- **`TRUST-02`** 🔜 — Tool-Use Regression Suite
  - *Target*: `tests/tool_scenarios.yaml`, `.github/workflows/ci.yml`
  - *Deliverable*: Scripted NL scenarios asserting correct tool selection + arguments through `loop.py`; runs in CI pre-release so prompt/refactors can't silently break routing.
- **`OPS-01`** 🔜 — Self-Updater with Safe Swap & Changelog
  - *Target*: `updater.py`, `.github/workflows/release.yml`
  - *Deliverable*: Version check → download → verify signature → swap binaries → restart backend with rollback on failed health probe; changelog shown in-app.
- **`KNOW-01`** 🔜 — Downloads Janitor
  - *Target*: `file_janitor.py`, `tools/filesystem.py`
  - *Deliverable*: Auto-sort downloads by type/date, duplicate hash finder, age-out rules with review-before-delete; nightly summary nudge.
- **`FIT-01`** 🔜 — Wearable Health Data Ingestion
  - *Target*: `health_ingest.py`, `proactive.py`
  - *Deliverable*: Google Fit / Apple Health / smartwatch steps + sleep sync feeding the wellness score and a "readiness" line in the morning briefing.

---

---


## 📅 Day 15 — Subagent Model Binding, RTSP Camera & Polyglot (🟡 Medium Priority)
- **`PL-10`** ⬜ — Heterogeneous Subagent Model Binding
  - *Target*: `swarm.py`
  - *Deliverable*: Role-based subagent model binding (DeepSeek Coder for Auditor, Gemini Flash for Researcher).
- **`JARVIS-05`** ⬜ — Smart Camera & RTSP Security Vision Sentinel
  - *Target*: `camera_sentinel.py`
  - *Deliverable*: RTSP security camera stream object detector notifying room entry or visitors.
- **`JARVIS-06`** ⬜ — Room Arrival Auto-Briefing & Voice Synthesizer
  - *Target*: `presence_briefing.py`
  - *Deliverable*: Presence-triggered 15-second executive voice report upon entering workspace.
- **`JARVIS-10`** ⬜ — Multi-Lingual Whisper & Real-Time Code Polyglot
  - *Target*: `polyglot.py`
  - *Deliverable*: 50+ language real-time speech-to-code translator.

---

---


## 📅 Day 16 — AR Bridge, Workspace Layout & Perception HUD (🟡 Medium Priority)
- **`JARVIS-08`** ⬜ — Dynamic AR Smart Glasses & Headset Mirroring Bridge
  - *Target*: `ar_bridge.py`
  - *Deliverable*: WebSockets HUD streaming for XREAL, Meta Ray-Ban, and Apple Vision Pro headsets.
- **`SYS-01`** ⬜ — Smart Workspace Window Auto-Organizer
  - *Target*: `workspace_layout.py`
  - *Deliverable*: Auto-arranges editor, terminal, browser, and Meridian HUD windows into mode presets.
- **`PL-05`** ⬜ — Frontend Perception HUD & Hardware Toggles
  - *Target*: `PerceptionHUD.tsx`, `NavRail.tsx`
  - *Deliverable*: Visual webcam/mic indicators and hardware mute switches.
- **`PL-20`** ⬜ — Active Brain Model & Execution Mode Header Pill
  - *Target*: `StatusBar.tsx`, `NavRail.tsx`
  - *Deliverable*: Persistent status badge showing active loaded model and execution mode.
- **`PL-22`** ⬜ — Inline Connection & API Key Health Checks
  - *Target*: `Settings.tsx`
  - *Deliverable*: Real-time connection status badges for Ollama and API keys.

---

---


## 📅 Day 17 — Butler Expansion II: Household, Finance & Rhythm (🟡 Medium Priority · ⬜ Not started)
- **`BUTLER-03`** ⬜ — Wellness & Ergonomics Butler
  - *Target*: `wellness.py`, `proactive.py`
  - *Deliverable*: Hydration/posture/eye-strain/stretch micro-breaks respecting Focus Guard and game throttling; daily wellness score.
- **`BUTLER-05`** ⬜ — Household Ops: Grocery, Pantry & Chore Tracker
  - *Target*: `household.py`, `database.py`
  - *Deliverable*: Voice/NL list capture, low-stock pantry suggestions, chore rotations, WhatsApp-shared shopping lists.
- **`BUTLER-07`** ⬜ — Evening Wind-Down & Daily Review
  - *Target*: `proactive.py`, `database.py`
  - *Deliverable*: End-of-day digest (tasks/git/focus/calendar), journal reflection prompt, shutdown-ritual workspace preset.
- **`BUTLER-10`** ⬜ — Bill-Due Radar & Cashflow Calendar
  - *Target*: `bill_radar.py`, `tools/documents.py`
  - *Deliverable*: Recurring-bill register from FIN-01 parsing, pre-debit reminders, missing/anomalous bill flags.

---

## 📅 Day 18 — Identity, Credential & Peripheral Defense (🟡 Medium Priority · ⬜ Not started)
- **`SEC-32`** ⬜ — Built-in TOTP 2FA Generator
  - *Target*: `tools/vault.py`, `Settings.tsx`
  - *Deliverable*: Vault-stored RFC-6238 TOTP seeds, one-tap code copy, expiry countdown UI — replaces phone authenticator apps.
- **`SEC-35`** ⬜ — Password Health Auditor
  - *Target*: `tools/vault.py`, `security_auditor.py`
  - *Deliverable*: Strength/reuse/age audit across stored logins with breach-corpus cross-check; weak-password report card.
- **`SEC-29`** ⬜ — Network Guardian
  - *Target*: `network_guardian.py`
  - *Deliverable*: New-LAN-device alerts, ARP-spoofing detection, per-process suspicious outbound connection monitor, open-port sweep feeding JARVIS-07 isolation.
- **`SEC-33`** ⬜ — USB & Peripheral Watchdog
  - *Target*: `usb_watchdog.py`
  - *Deliverable*: New USB device alerts, HID keystroke-burst (BadUSB) detection, trusted-device allowlist.
- **`SEC-39`** ⬜ — DNS Filter & Web Shield
  - *Target*: `dns_shield.py`, `tools/web_browser.py`
  - *Deliverable*: Local malicious-domain blocklist with auto-updates, DNS-over-HTTPS enforcement, hosts-file hijack detection, per-app domain blocking.
- **`SEC-40`** ⬜ — Webcam & Mic Access Guard
  - *Target*: `cam_guard.py`, `PerceptionHUD.tsx`
  - *Deliverable*: Per-process camera/microphone access monitoring via OS APIs, unknown-process block + toast alert, indicator sync with PL-05 HUD.
- **`SEC-41`** ⬜ — Email Attachment Detonation Sandbox
  - *Target*: `external_connectors.py`, `sandbox_runner.py`
  - *Deliverable*: Detonate inbound attachments in the SEC-27 ephemeral sandbox before delivery; behavioral verdict (drops persistence? encrypts files? phones home?) attached to the email.

---

## 📅 Day 19 — Communication Intelligence & Trust Layer (🟡 Medium Priority · ⬜ Not started)
- **`BUTLER-24`** ⬜ — Email Zero Triage
  - *Target*: `external_connectors.py`, `api.py`
  - *Deliverable*: Inbox classifier (needs-reply / FYI / noise), reply drafts in the user's voice, unsubscribe suggestions, batch-action UI.
- **`BUTLER-23`** ⬜ — Meeting Prep Briefing
  - *Target*: `proactive.py`, `oauth_manager.py`
  - *Deliverable*: T-minus-10-min meeting cards: attendee CRM profile (BUTLER-02), last email-thread summary, agenda talking points.
- **`BUTLER-26`** ⬜ — Memory Time Machine
  - *Target*: `memory_backup.py`, `vault.py`
  - *Deliverable*: Encrypted scheduled snapshots of SQLite DB + vault + memory graphs; diffable restore points; one-click rollback.
- **`BUTLER-25`** ⬜ — Voice Thought Bucket
  - *Target*: `voice/wakeword.py`, `temporal_memory.py`
  - *Deliverable*: "Note: …" instant voice capture anywhere, auto-tagging, contextual resurfacing via RAG.
- **`BUTLER-14`** ⬜ — Undo & Action Journal
  - *Target*: `loop_dispatcher.py`, `Timeline.tsx`
  - *Deliverable*: Every tool call journaled with a reversible flag; "undo that" executes the inverse for supported actions.
- **`CALL-05`** ⬜ — WhatsApp Voice Call Bridge
  - *Target*: `whatsapp_manager.py`
  - *Deliverable*: Extend the Playwright session for WhatsApp voice calls: dial by contact alias, live transcript capture.

---

---


## 📅 Day 20 — Knowledge & Cost Intelligence (🟡 Medium Priority · ⬜ Not started)
- **`TRUST-03`** ⬜ — Cloud Spend & Token Meter
  - *Target*: `llm_provider.py`, `Settings.tsx`
  - *Deliverable*: Per-provider token/cost dashboard, monthly budget caps, automatic downgrade to local Ollama when overspend threshold hits.
- **`KNOW-02`** ⬜ — Screenshot Memory
  - *Target*: `screenshot_memory.py`, `doc_indexer.py`
  - *Deliverable*: Auto-captured screenshots OCR-indexed into RAG ("that error I saw Tuesday"), retention window, instant visual recall.
- **`KNOW-03`** ⬜ — Universal Search Hub
  - *Target*: `search_hub.py`, `CommandPalette.tsx`
  - *Deliverable*: One query fusing RAG docs, code graph symbols, chat history, screenshots, clipboard history, and files; keyboard-first results UI.
- **`OPS-04`** ⬜ — Local-Only Mode Switch
  - *Target*: `mode.py`, `security_middleware.py`
  - *Deliverable*: Single audited toggle that blocks every outbound cloud/API call; Settings shows live proof-of-enforcement badge.
- **`FIN-04`** ⬜ — Wishlist Price Watcher
  - *Target*: `price_watcher.py`, `tools/web_browser.py`
  - *Deliverable*: Track product pages for drops with price-history sparklines; proactive alert + "buy now?" deep link.

---

## 📅 Day 21 — Life Expansion: Vehicle, Family & Media (🟡 Medium Priority · ⬜ Not started)
- **`CAR-01`** ⬜ — Car Logbook & Service Predictor
  - *Target*: `car_logbook.py`, `documents.py`
  - *Deliverable*: Fuel/service/expense entries, mileage-based service-due predictions, insurance renewal tie-in with BUTLER-06 expiry ladder.
- **`FAM-01`** ⬜ — Shared Family Board
  - *Target*: `family_board.py`, `database.py`
  - *Deliverable*: Role-based shared lists/calendar/shopping (extends BUTLER-05 beyond solo), WhatsApp broadcast of updates.
- **`OPS-02`** ⬜ — Multi-Machine State Sync
  - *Target*: `p2p.py`, `memory_backup.py`
  - *Deliverable*: Encrypted delta-sync of settings + memory graphs between desktops over the existing P2P layer (ECO-01 covers phones only).
- **`OPS-03`** ⬜ — Butler Skill Plugin SDK
  - *Target*: `plugins.py`, `docs/PLUGIN_SDK.md`
  - *Deliverable*: Signed third-party butler-skill packages with manifest, permission tiers, sandboxed install flow via plugin marketplace.
- **`MED-01`** ⬜ — Photo Organizer & Memories
  - *Target*: `photo_organizer.py`, `vision_face.py`
  - *Deliverable*: Dedupe, face-tagged albums (reuses PL-01 embeddings), auto-album generation, "on this day" resurfacing.

---

---


## 📅 Day 22 — Mascot Expressions, Visualizer & UI Polish (🟡 Medium & 🟢 Low Priority)
- **`PL-13`** ⬜ — Mascot Visor Expressions & Micro-Emotions
  - *Target*: `Mascot.tsx`
  - *Deliverable*: Dynamic SVG visor eyes (`^ _ ^`, `> _ <`, `- _ -`) and sleeping particle animations.
- **`PL-14`** ⬜ — Mascot Real-Time Voice Audio Visualizer
  - *Target*: `Mascot.tsx`
  - *Deliverable*: Circular 8-bar audio equalizer reacting to STT/TTS frequencies.
- **`PL-15`** ⬜ — Agent Loop Action Auras for Mascot
  - *Target*: `Mascot.tsx`
  - *Deliverable*: Action-specific visual aura effects (browsing particles, vision sonar beam, auditing shield).
- **`PL-16`** ⬜ — Desktop Floating Pet Edge-Snapping & Drag Physics
  - *Target*: `Mascot.tsx`
  - *Deliverable*: Screen edge-snapping, drag physics, and interactive pet click behaviors.
- **`PL-19`** ⬜ — Collapsible Timeline Step Accordions & Diff Preview
  - *Target*: `Timeline.tsx`
  - *Deliverable*: Collapsible agent step accordions and code diff previews.
- **`PL-21`** ⬜ — Command Palette View Navigation & Action Toggles
  - *Target*: `CommandPalette.tsx`
  - *Deliverable*: Extended `Ctrl+K` command palette with navigation and mode toggles.
- **`PL-27`** ⬜ — Anime.js UI Animation Integration
  - *Target*: `meridian_website/package.json`, `src/`
  - *Deliverable*: Anime.js timeline animations, SVG morphing, and staggered transitions.

---

---


## 📅 Day 23 — Butler Expansion III: Learning & Planning Polish (🟢 Low Priority · ⬜ Not started)
- **`BUTLER-08`** ⬜ — Learning Queue & Spaced Reading Digest
  - *Target*: `learning_queue.py`, `tools/web_browser.py`
  - *Deliverable*: "Save for later" queue, scheduled digest slot, SM-2 flashcards with chat recall quizzes.
- **`BUTLER-09`** ⬜ — Weather-Aware Day Planner & Outfit Advisor
  - *Target*: `day_planner.py`, `geo_location.py`
  - *Deliverable*: Morning plan timeline merging weather/calendar/habits; outfit suggestions; rain-alert proactive replans.

---

## 📅 Day 24 — Polish: Persona & Reflection (🟢 Low Priority · ⬜ Not started)
- **`BUTLER-12`** ⬜ — Butler Persona & Mood Engine
  - *Target*: `llm_provider.py`, `Mascot.tsx`
  - *Deliverable*: Personality slider (concise ↔ wingman ↔ formal), context-driven mood (deadline day vs. Friday evening), TTS tone adaptation via AST-07 params.
- **`BUTLER-27`** ⬜ — Weekly Review Generator
  - *Target*: `proactive.py`, `database.py`
  - *Deliverable*: Sunday auto-review: wins, misses, focus metrics, next-week plan; voice-readable on demand.

---

## 📅 Day 25 — Security Polish: Hygiene & Cleanup (🟢 Low Priority · ⬜ Not started)
- **`SEC-42`** ⬜ — Wi-Fi Security Assessor
  - *Target*: `wifi_assessor.py`, `proactive.py`
  - *Deliverable*: Warn on open/WEP/WPA2-weak networks at join time, auto-tighten firewall + sharing rules on public Wi-Fi, network trust profiles.
- **`SEC-43`** ⬜ — Secure File Shredder & Sensitive Vault
  - *Target*: `secure_shredder.py`, `tools/filesystem.py`
  - *Deliverable*: DoD 5220.20-M style multi-pass wipe with verification, encrypted sensitive-file vault inside the existing vault system, wipe certificates for audit.

---

---


## 📅 Day 26 — Long-Tail Polish (🟢 Low Priority · ⬜ Not started)
- **`TRUST-04`** ⬜ — Citation Guardrails
  - *Target*: `loop_stream.py`, `prompt_templates.py`
  - *Deliverable*: Web/RAG-sourced answers must carry citations; uncited factual claims flagged inline.
- **`KNOW-04`** ⬜ — Smart Bookmark Manager
  - *Target*: `bookmark_manager.py`, `tools/web_browser.py`
  - *Deliverable*: Deduped, auto-tagged bookmarks with dead-link pruning and full-text page recall.
- **`FIN-05`** ⬜ — Group Expense Settlement
  - *Target*: `expense_pool.py`, `whatsapp_manager.py`
  - *Deliverable*: Splitwise-style pools, minimal-settlement calculation, WhatsApp settlement reminders.
- **`FIN-06`** ⬜ — Net Worth Snapshot
  - *Target*: `networth_tracker.py`, `documents.py`
  - *Deliverable*: Weekly assets-vs-liabilities card in the morning briefing with trend arrow.
- **`CAR-02`** ⬜ — Parking Locator
  - *Target*: `geo_location.py`
  - *Deliverable*: Auto-save parked location on arrival ("where's my car?"), walking directions back.
- **`FAM-02`** ⬜ — Kids Mode & Screen Limits
  - *Target*: `parental_controls.py`
  - *Deliverable*: Per-profile app time budgets, bedtime lock, parent activity report.
- **`ACC-01`** ⬜ — Accessibility & Voice-Only Control Pass
  - *Target*: `meridian_frontend/src/*`
  - *Deliverable*: Full keyboard navigation + screen-reader labels, high-contrast theme, font scaling, voice-only complete control mode audit.
- **`MED-02`** ⬜ — Journal Prompts & Gratitude Mode
  - *Target*: `proactive.py`, `database.py`
