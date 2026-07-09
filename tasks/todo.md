# Task List

- [x] **Task 1**: Implement dynamic settings loading (health thresholds, distraction list, disk path) in [proactive.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/proactive.py)
  - **Acceptance**: Health warning thresholds, disk path, and distraction lists are loaded dynamically via `get_user_profile` from the database. Falls back to default values if not defined. Disk path uses `os.path.abspath(os.sep)`.
  - **Verify**: Compilation checks.
  - **Files**: `meridian_backend/src/core/proactive.py`

- [x] **Task 2**: Implement dynamic Game Mode detection and PID tracking in [proactive.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/proactive.py)
  - **Acceptance**: Detect fullscreen/busy state via `SHQueryUserNotificationState` and window metrics. Store PID and process name when Game Mode is enabled. If user alt-tabs, keep Game Mode active if the game PID is still running. Disable Game Mode once the game process exits.
  - **Verify**: Inspect code. Verify no `psutil.process_iter` loop is used for background check (only direct PID checks).
  - **Files**: `meridian_backend/src/core/proactive.py`

- [x] **Task 3**: Upgrade clipboard traceback regex in [proactive.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/proactive.py)
  - **Acceptance**: Combined regular expression `_TRACEBACK_RE` matches Python tracebacks, Rust panics, and JavaScript/Node.js stack frames.
  - **Verify**: Check regex correctness.
  - **Files**: `meridian_backend/src/core/proactive.py`

- [x] **Task 4**: Create `get_auditor_model` helper in [database.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/database.py) and refactor all auditor references
  - **Acceptance**: Create helper that reads `meridian_auditor_model` from database profile with env var fallback and default `"qwen2.5-coder:1.5b-instruct-q8_0"`. Replace all static `"qwen2.5-coder:1.5b-instruct-q8_0"` string literals in `database.py`, `api.py`, and `loop.py`.
  - **Verify**: Check file occurrences, compile.
  - **Files**: `meridian_backend/database.py`, `meridian_backend/api.py`, `meridian_backend/src/core/loop.py`

- [x] **Task 5**: Dynamize voice default and wake word threshold in [tts.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/voice/tts.py) and [wakeword.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/voice/wakeword.py)
  - **Acceptance**: Load default voice in `tts.py` (default `"M1"`) and sensitivity threshold in `wakeword.py` (default `0.6`) from `user_profile` table.
  - **Verify**: Verification checks.
  - **Files**: `meridian_backend/src/voice/tts.py`, `meridian_backend/src/voice/wakeword.py`

- [x] **Task 6**: Dynamize browser viewport dimensions and vision model in [web_browser.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/tools/web_browser.py)
  - **Acceptance**: Viewport dimensions `_viewport_w` and `_viewport_h` are loaded dynamically (default `1280` x `800`) and `MERIDIAN_VISION_MODEL` is resolved with fallback to `"moondream:1.8b"`.
  - **Verify**: Verify screenshot captures.
  - **Files**: `meridian_backend/src/tools/web_browser.py`

- [x] **Task 8**: Dynamize Whisper model size, silence VAD timeout, energy threshold, and max duration in [stt.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/voice/stt.py)
  - **Acceptance**: Load default model size (default `"base"`), silence timeout (default `1.0`), energy threshold (default `300.0`), and max duration (default `8.0`) from `user_profile` in `stt.py`.
  - **Verify**: Inspect code.
  - **Files**: `meridian_backend/src/voice/stt.py`

- [x] **Task 9**: Dynamize custom wake word model path and alert text details in [wakeword.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/voice/wakeword.py)
  - **Acceptance**: Load wake word model filename (default `"hey_meridian.onnx"`) and wake phrase text (default `"Hey Meridian"`) dynamically from database profile in `wakeword.py`.
  - **Verify**: Inspect code.
  - **Files**: `meridian_backend/src/voice/wakeword.py`

- [x] **Task 11**: Create centralized `get_brain_model()` and `get_vision_model()` in [database.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/database.py)
  - **Acceptance**: Implement dynamic getters that fallback to env vars and default models.
  - **Verify**: Check signatures.
  - **Files**: `meridian_backend/database.py`

- [x] **Task 12**: Refactor tool files to use the new model getters
  - **Acceptance**: Update `web_browser.py`, `recording.py`, `desktop.py`, `shell.py`, `review.py`, `web.py`, `dynamic_manager.py`, and `db_query.py` to import and call `get_brain_model()` / `get_vision_model()`.
  - **Verify**: Verify all files compile cleanly.
  - **Files**: `meridian_backend/src/tools/web_browser.py`, `meridian_backend/src/tools/recording.py`, `meridian_backend/src/tools/desktop.py`, `meridian_backend/src/tools/shell.py`, `meridian_backend/src/tools/review.py`, `meridian_backend/src/tools/web.py`, `meridian_backend/src/tools/dynamic_manager.py`, `meridian_backend/src/tools/db_query.py`

- [x] **Task 13**: Refactor `system.py` to dynamically resolve drive metrics path
  - **Acceptance**: Use `os.path.abspath(os.sep)` instead of hardcoded `'C:\\'`.
  - **Verify**: Inspect code and check syntax.
  - **Files**: `meridian_backend/src/tools/system.py`

- [x] **Task 14**: Verify changes and compile a new installer build
  - **Acceptance**: Run `python build_standalone.py` to compile executables and installers.
  - **Verify**: Build script completes successfully.
  - **Files**: None
