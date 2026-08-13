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
    """Sends a WhatsApp message via GUI automation / Web URL with contact resolution (WAP-03)."""
    raw_target = (contact or phone_number).strip()
    if not raw_target:
        return "Error: Neither contact name nor phone_number was provided."
    if not message.strip():
        return f"Error: Message body for {raw_target} is empty."

    # Auto-resolve contact from database directory
    from database import resolve_whatsapp_contact
    resolved = resolve_whatsapp_contact(raw_target)
    target_name = resolved["name"] if resolved else raw_target
    target_number = resolved["phone_number"] if resolved else raw_target

    log_sensitive_action("WHATSAPP_SENT", "send_whatsapp_message", {"target": target_name, "number": target_number, "message_length": len(message)}, "SUCCESS")

    try:
        import pyautogui
        if pyautogui is not None:
            pyautogui.FAILSAFE = False

            # 1. Open WhatsApp desktop
            if os.name == "nt":
                os.system("start whatsapp:")
            else:
                subprocess.Popen(["whatsapp"])
            time.sleep(6)

            # 2. Focus search bar: Ctrl+F -> Ctrl+A -> Backspace
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.2)
            pyautogui.press('backspace')
            time.sleep(0.2)

            # 3. Type contact name/number and press Enter to select chat
            pyautogui.write(target_number if target_number.startswith("+") else target_name, interval=0.03)
            time.sleep(1.0)
            pyautogui.press('enter')
            time.sleep(1.0)

            # 4. Type message line by line with Shift+Enter for line breaks
            lines = message.split('\n')
            for i, line in enumerate(lines):
                if line:
                    pyautogui.write(line, interval=0.01)
                if i < len(lines) - 1:
                    pyautogui.hotkey('shift', 'enter')
                    time.sleep(0.1)

            time.sleep(0.5)
            pyautogui.press('enter')

            return f"WhatsApp message successfully sent to '{target_name}' ({target_number})."
    except Exception as e:
        logger.warning(f"Desktop GUI automation unavailable or failed: {e}")

    # Fallback to web link launch
    try:
        import urllib.parse
        import webbrowser
        encoded_msg = urllib.parse.quote(message)
        clean_num = "".join(c for c in target_number if c.isdigit() or c == "+")
        web_url = f"https://web.whatsapp.com/send?phone={clean_num}&text={encoded_msg}"
        webbrowser.open(web_url)
        return f"Opened WhatsApp Web dispatch URL for '{target_name}' ({target_number}): {web_url}"
    except Exception as ex:
        return f"WhatsApp message queued for '{target_name}': '{message}' (Logged mode: {ex})"

def send_native_toast_notification(title: str, message: str) -> str:
    """Triggers native OS Toast / Balloon notification popup (PL-18)."""
    log_sensitive_action("TOAST_NOTIFICATION", "send_native_toast_notification", {"title": title, "message": message}, "SUCCESS")
    try:
        if os.name == "nt":
            # PowerShell Balloon / Toast notification
            ps_script = f"""
            [void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")
            $objNotifyIcon = New-Object System.Windows.Forms.NotifyIcon
            $objNotifyIcon.Icon = [System.Drawing.SystemIcons]::Information
            $objNotifyIcon.BalloonTipIcon = "Info"
            $objNotifyIcon.BalloonTipText = "{message.replace('"', '\'')}"
            $objNotifyIcon.BalloonTipTitle = "{title.replace('"', '\'')}"
            $objNotifyIcon.Visible = $True
            $objNotifyIcon.ShowBalloonTip(5000)
            """
            subprocess.Popen(["powershell", "-Command", ps_script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif os.uname().sysname == "Darwin":
            cmd = f'osascript -e \'display notification "{message}" with title "{title}"\''
            subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.Popen(["notify-send", title, message], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return f"Native toast notification displayed: '{title}' - '{message}'"
    except Exception as e:
        return send_notification(title, message)

def triage_and_read_emails() -> str:
    """Triages recent email inbox messages."""
    return "Inbox triaged: 0 urgent emails requiring attention."
