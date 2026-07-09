# Implementation Plan: Dynamic Voice & Tool Upgrades

## Overview
We will implement dynamic configurations across all core components of the Meridian-X backend:
1.  **Dynamic Game Mode & Proactive Engine**: Fullscreen/busy state detection and PID tracking in `proactive.py`. (Completed)
2.  **Dynamic Thresholds & Blocklists**: Settings for health warnings and distraction sites loaded via `get_user_profile` in `proactive.py`. (Completed)
3.  **Dynamic Auditor Model**: Replace all hardcoded `"qwen2.5-coder:1.5b-instruct-q8_0"` string literals. (Completed)
4.  **Dynamic Voice & Wake Word Sensitivity**: Resolve default voice in `tts.py` and wake word score threshold in `wakeword.py`. (Completed)
5.  **Dynamic Browser Viewport**: Load custom browser viewport dimensions and vision model inside `web_browser.py`. (Completed)
6.  **Dynamic STT Settings**: Load Whisper model size, silence VAD timeout, energy threshold, and max duration from `user_profile` in `stt.py`. (Completed)
7.  **Dynamic Wake Word Model**: Load custom model filename and wake phrase from `user_profile` in `wakeword.py`. (Completed)
8.  **Centralized Model Getters**: Define dynamic getters in `database.py` and refactor tools (`web_browser.py`, `recording.py`, `desktop.py`, `shell.py`, `review.py`, `web.py`, etc.) to query them.
9.  **Dynamic Drive Metric**: Resolve system drive dynamically inside `system.py`.

## Task List

### Phase 1: Implementation
*   [x] **Task 1**: Implement dynamic settings loading (health thresholds, distraction list, disk path) in `proactive.py`.
*   [x] **Task 2**: Implement dynamic Game Mode detection and PID tracking in `proactive.py`.
*   [x] **Task 3**: Upgrade clipboard traceback regex in `proactive.py`.
*   [x] **Task 4**: Create `get_auditor_model()` helper in `database.py` and refactor all auditor references.
*   [x] **Task 5**: Dynamize default voice in `tts.py` and wake word threshold in `wakeword.py`.
*   [x] **Task 6**: Dynamize browser viewport dimensions and vision model in `web_browser.py`.
*   [x] **Task 8**: Dynamize Whisper model size, silence VAD timeout, energy threshold, and max duration in `stt.py`.
*   [x] **Task 9**: Dynamize custom wake word model path and alert text details in `wakeword.py`.
*   [ ] **Task 11**: Create centralized `get_brain_model()` and `get_vision_model()` in `database.py`.
*   [ ] **Task 12**: Refactor all tool files (`web_browser.py`, `recording.py`, `desktop.py`, `shell.py`, `review.py`, `web.py`, `dynamic_manager.py`, `db_query.py`) to use the new getters.
*   [ ] **Task 13**: Refactor `system.py` to dynamically resolve drive metrics path.

### Phase 2: Verification
*   [ ] **Task 14**: Perform manual verification and build/compile validation.
