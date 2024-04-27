import discord
from discord.ext import commands
from datetime import datetime

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def user(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title="User Information", color=member.color)

        # Add user information to the embed
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Display Name", value=member.display_name, inline=False)
        embed.add_field(name="Username", value=member, inline=False)
        embed.add_field(name="Roles", value=", ".join(role.name for role in member.roles[1:]), inline=False)
        embed.add_field(name="Account Created On", value=member.created_at.strftime("%Y-%m-%d"), inline=False)
        embed.add_field(name="Joined Server On", value=member.joined_at.strftime("%Y-%m-%d"), inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(User(bot))
