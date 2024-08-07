from discord.ext import commands
import oyun.configr as configr
config=configr.config
ALİVE=config.alive()
AUTHOR, MAİN_AUTH=config.athr()
WORKTYPE=config.wrktyp()
class Alive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def alive(self, ctx):
        user=str(ctx.author)
        if WORKTYPE=="private":
            if user==AUTHOR or user==MAİN_AUTH:
                await ctx.send(f"{ALİVE}{AUTHOR}")
            else:
                await ctx.send("BOT PRİVATE KULLANAMAZSIN!!!")
        elif WORKTYPE=="public":
            await ctx.send(f"{ALİVE}{AUTHOR}")
async def setup(bot):
    await bot.add_cog(Alive(bot)) 