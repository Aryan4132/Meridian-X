"""Discord bridge support: rate limiting, allowlist, chunking, slash commands.

Split from ``src.core.discord_bridge`` (Phase 2 god-file refactor). Pure
move — zero behavior changes. ``discord_bridge.py`` re-exports every
symbol so existing imports keep working.
"""

import os
import threading
import time
from typing import Dict, List


# ---------------------------------------------------------------------------
# Per-user token bucket rate limiter: max 5 messages per 60 seconds per user
# ---------------------------------------------------------------------------
_discord_rate_lock = threading.Lock()
_discord_rate_buckets: Dict[int, Dict] = {}
_DISCORD_RATE_LIMIT = 5
_DISCORD_RATE_WINDOW = 60.0


def _is_rate_limited_discord(user_id: int) -> bool:
    """Return True if user_id has exceeded the rate limit."""
    with _discord_rate_lock:
        now = time.time()
        bucket = _discord_rate_buckets.get(user_id)
        if bucket is None:
            _discord_rate_buckets[user_id] = {"tokens": _DISCORD_RATE_LIMIT - 1, "last_refill": now}
            return False
        elapsed = now - bucket["last_refill"]
        if elapsed >= _DISCORD_RATE_WINDOW:
            bucket["tokens"] = _DISCORD_RATE_LIMIT - 1
            bucket["last_refill"] = now
            return False
        if bucket["tokens"] > 0:
            bucket["tokens"] -= 1
            return False
        return True


# ---------------------------------------------------------------------------
# SEC-17: Sender allowlist check
# ---------------------------------------------------------------------------
def _is_sender_allowed(author_id: int) -> bool:
    """Check if Discord user ID is on the Meridian allowlist.

    Fail-closed: an unset or unparseable allowlist denies everyone, since the
    bot executes agent commands on the host.
    """
    allowed_ids_raw = os.environ.get("MERIDIAN_ALLOWED_DISCORD_IDS", "")
    if not allowed_ids_raw.strip():
        return False  # No allowlist configured — deny access
    allowed_ids = {int(x.strip()) for x in allowed_ids_raw.split(",") if x.strip().isdigit()}
    if not allowed_ids:
        return False  # Parsing yielded empty set — deny access
    return author_id in allowed_ids


# ---------------------------------------------------------------------------
# Message chunker: Discord's max message length is 2000 chars
# ---------------------------------------------------------------------------
_DISCORD_MAX_LEN = 2000


async def _send_discord_message(target, text: str) -> None:
    """Send text to a Discord messageable target, splitting into chunks if > 2000 chars.

    Splits on paragraph boundaries when possible (matching Telegram bridge pattern).
    ``target`` must be a discord.abc.Messageable (channel, user, message for reply).
    """
    if not text:
        return

    is_message = hasattr(target, "reply")  # discord.Message vs channel/user

    chunks: List[str] = []
    remaining = text
    while len(remaining) > _DISCORD_MAX_LEN:
        split_at = remaining.rfind("\n\n", 0, _DISCORD_MAX_LEN)
        if split_at == -1:
            split_at = remaining.rfind("\n", 0, _DISCORD_MAX_LEN)
        if split_at == -1:
            split_at = _DISCORD_MAX_LEN
        chunks.append(remaining[:split_at].strip())
        remaining = remaining[split_at:].strip()
    if remaining:
        chunks.append(remaining)

    for i, chunk in enumerate(chunks):
        suffix = f"\n_(Part {i+1}/{len(chunks)})_" if len(chunks) > 1 else ""
        try:
            if is_message and i == 0:
                await target.reply(chunk + suffix)
            elif is_message:
                await target.channel.send(chunk + suffix)
            else:
                await target.send(chunk + suffix)
        except Exception as e:
            print(f"[Discord Bridge] Failed to send chunk {i+1}: {e}")


# ---------------------------------------------------------------------------
# Bot slash command handler
# ---------------------------------------------------------------------------
async def _handle_slash_command(message, cmd: str) -> bool:
    """Handle /help, /status, /cancel bot commands. Returns True if handled."""
    if cmd in ["/help", "!help", "help"]:
        help_text = (
            "🤖 **Meridian-X Discord Bridge**\n\n"
            "• `/help` or `!help` — Show this help message\n"
            "• `/status` or `!status` — Check Meridian-X backend health\n"
            "• `/cancel` or `!cancel` — Interrupt the active agent loop\n\n"
            "_Or just mention me with a goal to run the agent._"
        )
        await _send_discord_message(message, help_text)
        return True

    elif cmd in ["/status", "!status", "status"]:
        import httpx
        try:
            port = os.getenv("PORT", os.getenv("MERIDIAN_PORT", "4132"))
            async with httpx.AsyncClient(timeout=5.0) as client:
                res = await client.get(f"http://localhost:{port}/api/health")
                if res.status_code == 200:
                    data = res.json()
                    status_text = (
                        f"✅ **Meridian-X Status**\n"
                        f"• Backend: {data.get('status', 'unknown')}\n"
                        f"• SQLite: {data.get('sqlite', 'unknown')}\n"
                        f"• MongoDB: {data.get('mongodb', 'unknown')}\n"
                        f"• Ollama: {data.get('ollama', 'unknown')}"
                    )
                else:
                    status_text = f"⚠️ Backend returned HTTP {res.status_code}."
        except Exception as e:
            status_text = f"❌ Backend unreachable: {e}"
        await _send_discord_message(message, status_text)
        return True

    elif cmd in ["/cancel", "!cancel", "cancel"]:
        try:
            from src.core.loop import interrupt_agent_loop
            interrupt_agent_loop()
            await _send_discord_message(message, "⛔ Agent loop interrupted.")
        except Exception as e:
            await _send_discord_message(message, f"⚠️ Could not interrupt: {e}")
        return True

    return False
