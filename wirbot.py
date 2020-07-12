import sys
import os
import random
import discord
from time import sleep
import gc
from discord.ext import commands

token = open("token.txt", 'r').read()
client = discord.Client()

bot = commands.Bot(command_prefix = '&')

@bot.event
async def on_ready():
    print('Soy yo! El {0.user}'.format(bot))

#comandos misc/utiles

@bot.command()
async def hola (ctx):
    await ctx.send("Te pica la cola!")

@bot.command()
async def comandos(ctx):
    await ctx.author.send(open("comandos.txt", "r").read())

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! Son las bolas de king kong! {round(bot.latency *1000)} ms")

@bot.command()
async def silencio (ctx, members: commands.Greedy[discord.Member]):
    silenced = ', '.join(x.mention for x in members)
    await ctx.send(f"{silenced} https://imgur.com/a/SgeN6L9")

@bot.command()
async def insulto(ctx, members: commands.Greedy[discord.Member]):
    insultos = ["Puto", "Sabandija", "Imbecil", "Piruja", "Troglodita", "Hijo de remilputa", "Conchetumadre",
     "Vieja anacronica con olor a formol y discipula de matusalen", "vieja bruja", "Tramposo", "Pinche vato gay", "Ojala te venda el cubos"]
    insultados = ', '.join(x.mention for x in members)
    await ctx.send(f"{insultados} {random.choice(insultos)}")

@bot.command(aliases=['caracola', '8b'])
async def caracola_magica(ctx, *, question):
    respuestas = ["Tranquis panquis", "ez", "No lo se bro", "No seas puto", "A cambio de una rtx", "Inesquibable", "Cuckeable",
     "veni veni", "ay mano", "El lunes sin falta", "Preguntale a tus amiguitas :upside_down:"]
    await ctx.send(random.choice(respuestas))

@bot.command()
async def elige (ctx, *, cosas = "si|no"):
    items = str(cosas).split('|')
    # if "tom gay" in [x.lower() for x in items]:
    #     await ctx.send("tom gay")
    await ctx.send(random.choice(items))

@bot.command(aliases=["Tg", "tom_gay", "tg"])
async def _tomgay (ctx):
    await ctx.send("Tom gay", tts=True)

@bot.command()
async def spam(ctx, member: discord.Member, *, mensaje="Oye"):
    # user = await client.get_user(member)
    if member.name == "Westbound": 
        await ctx.author.send("Nel putx")
        return
    try:
        mensajes = random.randint(15,25)
        for i in range(mensajes):
            await member.send(f"{member.name} {mensaje}")
            sleep(random.randint(1,5))
    except Exception as e:
        print(e)



#nice

@bot.command()
async def nice(ctx):
    path = os.path.join('Imagenes/Nice/')
    files = [f for f in os.listdir(path)]
    await ctx.send(file = discord.File(f"{path}{random.choice(files)}"))

#prankeanding


#animemes

@bot.command()
async def padoru(ctx):
    path = os.path.join('Imagenes/Animemes/Padoru/')
    files = [f for f in os.listdir(path)]
    await ctx.send(file = discord.File(f"{path}{random.choice(files)}"))

@bot.command()
async def uwu(ctx):
    path = os.path.join("Imagenes/Animemes/uwu.gif")
    await ctx.send(file = discord.File(path))

@bot.command()
async def aaaa (ctx):
    path = os.path.join("Imagenes/Animemes/aaaa/")
    files = [f for f in os.listdir(path)]
    await ctx.send(file = discord.File(f"{path}{random.choice(files)}"))

@bot.command()
async def gay_shit(ctx):
    path = os.path.join("Imagenes/Animemes/gay_shit/")
    files = [f for f in os.listdir(path)]
    await ctx.send(file = discord.File(f"{path}{random.choice(files)}"))

@bot.command()
async def love(ctx):
    path = os.path.join("Imagenes/Animemes/Love/")
    files = [f for f in os.listdir(path)]
    await ctx.send(file = discord.File(path+random.choice(files)))

@bot.command(aliases = ["mad", "anger"])
async def angery(ctx):
    path = os.path.join("Imagenes/Animemes/Angery/")
    files = [f for f in os.listdir(path)]
    await ctx.send(file = discord.File(path+random.choice(files)))

@bot.command()
async def mamadas(ctx):
    path = os.path.join("Imagenes/Animemes/Mamadas/")
    files = [f for f in os.listdir(path)]
    await ctx.send(file = discord.File(path+random.choice(files)))

#debug

@bot.command()
async def name(ctx, member: discord.Member):
    print (member.name)
    print (member.mention)


#moderation

# @bot.command()
# async def kick (ctx, member: discord.Member, *, reason = None):
#     await member.kick(reason=reason)

# @bot.command()
# async def ban (ctx, member: discord.Member, *, reason = None):
#     await member.ban(reason=reason)


# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

bot.run(token)
gc.collect()