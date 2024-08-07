from discord.ext import commands
import oyun.configr as configr

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setvar_alive')
    async def setvar_alive(self, ctx, *, new_value: str):
        configr.update_config_line('ALİVE', new_value)
        await ctx.send(f"ALİVE değeri güncellendi: {new_value}")

    @commands.command(name='setvar_token')
    async def setvar_token(self, ctx, *, new_value: str):
        configr.update_config_line('TOKEN', new_value)
        await ctx.send(f"TOKEN değeri güncellendi: {new_value}")

    @commands.command(name='setvar_author')
    async def setvar_author(self, ctx, *, new_value: str):
        configr.update_config_line('AUTHOR', new_value)
        await ctx.send(f"AUTHOR değeri güncellendi: {new_value}")

    @commands.command(name='setvar_worktype')
    async def setvar_worktype(self, ctx, *, new_value: str):
        if new_value not in ["private", "public"]:
            await ctx.send("HATA: WORKTYPE değeri 'private' veya 'public' olmalıdır.")
            return
        configr.update_config_line('WORKTYPE', new_value)
        await ctx.send(f"WORKTYPE değeri güncellendi: {new_value}")

async def setup(bot):
    await bot.add_cog(Config(bot))
