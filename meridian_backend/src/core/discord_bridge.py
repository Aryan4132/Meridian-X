"""
discord_bridge.py — Discord Bot Bridge for Meridian-X

Provides bidirectional Discord communication:
- Bot listens for @mentions and DMs, routes to agent loop
- Public API: send messages, read history, add reactions, list channels
- Slash commands: /help, /status, /cancel
- Voice attachment support: download → STT → agent → TTS reply
"""

import os
import asyncio
import threading
import time
import tempfile
from typing import Optional, Dict, Any, List

try:
    import discord  # type: ignore
    from discord.ext import commands  # type: ignore
except ImportError:
    discord = None
    commands = None


# ---------------------------------------------------------------------------
# Module state
# ---------------------------------------------------------------------------
DISCORD_ACTIVE = False
_bot = None
_thread = None
_loop = None

_recent_messages_lock = threading.Lock()
_recent_discord_messages: List[Dict[str, Any]] = []


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


# ---------------------------------------------------------------------------
# Voice attachment processing
# ---------------------------------------------------------------------------
async def _process_voice_attachment(message) -> Optional[str]:
    """Download audio attachment from Discord message, transcribe via STT.

    Returns transcription text or None if no audio attachment or STT fails.
    """
    if not message.attachments:
        return None

    audio_attachment = None
    audio_extensions = (".ogg", ".wav", ".mp3", ".m4a", ".flac", ".webm", ".opus")
    for att in message.attachments:
        if att.filename and any(att.filename.lower().endswith(ext) for ext in audio_extensions):
            audio_attachment = att
            break

    if audio_attachment is None:
        return None

    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, f"meridian_discord_voice_{int(time.time())}_{audio_attachment.filename}")

    try:
        await audio_attachment.save(temp_path)
        print(f"[Discord Bridge] Downloaded voice attachment: {audio_attachment.filename}")

        from src.voice.stt import transcribe_audio_file
        transcription = transcribe_audio_file(temp_path)
        print(f"[Discord Bridge] Voice transcription: '{transcription}'")
        return transcription
    except Exception as e:
        print(f"[Discord Bridge] Voice transcription failed: {e}")
        return None
    finally:
        try:
            os.remove(temp_path)
        except Exception:
            pass


async def _send_tts_reply(message, reply_text: str) -> None:
    """Synthesize TTS audio and send as voice file reply."""
    try:
        from src.voice.tts import get_tts_engine
        engine = get_tts_engine()
        if not engine:
            return

        print("[Discord Bridge] Synthesizing speech reply...")
        style = engine.get_voice_style(voice_name="M1")
        wav, duration = engine.synthesize(reply_text, voice_style=style, lang="na")

        temp_dir = tempfile.gettempdir()
        temp_wav = os.path.join(temp_dir, f"meridian_discord_reply_{int(time.time())}.wav")
        engine.save_audio(wav, temp_wav)

        try:
            await message.reply(file=discord.File(temp_wav, filename="meridian_reply.wav"))  # type: ignore
        finally:
            try:
                os.remove(temp_wav)
            except Exception:
                pass
    except Exception as e:
        print(f"[Discord Bridge] TTS reply failed: {e}")


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
# Agent loop execution
# ---------------------------------------------------------------------------
async def _run_agent_for_message(message, prompt_text: str, is_voice: bool = False) -> None:
    """Run the ReAct agent loop for a Discord message and reply with result."""
    # Send thinking indicator
    try:
        await message.reply("🤔 Processing command...")
    except Exception:
        pass

    async with message.channel.typing():
        try:
            from src.core.loop import run_react_agent_loop
            from database import get_user_profile, get_ollama_client_host
            provider = get_user_profile("meridian_provider") or os.environ.get("MERIDIAN_PROVIDER") or "ollama"
            model = (
                get_user_profile("meridian_model")
                or os.environ.get("MERIDIAN_MODEL")
                or ""
            )
            model_source = (
                get_user_profile("meridian_model_source")
                or os.environ.get("MERIDIAN_MODEL_SOURCE")
                or ("local" if provider == "ollama" else "api")
            )
            ollama_host = get_ollama_client_host()
            if not ollama_host.startswith("http"):
                ollama_host = f"http://{ollama_host}"

            reply_parts = []
            async for event in run_react_agent_loop(
                prompt_text, model, ollama_host,
                model_source=model_source, api_provider=provider,
            ):
                if event.startswith("event: text\n"):
                    for line in event.splitlines():
                        if line.startswith("data: "):
                            reply_parts.append(line[6:])

            reply_text = "".join(reply_parts).strip() or "Task completed."
            # NOTE: run_react_agent_loop already logs user + assistant turns
            # to conversations — do not duplicate here.

            # Send chunked text reply
            await _send_discord_message(message, reply_text)

            # Send TTS voice reply if original message was a voice attachment
            if is_voice:
                await _send_tts_reply(message, reply_text)

        except Exception as e:
            print(f"[Discord Bridge] Error processing command: {e}")
            try:
                await message.reply(f"❌ Error processing command: {str(e)}")
            except Exception:
                pass


# ---------------------------------------------------------------------------
# Public API functions (called from communication.py tool wrappers)
# ---------------------------------------------------------------------------
def read_discord_msgs(channel_id: Optional[str] = None, limit: int = 10) -> str:
    """Reads recent messages from specified channel or logged buffer."""
    global _bot, _loop, DISCORD_ACTIVE
    if DISCORD_ACTIVE and _bot and _loop and _loop.is_running():
        try:
            async def _fetch():
                target_id = int(channel_id) if (channel_id and channel_id.isdigit()) else None
                msgs = []
                if target_id:
                    channel = _bot.get_channel(target_id)
                    if channel:
                        async for m in channel.history(limit=limit):
                            msgs.append(f"[{m.created_at.strftime('%Y-%m-%d %H:%M')}] {m.author} (ID {m.id}): {m.content}")
                        return "\n".join(msgs) if msgs else f"No recent messages in channel {target_id}."

                for guild in _bot.guilds:
                    for ch in guild.text_channels:
                        if ch.permissions_for(guild.me).read_message_history:
                            async for m in ch.history(limit=min(limit, 5)):
                                msgs.append(f"[{ch.name}] {m.author}: {m.content}")
                return "\n".join(msgs[:limit]) if msgs else "No recent messages found across active channels."

            future = asyncio.run_coroutine_threadsafe(_fetch(), _loop)
            return future.result(timeout=10.0)
        except Exception as e:
            print(f"[Discord Bridge] Fetch history error: {e}")

    with _recent_messages_lock:
        if not _recent_discord_messages:
            return "No recent Discord messages logged."
        filtered = _recent_discord_messages
        if channel_id:
            filtered = [m for m in _recent_discord_messages if m["channel_id"] == channel_id]
        recent_slice = filtered[-limit:]
        res = [f"[{m['author']} in {m['channel_id']}]: {m['content']}" for m in recent_slice]
        return "\n".join(res) if res else f"No logged messages for channel {channel_id}."


def add_discord_reaction_msg(message_id: str, emoji: str, channel_id: Optional[str] = None) -> str:
    """Adds an emoji reaction to a specific message by ID."""
    if not message_id or not emoji:
        return "Error: Message ID and emoji are required."

    global _bot, _loop, DISCORD_ACTIVE
    if DISCORD_ACTIVE and _bot and _loop and _loop.is_running():
        try:
            async def _react():
                msg_id = int(message_id) if message_id.isdigit() else None
                chan_id = int(channel_id) if (channel_id and channel_id.isdigit()) else None
                if not msg_id:
                    return "Error: Invalid message_id."

                if chan_id:
                    channel = _bot.get_channel(chan_id)
                    if channel:
                        msg = await channel.fetch_message(msg_id)
                        await msg.add_reaction(emoji)
                        return f"Reaction '{emoji}' added to message {msg_id} in channel {chan_id}."

                for guild in _bot.guilds:
                    for ch in guild.text_channels:
                        try:
                            msg = await ch.fetch_message(msg_id)
                            await msg.add_reaction(emoji)
                            return f"Reaction '{emoji}' added to message {msg_id} in channel '{ch.name}'."
                        except Exception:
                            continue
                return f"Error: Message {msg_id} not found in connected channels."

            future = asyncio.run_coroutine_threadsafe(_react(), _loop)
            return future.result(timeout=10.0)
        except Exception as e:
            return f"Error adding reaction: {e}"

    return "Error: Discord bot bridge is inactive. Cannot add reactions."


def list_discord_channels_info() -> str:
    """Lists servers and text channels accessible by the Discord bot."""
    global _bot, _loop, DISCORD_ACTIVE
    if DISCORD_ACTIVE and _bot and _loop and _loop.is_running():
        try:
            async def _list_ch():
                lines = []
                for guild in _bot.guilds:
                    lines.append(f"🏰 Guild: {guild.name} (ID: {guild.id})")
                    for ch in guild.text_channels:
                        lines.append(f"  • #{ch.name} (ID: {ch.id})")
                return "\n".join(lines) if lines else "Bot is connected to 0 guilds/channels."

            future = asyncio.run_coroutine_threadsafe(_list_ch(), _loop)
            return future.result(timeout=10.0)
        except Exception as e:
            return f"Error listing Discord channels: {e}"

    return "Discord bot bridge is inactive. Set DISCORD_BOT_TOKEN to enable bot bridge."


def send_discord_msg(target: str = "", message: str = "", channel_id: Optional[str] = None) -> str:
    """Dispatches a message to a Discord channel or user via active bot or Webhook URL fallback."""
    if not message or not message.strip():
        return "Error: Empty message provided."

    global _bot, _loop, DISCORD_ACTIVE
    if DISCORD_ACTIVE and _bot and _loop and _loop.is_running():
        try:
            async def _dispatch():
                target_id = int(channel_id) if (channel_id and channel_id.isdigit()) else (int(target) if (target and target.isdigit()) else None)

                if target_id:
                    channel = _bot.get_channel(target_id)
                    if channel:
                        await _send_discord_message(channel, message)
                        return f"Message sent to Discord channel {target_id} via Bot."

                    # Try fetching user by User ID to open DM
                    try:
                        user = _bot.get_user(target_id) or await _bot.fetch_user(target_id)
                        if user:
                            dm = await user.create_dm()
                            await _send_discord_message(dm, message)
                            return f"DM sent to Discord user {user.name} ({target_id}) via Bot."
                    except Exception as fe:
                        print(f"[Discord Bridge] User fetch error for {target_id}: {fe}")

                if target:
                    for guild in _bot.guilds:
                        member = guild.get_member_named(target)
                        if member:
                            dm = await member.create_dm()
                            await _send_discord_message(dm, message)
                            return f"DM sent to Discord user {target} ({member.id}) via Bot."

                return "Error: Specified Discord channel or user ID not found or bot lacks DM access."

            future = asyncio.run_coroutine_threadsafe(_dispatch(), _loop)
            return future.result(timeout=10.0)
        except Exception as e:
            print(f"[Discord Bridge] Bot dispatch failed: {e}")

    # Webhook fallback
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "")
    if webhook_url:
        try:
            import httpx
            with httpx.Client(timeout=10.0) as client:
                resp = client.post(webhook_url, json={"content": message})
                if resp.status_code in (200, 204):
                    return "Discord message dispatched via Webhook."
                else:
                    return f"Discord Webhook returned status code {resp.status_code}."
        except Exception as e:
            return f"Discord Webhook dispatch error: {e}"

    return "Error: Discord bot bridge is inactive (DISCORD_BOT_TOKEN missing/stopped) and DISCORD_WEBHOOK_URL is not configured."


# ---------------------------------------------------------------------------
# Bridge lifecycle
# ---------------------------------------------------------------------------
def start_discord_bridge():
    """Start the Discord bot in a background daemon thread."""
    global _thread
    if not discord:
        print("[Discord Bridge] discord.py library not installed. Bot bridge disabled.")
        return

    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        print("[Discord Bridge] DISCORD_BOT_TOKEN not configured in .env. Bot bridge disabled.")
        return

    global DISCORD_ACTIVE
    if DISCORD_ACTIVE:
        return

    # NOTE: DISCORD_ACTIVE is set True inside on_ready, not here.
    # This prevents the flag from being True while the bot is still connecting.
    _thread = threading.Thread(target=_run_bot, args=(token,), daemon=True)
    _thread.start()
    print("[Discord Bridge] Background thread started. Waiting for on_ready...")


def stop_discord_bridge():
    """Gracefully stop the Discord bot and close its event loop."""
    global DISCORD_ACTIVE, _bot, _loop
    if not DISCORD_ACTIVE:
        return
    DISCORD_ACTIVE = False
    print("[Discord Bridge] Stopping Discord bot...")
    if _bot and _loop and _loop.is_running():
        try:
            future = asyncio.run_coroutine_threadsafe(_bot.close(), _loop)
            future.result(timeout=5.0)
        except Exception as e:
            print("[Discord Bridge] Error during bot close:", e)
    # BUG-12 fix: explicitly stop the private event loop after bot close to prevent leak
    if _loop and not _loop.is_closed():
        try:
            _loop.call_soon_threadsafe(_loop.stop)
        except Exception:
            pass
    print("[Discord Bridge] Stopped.")


# ---------------------------------------------------------------------------
# Bot runner (background thread)
# ---------------------------------------------------------------------------
def _run_bot(token):
    """Main bot entry point — runs in a dedicated daemon thread."""
    global _bot, _loop, DISCORD_ACTIVE
    if not discord or not commands:
        print("[Discord Bridge] discord.py package not installed.")
        return

    _loop = asyncio.new_event_loop()
    # N-1 fix: do NOT call asyncio.set_event_loop(_loop) in a non-main thread.

    intents = discord.Intents.default()  # type: ignore
    intents.message_content = True
    _bot = commands.Bot(command_prefix="!", intents=intents)  # type: ignore

    @_bot.event
    async def on_ready():
        global DISCORD_ACTIVE
        DISCORD_ACTIVE = True
        print(f"[Discord Bridge] Bot is online as {_bot.user}")

    @_bot.event
    async def on_message(message):
        if message.author == _bot.user:
            return

        # Log all messages to buffer
        with _recent_messages_lock:
            _recent_discord_messages.append({
                "id": str(message.id),
                "author": str(message.author),
                "author_id": str(message.author.id),
                "channel_id": str(message.channel.id),
                "content": message.content,
                "timestamp": time.time()
            })
            if len(_recent_discord_messages) > 100:
                _recent_discord_messages.pop(0)

        is_dm = isinstance(message.channel, discord.DMChannel)  # type: ignore
        is_mention = _bot.user.mentioned_in(message)

        if not (is_mention or is_dm):
            return

        # SEC-17: Sender allowlist check
        if not _is_sender_allowed(message.author.id):
            from src.core.audit_logger import log_sensitive_action
            log_sensitive_action("SECURITY_VIOLATION", "bridge_unauthorized_sender", {"user_id": str(message.author.id), "platform": "discord"}, "FAILED")
            try:
                await message.reply("⚠️ Access Denied: Your Discord account is not on the Meridian-X allowlist.")
            except Exception:
                pass
            return

        # Clean mention string out of prompt
        prompt_text = message.content.replace(f"<@{_bot.user.id}>", "").replace(f"<@!{_bot.user.id}>", "").strip()

        # Check for slash commands first
        cmd = prompt_text.strip().lower()
        if await _handle_slash_command(message, cmd):
            return

        # Check for voice attachment
        is_voice = False
        if not prompt_text:
            voice_text = await _process_voice_attachment(message)
            if voice_text:
                prompt_text = voice_text
                is_voice = True

        if not prompt_text:
            return

        print(f"[Discord Bridge] Received command from {message.author}: '{prompt_text}'")

        # Rate limiting
        if _is_rate_limited_discord(message.author.id):
            print(f"[Discord Bridge] Rate limit hit for user {message.author.id}. Dropping message.")
            try:
                await message.reply("⏳ Rate limit reached. Please wait a moment before sending more commands.")
            except Exception:
                pass
            return

        # Run agent
        await _run_agent_for_message(message, prompt_text, is_voice=is_voice)

    try:
        _loop.run_until_complete(_bot.start(token))
    except Exception as e:
        print(f"[Discord Bridge] Bot loop encountered error: {e}")
    finally:
        DISCORD_ACTIVE = False
        # BUG-12 fix: always close the private event loop when the bot exits
        if not _loop.is_closed():
            _loop.close()


if __name__ == "__main__":
    print("🚀 [Discord Bridge Daemon] Starting standalone Discord bot daemon...")
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        print("[Discord Bridge] DISCORD_BOT_TOKEN not configured in .env. Bot bridge disabled.")
    elif not discord:
        print("[Discord Bridge] discord.py library not installed. Bot bridge disabled.")
    else:
        # Run in the foreground: a daemon thread would die with the main thread.
        _run_bot(token)

