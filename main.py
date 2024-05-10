import os,env
import logging

from discord.ext import tasks

import interactions

intents = interactions.Intents.DEFAULT
intents.message_content = True  # Required for interactions


bot = interactions.Client(token=env.DISCORD_API_TOKEN,intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as Catmium')

logging.basicConfig(filename='logs.txt', level=logging.ERROR)

# Load slash commands from separate files (replace with your actual commands)
async def load_extensions():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py') and filename != '__init__.py':
            extension = f'commands.{filename[:-3]}'
            await bot.load_extension(extension)  # Remove await here


# Example slash command (replace with your actual commands)
@bot.command(
    name="ping",
    description="Checks the bot's latency",
)
async def ping(ctx: interactions.CommandContext):
    await ctx.respond(f"Pong! Latency: {bot.latency}ms")

token = env.DISCORD_API_TOKEN
bot.start()
