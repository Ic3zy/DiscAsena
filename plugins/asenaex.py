from discord.ext import commands
import discord
import oyun.configr as configr
config=configr.config
WORKTYPE=config.wrktyp()
AUTHOR, MAİN_AUTH=config.athr()
auth=configr.main()
if not auth==MAİN_AUTH:
    MAİN_AUTH=auth
class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def asena(self, ctx):
        if WORKTYPE=="private":
            user=str(ctx.author)
            if user==AUTHOR or user==MAİN_AUTH:
                embed = discord.Embed(
                    title="●▬▬▬ **DiscAsena Private** ▬▬▬●",
                )
                embed.add_field(
                    name="🛠 : .soru [@kullanıcı]",
                    value="💬 : Belirtilen kullanıcıya rastgele bir soru sorar.",
                    inline=False
                )
                embed.add_field(
                    name="🛠 : .zorsoru [@kullanıcı]",
                    value="💬 : Belirtilen kullanıcıya rastgele zor bir soru sorar. ",
                    inline=False
                )
                embed.add_field(
                name="🛠 : .alive",
                value="💬 : Botun aktif olup olmadığını sorar.",
                inline=False
                )
                embed.add_field(
                name="🛠 : .tagall",
                value="💬 : Sunucudaki herkesi etiketlemek için kullanılır.",
                inline=False
                )
                embed.add_field(
                name="🛠 : .asena",
                value="💬 : Botun tüm komutlarına erişmek için kullanılır.",
                inline=False
                )
                embed.add_field(
                name="🛠 : .ban",
                value="💬 : Yanıtladığınız/Etiketlediğiniz kişiyi gruptan banlar.",
                inline=False
                )
                embed.add_field(
                name="🛠 : .unban",
                value="💬 : Sunucudan Banladığınız Kişinin banını açar ve sunucuya davet eder.",
                inline=False
                )
                embed.add_field(
                name="🛠 : .gay",
                value="💬 : Kişinin gay yğzdesini ölçer.",
                inline=False
                )
                embed.add_field(
                name="🛠 : .lez",
                value="💬 : Kişinin lez yüzdesini ölçer.",
                inline=False
                )
                embed.add_field(
                name="🛠 : .myt",
                value="💬 : Youtube'dan şarkı indirip göndermenizi sağlar.",
                inline=False
                )
                embed.add_field(
                name="🛠 : .rulet",
                value="💬 : Rulet oynar. Bilgi için .rlth yazınız.",
                inline=False
                )
                embed.add_field(
                name="🛠 : .kayitol",
                value="💬 : Rulet oynamak için kayıt olur.",
                inline=False
                )
                embed.add_field(
                name="🛠 : .money",
                value="💬 : Kaç coininiz olduğunu size söyler.",
                inline=False
                )
                embed.add_field(
                name="🛠 : .daily",
                value="💬 : 12 Saatte bir alabileceğiniz 200 coinlik bonus'tur",
                inline=False
                )
                """embed.add_field(
                name="🛠 : ",
                value="💬 : ",
                inline=False
                )"""
                await ctx.send(embed=embed)
        elif WORKTYPE=="public":
            embed = discord.Embed(
                title="●▬▬▬ **DiscAsena Public** ▬▬▬●",
            )
            embed.add_field(
                name="🛠 : .soru [@kullanıcı]",
                value="💬 : Belirtilen kullanıcıya rastgele bir soru sorar.",
                inline=False
            )
            embed.add_field(
                name="🛠 : .zorsoru [@kullanıcı]",
                value="💬 : Belirtilen kullanıcıya rastgele zor bir soru sorar. ",
                inline=False
            )
            embed.add_field(
            name="🛠 : .alive",
            value="💬 : Botun aktif olup olmadığını sorar.",
            inline=False
            )
            embed.add_field(
            name="🛠 : .tagall",
            value="💬 : Sunucudaki herkesi etiketlemek için kullanılır.",
            inline=False
            )
            embed.add_field(
            name="🛠 : .asena",
            value="💬 : Botun tüm komutlarına erişmek için kullanılır.",
            inline=False
            )
            embed.add_field(
            name="🛠 : .ban",
            value="💬 : Yanıtladığınız/Etiketlediğiniz kişiyi gruptan banlar.",
            inline=False
            )
            embed.add_field(
            name="🛠 : .unban",
            value="💬 : Sunucudan Banladığınız Kişinin banını açar ve sunucuya davet eder.",
            inline=False
            )
            embed.add_field(
            name="🛠 : .gay",
            value="💬 : Kişinin gay yğzdesini ölçer.",
            inline=False
            )
            embed.add_field(
            name="🛠 : .lez",
            value="💬 : Kişinin lez yüzdesini ölçer.",
            inline=False
            )
            embed.add_field(
            name="🛠 : .myt",
            value="💬 : Youtube'dan şarkı indirip göndermenizi sağlar.",
            inline=False
            )
            embed.add_field(
            name="🛠 : .rulet",
            value="💬 : Rulet oynar. Bilgi için .rlth yazınız.",
            inline=False
            )
            embed.add_field(
            name="🛠 : .kayitol",
            value="💬 : Rulet oynamak için kayıt olur.",
            inline=False
            )
            embed.add_field(
            name="🛠 : .money",
            value="💬 : Kaç coininiz olduğunu size söyler.",
            inline=False
            )
            embed.add_field(
            name="🛠 : .daily",
            value="💬 : 12 Saatte bir alabileceğiniz 200 coinlik bonus'tur",
            inline=False
            )
            """embed.add_field(
            name="🛠 : ",
            value="💬 : ",
            inline=False
            )"""
            await ctx.send(embed=embed)
    @commands.command(name="rlth")
    async def rlth(self, ctx):
        if WORKTYPE=="private":
            embed = discord.Embed(
                title="●▬▬▬ *DiscAsena Private* ▬▬▬●",
            )

            embed.add_field(
                name="🛠 : .rulet",
                value="💬 : Rulet oynamak için kullanılır\nRulet oyunu bilgileri:\n**🛠 : .kayitol**\n💬 : yazdığınızda eğer kayıtlı değil iseniz kayıt olursunuz.\n**🛠 : .rulet**\n💬 :  Ve Ardından bahis miktarınız ardından bahis yapmak istediğiniz kümeler.\n**Bahis Kümeleri**\n1 Den 36 ya kadar olan sayılar. Eğer tahmininiz tutarsa bahsinizin 36 katını alırsınız.\nkırmızı/siyah top kırmızı/siyah üzerine gelirse bahsinizin 2 katını alırsınız.\n1st12, 2st12, 3st12 Bunlar baştan, ortadan ve sondan 12 sayıya bahis yapmanızı sağlar. Bahsiniz tutar ise bahsinizin 3 katını alırsınız.\n1to19,19to36 Bunlar ise Rulet sayılarının 1. yarısı ve 2. yarısına bahis yapmanızı sağlar. Eğer bahsiniz tutarsa bahsinizin 2 katını alırsınız.",
                inline=False
            )
            await ctx.send(embed=embed)
        elif WORKTYPE=="public":
            embed = discord.Embed(
                title="●▬▬▬ *DiscAsena Private* ▬▬▬●",
            )

            embed.add_field(
                name="🛠 : .rulet",
                value="💬 : Rulet oynamak için kullanılır\nRulet oyunu bilgileri:\n**🛠 : .kayitol**\n💬 : yazdığınızda eğer kayıtlı değil iseniz kayıt olursunuz.\n**🛠 : .rulet**\n💬 :  Ve Ardından bahis miktarınız ardından bahis yapmak istediğiniz kümeler.\n**Bahis Kümeleri**\n1 Den 36 ya kadar olan sayılar. Eğer tahmininiz tutarsa bahsinizin 36 katını alırsınız.\nkırmızı/siyah top kırmızı/siyah üzerine gelirse bahsinizin 2 katını alırsınız.\n1st12, 2st12, 3st12 Bunlar baştan, ortadan ve sondan 12 sayıya bahis yapmanızı sağlar. Bahsiniz tutar ise bahsinizin 3 katını alırsınız.\n1to19,19to36 Bunlar ise Rulet sayılarının 1. yarısı ve 2. yarısına bahis yapmanızı sağlar. Eğer bahsiniz tutarsa bahsinizin 2 katını alırsınız.",
                inline=False
            )
            await ctx.send(embed=embed)
async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
