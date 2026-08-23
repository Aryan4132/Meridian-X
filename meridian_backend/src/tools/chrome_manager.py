import os
import sys
import shutil
import subprocess
import time
from typing import Optional, Dict, Any
from database import get_user_preference, save_user_preference

def find_chrome_executable() -> Optional[str]:
    """Resolves installed Google Chrome binary path across Windows, macOS, and Linux."""
    if sys.platform == "win32":
        local_app_data = os.environ.get("LOCALAPPDATA", "")
        program_files = os.environ.get("PROGRAMFILES", "C:\\Program Files")
        program_files_x86 = os.environ.get("PROGRAMFILES(X86)", "C:\\Program Files (x86)")
        candidates = [
            os.path.join(local_app_data, "Google\\Chrome\\Application\\chrome.exe"),
            os.path.join(program_files, "Google\\Chrome\\Application\\chrome.exe"),
            os.path.join(program_files_x86, "Google\\Chrome\\Application\\chrome.exe"),
        ]
        for path in candidates:
            if path and os.path.exists(path):
                return path
    elif sys.platform == "darwin":
        mac_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        if os.path.exists(mac_path):
            return mac_path
    else:
        for name in ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]:
            path = shutil.which(name)
            if path:
                return path
    return None

def get_chrome_user_data_dir() -> str:
    """Returns local Chrome User Data directory or fallback Meridian Butler profile path."""
    stored = get_user_preference("chrome_user_data_dir")
    if stored and os.path.exists(stored):
        return stored

    if sys.platform == "win32":
        local_app = os.environ.get("LOCALAPPDATA", "")
        if local_app:
            default_dir = os.path.join(local_app, "Google", "Chrome", "User Data")
            if os.path.exists(default_dir):
                return default_dir
    elif sys.platform == "darwin":
        home = os.path.expanduser("~")
        default_dir = os.path.join(home, "Library", "Application Support", "Google", "Chrome")
        if os.path.exists(default_dir):
            return default_dir
    else:
        home = os.path.expanduser("~")
        default_dir = os.path.join(home, ".config", "google-chrome")
        if os.path.exists(default_dir):
            return default_dir

    # Fallback to local workspace memory directory
    fallback_dir = os.path.abspath(os.path.join(os.getcwd(), "meridian_memory", "chrome_profile"))
    os.makedirs(fallback_dir, exist_ok=True)
    return fallback_dir

def launch_chrome_with_profile(url: str = "https://music.youtube.com", profile_dir: Optional[str] = None) -> str:
    """Launches Google Chrome with persistent user profile directory for authenticated Google sessions."""
    chrome_path = find_chrome_executable()
    user_data = profile_dir or get_chrome_user_data_dir()

    # Try Playwright persistent context first (non-headless for media audio playback)
    try:
        from playwright.sync_api import sync_playwright
        p = sync_playwright().start()
        # Launch persistent context non-headless
        context = p.chromium.launch_persistent_context(
            user_data_dir=user_data,
            headless=False,
            executable_path=chrome_path if chrome_path and os.path.exists(chrome_path) else None,
            args=[
                "--no-sandbox",
                "--disable-blink-features=AutomationControlled",
                "--autoplay-policy=no-user-gesture-required",
            ]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(url)
        page.wait_for_load_state("domcontentloaded")
        return f"Successfully opened Chrome with persistent profile context at: '{url}'"
    except Exception as e:
        # Fallback to direct OS subprocess dispatch
        if chrome_path and os.path.exists(chrome_path):
            try:
                cmd = [
                    chrome_path,
                    f"--user-data-dir={user_data}",
                    "--no-first-run",
                    "--no-default-browser-check",
                    "--autoplay-policy=no-user-gesture-required",
                    url
                ]
                subprocess.Popen(cmd)
                return f"Launched Chrome subprocess with profile '{user_data}' at URL: '{url}'"
            except Exception as sub_err:
                return f"Failed to launch Chrome subprocess: {sub_err}"
        else:
            import webbrowser
            webbrowser.open(url)
            return f"Opened system browser at URL: '{url}' (Playwright/Chrome executable fallback: {e})"

def get_chrome_profile_status() -> Dict[str, Any]:
    """Returns status of Chrome executable and user profile configuration."""
    chrome_path = find_chrome_executable()
    user_data = get_chrome_user_data_dir()
    return {
        "chrome_installed": chrome_path is not None,
        "chrome_path": chrome_path or "Not Found",
        "user_data_dir": user_data,
        "media_account_email": get_user_preference("media_account_email", "aryanshukla4132@gmail.com")
    }
