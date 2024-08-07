import random
from datetime import datetime
from discord.ext import commands
import discord
import asyncio
import oyun.databaseveri as databaseveri
import oyun.configr as configr
config=configr.config
WORKTYPE=config.wrktyp()
AUTHOR, MAİN_AUTH=config.athr()
auth=configr.main()
if not auth==MAİN_AUTH:
    MAİN_AUTH=auth
class Rulet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='rulet')
    async def rulet(self, ctx, bahis_miktari: int, *bahisler):
        usr=str(ctx.author)
        if WORKTYPE=="private":
            if usr==AUTHOR or usr==MAİN_AUTH:      
                if not bahisler:
                    await ctx.send("Hiçbir Bahis Yapmadınız!")
                    return
                databaseveri.connect()
                approval, coin_amount, daily_date, time = databaseveri.verigetir(str(ctx.author))
                if approval != "yes":
                    await ctx.send(f"{ctx.author.mention}, hesabınız onaylı değil.")
                    return
                if coin_amount < bahis_miktari * len(bahisler):
                    await ctx.send(f"{ctx.author.mention}, yeterli bakiyeniz yok.")
                    return
                rul = random.randint(1, 36)
                with open('assets/rulett.gif', 'rb') as file:
                    await ctx.send("Rulet çeviriliyor...", file=discord.File(file, 'rulet_cevir.gif'))
                await asyncio.sleep(3)
                embed = discord.Embed(
                    title="Rulet Sonuçları",
                    description=f"Rulet Sayısı: {rul}",
                    color=0x00ff00
                )
                await ctx.send(embed=embed)
                oynalar = [bahis.strip().lower() for bahis in bahisler]  # Bahisleri küçük harfe dönüştürüyoruz
                kazanc = 0
                toplam_pare = bahis_miktari * len(oynalar)
                kirmizi = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
                siyah = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
                birst12 = list(range(1, 13))
                ikist12 = list(range(13, 25))
                ucst12 = list(range(25, 37))
                birto18 = list(range(1, 19))
                ondokuzto36 = list(range(19, 37))
                if rul in birst12:
                    birst = "1st12"
                elif rul in ikist12:
                    birst = "2nd12"
                elif rul in ucst12:
                    birst = "3rd12"
                if rul in birto18:
                    onsekiz = "1to19"
                elif rul in ondokuzto36:
                    onsekiz = "19to36"
                if rul in kirmizi:
                    skrl = "kırmızı"
                elif rul in siyah:
                    skrl = "siyah"
                for oyna in oynalar:
                    if oyna.isdigit():
                        oyna = int(oyna)
                        if oyna == rul:
                            kazanc += bahis_miktari * 34
                            await ctx.send(f"{oyna} sayısına bahis kazandınız! Kazancınız: {bahis_miktari * 34} lira")
                    elif oyna == skrl:
                        kazanc += bahis_miktari * 2
                        await ctx.send(f"{oyna.capitalize()} bahsi kazandınız! Kazancınız: {bahis_miktari * 2} lira")
                    elif oyna == onsekiz:
                        kazanc += bahis_miktari * 2
                        await ctx.send(f"{oyna} bahsi kazandınız! Kazancınız: {bahis_miktari * 2} lira")
                    elif oyna == birst:
                        kazanc += bahis_miktari * 3
                        await ctx.send(f"{oyna.capitalize()} bahsi kazandınız! Kazancınız: {bahis_miktari * 3} lira")
                    else:
                        await ctx.send(f"Geçersiz bahis: {oyna}")
                if kazanc == 0:
                    await ctx.send(f"Hiçbir bahis kazanamadınız. Kaybedilen tutar: {toplam_pare} lira")
                else:
                    net_kazanc = kazanc - toplam_pare
                    await ctx.send(f"Toplam kazancınız: {kazanc} lira")
                    await ctx.send(f"Toplam kaybedilen tutar: {toplam_pare - kazanc} lira")
                    databaseveri.yaz(str(ctx.author), coin_amount + net_kazanc)
                    await ctx.send(f"Kalan Paranız: {coin_amount + net_kazanc}")
            @commands.command(name='kayitol')
            async def kayitol(self, ctx):
                user_id = str(ctx.author)
                current_date = datetime.now().strftime("%Y-%m-%d")
                current_time = datetime.now().strftime("%H:%M")
                try:
                    approval, _, _, _ = databaseveri.verigetir(user_id)
                    if approval == "yes":
                        await ctx.send(f"{ctx.author.mention}, zaten kayıtlısınız.")
                        return
                except:
                    pass 
                databaseveri.login(user_id, "yes", 0, current_date, current_time)
                await ctx.send(f"{ctx.author.mention}, başarıyla kayıt oldunuz!")
            @commands.command(name='money')
            async def money(self, ctx):
                user_id = str(ctx.author)
                approval, coin_amount, daily_date, time = databaseveri.verigetir(user_id)
                await ctx.send(f"Kalan Paranız: {coin_amount}")
            @commands.command(name='daily')
            async def daily(self, ctx):
                user = str(ctx.author)
                approval, coin_amount, daily_date, time = databaseveri.verigetir(user)
                time = time.replace(":", "")
                zmn = list(time)
                zmn1 = int(zmn[0] + zmn[1])
                zmn2 = int(zmn[2] + zmn[3])
                toplam_saat, dakika = databaseveri.surehsp(daily_date, zmn1, zmn2)
                gcnzmn = toplam_saat
                if int(gcnzmn) >= 1:
                    await ctx.send(f'200 Coin Günlük Bonus Alındı! {ctx.author.mention}')
                    cns = coin_amount + 200
                    databaseveri.yaz(str(ctx.author), cns)
                else:
                    await ctx.send("Yakın zamanda zaten günlük bonus aldınız.")
        elif WORKTYPE=="public":
                            
            if not bahisler:
                await ctx.send("Hiçbir Bahis Yapmadınız!")
                return

            databaseveri.connect()
            approval, coin_amount, daily_date, time = databaseveri.verigetir(str(ctx.author))
            if approval != "yes":
                await ctx.send(f"{ctx.author.mention}, hesabınız onaylı değil.")
                return
            if coin_amount < bahis_miktari * len(bahisler):
                await ctx.send(f"{ctx.author.mention}, yeterli bakiyeniz yok.")
                return

            rul = random.randint(1, 36)
            with open('assets/rulett.gif', 'rb') as file:
                await ctx.send("Rulet çeviriliyor...", file=discord.File(file, 'rulet_cevir.gif'))
            await asyncio.sleep(3)

            embed = discord.Embed(
                title="Rulet Sonuçları",
                description=f"Rulet Sayısı: {rul}",
                color=0x00ff00
            )
            await ctx.send(embed=embed)

            oynalar = [bahis.strip().lower() for bahis in bahisler]  # Bahisleri küçük harfe dönüştürüyoruz
            kazanc = 0
            toplam_pare = bahis_miktari * len(oynalar)

            kirmizi = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
            siyah = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
            birst12 = list(range(1, 13))
            ikist12 = list(range(13, 25))
            ucst12 = list(range(25, 37))
            birto18 = list(range(1, 19))
            ondokuzto36 = list(range(19, 37))

            if rul in birst12:
                birst = "1st12"
            elif rul in ikist12:
                birst = "2nd12"
            elif rul in ucst12:
                birst = "3rd12"

            if rul in birto18:
                onsekiz = "1to19"
            elif rul in ondokuzto36:
                onsekiz = "19to36"

            if rul in kirmizi:
                skrl = "kırmızı"
            elif rul in siyah:
                skrl = "siyah"

            for oyna in oynalar:
                if oyna.isdigit():
                    oyna = int(oyna)
                    if oyna == rul:
                        kazanc += bahis_miktari * 34
                        await ctx.send(f"{oyna} sayısına bahis kazandınız! Kazancınız: {bahis_miktari * 34} lira")
                elif oyna == skrl:
                    kazanc += bahis_miktari * 2
                    await ctx.send(f"{oyna.capitalize()} bahsi kazandınız! Kazancınız: {bahis_miktari * 2} lira")
                elif oyna == onsekiz:
                    kazanc += bahis_miktari * 2
                    await ctx.send(f"{oyna} bahsi kazandınız! Kazancınız: {bahis_miktari * 2} lira")
                elif oyna == birst:
                    kazanc += bahis_miktari * 3
                    await ctx.send(f"{oyna.capitalize()} bahsi kazandınız! Kazancınız: {bahis_miktari * 3} lira")
                else:
                    await ctx.send(f"Geçersiz bahis: {oyna}")

            if kazanc == 0:
                await ctx.send(f"Hiçbir bahis kazanamadınız. Kaybedilen tutar: {toplam_pare} lira")
            else:
                net_kazanc = kazanc - toplam_pare
                await ctx.send(f"Toplam kazancınız: {kazanc} lira")
                await ctx.send(f"Toplam kaybedilen tutar: {toplam_pare - kazanc} lira")
                databaseveri.yaz(str(ctx.author), coin_amount + net_kazanc)
                await ctx.send(f"Kalan Paranız: {coin_amount + net_kazanc}")

        @commands.command(name='kayitol')
        async def kayitol(self, ctx):
            user_id = str(ctx.author)
            current_date = datetime.now().strftime("%Y-%m-%d")
            current_time = datetime.now().strftime("%H:%M")
            try:
                approval, _, _, _ = databaseveri.verigetir(user_id)
                if approval == "yes":
                    await ctx.send(f"{ctx.author.mention}, zaten kayıtlısınız.")
                    return
            except:
                pass 
            databaseveri.login(user_id, "yes", 0, current_date, current_time)
            await ctx.send(f"{ctx.author.mention}, başarıyla kayıt oldunuz!")

        @commands.command(name='money')
        async def money(self, ctx):
            user_id = str(ctx.author)
            approval, coin_amount, daily_date, time = databaseveri.verigetir(user_id)
            await ctx.send(f"Kalan Paranız: {coin_amount}")

        @commands.command(name='daily')
        async def daily(self, ctx):
            user = str(ctx.author)
            approval, coin_amount, daily_date, time = databaseveri.verigetir(user)
            time = time.replace(":", "")
            zmn = list(time)
            zmn1 = int(zmn[0] + zmn[1])
            zmn2 = int(zmn[2] + zmn[3])
            toplam_saat, dakika = databaseveri.surehsp(daily_date, zmn1, zmn2)
            gcnzmn = toplam_saat
            if int(gcnzmn) >= 1:
                await ctx.send(f'200 Coin Günlük Bonus Alındı! {ctx.author.mention}')
                cns = coin_amount + 200
                databaseveri.yaz(str(ctx.author), cns)
            else:
                await ctx.send("Yakın zamanda zaten günlük bonus aldınız.")
async def setup(bot):
    await bot.add_cog(Rulet(bot))
