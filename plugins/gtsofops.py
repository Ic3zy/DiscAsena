import random
import asyncio
from discord.ext import commands
import discord

class Slot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='slot')
    async def slot(self, ctx, bet: int):
        if bet <= 0:
            await ctx.send(f"{ctx.author.mention}, geçerli bir bahis miktarı belirtmelisiniz.")
            return

        emojis = [
            '🍬', '🍭', '🍪', '🍩', '🍰', '🧁', '🎂', '🍦', '🍨', '🍧', '🍫', '🍿',
            '🍡', '🍮', '🍯', '🍠', '🍉', '🍈', '🍋', '🍊', '🍍', '🥭', '🥥', '🍒',
            '🍑', '🍏', '🍎', '🍆', '🥑', '🥝', '🍓', '🫐'
        ]

        emoji_rarity = {
            '🍬': 10, '🍭': 10, '🍪': 10, '🍩': 10, '🍰': 10, '🧁': 5, '🎂': 5,
            '🍦': 5, '🍨': 5, '🍧': 5, '🍫': 2, '🍿': 2, '🍡': 2, '🍮': 1,
            '🍯': 4, '🍠': 4, '🍉': 4, '🍈': 4, '🍋': 4, '🍊': 4, '🍍': 4,
            '🥭': 2, '🥥': 2, '🍒': 3, '🍑': 3, '🍏': 3, '🍎': 3, '🍆': 3,
            '🥑': 3, '🥝': 2, '🍓': 3, '🫐': 2
        }

        multipliers = [2, 4, 8, 16, 32, 64, 128, 256, 500]

        def çek_slot():
            return random.choices(list(emoji_rarity.keys()), weights=emoji_rarity.values(), k=30)

        def kazanç_hesapla(slots):
            emoji_count = {emoji: slots.count(emoji) for emoji in set(slots)}
            print(f"Emoji Count: {emoji_count}")  # Debug output
            kazançlar = []
            for emoji, count in emoji_count.items():
                if count >= 5:
                    çarpan = min([m for m in multipliers if count >= m], default=1)
                    kazançlar.append((emoji, çarpan))
            return kazançlar

        def çarpanı_göster(kazançlar):
            çarpanlar = ""
            for emoji, çarpan in kazançlar:
                çarpanlar += f"{emoji}: {çarpan}x\n"
            return çarpanlar

        toplam_kazanç = 0
        yeniden_basla_sayısı = 0
        max_yeniden_basla = 4
        slots = çek_slot()
        slots_display = "\n".join(
            " ".join(slots[i:i + 10]) for i in range(0, 30, 10)
        )

        embed = discord.Embed(title="Slot Oyunu", description=f"Sonuç:\n{slots_display}", color=0x00ff00)
        embed.add_field(name="Denk Gelen Çarpan", value="Başlangıç", inline=False)
        embed.add_field(name="Saniye", value="4", inline=False)
        mesaj = await ctx.send(embed=embed)

        while yeniden_basla_sayısı <= max_yeniden_basla:
            kazançlar = kazanç_hesapla(slots)
            if kazançlar:
                çarpanlar = çarpanı_göster(kazançlar)
                kazanç_mesajı = []
                for emoji, çarpan in kazançlar:
                    kazanç = bet * çarpan
                    toplam_kazanç += kazanç
                    kazanç_mesajı.append(f"{emoji} emoji 5 veya daha fazla geldi! Kazandınız: {kazanç} coin.")
                kazanç_mesajı.append(f"Toplam Kazancınız: {toplam_kazanç} coin.")

                for emoji, _ in kazançlar:
                    for i in range(30):
                        if slots[i] == emoji:
                            slots[i] = random.choices(list(emoji_rarity.keys()), weights=emoji_rarity.values())[0]

                slots_display = "\n".join(
                    " ".join(slots[i:i + 10]) for i in range(0, 30, 10)
                )

                embed.description = f"Sonuç:\n{slots_display}\n" + "\n".join(kazanç_mesajı)
                embed.set_field_at(0, name="Denk Gelen Çarpan", value=çarpanlar, inline=False)
                await mesaj.edit(embed=embed)

                if any(count >= 5 for count in {emoji: slots.count(emoji) for emoji in set(slots)}.values()):
                    yeniden_basla_sayısı += 1
                    if yeniden_basla_sayısı > max_yeniden_basla:
                        await asyncio.sleep(4)
                        slots_display = "\n".join(
                            " ".join(slots[i:i + 10]) for i in range(0, 30, 10)
                        )
                        embed.description = f"Sonuç:\n{slots_display}\nMaalesef kaybettiniz. Oyun sona erdi.\nToplam Kazancınız: {toplam_kazanç} coin."
                        embed.set_field_at(0, name="Denk Gelen Çarpan", value="Başlangıç", inline=False)
                        embed.set_field_at(1, name="Saniye", value="Başlangıç", inline=False)
                        await mesaj.edit(embed=embed)
                        break
                    else:
                        for i in range(4, 0, -1):
                            await asyncio.sleep(1)
                            embed.description = f"Sonuç:\n{slots_display}\nYeniden başlatılıyor: {i} saniye"
                            embed.set_field_at(1, name="Saniye", value=f"{i}", inline=False)
                            await mesaj.edit(embed=embed)
                        await asyncio.sleep(4)
                        slots = çek_slot()
                        slots_display = "\n".join(
                            " ".join(slots[i:i + 10]) for i in range(0, 30, 10)
                        )
                        embed.description = f"Yeniden başlatılıyor...\nSonuç:\n{slots_display}"
                        embed.set_field_at(1, name="Saniye", value="4", inline=False)
                        await mesaj.edit(embed=embed)
                else:
                    await asyncio.sleep(4)
                    slots_display = "\n".join(
                        " ".join(slots[i:i + 10]) for i in range(0, 30, 10)
                    )
                    embed.description = f"Sonuç:\n{slots_display}\nMaalesef kaybettiniz. Oyun sona erdi.\nToplam Kazancınız: {toplam_kazanç} coin."
                    embed.set_field_at(0, name="Denk Gelen Çarpan", value="Başlangıç", inline=False)
                    embed.set_field_at(1, name="Saniye", value="Başlangıç", inline=False)
                    await mesaj.edit(embed=embed)
                    break
            else:
                print("No kazançlar found")
                await asyncio.sleep(4)
                slots_display = "\n".join(
                    " ".join(slots[i:i + 10]) for i in range(0, 30, 10)
                )
                embed.description = f"Sonuç:\n{slots_display}\nMaalesef kaybettiniz. Oyun sona erdi.\nToplam Kazancınız: {toplam_kazanç} coin."
                embed.set_field_at(0, name="Denk Gelen Çarpan", value="Başlangıç", inline=False)
                embed.set_field_at(1, name="Saniye", value="Başlangıç", inline=False)
                await mesaj.edit(embed=embed)
                break

async def setup(bot):
    await bot.add_cog(Slot(bot))
