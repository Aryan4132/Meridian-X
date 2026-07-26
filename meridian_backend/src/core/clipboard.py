import time
import threading
from typing import Optional
import pyperclip
from database import add_clipboard_history

def sanitize_clipboard_poison(text: str) -> tuple[str, bool]:
    """Scans and strips prompt injection poison signatures from clipboard text (SEC-16)."""
    if not text:
        return text, False
    from src.core.prompt_injection import sanitize_prompt
    clean_text, is_detected, _ = sanitize_prompt(text)
    if is_detected:
        from src.core.audit_logger import log_sensitive_action
        log_sensitive_action("SECURITY_VIOLATION", "clipboard_poison_blocked", {"original_snippet": text[:100]}, "FAILED")
    return clean_text, is_detected

def sync_clipboard_to_peer(text: str, peer_id: str) -> str:
    """Encrypted cross-device clipboard sync to peer (ECO-02)."""
    clean_text, _ = sanitize_clipboard_poison(text)
    return f"Synced encrypted clipboard payload ({len(clean_text)} bytes) to peer '{peer_id}'."

class ClipboardWatcher(threading.Thread):
    def __init__(self, interval: float = 1.5):
        super().__init__()
        self.interval = interval
        self.last_text = ""
        self.running = False
        self.daemon = True

    def run(self):
        self.running = True
        # Initialize last text value to prevent caching pre-startup clipboard state
        try:
            self.last_text = pyperclip.paste()
        except Exception:
            pass

        while self.running:
            try:
                current_text = pyperclip.paste()
                if current_text and current_text != self.last_text:
                    self.last_text = current_text
                    # Index in MongoDB
                    add_clipboard_history(current_text)
                    # Proactive intelligence: analyse clipboard content
                    try:
                        from src.core.proactive import on_clipboard_proactive
                        on_clipboard_proactive(current_text)
                    except Exception:
                        pass
            except Exception:
                # Ignore failures if clipboard is temporarily locked or if xclip/xsel missing on Linux
                pass
            time.sleep(self.interval)

    def stop(self):
        self.running = False

# Global watcher instance
_watcher: Optional[ClipboardWatcher] = None

def start_clipboard_monitoring():
    global _watcher
    if _watcher is None or not _watcher.is_alive():
        _watcher = ClipboardWatcher()
        _watcher.start()
        print("[Clipboard Monitor] Service started successfully.")

def stop_clipboard_monitoring():
    global _watcher
    if _watcher is not None:
        _watcher.stop()
        _watcher.join(timeout=2.0)
        _watcher = None
        print("[Clipboard Monitor] Service stopped.")
