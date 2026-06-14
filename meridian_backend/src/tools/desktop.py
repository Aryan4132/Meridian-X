import os
import mss
import pyautogui
from typing import Dict, Any, List

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
        from database import get_ollama_client
        
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")
            
        with open(image_path, "rb") as f:
            img_data = f.read()
            
        client = get_ollama_client()
        vision_model = os.environ.get("MERIDIAN_VISION_MODEL", "moondream:1.8b")
        
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
    pyautogui.click(x, y)
    return f"Clicked at ({x}, {y})"

def gui_right_click(x: int, y: int) -> str:
    pyautogui.rightClick(x, y)
    return f"Right-clicked at ({x}, {y})"

def gui_double_click(x: int, y: int) -> str:
    pyautogui.doubleClick(x, y)
    return f"Double-clicked at ({x}, {y})"

def gui_drag(x1: int, y1: int, x2: int, y2: int, duration: float = 0.5) -> str:
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, duration=duration)
    return f"Dragged mouse from ({x1}, {y1}) to ({x2}, {y2})"

def gui_type(text: str, interval: float = 0.05) -> str:
    pyautogui.write(text, interval=interval)
    return f"Typed: '{text}' (interval={interval}s)"

def gui_hotkey(keys: List[str]) -> str:
    pyautogui.hotkey(*keys)
    return f"Pressed keys combination: {keys}"

def gui_scroll(x: int, y: int, clicks: int) -> str:
    pyautogui.moveTo(x, y)
    pyautogui.scroll(clicks)
    return f"Scrolled mouse wheel at ({x}, {y}) by {clicks} clicks"

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

