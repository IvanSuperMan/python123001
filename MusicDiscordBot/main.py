import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

# инициализация бота
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

@bot.event
async def on_ready():
    print(f'{bot.user.name} подключен к Discord!')

@bot.command(name='play', help='Проигрывает музыку из YouTube по запросу')
async def play(ctx, *, url=None):
    if not ctx.message.author.voice:
        await ctx.send("Вы не находитесь в голосовом канале")
        return

    else:
        channel = ctx.message.author.voice.channel
    try:
        await channel.connect()
    except:
        pass
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        ctx.voice_client.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: print('Ошибка воспроизведения:', e))

    await ctx.send(f'Сейчас играет: {info["title"]}')


@bot.command(name='leave', help='Выходит из голосового канала')
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Бот покинул канал")
    else:
        await ctx.send("Бот не находится в голосовом канале")

# токен вашего бота
bot.run('')