import discord
from discord.ext import commands
import random

class Attack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def attack(self, ctx, target: discord.Member):

        if ctx.author == target:
            await ctx.send(f"{ctx.author.display_name} is **confused**!\n:boom: They hit themselves in confusion!")
            return
        
        messages = [
            ":boom: It's super effective!",
            ":dash: It's not very effective...",
            ":grey_exclamation: But it missed!",
            f":no_entry_sign: It didn't affect {target.display_name}...",
            ":exclamation: But it failed!",
            f":boom: It's a one-hit KO! {target.display_name} fainted! :boom:"
        ]

        if random.random() < 0.05:
            result = messages[-1]
        else:
            result = random.choice(messages[:-1])

        await ctx.send(f"**{ctx.author.display_name}** attacked **{target.display_name}**!\n{result}")

    @attack.error
    async def punch_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You must specify someone to attack!")

async def setup(bot):
    await bot.add_cog(Attack(bot))
