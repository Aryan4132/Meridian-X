import argparse
import asyncio
import os
import sys
import json
import time

# Insert backend folder into path for core imports
backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meridian_backend")
sys.path.insert(0, backend_dir)

from src.core.loop import run_react_agent_loop
from api import get_ollama_client_host

async def run_cli_goal(goal: str, model: str):
    print(f"🚀 Initializing Meridian CLI Loop for goal: '{goal}'...")
    print(f"🧠 Model: {model}")
    print("--------------------------------------------------")
    
    ollama_host = get_ollama_client_host()
    
    # Run the generator
    async for event_str in run_react_agent_loop(goal, model, ollama_host):
        # Parse SSE events for CLI output
        lines = event_str.split("\n")
        event_type = ""
        data_parts = []
        for line in lines:
            if line.startswith("event:"):
                event_type = line.split(":", 1)[1].strip()
            elif line.startswith("data:"):
                data_parts.append(line.split(":", 1)[1])
        
        data = "\n".join(data_parts)
        if not data:
            continue
            
        if event_type == "thought":
            try:
                thought = json.loads(data)
                t_type = thought.get("type", "info").upper()
                text = thought.get("text", "")
                append = thought.get("append", False)
                
                if t_type == "PLANNING":
                    if append:
                        print(text, end="", flush=True)
                    else:
                        print(f"\n🤔 [Thought] {text}")
                elif t_type == "EXEC":
                    print(f"\n⚙️ [Action] {text}")
                    if "tool" in thought:
                        print(f"   Tool: {thought.get('tool')} Args: {thought.get('command')}")
                elif t_type == "STATUS":
                    print(f"\n✅ [Status] {text}")
                elif t_type == "WARNING":
                    print(f"\n⚠️ [Warning] {text}")
            except Exception:
                print(f"\n💭 {data}")
        elif event_type == "text":
            print(data, end="", flush=True)
        elif event_type == "confirmation":
            try:
                conf = json.loads(data)
                print("\n--------------------------------------------------")
                print(f"🚨 [SAFETY GATE] Action requires confirmation (Tier {conf.get('tier')})")
                print(f"   Tool: {conf.get('tool')}")
                print(f"   Args: {json.dumps(conf.get('args'), indent=2)}")
                
                # Block and read input on CLI
                ans = input("   Approve execution? (y/n): ")
                approved = ans.lower().strip() == 'y'
                
                # Directly approve in local memory since loop is running in CLI process
                from src.core.loop import active_confirmations
                conf_id = conf.get("id")
                if conf_id in active_confirmations:
                    active_confirmations[conf_id]["approved"] = approved
                    active_confirmations[conf_id]["event"].set()
                else:
                    # Fallback to REST confirm call if it was routed to the background API
                    import httpx
                    try:
                        httpx.post("http://127.0.0.1:4132/api/chat/confirm", json={"id": conf_id, "approved": approved}, timeout=2.0)
                    except Exception:
                        pass
                print("--------------------------------------------------\n")
            except Exception as e:
                print("Failed to process CLI confirmation:", e)

    print("\n--------------------------------------------------")
    print("🎯 Task completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Meridian-X: Autonomous Offline Desktop Agent")
    parser.add_argument("--goal", type=str, help="Execute a single goal autonomously via CLI")
    parser.add_argument("--model", type=str, default="qwen2.5-coder:7b-instruct-q4_K_M", help="Ollama model override")
    args = parser.parse_args()
    
    if args.goal:
        # Before running, launch backend in background so local REST endpoints like confirm/systems are online
        print("[System] Launching background FastAPI server for local API routing...")
        import subprocess
        backend_proc = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "api:app", "--host", "127.0.0.1", "--port", "4132"],
            cwd=backend_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        # Give server time to bind port
        time.sleep(1.5)
        
        try:
            asyncio.run(run_cli_goal(args.goal, args.model))
        finally:
            print("[System] Terminating background FastAPI server...")
            backend_proc.terminate()
            backend_proc.wait()
    else:
        # Default behavior: run FastAPI server in this process
        print("[System] Starting API Backend server...")
        os.chdir(backend_dir)
        import uvicorn
        from api import app
        uvicorn.run(app, host="0.0.0.0", port=4132)
