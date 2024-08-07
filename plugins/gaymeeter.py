from discord.ext import commands
import random
import time
import oyun.configr as configr
config=configr.config
WORKTYPE=config.wrktyp()
AUTHOR, MAİN_AUTH=config.athr()
auth=configr.main()
if not auth==MAİN_AUTH:
    MAİN_AUTH=auth
class GayMeet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def gay(self, ctx, member: commands.MemberConverter = None):
        if WORKTYPE=="private":
            usr=str(ctx.author)
            if usr==AUTHOR or usr==MAİN_AUTH:         
                sor=random.randint(1, 100)
                """if member:
                        await ctx.send(f'{user.mention} Kişinin gay yüzdesi hesaplanıyor...')
                        await ctx.send(f'{user.mention} Hesaplandı:{sor}')
                else:
                    if ctx.message.reference:
                        replied_message = await ctx.fetch_message(ctx.message.reference.message_id)
                        user = replied_message.author
                        await ctx.send(f'{user.mention} Kişinin gay yüzdesi hesaplanıyor...')
                        await ctx.send(f'{user.mention} Hesaplandı:{sor}')
                    else:
                        await ctx.send(f'{user.mention} Kişinin gay yüzdesi hesaplanıyor...')
                        await ctx.send(f'{user.mention} Hesaplandı:{sor}')"""
                if member:
                    await ctx.send(f'{member.mention} Kişinin gay yüzdesi hesaplanıyor...')
                    time.sleep(1)
                    await ctx.send(f'%{sor}')
                else:
                    if ctx.message.reference:
                        replied_message = await ctx.fetch_message(ctx.message.reference.message_id)
                        user = replied_message.author
                        await ctx.send(f'{user.mention} Kişinin gay yüzdesi hesaplanıyor...')
                        time.sleep(1)
                        await ctx.send(f'%{sor}')
                    else:
                        await ctx.send(f'{ctx.author.mention} Kişinin gay yüzdesi hesaplanıyor...')
                        time.sleep(1)
                        await ctx.send(f'%{sor}')
        elif WORKTYPE=="public":                        
            sor=random.randint(1, 100)
            """if member:
                    await ctx.send(f'{user.mention} Kişinin gay yüzdesi hesaplanıyor...')
                    await ctx.send(f'{user.mention} Hesaplandı:{sor}')
            else:
                if ctx.message.reference:
                    replied_message = await ctx.fetch_message(ctx.message.reference.message_id)
                    user = replied_message.author
                    await ctx.send(f'{user.mention} Kişinin gay yüzdesi hesaplanıyor...')
                    await ctx.send(f'{user.mention} Hesaplandı:{sor}')
                else:
                    await ctx.send(f'{user.mention} Kişinin gay yüzdesi hesaplanıyor...')
                    await ctx.send(f'{user.mention} Hesaplandı:{sor}')"""
            if member:
                await ctx.send(f'{member.mention} Kişinin gay yüzdesi hesaplanıyor...')
                time.sleep(1)
                await ctx.send(f'%{sor}')
            else:
                if ctx.message.reference:
                    replied_message = await ctx.fetch_message(ctx.message.reference.message_id)
                    user = replied_message.author
                    await ctx.send(f'{user.mention} Kişinin gay yüzdesi hesaplanıyor...')
                    time.sleep(1)
                    await ctx.send(f'%{sor}')
                else:
                    await ctx.send(f'{ctx.author.mention} Kişinin gay yüzdesi hesaplanıyor...')
                    time.sleep(1)
                    await ctx.send(f'%{sor}')
async def setup(bot):
    await bot.add_cog(GayMeet(bot))
