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

    status, messages = mail.search(None, "UNSEEN")
    if status != "OK" or not messages[0].strip():
        # Fall back to all mail if no unread
        status, messages = mail.search(None, "ALL")
    if status != "OK":
        return "Failed to search mail inbox folder."
        
    mail_ids = messages[0].split()
    latest_ids = mail_ids[-n:]
    latest_ids.reverse()

    lines = []
    # BUG-54 fix: wrap fetch loop in try/finally so mail.close()/logout() are always
    # called — even if mail.fetch() raises an exception — preventing IMAP connection leak.
    try:
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
                    
                    from_addr = msg.get("From", "Unknown")
                    date_str = msg.get("Date", "")

                    # Extract body: prefer plain text, fall back to HTML (tags stripped)
                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            ct = part.get_content_type()
                            cd = str(part.get("Content-Disposition", ""))
                            if "attachment" in cd:
                                continue
                            if ct == "text/plain":
                                try:
                                    charset = part.get_content_charset() or "utf-8"
                                    body = part.get_payload(decode=True).decode(charset, errors="ignore")
                                    break  # plain text found — no need to continue
                                except Exception:
                                    pass
                            elif ct == "text/html" and not body:
                                try:
                                    import re as _re
                                    charset = part.get_content_charset() or "utf-8"
                                    html = part.get_payload(decode=True).decode(charset, errors="ignore")
                                    # Strip HTML tags for readable plain text
                                    body = _re.sub(r"<[^>]+>", " ", html)
                                    body = _re.sub(r"\s{2,}", " ", body).strip()
                                except Exception:
                                    pass
                    else:
                        try:
                            charset = msg.get_content_charset() or "utf-8"
                            body = msg.get_payload(decode=True).decode(charset, errors="ignore")
                        except Exception:
                            body = ""

                    # Truncate body to 600 chars to keep LLM context manageable
                    body_preview = body.strip()[:600].replace("\n", " ").strip()
                    if len(body.strip()) > 600:
                        body_preview += " [...truncated]"

                    lines.append(
                        f"From: {from_addr}\nDate: {date_str}\nSubject: {subject}\nBody: {body_preview}\n"
                    )
    finally:
        try:
            mail.close()
            mail.logout()
        except Exception:
            pass
    return "\n".join(lines) if lines else "No emails found in inbox."

async def send_whatsapp_message(contact: str, message: str, wait_seconds: float = 15.0) -> str:
    """Launches WhatsApp desktop, waits for load, searches contact, and sends a message."""
    import asyncio
    suffix = "\n\n(Message from Meridian-X)"
    if message and suffix not in message:
        message = f"{message}{suffix}"
    # 1. Open WhatsApp desktop app
    try:
        import subprocess as _sp
        _sp.Popen(["cmd", "/c", "start", "whatsapp://"], shell=False)
    except Exception as e:
        print("Failed to start WhatsApp protocol handler:", e)
        
    # 2. Wait for it to load (non-blocking sleep)
    await asyncio.sleep(wait_seconds)
    
    # 3. Focus search box
    pyautogui.hotkey('ctrl', 'f')
    await asyncio.sleep(0.5)
    
    # 4. Select all existing search text
    pyautogui.hotkey('ctrl', 'a')
    await asyncio.sleep(0.5)
    
    # 5. Clear search box
    pyautogui.press('backspace')
    await asyncio.sleep(0.5)
    
    # 6. Type contact name and press Enter to select
    pyautogui.write(contact, interval=0.01)
    await asyncio.sleep(1.5)  # Wait for contact list search results to populate
    pyautogui.press('enter')
    await asyncio.sleep(1.0)
    
    # 7. Type message line by line, using shift+enter for newlines, and press Enter to send
    lines = message.split('\n')
    for i, line in enumerate(lines):
        if line:
            pyautogui.write(line, interval=0.01)
        if i < len(lines) - 1:
            pyautogui.hotkey('shift', 'enter')
            await asyncio.sleep(0.1)
            
    await asyncio.sleep(0.5)
    pyautogui.press('enter')
    
    return f"WhatsApp automation completed: Opened WhatsApp app, waited {wait_seconds}s, searched contact '{contact}', and sent message."


def triage_and_read_emails(n: int = 5) -> str:
    """Reads the latest unseen/seen emails, extracts their content, and runs LLM triage classification on them."""
    import ollama
    from database import get_ollama_client_host
    from src.tools.communication import read_emails
    
    emails_raw = read_emails(n)
    if "No emails found" in emails_raw or "Failed" in emails_raw or "configured" in emails_raw:
        return emails_raw
        
    try:
        from database import get_brain_model
        model = get_brain_model()
    except Exception:
        model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
        
    prompt = (
        f"You are an expert executive assistant. Triage the following email logs into a highly structured "
        f"report. For each email, classify its Category (Work, Personal, Billing, Spam, Update), "
        f"Priority (High, Medium, Low), suggest a 1-sentence Summary, and suggest a 1-sentence draft action item.\n\n"
        f"Email Logs:\n{emails_raw}\n\n"
        f"Format the output beautifully with markdown tables or clear headers. Output ONLY the triaged report."
    )
    
    try:
        host = get_ollama_client_host()
        client = ollama.Client(host=host)
        res = client.generate(model=model, prompt=prompt)
        triage_report = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
        return f"--- Email Triage Report ---\n\n{triage_report}"
    except Exception as e:
        return f"Emails fetched successfully but LLM triage classification failed: {e}\n\nRaw Emails:\n{emails_raw}"


