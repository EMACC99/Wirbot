import discord
import random
from discord.ext import commands
from time import sleep

class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Spam Loaded")
    
    @commands.command()
    async def spam(self, ctx, member: discord.Member, *, mensaje="Oye"):
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

def setup(bot):
    bot.add_cog(Spam(bot))