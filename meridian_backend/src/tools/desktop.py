import os
import mss
import pyautogui
from typing import Dict, Any, List
from src.core.audit_logger import log_sensitive_action

# Set fail-safe to prevent locked GUI
pyautogui.FAILSAFE = True

def screenshot(output_path: str) -> str:
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with mss.mss() as sct:
        sct.shot(output=output_path)
    return f"Screenshot saved to {output_path}"

def screenshot_region(x: int, y: int, w: int, h: int, output_path: str) -> str:
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": w, "height": h}
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output_path)
    return f"Screenshot of region saved to {output_path}"

def vision_analyze(image_path: str, prompt: str) -> str:
    try:
        from database import get_ollama_client, get_vision_model
        
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")
            
        with open(image_path, "rb") as f:
            img_data = f.read()
            
        client = get_ollama_client()
        vision_model = get_vision_model()
        
        res = client.generate(
            model=vision_model,
            prompt=prompt,
            images=[img_data]
        )
        return (res.response if hasattr(res, "response") else res.get("response", "No response from vision model"))
    except Exception as e:
        return f"Vision analysis failed: {str(e)}"

def ocr_screen(image_path: str) -> str:
    # Use vision model to perform text extraction (fully offline OCR)
    prompt = "Extract and transcribe all text visible in this image verbatim. Do not summarize or add explanations."
    return vision_analyze(image_path, prompt)

def find_on_screen(image_path: str, target_desc: str) -> str:
    # Use vision model to find coordinate coordinates
    prompt = f"Analyze the image and locate the UI element matching description: '{target_desc}'. Estimate its coordinates relative to the screen size (as percentage or pixel bounding boxes x, y, width, height) if possible."
    return vision_analyze(image_path, prompt)

def gui_click(x: int, y: int) -> str:
    try:
        pyautogui.click(x, y)
        log_sensitive_action("GUI_INPUT", "click", {"x": x, "y": y}, "SUCCESS")
        return f"Clicked at ({x}, {y})"
    except Exception as e:
        log_sensitive_action("GUI_INPUT", "click", {"x": x, "y": y, "error": str(e)}, "FAILED")
        raise e

def gui_right_click(x: int, y: int) -> str:
    try:
        pyautogui.rightClick(x, y)
        log_sensitive_action("GUI_INPUT", "right_click", {"x": x, "y": y}, "SUCCESS")
        return f"Right-clicked at ({x}, {y})"
    except Exception as e:
        log_sensitive_action("GUI_INPUT", "right_click", {"x": x, "y": y, "error": str(e)}, "FAILED")
        raise e

def gui_double_click(x: int, y: int) -> str:
    try:
        pyautogui.doubleClick(x, y)
        log_sensitive_action("GUI_INPUT", "double_click", {"x": x, "y": y}, "SUCCESS")
        return f"Double-clicked at ({x}, {y})"
    except Exception as e:
        log_sensitive_action("GUI_INPUT", "double_click", {"x": x, "y": y, "error": str(e)}, "FAILED")
        raise e

def gui_drag(x1: int, y1: int, x2: int, y2: int, duration: float = 0.5) -> str:
    try:
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, duration=duration)
        log_sensitive_action("GUI_INPUT", "drag", {"x1": x1, "y1": y1, "x2": x2, "y2": y2, "duration": duration}, "SUCCESS")
        return f"Dragged mouse from ({x1}, {y1}) to ({x2}, {y2})"
    except Exception as e:
        log_sensitive_action("GUI_INPUT", "drag", {"x1": x1, "y1": y1, "x2": x2, "y2": y2, "duration": duration, "error": str(e)}, "FAILED")
        raise e

def gui_type(text: str, interval: float = 0.05) -> str:
    try:
        pyautogui.write(text, interval=interval)
        # Avoid logging the exact keystroke content for security/passwords unless requested, or mask it
        masked_text = text if len(text) <= 3 else text[:2] + "..." + text[-1:]
        log_sensitive_action("GUI_INPUT", "type", {"text_len": len(text), "preview": masked_text, "interval": interval}, "SUCCESS")
        return f"Typed: '{text}' (interval={interval}s)"
    except Exception as e:
        log_sensitive_action("GUI_INPUT", "type", {"text_len": len(text), "interval": interval, "error": str(e)}, "FAILED")
        raise e

def gui_hotkey(keys: List[str]) -> str:
    try:
        pyautogui.hotkey(*keys)
        log_sensitive_action("GUI_INPUT", "hotkey", {"keys": keys}, "SUCCESS")
        return f"Pressed keys combination: {keys}"
    except Exception as e:
        log_sensitive_action("GUI_INPUT", "hotkey", {"keys": keys, "error": str(e)}, "FAILED")
        raise e

def gui_scroll(x: int, y: int, clicks: int) -> str:
    try:
        pyautogui.moveTo(x, y)
        pyautogui.scroll(clicks)
        log_sensitive_action("GUI_INPUT", "scroll", {"x": x, "y": y, "clicks": clicks}, "SUCCESS")
        return f"Scrolled mouse wheel at ({x}, {y}) by {clicks} clicks"
    except Exception as e:
        log_sensitive_action("GUI_INPUT", "scroll", {"x": x, "y": y, "clicks": clicks, "error": str(e)}, "FAILED")
        raise e

def get_mouse_position() -> str:
    pos = pyautogui.position()
    return f"Current Mouse Position: x={pos.x}, y={pos.y}"

# --- Visual Screen Segmentation & Anchor Mapping ---
active_screen_segments: Dict[str, Dict[str, int]] = {}

def find_ui_elements_pil(image_path: str) -> List[List[int]]:
    from PIL import Image, ImageFilter
    try:
        img = Image.open(image_path)
        gray = img.convert("L")
        edges = gray.filter(ImageFilter.FIND_EDGES)
        
        width, height = img.size
        boxes = []
        
        stride_x = max(30, width // 15)
        stride_y = max(30, height // 15)
        
        for x in range(stride_x, width - stride_x, stride_x):
            for y in range(stride_y, height - stride_y, stride_y):
                # Sample local edge intensity
                box_area = edges.crop((x - 12, y - 12, x + 12, y + 12))
                stat = sum(box_area.getdata()) / 576.0
                if stat > 20.0:
                    # Deduplicate nearby anchors
                    too_close = False
                    for bx, by in boxes:
                        if abs(bx - x) < 50 and abs(by - y) < 50:
                            too_close = True
                            break
                    if not too_close:
                        boxes.append([x, y])
                        if len(boxes) >= 30:
                            break
            if len(boxes) >= 30:
                break
        
        if not boxes:
            # Fallback grid if no high contrast edges detected
            for x in range(width // 5, width, width // 5):
                for y in range(height // 5, height, height // 5):
                    boxes.append([x, y])
        return boxes
    except Exception as e:
        print("[Visual Segmenter] Error finding UI elements:", e)
        return [[200, 200], [400, 400], [600, 600]]

def segment_screen(image_path: str, output_path: str) -> str:
    from PIL import Image, ImageDraw, ImageFont
    
    if not os.path.exists(image_path):
        return f"Error: Source screenshot not found at {image_path}"
        
    try:
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        
        boxes = find_ui_elements_pil(image_path)
        
        global active_screen_segments
        active_screen_segments.clear()
        
        for idx, (x, y) in enumerate(boxes):
            badge_id = str(idx + 1)
            active_screen_segments[badge_id] = {"x": x, "y": y}
            
            # Draw red circles
            r = 14
            draw.ellipse([x - r, y - r, x + r, y + r], fill="red", outline="white", width=2)
            
            try:
                font = ImageFont.load_default()
            except Exception:
                font = None
            draw.text((x - 4, y - 6), badge_id, fill="white", font=font)
            
        img.save(output_path)
        
        summary = f"Detected {len(boxes)} visual anchors. Badge overlay saved to: {output_path}\n"
        summary += "Mapped Anchors:\n"
        for bid, coords in active_screen_segments.items():
            summary += f"Badge {bid} -> x: {coords['x']}, y: {coords['y']}\n"
        return summary
    except Exception as e:
        return f"Visual segmentation mapping failed: {str(e)}"

def gui_click_badge(badge_id: str) -> str:
    global active_screen_segments
    if badge_id not in active_screen_segments:
        return f"Error: Badge ID '{badge_id}' not found in active screen segments mapping. Run segment_screen first."
    coords = active_screen_segments[badge_id]
    x, y = coords["x"], coords["y"]
    return gui_click(x, y)


def screenshot_to_code(image_path: str, tech_stack: str = "html/css/vanilla js") -> str:
    """Analyze a screenshot of a UI design and generate clean, responsive frontend code (HTML/CSS/JS) to match it."""
    prompt = (
        f"Analyze this UI screenshot and write a single, complete, fully-functional, responsive file containing all code "
        f"(HTML, CSS in a <style> block, and JS in a <script> block) to clone it using the '{tech_stack}' stack.\n"
        f"Ensure there are no external dependencies, use beautiful modern colors/layout/typography, and output ONLY the raw code. "
        f"Do not include explanations or markdown code fences."
    )
    return vision_analyze(image_path, prompt)


