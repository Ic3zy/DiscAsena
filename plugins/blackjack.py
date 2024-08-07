import random
from datetime import datetime
from discord.ext import commands
import discord
import asyncio
import oyun.databaseveri as databaseveri
import oyun.configr as configr
config=configr.config
AUTHOR, MAİN_AUTH=config.athr()
WORKTYPE=config.wrktyp()
auth=configr.main()
if not auth==MAİN_AUTH:
    MAİN_AUTH=auth
class Blackjack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    def hesapla_eldeki_kartlar(self, kartlar):
        toplam = sum(kartlar)
        as_sayisi = kartlar.count(1)
        while toplam <= 11 and as_sayisi > 0:
            toplam += 10
            as_sayisi -= 1
        return toplam
    @commands.command(name='bj')
    async def blackjack(self, ctx, bahis_miktari: int):
        if WORKTYPE=="private":
            user=str(ctx.author)
            if user==AUTHOR or user==MAİN_AUTH:
            
                qkart = random.randint(1, 10)
                qkart2 = random.randint(1, 10)
                asvarmi = False
                sigorta_miktari = 0
                if qkart == 1:
                    asvarmi = True
                krupye_kartlar = [qkart, qkart2]
                kartlar = random.randint(1, 10)
                kartlar2 = random.randint(1, 10)
                oyuncu_kartlar = [kartlar, kartlar2]
                qkrt = self.hesapla_eldeki_kartlar(krupye_kartlar)
                krt = self.hesapla_eldeki_kartlar(oyuncu_kartlar)
                kbj = krt == 21
                qbj = qkrt == 21
                if asvarmi:
                    await ctx.send("Krupiyede As var. Sigorta almak ister misiniz? (evet/hayır): ")
                    def check(m):
                        return m.author == ctx.author and m.channel == ctx.channel
                    try:
                        msg = await self.bot.wait_for('message', timeout=30.0, check=check)
                        if msg.content.lower() == "evet":
                            sigorta_miktari = bahis_miktari / 2
                            await ctx.send(f"Sigorta bahsi olarak {sigorta_miktari} coin kesildi.")
                            approval, coin_amount, daily_date, time = databaseveri.verigetir(str(ctx.author))
                            yeni_coin = coin_amount - sigorta_miktari
                            databaseveri.yaz(str(ctx.author), yeni_coin)
                            await ctx.send(f"Yeni bakiyeniz: {yeni_coin}")
                    except asyncio.TimeoutError:
                        await ctx.send('Zaman aşımına uğradı. Sigorta alma işlemi iptal edildi.')
                if qbj:
                    result = "kasa"
                    kznn = "Kasa Black Jack!"
                    await ctx.send(kznn)
                    approval, coin_amount, daily_date, time = databaseveri.verigetir(str(ctx.author))
                    if approval == "yes":
                        yeni_coin = coin_amount - bahis_miktari + (sigorta_miktari * 2)
                        databaseveri.yaz(str(ctx.author), yeni_coin)
                        await ctx.send(f"Kasa blackjack yaptı. Yeni bakiyeniz: {yeni_coin}")
                    return
                if kbj:
                    result = "oyuncu"
                    kznn = "Kullanıcı Black Jack!"
                elif qbj:
                    result = "kasa"
                    kznn = "Kasa Black Jack!"
                    await ctx.send(kznn)
                    return
                await ctx.send(f"Krupye eli : [{qkart}, *]\nSenin elin : {oyuncu_kartlar} ({krt})")
                ek = await ctx.send("Kart eklemek ister misin? (evet/hayır): ")
                def check(m):
                    return m.author == ctx.author and m.channel == ctx.channel
                try:
                    msg = await self.bot.wait_for('message', timeout=30.0, check=check)
                    ek = msg.content.lower()
                except asyncio.TimeoutError:
                    await ctx.send('Zaman aşımına uğradı. Kart ekleme işlemi iptal edildi.')
                    return
                while ek == "evet":
                    ekkrt = random.randint(1, 10)
                    oyuncu_kartlar.append(ekkrt)
                    krt = self.hesapla_eldeki_kartlar(oyuncu_kartlar)
                    await ctx.send(f"Krupye eli : [{qkart}, *]\nSenin elin : {oyuncu_kartlar} ({krt})")
                    if krt > 21:
                        result = "kasa"
                        kznn = "Kasa kazandı"
                        break
                    await ctx.send("Kart eklemek ister misin? (evet/hayır): ")
                    try:
                        msg = await self.bot.wait_for('message', timeout=30.0, check=check)
                        ek = msg.content.lower()
                    except asyncio.TimeoutError:
                        await ctx.send('Zaman aşımına uğradı. Kart ekleme işlemi iptal edildi.')
                        return
                while qkrt < 17:
                    qek = random.randint(1, 10)
                    krupye_kartlar.append(qek)
                    qkrt = self.hesapla_eldeki_kartlar(krupye_kartlar)
                    await ctx.send(f"Kasa kart çekti: {krupye_kartlar} ({qkrt})")
                if krt <= 21:
                    if qkrt <= 21:
                        if qkrt == krt:
                            result = "beraberlik"
                            kznn = "Berabere"
                        elif qkrt < krt:
                            result = "oyuncu"
                            kznn = "Kullanıcı kazandı"
                        else:
                            result = "kasa"
                            kznn = "Kasa kazandı"
                    else:
                        result = "oyuncu"
                        kznn = "Kullanıcı kazandı"
                else:
                    result = "kasa"
                    kznn = "Kasa kazandı"
                await ctx.send(f"Krupye eli : {qkart}, {qkrt}\nSenin elin : {oyuncu_kartlar} ({krt})")
                await ctx.send(kznn)
                approval, coin_amount, daily_date, time = databaseveri.verigetir(str(ctx.author))
                if approval == "yes":
                    if result == "oyuncu":
                        yeni_coin = coin_amount + bahis_miktari * 2
                        databaseveri.yaz(str(ctx.author), yeni_coin)
                        await ctx.send(f"Yeni bakiyeniz: {yeni_coin}")
                    elif result == "kasa":
                        yeni_coin = coin_amount - bahis_miktari
                        databaseveri.yaz(str(ctx.author), yeni_coin)
                        await ctx.send(f"Yeni bakiyeniz: {yeni_coin}")
        elif WORKTYPE=="public": 
            qkart = random.randint(1, 10)
            qkart2 = random.randint(1, 10)
            asvarmi = False
            sigorta_miktari = 0
            if qkart == 1:
                asvarmi = True
            krupye_kartlar = [qkart, qkart2]
            kartlar = random.randint(1, 10)
            kartlar2 = random.randint(1, 10)
            oyuncu_kartlar = [kartlar, kartlar2]
            qkrt = self.hesapla_eldeki_kartlar(krupye_kartlar)
            krt = self.hesapla_eldeki_kartlar(oyuncu_kartlar)
            kbj = krt == 21
            qbj = qkrt == 21
            if asvarmi:
                await ctx.send("Krupiyede As var. Sigorta almak ister misiniz? (evet/hayır): ")
                def check(m):
                    return m.author == ctx.author and m.channel == ctx.channel
                try:
                    msg = await self.bot.wait_for('message', timeout=30.0, check=check)
                    if msg.content.lower() == "evet":
                        sigorta_miktari = bahis_miktari / 2
                        await ctx.send(f"Sigorta bahsi olarak {sigorta_miktari} coin kesildi.")
                        approval, coin_amount, daily_date, time = databaseveri.verigetir(str(ctx.author))
                        yeni_coin = coin_amount - sigorta_miktari
                        databaseveri.yaz(str(ctx.author), yeni_coin)
                        await ctx.send(f"Yeni bakiyeniz: {yeni_coin}")
                except asyncio.TimeoutError:
                    await ctx.send('Zaman aşımına uğradı. Sigorta alma işlemi iptal edildi.')
            if qbj:
                result = "kasa"
                kznn = "Kasa Black Jack!"
                await ctx.send(kznn)
                approval, coin_amount, daily_date, time = databaseveri.verigetir(str(ctx.author))
                if approval == "yes":
                    yeni_coin = coin_amount - bahis_miktari + (sigorta_miktari * 2)
                    databaseveri.yaz(str(ctx.author), yeni_coin)
                    await ctx.send(f"Kasa blackjack yaptı. Yeni bakiyeniz: {yeni_coin}")
                return
            if kbj:
                result = "oyuncu"
                kznn = "Kullanıcı Black Jack!"
            elif qbj:
                result = "kasa"
                kznn = "Kasa Black Jack!"
                await ctx.send(kznn)
                return
            await ctx.send(f"Krupye eli : [{qkart}, *]\nSenin elin : {oyuncu_kartlar} ({krt})")
            ek = await ctx.send("Kart eklemek ister misin? (evet/hayır): ")
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel
            try:
                msg = await self.bot.wait_for('message', timeout=30.0, check=check)
                ek = msg.content.lower()
            except asyncio.TimeoutError:
                await ctx.send('Zaman aşımına uğradı. Kart ekleme işlemi iptal edildi.')
                return
            while ek == "evet":
                ekkrt = random.randint(1, 10)
                oyuncu_kartlar.append(ekkrt)
                krt = self.hesapla_eldeki_kartlar(oyuncu_kartlar)
                await ctx.send(f"Krupye eli : [{qkart}, *]\nSenin elin : {oyuncu_kartlar} ({krt})")
                if krt > 21:
                    result = "kasa"
                    kznn = "Kasa kazandı"
                    break
                await ctx.send("Kart eklemek ister misin? (evet/hayır): ")
                try:
                    msg = await self.bot.wait_for('message', timeout=30.0, check=check)
                    ek = msg.content.lower()
                except asyncio.TimeoutError:
                    await ctx.send('Zaman aşımına uğradı. Kart ekleme işlemi iptal edildi.')
                    return
            while qkrt < 17:
                qek = random.randint(1, 10)
                krupye_kartlar.append(qek)
                qkrt = self.hesapla_eldeki_kartlar(krupye_kartlar)
                await ctx.send(f"Kasa kart çekti: {krupye_kartlar} ({qkrt})")
            if krt <= 21:
                if qkrt <= 21:
                    if qkrt == krt:
                        result = "beraberlik"
                        kznn = "Berabere"
                    elif qkrt < krt:
                        result = "oyuncu"
                        kznn = "Kullanıcı kazandı"
                    else:
                        result = "kasa"
                        kznn = "Kasa kazandı"
                else:
                    result = "oyuncu"
                    kznn = "Kullanıcı kazandı"
            else:
                result = "kasa"
                kznn = "Kasa kazandı"
            await ctx.send(f"Krupye eli : {qkart}, {qkrt}\nSenin elin : {oyuncu_kartlar} ({krt})")
            await ctx.send(kznn)
            approval, coin_amount, daily_date, time = databaseveri.verigetir(str(ctx.author))
            if approval == "yes":
                if result == "oyuncu":
                    yeni_coin = coin_amount + bahis_miktari * 2
                    databaseveri.yaz(str(ctx.author), yeni_coin)
                    await ctx.send(f"Yeni bakiyeniz: {yeni_coin}")
                elif result == "kasa":
                    yeni_coin = coin_amount - bahis_miktari
                    databaseveri.yaz(str(ctx.author), yeni_coin)
                    await ctx.send(f"Yeni bakiyeniz: {yeni_coin}")
async def setup(bot):
    await bot.add_cog(Blackjack(bot))
