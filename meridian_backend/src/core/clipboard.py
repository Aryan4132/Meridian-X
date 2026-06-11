import time
import threading
from typing import Optional
import pyperclip
from database import add_clipboard_history

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
            except Exception as e:
                # Ignore failures if clipboard is temporarily locked by other applications
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
