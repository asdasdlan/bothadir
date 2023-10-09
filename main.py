import os
import discord
from discord.ext import commands


from fonksiyonlar import *



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='_', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)




@bot.command()
async def rastgeleresim(ctx):
    resimler = os.listdir("m1l3\m1l4\images")
    resim = random.choice(resimler)

    # Dosya adını bir değişkenden bu şekilde değiştirebilirsiniz!
    with open(f'm1l3\m1l4\images\{resim}', 'rb') as f:
            picture = discord.File(f)

   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


oneriler = ["yokuşlar için elektrikli bisiklet","hava kirliliği için elektrikli arabalar"]

@bot.command()
async def banafikirver(ctx):
    await ctx.send(random.choise(oneriler))

bot.run("")
