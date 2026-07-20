import os
import asyncio
import threading
import time
import discord
from discord.ext import commands

DISCORD_ACTIVE = False
_bot = None
_thread = None
_loop = None

# Discord rate limiter configuration
_discord_rate_lock = threading.Lock()
_discord_rate_buckets = {}
_DISCORD_RATE_LIMIT = 5
_DISCORD_RATE_WINDOW = 60.0

def _is_rate_limited_discord(user_id: int) -> bool:
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

def start_discord_bridge():
    global DISCORD_ACTIVE, _thread
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        print("[Discord Bridge] DISCORD_BOT_TOKEN not configured in .env. Bot bridge disabled.")
        return

    if DISCORD_ACTIVE:
        return

    DISCORD_ACTIVE = True
    _thread = threading.Thread(target=_run_bot, args=(token,), daemon=True)
    _thread.start()
    print("[Discord Bridge] Background thread started.")

def stop_discord_bridge():
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

def _run_bot(token):
    global _bot, _loop
    _loop = asyncio.new_event_loop()
    # N-1 fix: do NOT call asyncio.set_event_loop(_loop) in a non-main thread.

    intents = discord.Intents.default()
    intents.message_content = True
    _bot = commands.Bot(command_prefix="!", intents=intents)

    @_bot.event
    async def on_ready():
        print(f"[Discord Bridge] Bot is online as {_bot.user}")

    @_bot.event
    async def on_message(message):
        if message.author == _bot.user:
            return

        is_dm = isinstance(message.channel, discord.DMChannel)
        is_mention = _bot.user.mentioned_in(message)

        if is_mention or is_dm:
            # Clean mention string out of prompt
            prompt_text = message.content.replace(f"<@{_bot.user.id}>", "").replace(f"<@!{_bot.user.id}>", "").strip()
            if not prompt_text:
                return

            print(f"[Discord Bridge] Received command from {message.author}: '{prompt_text}'")

            # Check rate limiting
            if _is_rate_limited_discord(message.author.id):
                print(f"[Discord Bridge] Rate limit hit for user {message.author.id}. Dropping message.")
                try:
                    await message.reply("⏳ Rate limit reached. Please wait a moment before sending more commands.")
                except Exception:
                    pass
                return

            # Check for bot commands
            cmd = prompt_text.strip().lower()
            if cmd in ["/help", "!help", "help"]:
                help_text = (
                    "🤖 **Meridian-X Discord Bridge**\n\n"
                    "• `/help` or `!help` — Show this help message\n"
                    "• `/status` or `!status` — Check Meridian-X backend health\n"
                    "• `/cancel` or `!cancel` — Interrupt the active agent loop\n\n"
                    "_Or just mention me with a goal to run the agent._"
                )
                try:
                    await message.reply(help_text)
                except Exception:
                    pass
                return
            elif cmd in ["/status", "!status", "status"]:
                import httpx
                try:
                    async with httpx.AsyncClient(timeout=5.0) as client:
                        res = await client.get("http://localhost:4132/api/health")
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
                try:
                    await message.reply(status_text)
                except Exception:
                    pass
                return
            elif cmd in ["/cancel", "!cancel", "cancel"]:
                try:
                    from src.core.loop import interrupt_agent_loop
                    interrupt_agent_loop()
                    await message.reply("⛔ Agent loop interrupted.")
                except Exception as e:
                    await message.reply(f"⚠️ Could not interrupt: {e}")
                return

            async with message.channel.typing():
                try:
                    from src.core.loop import run_react_agent_loop
                    model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
                    ollama_host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
                    if not ollama_host.startswith("http"):
                        ollama_host = f"http://{ollama_host}"

                    reply_parts = []
                    async for event in run_react_agent_loop(prompt_text, model, ollama_host):
                        if event.startswith("event: text\n"):
                            for line in event.splitlines():
                                if line.startswith("data: "):
                                    reply_parts.append(line[6:])

                    reply_text = "".join(reply_parts).strip() or "Task completed."

                    from database import add_to_conversations
                    add_to_conversations("user", prompt_text)
                    add_to_conversations("assistant", reply_text)

                    # Discord has a 2000 character limit per message
                    if len(reply_text) > 2000:
                        for i in range(0, len(reply_text), 2000):
                            await message.reply(reply_text[i:i+2000])
                    else:
                        await message.reply(reply_text)

                except Exception as e:
                    print(f"[Discord Bridge] Error processing command: {e}")
                    try:
                        await message.reply(f"❌ Error processing command: {str(e)}")
                    except Exception:
                        pass

    try:
        _loop.run_until_complete(_bot.start(token))
    except Exception as e:
        print(f"[Discord Bridge] Bot loop encountered error: {e}")
    finally:
        # BUG-12 fix: always close the private event loop when the bot exits
        if not _loop.is_closed():
            _loop.close()
