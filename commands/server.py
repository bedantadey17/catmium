import discord
from discord.ext import commands
from datetime import datetime

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def server(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title="Server Information", color=discord.Color.blurple())
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="Members", value=guild.member_count, inline=False)
        bot_count = sum(1 for member in guild.members if member.bot)
        embed.add_field(name="Bots", value=bot_count, inline=False)
        embed.add_field(name="Server Created On", value=guild.created_at.strftime("%Y-%m-%d"), inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Server(bot))
