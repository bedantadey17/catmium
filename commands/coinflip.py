import discord
from discord.ext import commands
import random

class CoinFlip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx):
        outcomes = ['Heads', 'Tails', 'side']
        outcome = random.choices(outcomes, weights=[49.975, 49.975, 0.05], k=1)[0]

        if outcome == 'side':
            message = f"{ctx.author.mention} flipped a coin!\n:coin::question: It landed **on the side**...? That's rare!"
        else:
            message = f"{ctx.author.mention} flipped a coin!\n:coin: Landed on **{outcome}**!"

        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(CoinFlip(bot))
