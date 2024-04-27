from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calc(self, ctx, *, equation=None):
        if equation is None:
            await ctx.send("You need to use numbers!")
            return

        try:
            result = eval(equation)
            await ctx.send(f"**Equation queried:** `{equation}`\n**Result:** `{result}`")
        except Exception as e:
            await ctx.send(f"**Error:** {e}")

async def setup(bot):
    await bot.add_cog(Calculator(bot))
