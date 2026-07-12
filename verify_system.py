#!/usr/bin/env python
import os
import sys
import socket
import subprocess
import platform

def print_result(title, success, details=""):
    status = " [OK] " if success else " [FAIL]"
    msg = f"{status} {title}"
    if details:
        msg += f"\n       -> {details}"
    print(msg)

def check_python():
    print("\n--- Checking Python Environment ---")
    py_ver = sys.version.split()[0]
    success = sys.version_info >= (3, 8)
    print_result(f"Python version: {py_ver}", success, "Requires Python >= 3.8")
    
    # Check imports
    modules = {
        "fastapi": "FastAPI backend framework",
        "pymongo": "MongoDB client driver",
        "psutil": "Process and system metrics",
        "httpx": "Async HTTP client",
        "numpy": "Vector calculations",
        "turbovec": "Vector storage database index",
        "ollama": "Local LLM driver client",
        "pydantic": "Data validation models"
    }
    
    for mod, desc in modules.items():
        try:
            __import__(mod)
            print_result(f"Module '{mod}' installed", True, desc)
        except ImportError:
            print_result(f"Module '{mod}' MISSING", False, f"Please install via: pip install {mod}")

def check_node():
    print("\n--- Checking Node.js Environment ---")
    try:
        node_ver = subprocess.check_output(["node", "--version"], text=True).strip()
        print_result(f"Node.js: {node_ver}", True)
    except Exception:
        print_result("Node.js: Not found in path", False, "Required for Tauri and Frontend compilation")
        
    try:
        npm_ver = subprocess.check_output(["npm", "--version"], text=True).strip()
        print_result(f"npm: {npm_ver}", True)
    except Exception:
        print_result("npm: Not found in path", False, "Required for frontend packaging")

def check_databases():
    print("\n--- Checking Databases ---")
    
    # 1. SQLite Check
    db_dir = os.path.join(os.getcwd(), ".meridian")
    db_path = os.path.join(db_dir, "metadata.db")
    try:
        import sqlite3
        os.makedirs(db_dir, exist_ok=True)
        conn = sqlite3.connect(db_path, timeout=5.0)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS system_verify (id INTEGER PRIMARY KEY, ts REAL)")
        cursor.execute("INSERT INTO system_verify (ts) VALUES (?)", (1.0,))
        conn.commit()
        cursor.execute("SELECT id FROM system_verify")
        cursor.fetchone()
        cursor.execute("DROP TABLE system_verify")
        conn.commit()
        conn.close()
        print_result(f"SQLite DB connectivity", True, f"Path: {db_path}")
    except Exception as e:
        print_result("SQLite DB connectivity", False, f"Failed: {e}")
        
    # 2. MongoDB Check
    try:
        import pymongo
        mongo_uri = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/meridian_kg")
        client = pymongo.MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)
        client.admin.command('ping')
        print_result("MongoDB connectivity", True, f"URI: {mongo_uri}")
    except Exception as e:
        print_result("MongoDB connectivity (Optional)", False, f"Unreachable: {e}. Graph storage will fall back.")

def check_ollama():
    print("\n--- Checking Ollama Service ---")
    host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434").strip()
    if not host.startswith("http://") and not host.startswith("https://"):
        host = f"http://{host}"
    try:
        import httpx
        res = httpx.get(f"{host}/api/tags", timeout=3.0)
        if res.status_code == 200:
            models_data = res.json()
            models = [m["name"] for m in models_data.get("models", [])]
            print_result(f"Ollama server reachable", True, f"Host: {host}")
            
            # Check for embedding model
            embed_model = "nomic-embed-text"
            has_embed = any(embed_model in m for m in models)
            print_result(f"Ollama model '{embed_model}' present", has_embed, 
                         "Required for semantic cache and vector retrieval" if not has_embed else "")
            
            # Check provider
            provider = os.environ.get("MERIDIAN_PROVIDER", "ollama").lower()
            brain_model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
            
            if provider == "ollama":
                has_brain = any(brain_model in m for m in models)
                print_result(f"Ollama brain model '{brain_model}' present", has_brain,
                             f"Current active brain LLM model. Installed models: {', '.join(models)}")
            else:
                print_result(f"Using remote provider '{provider}' with model '{brain_model}'", True,
                             f"Ollama model check skipped. Installed local models: {', '.join(models)}")
        else:
            print_result(f"Ollama server returned {res.status_code}", False, f"Check if Ollama service is running on {host}")
    except Exception as e:
        print_result("Ollama server unreachable", False, f"Error: {e}. Check if Ollama is running.")

def check_ports():
    print("\n--- Checking Port Availability ---")
    ports = [8000, 1420] # 8000: Python Backend, 1420: Tauri Frontend Dev Port
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        try:
            s.bind(("127.0.0.1", port))
            print_result(f"Port {port} is free", True)
        except OSError:
            print_result(f"Port {port} is IN USE", False, "May conflict with startup or run loops")
        finally:
            s.close()

def check_audio():
    print("\n--- Checking Audio Subsystem ---")
    try:
        import sounddevice as sd
        devices = sd.query_devices()
        input_devices = [d for d in devices if d['max_input_channels'] > 0]
        if input_devices:
            print_result(f"Audio capture devices: {len(input_devices)} found", True, 
                         f"Default: '{sd.query_devices(kind='input')['name']}'")
        else:
            print_result("Audio capture devices: None found", False, "Voice/Speech control pipeline will degrade")
    except Exception as e:
        # Check pyaudio fallback
        try:
            import pyaudio
            pa = pyaudio.PyAudio()
            count = pa.get_device_count()
            if count > 0:
                 print_result(f"Audio capture devices (PyAudio): {count} found", True)
            else:
                 print_result("Audio capture devices: None found", False, "Voice control will degrade")
            pa.terminate()
        except Exception:
            print_result("Audio drivers (sounddevice/pyaudio) missing or failed", False, 
                         "Please run: pip install sounddevice or pip install pyaudio")

def main():
    # Load .env variables first
    env_path = os.path.join(os.getcwd(), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ[key.strip()] = val.strip().strip("\"'")

    print("=========================================")
    print("       Meridian-X System Verification     ")
    print("=========================================")
    print(f"Platform: {platform.system()} {platform.release()} ({platform.machine()})")
    
    check_python()
    check_node()
    check_databases()
    check_ollama()
    check_ports()
    check_audio()
    
    print("\n=========================================")
    print("Verification complete.")

if __name__ == "__main__":
    main()
