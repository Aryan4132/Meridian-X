import os
import sys
import json
import shutil
import subprocess
import time
import urllib.request
from typing import Optional, Dict, Any, List
from database import get_user_preference

def find_browser_executable(browser: str = "chrome") -> Optional[str]:
    """Resolves installed browser executable path (Chrome, Edge, Brave, Chromium) across platforms."""
    b_type = (browser or "chrome").lower()

    if sys.platform == "win32":
        local_app = os.environ.get("LOCALAPPDATA", "")
        prog_files = os.environ.get("PROGRAMFILES", "C:\\Program Files")
        prog_files_x86 = os.environ.get("PROGRAMFILES(X86)", "C:\\Program Files (x86)")

        candidates_map = {
            "chrome": [
                os.path.join(prog_files, "Google\\Chrome\\Application\\chrome.exe"),
                os.path.join(local_app, "Google\\Chrome\\Application\\chrome.exe"),
                os.path.join(prog_files_x86, "Google\\Chrome\\Application\\chrome.exe"),
            ],
            "edge": [
                os.path.join(prog_files_x86, "Microsoft\\Edge\\Application\\msedge.exe"),
                os.path.join(prog_files, "Microsoft\\Edge\\Application\\msedge.exe"),
                os.path.join(local_app, "Microsoft\\Edge\\Application\\msedge.exe"),
            ],
            "brave": [
                os.path.join(prog_files, "BraveSoftware\\Brave-Browser\\Application\\brave.exe"),
                os.path.join(local_app, "BraveSoftware\\Brave-Browser\\Application\\brave.exe"),
                os.path.join(prog_files_x86, "BraveSoftware\\Brave-Browser\\Application\\brave.exe"),
            ],
            "chromium": [
                os.path.join(local_app, "Chromium\\Application\\chrome.exe"),
                os.path.join(prog_files, "Chromium\\Application\\chrome.exe"),
            ]
        }

        if b_type in candidates_map:
            for p in candidates_map[b_type]:
                if p and os.path.exists(p):
                    return p
        elif b_type == "auto":
            for b in ["chrome", "edge", "brave", "chromium"]:
                for p in candidates_map[b]:
                    if p and os.path.exists(p):
                        return p

    elif sys.platform == "darwin":
        mac_paths = {
            "chrome": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "edge": "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "brave": "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
            "chromium": "/Applications/Chromium.app/Contents/MacOS/Chromium",
        }
        if b_type in mac_paths and os.path.exists(mac_paths[b_type]):
            return mac_paths[b_type]
        if b_type == "auto":
            for p in mac_paths.values():
                if os.path.exists(p):
                    return p
    else:
        linux_bins = {
            "chrome": ["google-chrome", "google-chrome-stable"],
            "edge": ["microsoft-edge", "microsoft-edge-stable"],
            "brave": ["brave-browser"],
            "chromium": ["chromium", "chromium-browser"],
        }
        targets = linux_bins.get(b_type, []) if b_type != "auto" else [item for sub in linux_bins.values() for item in sub]
        for name in targets:
            p = shutil.which(name)
            if p:
                return p

    # General PATH fallback
    return shutil.which(browser)

def find_chrome_executable() -> Optional[str]:
    """Resolves installed Google Chrome binary path across Windows, macOS, and Linux."""
    return find_browser_executable("chrome") or find_browser_executable("auto")

def detect_cdp_browser(host: str = "127.0.0.1", ports: Optional[List[int]] = None) -> Optional[Dict[str, Any]]:
    """Detects if any browser (Chrome, Edge, Brave, etc.) is currently running with remote debugging enabled."""
    target_ports = ports or [9222, 9223, 9224]
    for port in target_ports:
        url = f"http://{host}:{port}/json/version"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Meridian-CDP-Probe"})
            with urllib.request.urlopen(req, timeout=0.5) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode("utf-8", errors="ignore"))
                    return {
                        "port": port,
                        "cdp_url": f"http://{host}:{port}",
                        "browser": data.get("Browser", "Unknown Browser"),
                        "protocol_version": data.get("Protocol-Version", ""),
                        "webSocketDebuggerUrl": data.get("webSocketDebuggerUrl", ""),
                    }
        except Exception:
            continue
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

def launch_browser_in_debug_mode(
    port: int = 9222,
    browser: str = "chrome",
    url: str = "about:blank",
    profile_dir: Optional[str] = None
) -> Dict[str, Any]:
    """Launches Chrome or any Chromium browser in remote debugging mode with persistent profile (not guest mode)."""
    # 1. Check if browser is already active on this port
    existing = detect_cdp_browser(ports=[port])
    if existing:
        return {
            "success": True,
            "port": port,
            "cdp_url": existing["cdp_url"],
            "browser": existing["browser"],
            "already_running": True,
            "message": f"Attached to existing debugging session on {existing['cdp_url']} ({existing['browser']})"
        }

    # 2. Locate browser binary
    exe_path = find_browser_executable(browser) or find_browser_executable("auto")
    if not exe_path or not os.path.exists(exe_path):
        return {
            "success": False,
            "error": f"Browser executable for '{browser}' not found. Please verify browser installation."
        }

    # 3. Resolve persistent profile (avoids guest/incognito mode)
    if profile_dir:
        user_data = profile_dir
    else:
        # Use dedicated debug profile to prevent lock conflicts with standard user browsing
        local_app = os.environ.get("LOCALAPPDATA", "")
        if sys.platform == "win32" and local_app:
            user_data = os.path.join(local_app, "Google", "Chrome", "User Data - MeridianDebug")
        else:
            user_data = os.path.abspath(os.path.join(os.getcwd(), "meridian_memory", "chrome_debug_profile"))
    os.makedirs(user_data, exist_ok=True)

    # 4. Launch with remote debugging flag and persistent user directory
    cmd = [
        exe_path,
        f"--remote-debugging-port={port}",
        f"--user-data-dir={user_data}",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-blink-features=AutomationControlled",
        "--autoplay-policy=no-user-gesture-required",
    ]
    if url and url != "about:blank":
        cmd.append(url)

    try:
        subprocess.Popen(cmd)
    except Exception as e:
        return {"success": False, "error": f"Failed to start browser subprocess: {e}"}

    # 5. Wait for CDP endpoint to become ready
    deadline = time.time() + 6.0
    while time.time() < deadline:
        detected = detect_cdp_browser(ports=[port])
        if detected:
            return {
                "success": True,
                "port": port,
                "cdp_url": detected["cdp_url"],
                "browser": detected["browser"],
                "profile": user_data,
                "message": f"Successfully launched {browser} in debugging mode on port {port} (profile: {user_data})"
            }
        time.sleep(0.3)

    return {
        "success": True,
        "port": port,
        "cdp_url": f"http://127.0.0.1:{port}",
        "profile": user_data,
        "message": f"Started {browser} with remote-debugging-port={port} (CDP readiness check pending)"
    }

def launch_chrome_with_profile(url: str = "https://music.youtube.com", profile_dir: Optional[str] = None) -> str:
    """Launches Google Chrome with persistent user profile directory in debugging mode."""
    res = launch_browser_in_debug_mode(port=9222, browser="chrome", url=url, profile_dir=profile_dir)
    if res.get("success"):
        return f"{res.get('message')} - Navigated to: {url}"
    return f"Failed to launch Chrome with profile: {res.get('error')}"

def get_chrome_profile_status() -> Dict[str, Any]:
    """Returns status of Chrome executable, CDP debug connection, and user profile configuration."""
    chrome_path = find_chrome_executable()
    user_data = get_chrome_user_data_dir()
    cdp_active = detect_cdp_browser()
    return {
        "chrome_installed": chrome_path is not None,
        "chrome_path": chrome_path or "Not Found",
        "user_data_dir": user_data,
        "cdp_active": cdp_active is not None,
        "cdp_info": cdp_active,
        "media_account_email": get_user_preference("media_account_email", os.getenv("DEFAULT_MEDIA_EMAIL", ""))
    }
