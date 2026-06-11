import os
import discord
from discord.ext import commands
import requests

# Configuration — token must be set in environment or .env file
TOKEN = os.environ.get('DISCORD_BOT_TOKEN', '')
OLLAMA_URL = 'http://localhost:11434/api/generate'
MODEL_NAME = 'gemma4:31b-cloud'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Meridian-X is now online as {bot.user}')

@bot.event
async def on_message(message):
    # Prevent bot from responding to itself
    if message.author == bot.user:
        return

    # Only respond if bot is mentioned or it's a DM
    if bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        # Clean the message (remove the mention)
        user_input = message.content.replace(f'<@{bot.user.id}>', '').strip()
        
        async with message.channel.typing():
            try:
                # Call local Ollama API
                payload = {
                    'model': MODEL_NAME,
                    'prompt': user_input,
                    'stream': False
                }
                response = requests.post(OLLAMA_URL, json=payload)
                response.raise_for_status()
                
                result = response.json()
                bot_response = result.get('response', 'I encountered an error processing that.')
                
                # Discord has a 2000 character limit
                if len(bot_response) > 2000:
                    for i in range(0, len(bot_response), 2000):
                        await message.reply(bot_response[i:i+2000])
                else:
                    await message.reply(bot_response)
                    
            except Exception as e:
                await message.reply(f'Error connecting to Meridian-X backend: {str(e)}')

bot.run(TOKEN)