# Meridian-X: Intelligent Desktop Workspace Companion

Meridian-X is an agentic, context-aware desktop development assistant built with **Tauri, React, FastAPI, SQLite, Turbovec, and local LLMs (Ollama)**. It is designed to act as an offline-first companion that monitors work progress, parses documents, executes secure python sandbox scripts, and secures local workspace environments.

---

## 🚀 Key Features

### 1. 🤖 ReAct Reasoning Agent Loop
* Runs an asynchronous **Reasoning ➔ Acting ➔ Observing** agent flow powered by local models (e.g., `qwen2.5-coder` or custom offline variants).
* Streams live reasoning timelines and thought patterns to the frontend using Server-Sent Events (SSE).

### 2. 🦊 Interactive Mascot Companion
* A dedicated visual companion window that reflects the agent's active cognitive state in real-time.
* Supports visual reaction wardrobes:
  * 🕵️‍♂️ **Detective Hat**: Active during Security Auditor checks.
  * 👷‍♂️ **Construction Hat**: Active during codebase diagnostic audits and self-healing.
  * 🥱 **Tired State**: Triggers when offline fallbacks occur or during Pomodoro break cycles.
  * ✍️ **Typing State**: Reacts in real-time to user keystrokes.

### 3. 🛡️ Security Auditor Consensus & Safety Gates
* Runs local security audits via an isolated validator model (`qwen2.5-coder:1.5b`) for any tool invocation of Tier 2 or higher.
* Uses an authorization safety gate for write/execution operations (Tier 3+), halting execution and awaiting explicit user validation from the chat pane.

### 4. ⚡ Context-Aware Resource Governor
* Monitors system usage to ensure developer performance is unaffected by background processes.
* Skips background intelligence tasks if:
  * System CPU utilization exceeds **85.0%**.
  * Foregrounds match heavy developer/gaming processes (e.g., *Valorant, Cyberpunk, Blender, Unity, Unreal, Visual Studio*).

### 5. 🔑 Cryptographic P2P Database Sync
* Secure database and semantic cache synchronization across local network peer nodes.
* Enforces a handshake token policy (`P2P_SECRET_TOKEN`) to prevent unauthorized rogue nodes from reading or modifying database graphs.

### 6. 📄 Native Offline RAG Document Parser
* Deep file ingestion supporting `.txt`, `.md`, `.json`, `.csv`, `.pdf` (via `pypdf`), and `.docx` (via `python-docx`) natively.
* Seamlessly extracts and chunks documents, creating vector embeddings via local models (`nomic-embed-text`) and saving them into **Turbovec** (vector search) and **SQLite** (metadata storage).

### 7. ✏️ Rich Inline Code Merge Editor
* An interactive self-healing diff code panel.
* Displays character/line metadata count previews.
* Includes a **"Revert to Proposal"** button to allow instant resets of manual diff changes back to the original model proposal.

---

## 🏗️ Architecture Layout

```
                 +-----------------------------------+
                 |           Tauri Webview           |
                 |      (Vite + React Frontend)      |
                 +-----------------------------------+
                       /                       \
        Event Streams /                         \ IPC / HTTP
                     /                           \
                    v                             v
     +---------------------------+       +---------------------------+
     |      Mascot Companion     |       |      FastAPI Backend      |
     |          Window           |       |         (Python)          |
     +---------------------------+       +---------------------------+
                                           /           |           \
                                          /            |            \
                                         v             v             v
                              +------------+    +------------+    +------------+
                              |  Turbovec  |    |   SQLite   |    |  MongoDB   |
                              |  (Vectors) |    | (Metadata) |    |  (Graph)   |
                              +------------+    +------------+    +------------+
                                     \                 |                 /
                                      \                |                /
                                       v               v               v
                                    +-------------------------------------+
                                    |         Local Ollama Engine         |
                                    |     (Inference & Embeddings)        |
                                    +-------------------------------------+
```

---

## 🛠️ Getting Started

### Prerequisites
* **Python 3.10+** (in `meridian_backend/venv`)
* **Node.js** & **npm** (for the Tauri frontend)
* **Ollama** running locally with:
  * `ollama pull qwen2.5-coder:7b-instruct-q4_K_M` (standard reasoning)
  * `ollama pull qwen2.5-coder:1.5b-instruct-q8_0` (auditor validation)
  * `ollama pull nomic-embed-text` (semantic RAG embeddings)

### Configuration (`.env`)
Create a `meridian_backend/.env` file with parameters:
```env
P2P_SECRET_TOKEN=your-secure-handshake-token
OLLAMA_HOST=http://127.0.0.1:11434
MERIDIAN_MODEL=qwen2.5-coder:7b-instruct-q4_K_M
```

### Running the System
You can launch the entire ecosystem using the main script in the workspace root:
```bash
# Start both backend and Tauri frontend
start_meridian.bat
```
Alternatively, run them in separate terminals:
1. **Backend**:
   ```bash
   cd meridian_backend
   venv\Scripts\python.exe api.py
   ```
2. **Frontend**:
   ```bash
   cd meridain_frontend
   npm run dev
   ```

---

## 🧪 Running Automated Tests
Run the integration and unit tests verifying the core system features:
```bash
cd meridian_backend
venv\Scripts\python.exe C:\Users\aryan\.gemini\antigravity-ide\brain\032a8894-1f8a-40eb-b034-64746a282aef\scratch\verify_advanced_features.py
```
