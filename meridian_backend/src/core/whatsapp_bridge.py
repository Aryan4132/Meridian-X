import os
import time
import threading
import tempfile
from playwright.sync_api import sync_playwright

WHATSAPP_ACTIVE = False
_thread = None
_qr_path = os.path.join(tempfile.gettempdir(), "meridian_whatsapp_qr.png")
_authenticated = False

def start_whatsapp_bridge():
    global WHATSAPP_ACTIVE, _thread
    if not os.environ.get("WHATSAPP_AUTHORIZED_CONTACT"):
        print("[WhatsApp Bridge] WHATSAPP_AUTHORIZED_CONTACT not configured in .env. Bot bridge disabled.")
        return
        
    if WHATSAPP_ACTIVE:
        return
        
    WHATSAPP_ACTIVE = True
    _thread = threading.Thread(target=_run_browser, daemon=True)
    _thread.start()
    print("[WhatsApp Bridge] Background browser thread started.")

def stop_whatsapp_bridge():
    global WHATSAPP_ACTIVE
    WHATSAPP_ACTIVE = False
    print("[WhatsApp Bridge] Background browser thread stopped.")

def get_whatsapp_qr_path() -> Optional[str]:
    """Returns path to QR code screenshot if auth is pending."""
    global _authenticated
    if _authenticated:
        return None
    if os.path.exists(_qr_path):
        return _qr_path
    return None

def _run_browser():
    global WHATSAPP_ACTIVE, _authenticated
    
    auth_contact = os.environ.get("WHATSAPP_AUTHORIZED_CONTACT")
    backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    session_dir = os.path.join(backend_dir, "src", "core", "whatsapp_session")
    os.makedirs(session_dir, exist_ok=True)
    
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    
    # Remove any old QR code screenshot on start
    try:
        if os.path.exists(_qr_path):
            os.remove(_qr_path)
    except Exception:
        pass
        
    with sync_playwright() as p:
        print("[WhatsApp Bridge] Launching persistent Chromium context...")
        context = p.chromium.launch_persistent_context(
            user_data_dir=session_dir,
            headless=True,
            user_agent=user_agent,
            viewport={"width": 1024, "height": 768}
        )
        
        page = context.new_page()
        page.goto("https://web.whatsapp.com")
        
        last_processed_msg = None
        
        while WHATSAPP_ACTIVE:
            try:
                # 1. Check if authenticated
                # If we see the main chat list pane (usually contains element with id 'pane-side' or class '_1jJ70' / '_1pJ9J')
                is_logged_in = page.locator("#pane-side, [data-testid='chat-list']").first.is_visible(timeout=2000)
                
                if not is_logged_in:
                    _authenticated = False
                    # Check if QR code is visible on screen to screenshot
                    # Canvas containing QR code or div containing it
                    qr_canvas = page.locator("canvas, [data-testid='qrcode']").first
                    if qr_canvas.is_visible(timeout=2000):
                        print("[WhatsApp Bridge] Auth pending: Capture QR code screenshot...")
                        qr_canvas.screenshot(path=_qr_path)
                    time.sleep(3.0)
                    continue
                else:
                    _authenticated = True
                    # Clean up QR code screenshot if we logged in successfully
                    try:
                        if os.path.exists(_qr_path):
                            os.remove(_qr_path)
                    except Exception:
                        pass
                
                # 2. Check for unread chats
                # Selector for unread message count badge (usually a green circle with unread count class/aria-label)
                unread_badges = page.locator("[aria-label*='unread message'], [aria-label*='pesan tidak terbaca'], [class*='unread']").all()
                
                for badge in unread_badges:
                    try:
                        if not badge.is_visible():
                            continue
                            
                        # Click on the parent chat row element
                        # Typically a div with role="row" or class containing list item
                        chat_row = page.locator(f"xpath=//span[@aria-label='{badge.get_attribute('aria-label')}']/ancestor::div[@role='row']")
                        if not chat_row.first.is_visible():
                            continue
                            
                        chat_row.first.click()
                        time.sleep(1.0)
                        
                        # Verify the contact name in the header
                        header_title = page.locator("header span[title]").first
                        if not header_title.is_visible():
                            continue
                            
                        contact_name = header_title.get_attribute("title")
                        if not contact_name or auth_contact.lower() not in contact_name.lower():
                            print(f"[WhatsApp Bridge] Skipping message from unauthorized contact: {contact_name}")
                            continue
                            
                        # Extract the last incoming message text
                        # Class .message-in usually contains incoming messages
                        message_bubbles = page.locator(".message-in span.selectable-text").all()
                        if not message_bubbles:
                            continue
                            
                        last_msg_text = message_bubbles[-1].inner_text().strip()
                        
                        # Avoid reprocessing the exact same message
                        if last_msg_text == last_processed_msg:
                            continue
                            
                        last_processed_msg = last_msg_text
                        print(f"[WhatsApp Bridge] Received command from {contact_name}: '{last_msg_text}'")
                        
                        # Process using reactive agent loop
                        from api import get_react_thoughts
                        model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
                        ocr_model = "PaddleOCR-v4"
                        
                        result = get_react_thoughts(last_msg_text, model, ocr_model)
                        reply_text = result.get("text", "Task completed.")
                        
                        # Log to database conversation history
                        from database import add_to_conversations
                        add_to_conversations("user", last_msg_text)
                        add_to_conversations("assistant", reply_text)
                        
                        # Type the response in message input box
                        # Input box has role="textbox" and contenteditable="true"
                        input_box = page.locator("div[contenteditable='true'][role='textbox']").first
                        if input_box.is_visible():
                            input_box.click()
                            input_box.fill(reply_text)
                            time.sleep(0.5)
                            input_box.press("Enter")
                            print(f"[WhatsApp Bridge] Sent reply to {contact_name}")
                            
                    except Exception as chat_err:
                        print(f"[WhatsApp Bridge] Error processing unread chat: {chat_err}")
                        
                time.sleep(2.0)
                
            except Exception as loop_err:
                print(f"[WhatsApp Bridge] Loop error: {loop_err}")
                time.sleep(5.0)
                
        print("[WhatsApp Bridge] Closing Playwright browser context...")
        context.close()
