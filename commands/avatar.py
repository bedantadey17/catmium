import discord,random
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
        avatar_link = f"[**{member.display_name}'s Avatar**]({avatar_url})"

        embed = discord.Embed(description=avatar_link, color=member.color)
        embed.set_image(url=avatar_url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Avatar(bot))

