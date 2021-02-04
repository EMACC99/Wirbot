"""
Wirbank User Operations
~~~~~~~~~~~~~~~~~~~

Conector Para la base de datos del Wirbank

:copyright: (c) 2020 Eduardo Ceja
:license: MIT, see LICENSE for more details.

"""
__title__ = 'Wribot'
__author__ = 'Eduardo Ceja'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 Eduardo Ceja'
__version__ = '2.1.0'


import os
import random
import gc
import discord
from discord.ext import commands, tasks
from itertools import cycle


token = open("token.txt", 'r').read()
client = discord.Client()

prefix = '&'
bot = commands.Bot(command_prefix = commands.when_mentioned_or(prefix))

status_list = ['Mamandosela al admin \n', 'Viendo fotos de wirluis trapo \n', 
            '¿Debería tener Only Fans 🤔?\n', '¿Qué me ves cara de pez?\n', 
            'Dale el beso Tom\n', "Cuckeando\n"]

random.shuffle(status_list)
status = cycle(status_list)
default = '\n¡Usa &comandos para ver todo lo que puedo hacer!\n'


@bot.event
async def on_ready():
    change_status.start()
    print('Soy yo! El {0.user} de prueba uwu'.format(bot))

@client.event
async def on_member_join(self, member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f"Bienvenido al server {member.mention}!!")

@tasks.loop(minutes=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)+default))
    # await bot.change_presence(activity=discord.Game(random.choice(status_list)))



# @bot.event
# async def on_command_error(ctx,error):
#     await ctx.send(error)
    

@bot.command()
async def load (ctx,extension):
    if ctx.author.name == "Westbound":
        bot.load_extension(f'cogs.{extension}')
        print(f"{extension} Loaded")
        await ctx.send(f"{extension} Loaded")
    else:
        await ctx.send("Username is not in the sudoers file. This incident will be reported" )

@bot.command()
async def unload(ctx, extension):
    if ctx.author.name == "Westbound":
        bot.unload_extension(f'cogs.{extension}')
        print(f"{extension} Unloaded")
        await ctx.send(f"{extension} Unloaded")
    else:
        await ctx.send("Username is not in the sudoers file. This incident will be reported" )

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


# async def on_message(message):
#     if bot.user.mentioned_in(message):
#         await message.channel.send('¿Que putas quieres?')


bot.run(token)    
gc.collect()