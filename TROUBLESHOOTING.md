# Meridian-X — Troubleshooting Guide

This guide compiles common setup, dependency, runtime, and hardware resource issues when running Meridian-X locally, along with step-by-step mitigation paths.

---

## 1. Local LLM / Ollama Unreachable

### Symptom:
- The UI shows "Ollama server unreachable" or "Failed to connect to http://127.0.0.1:11434".
- Error in backend logs: `httpx.ConnectError: [Errno 61] Connection refused`.

### Solutions:
1. **Verify Service is Running**:
   - Check if Ollama is running in your task tray (Windows/macOS) or run `systemctl status ollama` (Linux).
   - Try opening `http://127.0.0.1:11434` in your browser. It should output: `"Ollama is running"`.
2. **Configure Custom Host**:
   - If Ollama is running on a different port or machine, update `OLLAMA_HOST` in your `.env` file (e.g. `OLLAMA_HOST=http://192.168.1.50:11434`).
3. **Verify Models are Downloaded**:
   - The semantic cache and LLM loop require the models to be downloaded locally. Run:
     ```bash
     ollama pull nomic-embed-text
     ollama pull qwen2.5-coder:7b-instruct-q4_K_M
     ollama pull qwen2.5-coder:1.5b-instruct-q8_0
     ```

---

## 2. Database Locked Error (SQLite)

### Symptom:
- Error in backend logs: `sqlite3.OperationalError: database is locked`.

### Cause:
SQLite locks the database file when one process is writing and another tries to access/write. In Meridian-X, this can occur if backend threads or multiple instances access SQLite simultaneously.

### Solutions:
1. **WAL Mode Enabled**:
   - Meridian-X attempts to enable Write-Ahead Logging (WAL) mode automatically on startup, which allows concurrent reads and writes safely. Ensure that the database file has not been marked read-only.
2. **Increase Timeout**:
   - The connection timeout is configured to `10.0` seconds in `database.py` (which usually prevents this issue). Do not run multiple developer processes of `api.py` at the same time. Check for ghost processes:
     ```powershell
     Get-Process -Name python | Stop-Process -Force
     ```

---

## 3. MongoDB Connectivity Failures

### Symptom:
- Warning logs: `[MongoDB Graph] MongoDB offline, skipped fact saving`.

### Cause:
MongoDB is utilized for storing structured knowledge graphs and smart clipboard history. If MongoDB is offline, Meridian-X is designed with **graceful degradation** and will continue functioning, storing core state in SQLite and Turbovec files.

### Solutions:
1. **Start MongoDB Service**:
   - On Windows: Open `services.msc`, locate `MongoDB Server`, right-click and choose **Start**.
   - On Linux/macOS: Run `sudo systemctl start mongod` or `brew services start mongodb-community`.
2. **Verify Port**:
   - Make sure MongoDB is listening on the default port `27017` or update `MONGODB_URI` in `.env`.

---

## 4. Audio Input / Microphone Capture Degradation

### Symptom:
- Voice assistant does not register wake words (`Hey Meridian`).
- STT (Speech-to-Text) loops do not transcribe or throw `sounddevice` or `pyaudio` exceptions.

### Solutions:
1. **Check OS Permissions**:
   - Go to System Settings -> Privacy & Security -> Microphone and ensure that terminal/your terminal application has permission to access the microphone.
2. **Verify Microphone Device**:
   - Run `python verify_system.py` to check for active input channels.
   - If your default input device is muted or sample rate is mismatched (e.g. not 16000Hz), adjust your sound control panel properties to `1 channel, 16-bit, 16000Hz (CD Quality)`.

---

## 5. Hardware & VRAM Requirements

Running local models requires sufficient compute capacity. Use this scale to determine the correct configurations in `.env`:

| RAM / VRAM | Recommended Models | Notes |
|---|---|---|
| **8 GB RAM (No GPU)** | `qwen2.5-coder:1.5b` (Brain) <br> `moondream:1.8b` (Vision) | Slow inference speeds, use CPU execution. |
| **16 GB RAM / 6GB VRAM** | `qwen2.5-coder:7b-instruct-q4` (Brain) <br> `moondream:1.8b` (Vision) | Standard developer setup. Fast inference. |
| **32 GB+ RAM / 12GB+ VRAM** | `qwen2.5-coder:14b` or `llama3:8b` (Brain) | Premium setup, high accuracy. |

If you experience high CPU lag, switch `MERIDIAN_MODEL` to a smaller quantized model size (e.g. `1.5b-instruct` or `3b-instruct`).
