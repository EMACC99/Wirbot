import discord
import random
from discord.ext import commands
from time import sleep
import json
import os

class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Spam Loaded")
    
    @commands.command()
    async def spam(self, ctx, member: discord.Member, *, mensaje="Oye"):
        path = os.path.join('Roles/')        
        with open(path+'roles.json', 'r') as f:
            roles = json.load(f)
            
        for role in roles.values():
            if discord.utils.get(ctx.guild.roles, id=role) in ctx.author.roles:
                try:
                    mensajes = random.randint(15,25)
                    for i in range(mensajes):
                        # await member.send(f"{member.name} {mensaje}")
                        await member.send(f"{mensaje}")
                        
                        sleep(random.randint(1,5))
                except Exception as e:
                    print(e)                
                
                return
    
        await ctx.send("no tienes permisos")

        # if member.name == "Westbound": 
        #     await ctx.author.send("Nel putx")
        #     return

def setup(bot):
    bot.add_cog(Spam(bot))
