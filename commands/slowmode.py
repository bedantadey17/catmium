import discord
from discord.ext import commands

class Slowmode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, duration: int = 0):
        if duration < 0:
            await ctx.send("Duration cannot be negative.")
            return

        if duration == 0:
            await ctx.channel.edit(slowmode_delay=0)
            await ctx.send("Slowmode disabled.")
        else:
            await ctx.channel.edit(slowmode_delay=duration)
            await ctx.send(f"Slowmode set to {duration} seconds.")

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command.")

async def setup(bot):
    await bot.add_cog(Slowmode(bot))
