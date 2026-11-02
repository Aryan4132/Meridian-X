#!/usr/bin/env python3
"""
Meridian-X Universal Doctor & Self-Healing Pre-flight CLI.
Runs comprehensive diagnostics on Python runtime, ML/Audio runtimes, SQLite schemas,
Ollama daemon, networking ports, frontend build assets, and mobile Flutter SDK.

Usage:
    python doctor.py
    python doctor.py --fix
    python doctor.py --json
"""

import sys
import os
import json
import socket
import sqlite3
import argparse
import subprocess
import platform
from typing import Dict, Any, List, Optional

# Reconfigure stdout/stderr to UTF-8 on Windows consoles to support rich glyphs safely
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

try:
    import urllib.request
    import urllib.error
except ImportError:
    pass

ANSI_CYAN = "\033[96m"
ANSI_GREEN = "\033[92m"
ANSI_YELLOW = "\033[93m"
ANSI_RED = "\033[91m"
ANSI_BOLD = "\033[1m"
ANSI_DIM = "\033[2m"
ANSI_RESET = "\033[0m"

def colorize(text: str, color_code: str) -> str:
    if os.environ.get("NO_COLOR") or not sys.stdout.isatty():
        return text
    return f"{color_code}{text}{ANSI_RESET}"

def check_python_runtime() -> Dict[str, Any]:
    v = sys.version_info
    ver_str = f"{v.major}.{v.minor}.{v.micro}"
    is_supported = v.major == 3 and v.minor >= 10
    in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    
    return {
        "name": "Python Environment",
        "status": "PASS" if is_supported else "FAIL",
        "version": ver_str,
        "executable": sys.executable,
        "in_virtualenv": in_venv,
        "message": f"Python {ver_str} ({'virtualenv' if in_venv else 'system global'})" if is_supported else f"Python 3.10+ required; found {ver_str}"
    }

def check_dependencies() -> Dict[str, Any]:
    deps = {
        "fastapi": "FastAPI Web Engine",
        "uvicorn": "ASGI Server",
        "pydantic": "Data Schemas",
        "torch": "PyTorch ML Runtime",
        "onnxruntime": "ONNX Wakeword Inference",
        "sounddevice": "Audio I/O Driver",
        "playwright": "Headless Browser Automation",
    }
    results = {}
    missing_critical = []
    
    for mod_name, label in deps.items():
        try:
            m = __import__(mod_name)
            ver = getattr(m, "__version__", "installed")
            results[mod_name] = {"installed": True, "version": str(ver), "label": label}
        except ImportError:
            results[mod_name] = {"installed": False, "version": None, "label": label}
            if mod_name in ("fastapi", "uvicorn", "pydantic"):
                missing_critical.append(mod_name)
                
    status = "FAIL" if missing_critical else ("WARN" if not results.get("torch", {}).get("installed") else "PASS")
    return {
        "name": "Python Package Dependencies",
        "status": status,
        "modules": results,
        "missing_critical": missing_critical,
        "message": f"{len(deps) - len(missing_critical)}/{len(deps)} libraries available"
    }

def check_database() -> Dict[str, Any]:
    # Look for database in typical locations
    db_candidates = [
        os.path.join(os.path.dirname(__file__), "meridian_memory", "metadata.db"),
        os.path.join(os.path.dirname(__file__), "meridian_backend", "meridian.db"),
        os.path.join(os.path.dirname(__file__), "meridian.db"),
        os.path.join(os.path.dirname(__file__), "meridian_data", "meridian.db"),
    ]
    db_path = None
    for cand in db_candidates:
        if os.path.exists(cand):
            db_path = cand
            break

    if not db_path:
        db_path = db_candidates[0]

    if not os.path.exists(db_path):
        return {
            "name": "Database & Storage",
            "status": "WARN",
            "path": db_path,
            "exists": False,
            "message": f"Database not yet created at {db_path} (will auto-create on first backend startup)"
        }

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("PRAGMA journal_mode;")
        journal_mode = cur.fetchone()[0]
        cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table';")
        table_count = cur.fetchone()[0]
        
        # Test FTS5 support
        fts5_supported = False
        try:
            cur.execute("CREATE VIRTUAL TABLE IF NOT EXISTS _doctor_fts_test USING fts5(content);")
            cur.execute("DROP TABLE _doctor_fts_test;")
            fts5_supported = True
        except Exception:
            fts5_supported = False
            
        conn.close()
        
        return {
            "name": "Database & Storage",
            "status": "PASS",
            "path": db_path,
            "exists": True,
            "journal_mode": journal_mode,
            "table_count": table_count,
            "fts5_supported": fts5_supported,
            "message": f"SQLite WAL: {journal_mode.upper()} | {table_count} tables | FTS5: {'Active' if fts5_supported else 'Disabled'}"
        }
    except Exception as e:
        return {
            "name": "Database & Storage",
            "status": "FAIL",
            "path": db_path,
            "exists": True,
            "error": str(e),
            "message": f"Failed to connect to database: {e}"
        }

def check_ollama(host: Optional[str] = None) -> Dict[str, Any]:
    raw_url = host or os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
    if not raw_url.startswith("http://") and not raw_url.startswith("https://"):
        raw_url = f"http://{raw_url}"
    ollama_url = raw_url.replace("://0.0.0.0", "://127.0.0.1")
    if ollama_url in ("http://127.0.0.1", "http://localhost"):
        ollama_url = f"{ollama_url}:11434"
        
    tags_url = f"{ollama_url.rstrip('/')}/api/tags"
    try:
        req = urllib.request.Request(tags_url, headers={"User-Agent": "MeridianX-Doctor"})
        with urllib.request.urlopen(req, timeout=3.0) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            models = [m.get("name") for m in data.get("models", [])]
            return {
                "name": "Local AI Engine (Ollama)",
                "status": "PASS",
                "url": ollama_url,
                "reachable": True,
                "models": models,
                "model_count": len(models),
                "message": f"Online at {ollama_url} with {len(models)} model(s) ({', '.join(models[:3])}{'...' if len(models) > 3 else ''})"
            }
    except Exception as e:
        return {
            "name": "Local AI Engine (Ollama)",
            "status": "WARN",
            "url": ollama_url,
            "reachable": False,
            "models": [],
            "error": str(e),
            "message": f"Ollama not running at {ollama_url}. Cloud providers (OpenAI/Anthropic/Gemini) can still be used."
        }

def is_port_in_use(port: int, host: str = "127.0.0.1") -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex((host, port)) == 0

def check_ports() -> Dict[str, Any]:
    port_specs = [
        {"port": 4132, "name": "Meridian Backend API & WebSocket", "expected": "Available or Active Backend"},
        {"port": 4133, "name": "Companion / Frontend Dev Port", "expected": "Available or Vite Dev"},
        {"port": 11434, "name": "Ollama Local LLM Server", "expected": "Active if local LLMs used"},
    ]
    
    ports_status = []
    for p in port_specs:
        in_use = is_port_in_use(p["port"])
        ports_status.append({
            "port": p["port"],
            "name": p["name"],
            "in_use": in_use,
            "status": "OCCUPIED" if in_use else "AVAILABLE"
        })
        
    return {
        "name": "Port & Socket Allocation",
        "status": "PASS",
        "ports": ports_status,
        "message": " | ".join(f"{p['port']}: {'IN USE' if p['in_use'] else 'FREE'}" for p in ports_status)
    }

def check_frontend() -> Dict[str, Any]:
    repo_root = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(repo_root, "meridian_frontend", "dist")
    index_html = os.path.join(dist_dir, "index.html")
    is_built = os.path.exists(index_html)
    
    node_version = None
    try:
        res = subprocess.run(["node", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2.0)
        if res.returncode == 0:
            node_version = res.stdout.strip()
    except Exception:
        pass

    return {
        "name": "Frontend Assets (React/Vite)",
        "status": "PASS" if is_built else "WARN",
        "dist_exists": is_built,
        "dist_path": dist_dir,
        "node_version": node_version,
        "message": f"Production dist bundle {'ready' if is_built else 'not yet compiled (run npm run build)'} | Node: {node_version or 'N/A'}"
    }

def check_mobile_toolchain() -> Dict[str, Any]:
    repo_root = os.path.dirname(os.path.abspath(__file__))
    mobile_dir = os.path.join(repo_root, "meridian_mobile")
    has_mobile_project = os.path.exists(os.path.join(mobile_dir, "pubspec.yaml"))
    
    flutter_version = None
    try:
        res = subprocess.run(["flutter", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=3.0)
        if res.returncode == 0:
            flutter_version = res.stdout.split("\n")[0].strip()
    except Exception:
        pass

    status = "PASS" if (has_mobile_project and flutter_version) else "INFO"
    return {
        "name": "Mobile Companion (Flutter)",
        "status": status,
        "project_exists": has_mobile_project,
        "flutter_cli": flutter_version or "Not found in PATH (Optional for mobile dev)",
        "message": f"Flutter project: {'Found' if has_mobile_project else 'Missing'} | CLI: {flutter_version or 'Optional'}"
    }

def perform_self_healing() -> List[str]:
    actions_taken = []
    repo_root = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Ensure required data directories exist
    dirs_to_create = [
        os.path.join(repo_root, "meridian_data"),
        os.path.join(repo_root, "meridian_backend", "data"),
    ]
    for d in dirs_to_create:
        if not os.path.exists(d):
            os.makedirs(d, exist_ok=True)
            actions_taken.append(f"Created missing directory: {d}")

    # 2. Check for zombie/hung processes on port 4132 if user desires clean slate
    try:
        import psutil
        for conn in psutil.net_connections(kind="inet"):
            if conn.laddr and conn.laddr.port == 4132 and conn.status == psutil.CONN_LISTEN:
                pid = conn.pid
                if pid and pid != os.getpid():
                    p = psutil.Process(pid)
                    p_name = p.name()
                    p.terminate()
                    actions_taken.append(f"Terminated stale process listening on port 4132 (PID: {pid}, Name: {p_name})")
    except Exception as e:
        actions_taken.append(f"Port 4132 check note: {e}")

    # 3. Initialize SQLite tables if database file missing
    db_path = os.path.join(repo_root, "meridian_backend", "meridian.db")
    if not os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("CREATE TABLE IF NOT EXISTS system_metadata (key TEXT PRIMARY KEY, value TEXT);")
            conn.commit()
            conn.close()
            actions_taken.append(f"Initialized blank SQLite WAL database at {db_path}")
        except Exception as e:
            actions_taken.append(f"Failed to auto-init DB: {e}")

    return actions_taken

def run_doctor(auto_fix: bool = False, verbose: bool = False) -> Dict[str, Any]:
    checks = [
        check_python_runtime(),
        check_dependencies(),
        check_database(),
        check_ollama(),
        check_ports(),
        check_frontend(),
        check_mobile_toolchain(),
    ]
    
    fixes = []
    if auto_fix:
        fixes = perform_self_healing()
        
    overall_status = "PASS"
    for c in checks:
        if c["status"] == "FAIL":
            overall_status = "FAIL"
            break
        elif c["status"] == "WARN" and overall_status != "FAIL":
            overall_status = "WARN"

    return {
        "status": overall_status,
        "platform": f"{platform.system()} {platform.release()} ({platform.machine()})",
        "checks": checks,
        "fixes_applied": fixes,
    }

def print_doctor_report(report: Dict[str, Any], verbose: bool = False) -> None:
    print("\n" + "=" * 65)
    print(colorize("  🩺  MERIDIAN-X SYSTEM DOCTOR & PRE-FLIGHT DIAGNOSTICS", ANSI_BOLD + ANSI_CYAN))
    print("=" * 65)
    print(f" Platform: {report['platform']}\n")

    status_icons = {
        "PASS": colorize(" [OK] ", ANSI_GREEN + ANSI_BOLD),
        "WARN": colorize(" [WARN] ", ANSI_YELLOW + ANSI_BOLD),
        "FAIL": colorize(" [FAIL] ", ANSI_RED + ANSI_BOLD),
        "INFO": colorize(" [INFO] ", ANSI_CYAN),
    }

    for c in report["checks"]:
        icon = status_icons.get(c["status"], "[?]")
        print(f" {icon} {colorize(c['name'], ANSI_BOLD)}")
        print(f"        {c['message']}")
        if verbose and "modules" in c:
            for mod, meta in c["modules"].items():
                mod_status = colorize("✓", ANSI_GREEN) if meta["installed"] else colorize("✗", ANSI_RED)
                print(f"          {mod_status} {mod:<14} ({meta['label']}) -> {meta['version'] or 'missing'}")
        if verbose and "ports" in c:
            for p in c["ports"]:
                print(f"          - Port {p['port']:<5} : {p['name']} -> {p['status']}")
        print()

    if report["fixes_applied"]:
        print(colorize(" 🛠️  SELF-HEALING ACTIONS PERFORMED:", ANSI_BOLD + ANSI_GREEN))
        for f in report["fixes_applied"]:
            print(f"   • {f}")
        print()

    print("-" * 65)
    final_status = report["status"]
    if final_status == "PASS":
        print(colorize(" ✅ All critical subsystems are operational and ready to run!", ANSI_GREEN + ANSI_BOLD))
    elif final_status == "WARN":
        print(colorize(" ⚠️  System operational with minor warnings (non-critical).", ANSI_YELLOW + ANSI_BOLD))
    else:
        print(colorize(" ❌ Critical check failed. Run `python doctor.py --fix` or resolve errors.", ANSI_RED + ANSI_BOLD))
    print("=" * 65 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Meridian-X Universal Doctor & Pre-Flight Check")
    parser.add_argument("--fix", action="store_true", help="Automatically heal common issues (ports, folders, db)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show granular sub-check output")
    parser.add_argument("--json", action="store_true", help="Output raw JSON diagnostic report")
    
    args = parser.parse_args()
    report = run_doctor(auto_fix=args.fix, verbose=args.verbose)
    
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_doctor_report(report, verbose=args.verbose)

    if report["status"] == "FAIL":
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
