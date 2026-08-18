# Meridian-X Codebase Audit: Frontend vs Backend Inconsistencies & Miscommunications

This document details all discovered mismatches, schema discrepancies, protocol differences, and URL resolution inconsistencies between the **React/Tauri Frontend** (`meridian_frontend`) and **FastAPI Backend** (`meridian_backend`).

---

## 1. API URL Resolution & Protocol Hardcoding

### 🚨 Issue 1.1: Relative Fetch Path in `SecurityPanel.tsx`

- **Location**: [`SecurityPanel.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/views/SecurityPanel.tsx#L18)
- **Problem**: `SecurityPanel.tsx` makes a direct fetch call to `/api/security/rotate-key` using a relative path.
- **Impact**: In Tauri desktop app mode (where the app runs under `tauri://localhost` or `http://tauri.localhost`), relative HTTP requests resolve to `tauri://localhost/api/security/rotate-key` instead of `http://localhost:4132/api/security/rotate-key`, causing CORS / 404 network errors.
- **Fix**: Use `${API_BASE_URL}/api/security/rotate-key`.

### ⚠️ Issue 1.2: Inconsistent API Endpoint Host Strategy

- **Location**: [`Timeline.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/views/Timeline.tsx), [`Settings.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/views/Settings.tsx), [`Productivity.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/views/Productivity.tsx)
- **Problem**: Some components use `API_BASE_URL` imported from `config.ts` (e.g. `${API_BASE_URL}/api/chat/stream`), while others directly hardcode `http://localhost:4132/api/...` (e.g. `http://localhost:4132/api/chat/clear`, `http://localhost:4132/api/voice/interrupt`).
- **Impact**: If the backend port changes (e.g. via `PORT` environment variable), hardcoded `http://localhost:4132` endpoints fail while `API_BASE_URL` endpoints adapt.
- **Fix**: Standardize all frontend fetch and EventSource calls to use `API_BASE_URL`.

---

## 2. Schema & Field Property Name Mismatches

### ⚠️ Issue 2.1: Pomodoro Profile Metric Keys

- **Location**: [`Productivity.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/views/Productivity.tsx) vs [`api.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/api.py#L2014)
- **Frontend Expects**: `data.pomodoros`
- **Backend Returns**: `pomodoros_completed` in `/api/developer/stats` and `count` in `/api/pomodoro/status`.
- **Impact**: `Productivity.tsx` display counters show `0` or `undefined` unless fallback logic handles key conversion.

### ⚠️ Issue 2.2: RAG File Ingestion Upload Response Object

- **Location**: [`Timeline.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/views/Timeline.tsx#L548) vs [`api.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/api.py#L1150)
- **Frontend Expects**: `{ filename: string, status: string }`
- **Backend Returns**: `{ name: string, status: string, chunks: number }`
- **Impact**: File upload success toast or log display renders empty filename string (`undefined`).

---

## 3. SSE Stream Protocol & Error Handling Discrepancies

### ⚠️ Issue 3.1: Server-Sent Events (SSE) Error Event Schema

- **Location**: [`Timeline.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/views/Timeline.tsx#L348) vs [`loop_stream.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/loop_stream.py)
- **Frontend Expects**: SSE JSON payload with `type: "error"`, `error: "message"`
- **Backend Behavior**: Certain unhandled exception handlers yield `{"error": "message"}` without top-level `type: "error"`.
- **Impact**: `Timeline.tsx` SSE stream parser misses exception messages and leaves chat stream state pending or frozen.

---

## 4. LocalStorage & Environment Key Name Divergence

### ⚠️ Issue 4.1: Auditor Model Fallback Resolution

- **Location**: [`Settings.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/views/Settings.tsx#L707) vs [`api.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/api.py#L1849) vs Agent Loop modules
- **Frontend Keys**: `meridian_auditor_model` (localStorage & profile payload)
- **Backend Env Key**: `MERIDIAN_AUDITOR_MODEL`
- **Impact**: While profile save maps `meridian_auditor_model` to `MERIDIAN_AUDITOR_MODEL`, fallback code in older agent modules occasionally checked `MERIDIAN_MODEL` instead of `MERIDIAN_AUDITOR_MODEL`.

---

## 5. Tauri Native IPC vs Web App Fallbacks

### ⚠️ Issue 5.1: Unguarded Tauri `invoke()` Calls in Non-Desktop Mode

- **Location**: [`NavRail.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/components/NavRail.tsx), [`Settings.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/views/Settings.tsx)
- **Problem**: Direct calls to `invoke('get_system_usage')` or `invoke('get_theme')`.
- **Impact**: When frontend is opened in standard web browser (`http://localhost:5173`) outside Tauri webview container, `window.__TAURI_INTERNALS__` is undefined, throwing unhandled JS errors.
- **Fix**: Wrap `invoke()` calls in try/catch or guard with `window.__TAURI_INTERNALS__` check.

---

## Summary Table

| Category | Component | Issue Description | Severity | Recommended Fix |
| --- | --- | --- | --- | --- |
| **API Host** | `SecurityPanel.tsx` | Relative `/api/security/rotate-key` fetch | **High** | Prefix with `API_BASE_URL` |
| **API Host** | `Timeline.tsx`, `Settings.tsx` | Mixed hardcoded `http://localhost:4132` | **Medium** | Standardize to `API_BASE_URL` |
| **Schema** | `Productivity.tsx` | `pomodoros` vs `pomodoros_completed` key | **Medium** | Standardize property mapping |
| **Schema** | `Timeline.tsx` | RAG upload `filename` vs `name` | **Low** | Return both `name` and `filename` |
| **SSE Stream** | `Timeline.tsx` | Error events missing `type: "error"` | **Medium** | Enforce `type: "error"` in SSE generator |
| **Tauri IPC** | `NavRail.tsx` | Unguarded `invoke()` in web mode | **Medium** | Add `window.__TAURI_INTERNALS__` guard |
