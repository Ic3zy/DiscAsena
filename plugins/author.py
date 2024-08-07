from discord.ext import commands
import oyun.databaseveri as databaseveri
import oyun.configr as configr
config=configr.config
AUTHOR, MAİN_AUTH=config.athr()
auth=configr.main()
if not auth==MAİN_AUTH:
    MAİN_AUTH=auth
class Auth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='paraver')
    async def paraver(self, ctx, member: commands.MemberConverter = None, eklenecek: str = None):
        user=str(ctx.author)
        if user==AUTHOR or user==MAİN_AUTH:
            if member is None or eklenecek is None:
                await ctx.send("Eksik argüman. Kullanım: .paraver @kullanıcı miktar")
                return
            userr=member.name
            approval, coin_amount, daily_date, time=databaseveri.verigetir(userr)
            print(userr,eklenecek,coin_amount)
            pra=int(coin_amount)+int(eklenecek)
            databaseveri.yaz(userr, pra)
            oldcoin2=int(coin_amount)+int(eklenecek)
            await ctx.send(f"{member.mention}\nKullanıcısına **{eklenecek}** coin eklendi.\nEski miktar: **{coin_amount}**\nYeni miktar: **{oldcoin2}**")
        else:
            await ctx.send(f"{ctx.author.mention} Bu komutu kullanmaya yetkin yok")
    @commands.command(name="block")
    async def block(self, ctx, member: commands.MemberConverter = None):
        user=str(ctx.author)
        if user==AUTHOR or user==MAİN_AUTH:
            if member:
                blk=member.name
                databaseveri.banned(blk)
                await ctx.send(f"{member.mention}\nAdlı kişi Rulet'ten banlandı.")
            else:
                if ctx.message.reference:
                    replied_message = await ctx.fetch_message(ctx.message.reference.message_id)
                    userr=replied_message.author
                    blk=userr.name
                    databaseveri.banned(blk)
                    await ctx.send(f"{userr.mention}\nAdlı kişi Rulet'ten banlandı.")
                else:
                    await ctx.send("Lütfen bir kişiyi etiketleyin yada mesajına yanıt verin.")
        else:
            await ctx.send(f"{ctx.author.mention} Bu komutu kullanmaya yetkin yok")
    @commands.command(name="unblock")
    async def unblock(self, ctx, member: commands.MemberConverter = None):
        user=str(ctx.author)
        if user==AUTHOR or user==MAİN_AUTH:
            if member:
                blk=member.name
                databaseveri.unbanned(blk)
                await ctx.send(f"{member.mention}\nAdlı kişinin Rulet'ten banı Kaldırıldı.")
            else:
                if ctx.message.reference:
                    replied_message = await ctx.fetch_message(ctx.message.reference.message_id)
                    userr=replied_message.author
                    blk=userr.name
                    databaseveri.unbanned(blk)
                    await ctx.send(f"{userr.mention}\nAdlı kişinin Rulet'ten banı Kaldırıldı.")
                else:
                    await ctx.send("Lütfen bir kişiyi etiketleyin yada mesajına yanıt verin.")
        else:
            await ctx.send(f"{ctx.author.mention} Bu komutu kullanmaya yetkin yok")
async def setup(bot):
    await bot.add_cog(Auth(bot))
