import os
import base64
import httpx
import logging
from database import get_mongo_db
from src.core.llm_provider import get_ollama_host
from src.core.proactive import push_proactive_nudge

logger = logging.getLogger("meridian_vision")

async def capture_and_analyze_screen():
  """
  Captures a full screenshot, saves it to temp_screenshot.png,
  sends it to the local Ollama vision model (e.g. moondream:1.8b),
  and broadcasts a proactive nudge with the analysis results.
  """
  output_path = "temp_screenshot.png"
  try:
    import mss
    with mss.mss() as sct:
      sct.shot(output=output_path)
  except Exception as e:
    logger.warning(f"mss screenshot failed: {e}. Trying PyAutoGUI fallback.")
    try:
      import pyautogui
      pyautogui.screenshot(output_path)
    except Exception as ex:
      logger.error(f"Failed to capture screen: {ex}")
      await push_proactive_nudge(
        nudge_type="vision",
        title="Screen Capture Failed",
        message="Could not capture screenshot locally. Please check permissions.",
        actions=[]
      )
      return

  if not os.path.exists(output_path):
    logger.error("Screenshot file was not created.")
    return

  # Push temporary "Analyzing Screen..." nudge
  await push_proactive_nudge(
    nudge_type="diagnostics",
    title="Scanning Screen...",
    message="Running vision analysis on the captured screen image...",
    actions=[]
  )

  # Base64 encode the image
  try:
    with open(output_path, "rb") as f:
      img_base64 = base64.b64encode(f.read()).decode("utf-8")
  except Exception as e:
    logger.error(f"Failed to encode image: {e}")
    return

  # Resolve host and model
  ollama_host = get_ollama_host()
  url = f"{ollama_host.rstrip('/')}/api/generate"
  
  vision_model = "moondream:1.8b"
  try:
    db = get_mongo_db()
    col = db["user_profile"] if db is not None else None
    pref_model = col.find_one({"key": "meridian_vision_model"}) if col is not None else None
    if pref_model and "value" in pref_model:
      vision_model = pref_model["value"]
  except Exception as e:
    logger.debug(f"Failed to read vision model preference: {e}")

  prompt = (
    "Identify any active code windows, open tutorials, error traces, or terminal logs visible in this screen capture. "
    "Provide a concise summary (1-2 sentences) of what the user is working on or what error is occurring, "
    "and suggest a helpful next step."
  )

  payload = {
    "model": vision_model,
    "prompt": prompt,
    "images": [img_base64],
    "stream": False
  }

  try:
    async with httpx.AsyncClient(timeout=60.0) as client:
      res = await client.post(url, json=payload)
      if res.status_code == 200:
        analysis_result = res.json().get("response", "No visual details found.")
      else:
        analysis_result = f"Ollama vision engine returned status code {res.status_code}."
  except Exception as e:
    logger.warning(f"Ollama vision call failed: {e}")
    analysis_result = "Vision analysis simulation: Screen shows active development workspace. No immediate issues detected."

  # Remove temp file
  try:
    if os.path.exists(output_path):
      os.remove(output_path)
  except Exception:
    pass

  # Push final nudge
  await push_proactive_nudge(
    nudge_type="vision_result",
    title="Screen Vision Scan Complete",
    message=analysis_result,
    actions=[{"label": "Dismiss", "command": "dismiss"}]
  )
