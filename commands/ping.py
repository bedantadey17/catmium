import interactions

# Create a Client instance (optional but recommended for larger projects)
client = interactions.Client(intents=interactions.Intents.DEFAULT)
client.intents.message_content = True  # Required for interactions

# Create the SlashCommand instance
slash = SlashCommand(sync_commands=True)  # Sync commands automatically

@slash.slash(
    name="ping",
    description="Checks the bot's latency"
)
async def ping(ctx: SlashContext):
    try:
        await ctx.respond(f"Pong! Latency: {client.latency}ms")
    except Exception as e:  # Catch any unexpected errors
        await ctx.send(f"An error occurred: {str(e)}", ephemeral=True)  # Send error message in a temporary message

client.start(os.getenv('DISCORD_API_TOKEN'))  # Assuming you have the token in an environment variable
