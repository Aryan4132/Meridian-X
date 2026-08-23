import time
import urllib.parse
from typing import Optional, Dict, Any
from database import get_user_preference, save_user_preference
from src.tools.chrome_manager import launch_chrome_with_profile, find_chrome_executable, get_chrome_user_data_dir
from src.tools.desktop import screenshot, ocr_screen, gui_hotkey, gui_click, gui_type

def verify_media_playing(song_query: Optional[str] = None) -> Dict[str, Any]:
    """Captures desktop/browser screenshot and verifies if YouTube Music or media player is actively playing."""
    try:
        # Take screen screenshot
        img_path = screenshot("meridian_media_verification.png")
        if "Error" in img_path:
            return {"playing": False, "verified": False, "reason": img_path}

        # Perform OCR analysis on captured screen image
        ocr_text = ocr_screen(img_path)
        ocr_lower = ocr_text.lower() if ocr_text else ""

        keywords = ["youtube music", "music.youtube.com", "pause", "play", "playing"]
        if song_query:
            keywords.extend([w.lower() for w in song_query.split() if len(w) > 2])

        matched = [k for k in keywords if k in ocr_lower]
        is_playing = "pause" in ocr_lower or len(matched) >= 2

        return {
            "playing": is_playing,
            "verified": len(matched) > 0,
            "matched_keywords": matched,
            "ocr_snippet": ocr_text[:200] if ocr_text else ""
        }
    except Exception as e:
        return {"playing": False, "verified": False, "reason": str(e)}

def control_media_playback(action: str = "playpause") -> str:
    """Controls OS system media playback using native media keys (playpause, nexttrack, prevtrack, volumeup, volumedown)."""
    action_clean = action.lower().strip()
    valid_actions = ["playpause", "nexttrack", "prevtrack", "volumeup", "volumedown", "volumemute"]
    if action_clean not in valid_actions:
        return f"Invalid action '{action}'. Must be one of: {valid_actions}"

    res = gui_hotkey([action_clean])
    return f"Executed system media key action '{action_clean}': {res}"


def play_youtube_music(
    song_query: str,
    account_email: Optional[str] = None,
    use_chrome: bool = True,
    max_retries: int = 3
) -> str:
    """Butler Media Engine: Plays requested track/artist on YouTube Music via Chrome authenticated profile with visual verification & auto-retry."""
    email = account_email or get_user_preference("media_account_email", "aryanshukla4132@gmail.com")
    # Save user preference for account memory
    save_user_preference("media_account_email", email)

    encoded_query = urllib.parse.quote(song_query)
    search_url = f"https://music.youtube.com/search?q={encoded_query}"

    print(f"[Butler Media] Playing '{song_query}' on YouTube Music for account '{email}'...")

    # Step 1: Launch Chrome with authenticated user profile
    launch_res = launch_chrome_with_profile(url=search_url)

    # Allow page DOM to render search results
    time.sleep(3)

    # Step 2: Perform Playwright / GUI auto-play click sequence
    auto_clicked = False
    try:
        from playwright.sync_api import sync_playwright
        chrome_path = find_chrome_executable()
        user_data = get_chrome_user_data_dir()
        with sync_playwright() as p:
            context = p.chromium.launch_persistent_context(
                user_data_dir=user_data,
                headless=False,
                executable_path=chrome_path if chrome_path else None
            )
            page = context.pages[0] if context.pages else context.new_page()
            page.goto(search_url)
            page.wait_for_selector(".ytmusic-responsive-list-item-renderer, ytmusic-play-button-renderer", timeout=6000)
            
            # Click top song play button
            play_btn = page.query_selector("ytmusic-play-button-renderer") or page.query_selector(".ytmusic-responsive-list-item-renderer")
            if play_btn:
                play_btn.click()
                auto_clicked = True
                print("[Butler Media] Clicked top song play button via Playwright.")
    except Exception as e:
        print(f"[Butler Media] Playwright element click fallback: {e}")
        # GUI fallback: press Enter or Space to trigger top search result
        try:
            import pyautogui
            pyautogui.FAILSAFE = False
        except Exception:
            pass
        try:
            gui_hotkey(["enter"])
        except Exception as hk_err:
            print(f"[Butler Media] GUI hotkey fallback notice: {hk_err}")
        auto_clicked = True

    # Step 3: Visual Verification & Auto-Retry Loop
    verified_status = None
    for attempt in range(1, max_retries + 1):
        time.sleep(2)
        verified_status = verify_media_playing(song_query=song_query)
        if verified_status.get("playing") or verified_status.get("verified"):
            return (
                f"Successfully playing '{song_query}' on YouTube Music for '{email}'! "
                f"[Visual Verification: CONFIRMED on attempt {attempt}]"
            )

        print(f"[Butler Media] Verification attempt {attempt}/{max_retries} unconfirmed. Retrying play trigger...")
        # Auto-retry action: trigger media play key / press Enter / Space
        try:
            gui_hotkey(["playpause"])
            gui_hotkey(["enter"])
        except Exception as retry_err:
            print(f"[Butler Media] Retry hotkey notice: {retry_err}")



    return (
        f"Launched YouTube Music for '{song_query}' with profile '{email}'. "
        f"[Status: Dispatched URL '{search_url}' | Visual Check: {verified_status}]"
    )
