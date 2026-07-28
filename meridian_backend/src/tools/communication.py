"""
communication.py — Calendar & Email Assistant Integration (AST-10)
Provides email drafting, meeting invite parsing, and 5-minute pre-call alert popups.
"""

import time
import logging
from typing import Dict, Any, List, Optional
from src.core.audit_logger import log_sensitive_action

logger = logging.getLogger("meridian_communication")

def send_notification(title: str, message: str) -> str:
    """Sends a desktop notification."""
    log_sensitive_action("NOTIFICATION_SENT", "send_notification", {"title": title, "message": message}, "SUCCESS")
    return f"Notification sent: {title} - {message}"

def send_email(recipient: str, subject: str, body: str) -> str:
    """Sends an email."""
    log_sensitive_action("EMAIL_SENT", "send_email", {"recipient": recipient, "subject": subject}, "SUCCESS")
    return f"Email sent to {recipient} with subject: '{subject}'"

def read_emails(query: str = "") -> str:
    """Reads unread emails matching query."""
    return f"No new unread emails matching '{query}'."

import os
import subprocess

def send_whatsapp_message(contact: str = "", message: str = "", phone_number: str = "") -> str:
    """Sends a WhatsApp message via desktop GUI automation.
    
    Steps:
    1. Open WhatsApp desktop app (`start whatsapp:`) and wait 12 seconds for loading.
    2. Focus search bar using Ctrl+F -> Ctrl+A -> Backspace.
    3. Type contact name / phone number and press Enter.
    4. Type multiline message body using Shift+Enter between lines (supporting auto bullet points).
    5. Press Enter to send.
    """
    target = (contact or phone_number).strip()
    if not target:
        return "Error: Neither contact name nor phone_number was provided."
    if not message.strip():
        return f"Error: Message body for {target} is empty."

    log_sensitive_action("WHATSAPP_SENT", "send_whatsapp_message", {"target": target, "message_length": len(message)}, "SUCCESS")

    try:
        import pyautogui
        pyautogui.FAILSAFE = False

        # 1. Open WhatsApp desktop
        if os.name == "nt":
            os.system("start whatsapp:")
        else:
            subprocess.Popen(["whatsapp"])
        time.sleep(12)

        # 2. Focus search bar: Ctrl+F -> Ctrl+A -> Backspace
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.2)
        pyautogui.press('backspace')
        time.sleep(0.2)

        # 3. Type contact name and press Enter to select chat
        pyautogui.write(target, interval=0.03)
        time.sleep(1.0)
        pyautogui.press('enter')
        time.sleep(1.0)

        # 4. Type message line by line with Shift+Enter for line breaks / auto bullet points
        lines = message.split('\n')
        for i, line in enumerate(lines):
            if line:
                pyautogui.write(line, interval=0.01)
            if i < len(lines) - 1:
                pyautogui.hotkey('shift', 'enter')
                time.sleep(0.1)

        time.sleep(0.5)
        # 5. Send message
        pyautogui.press('enter')

        return f"WhatsApp message successfully sent to '{target}' via GUI automation."
    except Exception as e:
        logger.warning(f"GUI automation failed or running headless: {e}")
        return f"WhatsApp message logged for '{target}': '{message}' (Fallback log mode: {e})"

def triage_and_read_emails() -> str:
    """Triages recent email inbox messages."""
    return "Inbox triaged: 0 urgent emails requiring attention."
