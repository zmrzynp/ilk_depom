
import discord
from discord.ext import commands
import random

print("Hello world")
z = "Zeynep"


intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriği okuma izni

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot {bot.user} olarak giriş yaptı!')

@bot.command()
async def Nasılsın(ctx):
    await ctx.send('İyidir sen?')


@bot.command()
async def En_sevdiğin_renk_ne(ctx):
    colors = ['kırmızı', 'turuncu', 'sarı', 'yeşil', 'mavi', 'lacivert', 'mor','pembe','mürdüm','siyah']
    chosen_color = random.choice(colors)
    await ctx.send(f'En sevdiğim renk {chosen_color}!')


bot.run('YOUR_BOT_TOKEN')
