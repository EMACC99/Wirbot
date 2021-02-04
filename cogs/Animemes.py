import os
import random
import discord
from discord.ext import commands

class Animeme(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Animemes loaded")

    @commands.command()
    async def padoru(self, ctx):
        path = os.path.join('Imagenes/Animemes/Padoru/')
        files = [f for f in os.listdir(path)]
        await ctx.send(file = discord.File(f"{path}{random.choice(files)}"))

    @commands.command()
    async def uwu(self, ctx):
        path = os.path.join("Imagenes/Animemes/uwu.gif")
        await ctx.send(file = discord.File(path))

    @commands.command()
    async def aaaa (self, ctx):
        path = os.path.join("Imagenes/Animemes/aaaa/")
        files = [f for f in os.listdir(path)]
        await ctx.send(file = discord.File(f"{path}{random.choice(files)}"))

    @commands.command()
    async def gay_shit(self,ctx):
        path = os.path.join("Imagenes/Animemes/gay_shit/")
        files = [f for f in os.listdir(path)]
        await ctx.send(file = discord.File(f"{path}{random.choice(files)}"))


    @commands.command()
    async def love(self,ctx):
        path = os.path.join("Imagenes/Animemes/Love/")
        files = [f for f in os.listdir(path)]
        await ctx.send(file = discord.File(path+random.choice(files)))


    @commands.command(aliases = ["mad", "anger"])
    async def angery(self, ctx):
        path = os.path.join("Imagenes/Animemes/Angery/")
        files = [f for f in os.listdir(path)]
        await ctx.send(file = discord.File(path+random.choice(files)))

    @commands.command()
    async def mamadas(self, ctx):
        path = os.path.join("Imagenes/Animemes/Mamadas/")
        files = [f for f in os.listdir(path)]
        await ctx.send(file = discord.File(path+random.choice(files)))

    @commands.command()
    async def nice(self, ctx):
        path = os.path.join('Imagenes/Nice/')
        files = [f for f in os.listdir(path)]
        await ctx.send(file = discord.File(f"{path}{random.choice(files)}"))


    @commands.command(aliases = ["police"])
    async def freeze(self, ctx):
        path = os.path.join('Imagenes/Animemes/')
        await ctx.send("It's the anime police", file = discord.File(f'{path}The_anime_police.jpg'))

    @commands.command(aliases = ["wirAnimepolice", "wirpolice", "wiranimepolice", "wirlag"])
    async def wirfreeze(self, ctx):
        await ctx.send("Al wirlag puto", file = discord.File("Imagenes/Animemes/wirpolice.jpg"))

def setup(bot):
    bot.add_cog(Animeme(bot))
