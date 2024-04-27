import env,discord,os
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='c!', intents=intents)

async def load_extensions():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py') and filename != '__init__.py':
            extension = f'commands.{filename[:-3]}'
            await bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def setup_hook():
    await load_extensions()

bot.run(env.DISCORD_API_TOKEN)