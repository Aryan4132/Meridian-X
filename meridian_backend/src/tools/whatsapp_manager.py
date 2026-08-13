"""
whatsapp_manager.py — WhatsApp Integration Engine (WAP-01, WAP-02)
Manages WhatsApp contacts, resolves recipient names, and pulls recent chat messages.
"""

import os
import time
import json
import logging
from typing import List, Dict, Any, Optional
from database import save_whatsapp_contact, get_whatsapp_contacts, resolve_whatsapp_contact

logger = logging.getLogger("meridian_whatsapp")

def manage_whatsapp_contacts(
    action: str = "list",
    name: str = "",
    phone_number: str = "",
    alias: str = "",
    notes: str = ""
) -> str:
    """Manages local WhatsApp contacts directory (add, list, resolve)."""
    act = action.lower().strip()
    if act in ("add", "save", "create"):
        if not name or not phone_number:
            return "Error: Both 'name' and 'phone_number' are required to save a contact."
        rec = save_whatsapp_contact(name, phone_number, alias=alias, notes=notes)
        return f"Saved WhatsApp contact: '{rec['name']}' ({rec['phone_number']}) [Alias: '{rec.get('alias', '')}']"
    
    elif act in ("resolve", "lookup", "find"):
        target = name or alias or phone_number
        rec = resolve_whatsapp_contact(target)
        if rec:
            return f"Resolved contact '{target}' -> Name: '{rec['name']}', Number: '{rec['phone_number']}', Alias: '{rec.get('alias', '')}'"
        return f"No matching WhatsApp contact found for '{target}'."

    else:
        contacts = get_whatsapp_contacts()
        if not contacts:
            return "No saved WhatsApp contacts found. Use action='add' to save contacts."
        lines = [f"- {c['name']} ({c['phone_number']}) [Alias: {c.get('alias', 'N/A')}]" for c in contacts]
        return "Saved WhatsApp Contacts:\n" + "\n".join(lines)

def read_whatsapp_messages(contact: str = "", limit: int = 5) -> str:
    """Reads recent messages for a WhatsApp contact or active chat session."""
    target_rec = resolve_whatsapp_contact(contact) if contact else None
    target_name = target_rec["name"] if target_rec else (contact or "Recent Chat")
    target_phone = target_rec["phone_number"] if target_rec else contact

    # Try Playwright session read if available
    try:
        from playwright.sync_api import sync_playwright
        user_data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "meridian_memory", "whatsapp_session"))
        os.makedirs(user_data_dir, exist_ok=True)
        
        with sync_playwright() as p:
            browser = p.chromium.launch_persistent_context(
                user_data_dir=user_data_dir,
                headless=True,
                args=["--no-sandbox", "--disable-setuid-sandbox"]
            )
            page = browser.pages[0] if browser.pages else browser.new_page()
            page.goto("https://web.whatsapp.com", timeout=20000)
            time.sleep(3)
            
            # Check if logged in (search box or qr present)
            if page.locator("div[contenteditable='true']").is_visible():
                if target_name:
                    search_box = page.locator("div[contenteditable='true']").first
                    search_box.fill(target_name)
                    time.sleep(1.5)
                    page.keyboard.press("Enter")
                    time.sleep(2)
                
                msg_elements = page.locator("div.message-in, div.message-out").all()
                messages = []
                for el in msg_elements[-limit:]:
                    text = el.inner_text().replace("\n", " ")
                    messages.append(text)
                
                browser.close()
                if messages:
                    return f"Recent WhatsApp messages for '{target_name}':\n" + "\n".join(f"- {m}" for m in messages)
            browser.close()
    except Exception as e:
        logger.debug(f"[WhatsApp] Playwright session read unavailable or unauthenticated: {e}")

    # Fallback status representation when headless browser session is unauthenticated
    return (
        f"WhatsApp Message Puller for '{target_name}' ({target_phone}):\n"
        f"- To pull live messages, ensure WhatsApp Web session is logged in at 'https://web.whatsapp.com'.\n"
        f"- Currently target contact resolved to: '{target_name}' ({target_phone})."
    )

def list_whatsapp_chats() -> str:
    """Lists recent active WhatsApp chats and unread message indicators."""
    contacts = get_whatsapp_contacts()
    if contacts:
        summary = [f"- {c['name']} ({c['phone_number']})" for c in contacts]
        return "Active WhatsApp Contact Directory:\n" + "\n".join(summary)
    return "No active WhatsApp chats found in database."

def login_whatsapp_session() -> str:
    """Launches a browser window to scan the WhatsApp Web QR code and pair your session."""
    user_data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "meridian_memory", "whatsapp_session"))
    os.makedirs(user_data_dir, exist_ok=True)
    
    try:
        from playwright.sync_api import sync_playwright
        from src.tools.communication import send_native_toast_notification
        
        send_native_toast_notification(
            title="WhatsApp Web Pairing",
            message="A browser window is opening. Scan the QR code on your phone (WhatsApp -> Linked Devices)."
        )
        
        with sync_playwright() as p:
            browser = p.chromium.launch_persistent_context(
                user_data_dir=user_data_dir,
                headless=False,
                args=["--no-sandbox", "--disable-setuid-sandbox"]
            )
            page = browser.pages[0] if browser.pages else browser.new_page()
            page.goto("https://web.whatsapp.com", timeout=30000)
            
            print("[WhatsApp] Browser window launched. Waiting for QR scan / login completion...")
            # Wait up to 90 seconds for chat search bar to appear after QR scan
            logged_in = False
            for _ in range(45):
                time.sleep(2)
                if page.locator("div[contenteditable='true']").is_visible():
                    logged_in = True
                    break
            
            browser.close()
            if logged_in:
                return "WhatsApp Web pairing complete! Session saved to local memory."
            return "WhatsApp Web pairing timed out or browser closed before QR scan."
    except Exception as e:
        logger.error(f"[WhatsApp] QR pairing error: {e}")
        import webbrowser
        webbrowser.open("https://web.whatsapp.com")
        return f"Opened default browser to 'https://web.whatsapp.com' for QR scan ({e})."
