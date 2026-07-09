# Spec: Dynamic Proactive Intelligence & Core Engine Upgrades

## Objective
Upgrade the core backend to remove all hardcoded configurations, thresholds, path strings, models, and process lists:
1.  **Dynamic Game Mode Detection**: Use Windows shell/metrics APIs to detect fullscreen/busy status dynamically. Track game session using PID + process name verification.
2.  **Dynamic System Health Thresholds**: Load CPU, RAM, and Disk warning thresholds from the database (`user_profile` table), defaulting to `85.0`, `88.0`, and `90.0` respectively.
3.  **Cross-Platform Disk Pathing**: Dynamically resolve the system's root path using `os.path.abspath(os.sep)` instead of hardcoding `"C:\\"`.
4.  **Dynamic Distractions Blocklist**: Load distraction sites from the database (`user_profile` table), defaulting to standard distraction domains.
5.  **Multi-Language Traceback Detection**: Expand clipboard error detection to identify exceptions/panics in Python, JavaScript/Node, and Rust.
6.  **Dynamic Auditor/Validator Model**: Load the secondary validation and critiquing model from `get_user_profile("meridian_auditor_model")` or env var `MERIDIAN_AUDITOR_MODEL`, defaulting to `"qwen2.5-coder:1.5b-instruct-q8_0"`.
7.  **Dynamic TTS Voice**: Load default voice name from `get_user_profile("meridian_voice")`, defaulting to `"M1"`.
8.  **Dynamic Wake Word Sensitivity**: Load the wake word detection score threshold from `get_user_profile("wakeword_threshold")`, defaulting to `0.6`.
9.  **Dynamic Web Browser Settings**: Load viewport dimensions from `get_user_profile` (defaulting to `1280` x `800`) and dynamically resolve `MERIDIAN_VISION_MODEL` with fallback to `"moondream:1.8b"`.
10. **Dynamic STT Settings**: Load default Whisper model size (`stt_model_size` defaulting to `"base"`), silence VAD timeout (`stt_silence_timeout` defaulting to `1.0`), energy/amplitude threshold (`stt_vad_threshold` defaulting to `300.0`), and maximum recording duration (`stt_max_duration` defaulting to `8.0`).
11. **Dynamic Wake Word Model**: Load custom model filename (`wakeword_model_filename` defaulting to `"hey_meridian.onnx"`) and wake phrase text (`wakeword_phrase` defaulting to `"Hey Meridian"`).
12. **Centralized Dynamic Brain & Vision Models**: Add `get_brain_model()` and `get_vision_model()` in `database.py` to dynamize LLM settings across all tool scripts.
13. **Cross-Platform Drive System Metrics**: Update `system.py` to resolve root drive using `os.path.abspath(os.sep)`.

## Tech Stack
*   **Language**: Python 3.x
*   **Database**: SQLite/MongoDB via existing `database.py` API
*   **Libraries**: `ctypes`, `psutil`, `os`, `re`, `platform`

## Commands
*   **Run Backend**: `& "meridian_backend\venv\Scripts\python.exe" api.py`
*   **Run Build**: `python build_standalone.py`

## Project Structure
*   [meridian_backend/src/core/proactive.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/proactive.py) → Updates to active window checking, health thresholds, disk path, distraction list, and traceback regex.
*   [meridian_backend/src/core/loop.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/loop.py) → Make the auditor model dynamic.
*   [meridian_backend/api.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/api.py) → Make the auditor model dynamic, get/set game mode.
*   [meridian_backend/database.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/database.py) → Dynamic profiles, `get_brain_model`, `get_vision_model`, `get_auditor_model`.
*   [meridian_backend/src/voice/tts.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/voice/tts.py) → Make the default voice name dynamic.
*   [meridian_backend/src/voice/wakeword.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/voice/wakeword.py) → Make the wake word sensitivity score threshold, custom model filename, and wake phrase dynamic.
*   [meridian_backend/src/voice/stt.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/voice/stt.py) → Make default Whisper model size, silence VAD timeout, energy threshold, and max duration dynamic.
*   [meridian_backend/src/tools/web_browser.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/tools/web_browser.py) → Make browser viewport dimensions and vision model dynamic.
*   [meridian_backend/src/tools/system.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/tools/system.py) → Dynamic system drive metrics.
*   [meridian_backend/src/tools/recording.py](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/tools/recording.py) → Centralized dynamic models.

## Code Style
Standard Python PEP 8 with error tolerance. Wrap all OS-level calls in `try-except` blocks.

## Testing Strategy
1.  **Game Mode**: Launch fullscreen apps, ensure Game Mode auto-enables, persists on Alt-Tab, and disables when closed.
2.  **System Health**: Set `cpu_warn_threshold` to `10.0` in SQLite and verify warning triggers.
3.  **Auditor Model**: Override `meridian_auditor_model` and verify it uses the new model name.
4.  **STT & Wake Word**: Override sensitivity, silence timeouts, model filenames, and VAD thresholds in database, verify they take effect during voice capture and transcription.
5.  **Tool LLM Configs**: Verify that the tool files correctly reference the dynamic database models.

## Success Criteria
- Pre-compiled installers build successfully.
- All configurations can be updated dynamically via user profiles without code changes.
