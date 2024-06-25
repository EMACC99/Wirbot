import os
import random
import discord
from discord.ext import commands


class Animeme(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.emoji = "<a:police_bear:837472471967072276>"

    @commands.Cog.listener()
    async def on_ready(self):
        print("Animemes loaded")

    @commands.hybrid_command(name="padoru", description="Hashire sori yo")
    async def padoru(self, ctx: commands.Context):
        path = os.path.join("Imagenes/Animemes/Padoru/")
        files = [f for f in os.listdir(path)]
        await ctx.send(file=discord.File(f"{path}{random.choice(files)}"))

    @commands.hybrid_command()
    async def uwu(self, ctx: commands.Context):
        path = os.path.join("Imagenes/Animemes/uwu.gif")
        await ctx.send(file=discord.File(path))

    @commands.hybrid_command()
    async def aaaa(self, ctx: commands.Context):
        path = os.path.join("Imagenes/Animemes/aaaa/")
        files = [f for f in os.listdir(path)]
        await ctx.send(file=discord.File(f"{path}{random.choice(files)}"))

    @commands.hybrid_command()
    async def gay_shit(self, ctx: commands.Context):
        path = os.path.join("Imagenes/Animemes/gay_shit/")
        files = [f for f in os.listdir(path)]
        await ctx.send(file=discord.File(f"{path}{random.choice(files)}"))

    @commands.hybrid_command()
    async def love(self, ctx: commands.Context):
        path = os.path.join("Imagenes/Animemes/Love/")
        files = [f for f in os.listdir(path)]
        await ctx.send(file=discord.File(path + random.choice(files)))

    @commands.command()
    async def angery(self, ctx: commands.Context):
        path = os.path.join("Imagenes/Animemes/Angery/")
        files = [f for f in os.listdir(path)]
        await ctx.send(file=discord.File(path + random.choice(files)))

    @commands.hybrid_command()
    async def mamadas(self, ctx: commands.Context):
        path = os.path.join("Imagenes/Animemes/Mamadas/")
        files = [f for f in os.listdir(path)]
        await ctx.send(file=discord.File(path + random.choice(files)))

    @commands.hybrid_command()
    async def nice(self, ctx: commands.Context):
        path = os.path.join("Imagenes/Nice/")
        files = [f for f in os.listdir(path)]
        await ctx.send(file=discord.File(f"{path}{random.choice(files)}"))

    @commands.hybrid_command()
    async def freeze(self, ctx: commands.Context):
        path = os.path.join("Imagenes/Animemes/")
        await ctx.send(
            "It's the anime police", file=discord.File(f"{path}The_anime_police.jpg")
        )

    @commands.hybrid_command()
    async def wirfreeze(self, ctx: commands.Context):
        await ctx.send(
            f"Al wirlag puto {self.emoji}",
            file=discord.File("Imagenes/Animemes/wirpolice.jpg"),
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Animeme(bot))
