import sys
import os
import random
import gc
import discord
from discord.ext import commands, tasks
from itertools import cycle

token = open("token.txt", 'r').read()
client = discord.Client()
prefix = '&'
bot = commands.Bot(command_prefix = prefix)


status = cycle(['Mamandosela al admin \n', 'Viendo fotos de wirluis trapo \n', '¿Debería tener Only Fans 🤔?\n', '¿Qué me ves cara de pez?\n', 'Dale el beso Tom\n', "Cuckeando\n"])
default = '\n¡Usa &comandos para ver todo lo que puedo hacer! \n'

mods = [] #id's de los roles de mod aqui


@bot.event
async def on_ready():
    change_status.start()
    print('Soy yo! El {0.user} de prueba uwu'.format(bot))

@tasks.loop(minutes=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)+default))

@bot.command()
async def load (ctx,extension):
    bot.load_extension(f'cogs.{extension}')
    print(f"{extension} Loaded")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print(f"{extension} Unloaded")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(token)
gc.collect()
