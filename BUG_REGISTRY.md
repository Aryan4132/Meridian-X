# Meridian-X — Permanent Bug Registry

> Living document. Append a new section after every audit. Never delete old entries — mark them `[FIXED]`.
> Last updated: **2026-06-17**

---

## Round 1 — June 17 2026 (All Fixed ✅)

| ID | Sev | File | Description | Status |
|---|---|---|---|---|
| BUG-1 | 🔴 | `discord_bridge.py` | Circular import (`from api import`) + sync LLM call blocking bot event loop | ✅ Fixed |
| BUG-2 | 🔴 | `database.py:65` | `res.get("embedding")` on ollama object — all embeddings returned zero vector | ✅ Fixed |
| BUG-3 | 🔴 | `loop.py:23` | `_loop_interrupted` bool not thread-safe with voice-monitor thread | ✅ Fixed |
| BUG-4 | 🟠 | `api.py:686` | `apiProvider=None` crashes cloud chat stream with 500 error | ✅ Fixed |
| BUG-5 | 🟠 | `loop.py:897,905,1668` | HTP worker prompts written to conversation DB — polluted user history | ✅ Fixed |
| BUG-6 | 🟠 | `scheduler.py:123` | `loop.close()` skipped on job failure — event loop leaked every error | ✅ Fixed |
| BUG-7 | 🟠 | `proactive.py:737` | `socket.setdefaulttimeout(2.0)` permanently altered global process timeout | ✅ Fixed |
| BUG-9 | 🟡 | `database.py:627` | `conn.close()` outside finally — left open on Turbovec rebuild failure | ✅ Fixed |
| BUG-10 | 🟡 | `loop.py:1273,1656` | `active_debates` dict never pruned — unbounded memory growth | ✅ Fixed |
| BUG-11 | 🟡 | `loop.py:1228` | Consensus debate ran on empty finish text — wasted 2 LLM calls | ✅ Fixed |
| BUG-12 | 🟡 | `discord_bridge.py:33` | `_loop` never closed in `stop_discord_bridge()` — loop object leaked | ✅ Fixed |
| BUG-13 | 🔵 | `api.py:676` | Shortcut `chat_stream` emitted malformed SSE for multi-line text | ✅ Fixed |
| BUG-14 | 🔵 | `loop.py:1190` | Temp self-question history entry not removed on voice barge-in return | ✅ Fixed |

---

## Round 2 — June 17 2026 (All Fixed ✅)

### BUG-15 🔴 CRITICAL — `telegram_bridge.py:139` + `whatsapp_bridge.py:141`

**Pattern:** Same circular import as BUG-1, never patched in the other two bridges.

```python
# telegram_bridge.py:139
from api import get_react_thoughts   # circular: api imports telegram_bridge at startup

# whatsapp_bridge.py:141
from api import get_react_thoughts   # same issue
```

Both bridges are launched by `api.py` lifespan. Importing `api` inside their handlers creates a circular dependency. Additionally `get_react_thoughts` is **synchronous** — in `whatsapp_bridge.py` this blocks Playwright's sync event loop; in `telegram_bridge.py` it blocks the poll thread for the full LLM inference time (20-60s), during which Telegram's 10-second long-poll times out and re-issues the update, causing the message to be **processed twice**.

**Fix:** Replace `get_react_thoughts` with direct `run_react_agent_loop` in a new event loop:
```python
import asyncio
from src.core.loop import run_react_agent_loop

model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
ollama_host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")

loop = asyncio.new_event_loop()
reply_parts = []
async def _run():
    async for event in run_react_agent_loop(prompt_text, model, ollama_host):
        if event.startswith("event: text\n"):
            for line in event.splitlines():
                if line.startswith("data: "):
                    reply_parts.append(line[6:])
try:
    loop.run_until_complete(_run())
finally:
    loop.close()

reply_text = "".join(reply_parts).strip() or "Task completed."
```

---

### BUG-16 🟠 HIGH — `shell.py:23` + `shell.py:97`

**Pattern:** `res.get("response", "")` called on `ollama.GenerateResponse` object (same root cause as BUG-2).

```python
command = res.get("response", "").strip()    # line 23 — AttributeError
fix_command = fix_res.get("response", "").strip()  # line 97 — AttributeError
```

Both calls silently fail and return empty strings. `nl_to_shell` returns `""`, then `nl_run` hits the guard `if command.startswith("Error")` which is false, and executes an empty PowerShell command.

**Fix:**
```python
command = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
fix_command = (fix_res.response if hasattr(fix_res, "response") else fix_res.get("response", "")).strip()
```

---

### BUG-17 🟠 HIGH — `p2p.py:116-120`

**Pattern 1 (line 116-117):** UDP broadcast message parsed with `.split(":")` — breaks for IPv6 peers and malformed packets.
```python
peer_info = msg.split(":")
peer_port = int(peer_info[1])   # IndexError if only one token; ValueError if not int
```

**Pattern 2 (line 120):** Self-detect uses only the primary hostname IP, misses loopback and secondary adapters.
```python
if peer_ip != socket.gethostbyname(socket.gethostname()) or peer_port != self.port:
    self.peers.add(...)   # adds self on machines where hostname resolves to 127.0.0.1
```

**Fix (port parsing):**
```python
# Use rsplit from the right to safely extract port regardless of IP format
remainder = msg[len("MERIDIAN_PEER:"):]
parts = remainder.rsplit(":", 1)
peer_port = int(parts[-1])
```

**Fix (self-detect):**
```python
try:
    local_ips = {info[4][0] for info in socket.getaddrinfo(socket.gethostname(), None)}
    local_ips.update({"127.0.0.1", "::1", "0.0.0.0"})
except Exception:
    local_ips = {"127.0.0.1", "::1"}
if peer_ip not in local_ips or peer_port != self.port:
    self.peers.add((peer_ip, peer_port))
```

---

### BUG-18 🟠 HIGH — `developer.py:272`

**Pattern:** `asyncio.Lock()` instantiated at module-import time, before any event loop exists.

```python
_lsp_client_lock = asyncio.Lock()   # created outside event loop context
```

In Python ≥ 3.10 this emits `DeprecationWarning`; in Python ≥ 3.12 the lock is attached to no loop. When `async with _lsp_client_lock` is later awaited inside `run_react_agent_loop`'s loop, Python raises `RuntimeError: Task got Future <Lock> attached to a different loop`.

**Fix:** Lazy-initialize the lock inside the coroutine:
```python
_lsp_client_lock: Optional[asyncio.Lock] = None

async def _get_lsp_client() -> LspClient:
    global _lsp_client_instance, _lsp_client_lock
    if _lsp_client_lock is None:
        _lsp_client_lock = asyncio.Lock()
    async with _lsp_client_lock:
        ...
```

---

### BUG-19 🟡 MEDIUM — `wakeword.py:79`

**Pattern:** Hardcoded model key derived from an assumed filename.

```python
score = predictions.get('hey_meridian', 0.0)
```

The key in `predictions` is the `.onnx` stem filename. If the model file is renamed (e.g., `hey_meridian_v2.onnx`), this returns `0.0` on every chunk — the wake word **silently never triggers**.

**Fix:**
```python
score = max(predictions.values()) if predictions else 0.0
```

---

### BUG-20 🟡 MEDIUM — `telegram_bridge.py:43-54`

**Pattern:** Single `httpx.Client` reused across all poll iterations; not reset after transport errors.

```python
client = httpx.Client(timeout=15.0)
while TELEGRAM_ACTIVE:
    try:
        res = client.get(...)
    except Exception as e:
        time.sleep(5.0)
        continue   # broken connection pool reused on next iteration
```

After any `httpx.ConnectError` or `httpx.RemoteProtocolError`, the internal pool is broken. Every subsequent request silently fails until the process restarts.

**Fix:**
```python
except httpx.TransportError:
    try:
        client.close()
    except Exception:
        pass
    client = httpx.Client(timeout=15.0)
    time.sleep(5.0)
    continue
```

---

### BUG-21 🟡 MEDIUM — `p2p.py:242`

**Pattern:** `s.recv(4096)` truncates large sync-reply JSON payloads.

```python
resp = s.recv(4096).decode('utf-8')
result = json.loads(resp)   # JSONDecodeError if payload > 4096 bytes
```

If the peer sends back a summary larger than 4 KB, `json.loads` raises `JSONDecodeError`. The outer `except Exception` on line 250 swallows it, logging it as a peer failure.

**Fix:**
```python
chunks = []
while True:
    chunk = s.recv(4096)
    if not chunk:
        break
    chunks.append(chunk)
resp = b"".join(chunks).decode("utf-8")
result = json.loads(resp)
```

---

### BUG-23 🔵 LOW — `watcher.py:91`

**Pattern:** `os.makedirs("")` raises `FileNotFoundError` for bare-filename paths.

```python
os.makedirs(os.path.dirname(abs_path), exist_ok=True)
```

If `file_path` is `"app.log"` (no directory component), `os.path.dirname` returns `""`, and `os.makedirs("")` raises `FileNotFoundError`.

**Fix:**
```python
parent = os.path.dirname(abs_path)
if parent:
    os.makedirs(parent, exist_ok=True)
```

---

## Round 2 Summary Table

| ID | Severity | File | Short Description | Status |
|---|---|---|---|---|
| BUG-15 | 🔴 Critical | `telegram_bridge.py`, `whatsapp_bridge.py` | Circular `from api import` + sync LLM → double-delivery on Telegram | ✅ Fixed |
| BUG-16 | 🟠 High | `shell.py:23,97` | `.get("response")` on ollama object → NL shell silently produces empty commands | ✅ Fixed |
| BUG-17 | 🟠 High | `p2p.py:116,120` | Port parse breaks on IPv6; self-detect adds own node as peer | ✅ Fixed |
| BUG-18 | 🟠 High | `developer.py:272` | `asyncio.Lock()` at module import → attached to wrong event loop in Python 3.12 | ✅ Fixed |
| BUG-19 | 🟡 Medium | `wakeword.py:79` | Hardcoded model key → wake word silently stops on file rename | ✅ Fixed |
| BUG-20 | 🟡 Medium | `telegram_bridge.py:43` | Broken `httpx.Client` reused after network error → permanent poll failure | ✅ Fixed |
| BUG-21 | 🟡 Medium | `p2p.py:242` | `recv(4096)` truncates large JSON sync replies → `JSONDecodeError` | ✅ Fixed |
| BUG-23 | 🔵 Low | `watcher.py:91` | `os.makedirs("")` raises if bare filename passed with no parent directory | ✅ Fixed |

---

## How to Use This Registry

1. **After every feature addition or refactor**, run `py_compile` on changed files and append new findings here.
2. **Severity guide:**
   - 🔴 Critical = will crash or silently corrupt data in production
   - 🟠 High = wrong behavior or user-visible 500 errors
   - 🟡 Medium = edge-case, resource leak, or latent failure
   - 🔵 Low = minor, cosmetic, or improvement
3. **Never remove fixed bugs** — mark them `✅ Fixed` with the date for audit trail.
4. **Reference Bug IDs in commit messages** (e.g., `Fix BUG-15: telegram circular import`).
5. **Quick re-audit command:**
   ```powershell
   cd meridian_backend
   Get-ChildItem -Recurse -Filter "*.py" | Where-Object { $_.FullName -notlike "*venv*" -and $_.FullName -notlike "*__pycache__*" } | ForEach-Object { $r = & venv\Scripts\python.exe -m py_compile $_.FullName 2>&1; if ($r) { Write-Host "FAIL: $($_.FullName)"; Write-Host $r } }; Write-Host "--- Syntax scan complete ---"
   ```
