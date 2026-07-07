import os
import time
import glob
import threading
import json
import mss
import pyautogui
import ollama
from typing import List, Dict, Any
from database import get_ollama_client_host
from database import get_mongo_db

# Active recording states
_recording_active = False
_record_thread = None
_frames_captured = 0

def _get_active_model() -> str:
    return os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")

def _get_vision_model() -> str:
    return os.environ.get("MERIDIAN_VISION_MODEL", "moondream:1.8b")

def _recording_worker(output_dir: str, fps: float):
    global _recording_active, _frames_captured
    os.makedirs(output_dir, exist_ok=True)
    
    with mss.mss() as sct:
        delay = 1.0 / fps
        while _recording_active:
            start_time = time.time()
            file_path = os.path.join(output_dir, f"frame_{int(time.time() * 1000)}.png")
            sct.shot(output=file_path)
            _frames_captured += 1
            
            # Match FPS frequency delay
            elapsed = time.time() - start_time
            sleep_time = max(0.01, delay - elapsed)
            time.sleep(sleep_time)

def record_screen(output_dir: str = "recordings", fps: float = 2.0) -> str:
    """Start capturing screen frames in the background at a specified frame rate (FPS)."""
    global _recording_active, _record_thread, _frames_captured
    if _recording_active:
        return "Error: Screen recording is already active."
        
    _recording_active = True
    _frames_captured = 0
    _record_thread = threading.Thread(target=_recording_worker, args=(output_dir, fps), daemon=True)
    _record_thread.start()
    return f"Started recording screen frames to '{output_dir}/' at {fps} FPS."

def stop_recording() -> str:
    """Stop screen frame capturing and return the total count of saved frames."""
    global _recording_active, _frames_captured
    if not _recording_active:
        return "No screen recording session is currently running."
        
    _recording_active = False
    if _record_thread:
        _record_thread.join(timeout=2.0)
    return f"Stopped screen recording. Captured {_frames_captured} frames."

def analyze_recording(frame_dir: str) -> str:
    """Analyze a directory of captured frames, sampling keyframes with Moondream to extract a workflow action plan."""
    if not os.path.exists(frame_dir):
        return f"Error: Frame directory '{frame_dir}' does not exist."
        
    frames = sorted(glob.glob(os.path.join(frame_dir, "frame_*.png")))
    if not frames:
        return f"No image frames discovered in '{frame_dir}'."
        
    client = ollama.Client(host=get_ollama_client_host())
    
    # Sample every 5th frame to avoid LLM rate limits/slowness
    sampled = frames[::5]
    descriptions = []
    
    print(f"[Recording Analyzer] Analyzing {len(sampled)} sampled frames out of {len(frames)} total...")
    for idx, fpath in enumerate(sampled):
        prompt = (
            "Analyze this screenshot from a screen recording of a user task. "
            "Identify the specific action the user is performing (e.g. clicking a text field, typing, navigating) "
            "and list the coordinates or elements involved in 1 short sentence."
        )
        try:
            res = client.generate(model=_get_vision_model(), prompt=prompt, images=[fpath])
            desc = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
            descriptions.append(f"Step {idx+1}: {desc}")
        except Exception as e:
            descriptions.append(f"Step {idx+1}: Failed to analyze frame due to {e}")
            
    # Compile the analysis into a sequence of execution commands
    prompt_qwen = (
        "You are a robotic macro compiler. Translate the following timeline of visual user actions "
        "into a structured JSON list representing a replayable workflow action plan.\n"
        "Supported action formats:\n"
        "- Click: {\"action\": \"click\", \"x\": int, \"y\": int}\n"
        "- Type: {\"action\": \"type\", \"text\": \"string\"}\n"
        "- Hotkey: {\"action\": \"hotkey\", \"keys\": [\"ctrl\", \"c\"]}\n\n"
        "Timeline:\n" + "\n".join(descriptions) + "\n\n"
        "Respond with ONLY the raw JSON array. No markdown fences or explanations."
    )
    try:
        res_qwen = client.generate(model=_get_active_model(), prompt=prompt_qwen)
        action_plan = (res_qwen.response if hasattr(res_qwen, "response") else res_qwen.get("response", "[]")).strip()
        if action_plan.startswith("```"):
            action_plan = action_plan.strip("`").replace("json\n", "").strip()
        return action_plan
    except Exception as e:
        return f"Failed to compile timeline actions: {e}"

def save_workflow(name: str, action_plan: str) -> str:
    """Save a compiled macro workflow action plan to MongoDB."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline. Workflow could not be saved."
        
    try:
        col = db["workflows"]
        # Parse action_plan string to ensure it's valid JSON
        plan_list = json.loads(action_plan)
        col.update_one(
            {"name": name},
            {"$set": {"plan": plan_list, "timestamp": time.time()}},
            upsert=True
        )
        return f"Successfully saved macro workflow '{name}' in database."
    except Exception as e:
        return f"Failed to save workflow: {e}"

def replay_workflow(name: str) -> str:
    """Execute a saved macro workflow action plan step-by-step using PyAutoGUI."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline. Replay unavailable."
        
    try:
        col = db["workflows"]
        wf = col.find_one({"name": name})
        if not wf:
            return f"Workflow '{name}' not found."
            
        plan = wf.get("plan", [])
        if not plan:
            return f"Workflow '{name}' contains no steps."
            
        # Temporarily enable PyAutoGUI safety fail-safe
        pyautogui.FAILSAFE = True
        
        steps_executed = 0
        for step in plan:
            action = step.get("action")
            if action == "click":
                x = int(step.get("x", 0))
                y = int(step.get("y", 0))
                pyautogui.click(x, y)
                steps_executed += 1
            elif action == "type":
                text = str(step.get("text", ""))
                # BUG-43 fix: pyautogui.typewrite() silently drops non-ASCII characters
                # (accented, CJK, emoji). Use clipboard paste for full Unicode support.
                try:
                    import pyperclip
                    pyperclip.copy(text)
                    pyautogui.hotkey('ctrl', 'v')
                except ImportError:
                    # Fallback to typewrite if pyperclip not available
                    pyautogui.typewrite(text)
                steps_executed += 1
            elif action == "hotkey":
                keys = list(step.get("keys", []))
                if keys:
                    pyautogui.hotkey(*keys)
                    steps_executed += 1
            time.sleep(0.5) # Grace period between steps
            
        return f"Successfully replayed macro workflow '{name}'. Executed {steps_executed} actions."
    except Exception as e:
        return f"Failed to replay workflow: {e}"

def list_workflows() -> str:
    """List all saved workflows available in MongoDB."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col = db["workflows"]
        wfs = list(col.find({}, {"_id": 0}))
        if not wfs:
            return "No workflows found in database."
        lines = ["Saved workflows:"]
        for w in wfs:
            lines.append(f"- Name: {w.get('name')} | Steps: {len(w.get('plan',[]))}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error listing workflows: {e}"
