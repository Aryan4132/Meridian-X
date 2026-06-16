import os
import asyncio
import threading
import discord
from discord.ext import commands

DISCORD_ACTIVE = False
_bot = None
_thread = None
_loop = None

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
    if _bot and _loop:
        try:
            future = asyncio.run_coroutine_threadsafe(_bot.close(), _loop)
            future.result(timeout=5.0)
        except Exception as e:
            print("[Discord Bridge] Error during bot close:", e)
    print("[Discord Bridge] Background thread stopped.")

def _run_bot(token):
    global _bot, _loop
    _loop = asyncio.new_event_loop()
    asyncio.set_event_loop(_loop)

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

            async with message.channel.typing():
                try:
                    from api import get_react_thoughts
                    model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
                    ocr_model = "PaddleOCR-v4"

                    result = get_react_thoughts(prompt_text, model, ocr_model)
                    reply_text = result.get("text", "Task completed.")

                    from database import add_to_conversations
                    add_to_conversations("user", prompt_text)
                    add_to_conversations("assistant", reply_text)

                    # Discord has a 2000 character limit
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
        _loop.close()
