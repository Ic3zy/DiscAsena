import discord
from discord.ext import commands
import yt_dlp
import os
import oyun.configr as configr
config=configr.config
WORKTYPE=config.wrktyp()
AUTHOR, MAİN_AUTH=config.athr()
auth=configr.main()
if not auth==MAİN_AUTH:
    MAİN_AUTH=auth
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='myt')
    async def myt(self, ctx, *, song_name):
        usr=str(ctx.author)
        if WORKTYPE=="private":
            if usr==AUTHOR or usr==MAİN_AUTH:      
                await ctx.send('Şarkıyı indiriyorum, lütfen bekleyin...')
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'outtmpl': 'downloads/%(title)s.%(ext)s',
                    'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe', 
                    'noplaylist': True,
                }
                if not os.path.exists('downloads'):
                    os.makedirs('downloads')
                try:
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(f"ytsearch:{song_name}", download=True)
                        if 'entries' in info and info['entries']:
                            filename = ydl.prepare_filename(info['entries'][0])
                            filename_mp3 = filename.replace('.webm', '.mp3').replace('.m4a', '.mp3')
                            if os.path.exists(filename_mp3):
                                await ctx.send(file=discord.File(filename_mp3))
                            else:
                                await ctx.send('Şarkı dosyası bulunamadı.')
                        else:
                            await ctx.send('Şarkı bulunamadı.')
                except Exception as e:
                    await ctx.send(f'Bir hata oluştu: {str(e)}')
        elif WORKTYPE=="public":                    
            await ctx.send('Şarkıyı indiriyorum, lütfen bekleyin...')
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': 'downloads/%(title)s.%(ext)s',
                'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe', 
                'noplaylist': True,
            }
            if not os.path.exists('downloads'):
                os.makedirs('downloads')
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(f"ytsearch:{song_name}", download=True)
                    if 'entries' in info and info['entries']:
                        filename = ydl.prepare_filename(info['entries'][0])
                        filename_mp3 = filename.replace('.webm', '.mp3').replace('.m4a', '.mp3')
                        if os.path.exists(filename_mp3):
                            await ctx.send(file=discord.File(filename_mp3))
                        else:
                            await ctx.send('Şarkı dosyası bulunamadı.')
                    else:
                        await ctx.send('Şarkı bulunamadı.')
            except Exception as e:
                await ctx.send(f'Bir hata oluştu: {str(e)}')
async def setup(bot):
    await bot.add_cog(Music(bot))
