import os
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.header import decode_header
from plyer import notification
import pyautogui
import time
from typing import Dict, Any, List

def send_notification(title: str, message: str) -> str:
    suffix = "\n\n(Message from Meridian-X)"
    if message and suffix not in message:
        message = f"{message}{suffix}"
    notification.notify(
        title=title,
        message=message,
        app_name="Meridian-X",
        timeout=5
    )
    return "Notification dispatched successfully."

def send_email(to: str, subject: str, body: str) -> str:
    # Read email credentials from environment variables or .env file
    smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    sender_email = os.environ.get("SMTP_EMAIL")
    sender_password = os.environ.get("SMTP_PASSWORD")
    
    if not sender_email or not sender_password:
        raise ValueError("SMTP credentials (SMTP_EMAIL, SMTP_PASSWORD) not configured in environment.")

    suffix = "\n\n(Message from Meridian-X)"
    if body and suffix not in body:
        body = f"{body}{suffix}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [to], msg.as_string())
        
    return f"Successfully sent email to {to}"

def read_emails(n: int = 5) -> str:
    imap_server = os.environ.get("IMAP_SERVER", "imap.gmail.com")
    username = os.environ.get("SMTP_EMAIL")
    password = os.environ.get("SMTP_PASSWORD")
    
    if not username or not password:
        raise ValueError("IMAP credentials (SMTP_EMAIL, SMTP_PASSWORD) not configured in environment.")

    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(username, password)
    mail.select("inbox")

    status, messages = mail.search(None, "ALL")
    if status != "OK":
        return "Failed to search mail inbox folder."
        
    mail_ids = messages[0].split()
    latest_ids = mail_ids[-n:]
    latest_ids.reverse()

    lines = []
    for m_id in latest_ids:
        status, msg_data = mail.fetch(m_id, "(RFC822)")
        if status != "OK":
            continue
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8", errors="ignore")
                
                from_addr = msg.get("From")
                lines.append(f"From: {from_addr}\nSubject: {subject}\n")
                
    mail.close()
    mail.logout()
    return "\n".join(lines) if lines else "No emails found in inbox."

def send_whatsapp_message(contact: str, message: str) -> str:
    """Launches WhatsApp desktop, waits for load, searches contact, and sends a message."""
    suffix = "\n\n(Message from Meridian-X)"
    if message and suffix not in message:
        message = f"{message}{suffix}"
    # 1. Open WhatsApp desktop app
    try:
        os.system("start whatsapp://")
    except Exception as e:
        print("Failed to start WhatsApp protocol handler:", e)
        
    # 2. Wait for it to load (typical WebView2 app load time on Windows is 10-20 seconds; we use 15s)
    time.sleep(15.0)
    
    # 3. Focus search box
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.5)
    
    # 4. Select all existing search text
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    
    # 5. Clear search box
    pyautogui.press('backspace')
    time.sleep(0.5)
    
    # 6. Type contact name and press Enter to select
    pyautogui.write(contact, interval=0.01)
    time.sleep(1.5)  # Wait for contact list search results to populate
    pyautogui.press('enter')
    time.sleep(1.0)
    
    # 7. Type message line by line, using shift+enter for newlines, and press Enter to send
    lines = message.split('\n')
    for i, line in enumerate(lines):
        if line:
            pyautogui.write(line, interval=0.01)
        if i < len(lines) - 1:
            pyautogui.hotkey('shift', 'enter')
            time.sleep(0.1)
            
    time.sleep(0.5)
    pyautogui.press('enter')
    
    return f"WhatsApp automation completed: Opened WhatsApp app, waited 15s, searched contact '{contact}', and sent message."

