import random
import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Main commands loaded")

    @commands.command()
    async def silencio (self, ctx, members: commands.Greedy[discord.Member]):
        silenced = ', '.join(x.mention for x in members)
        # hacer que se mutee si estan en voice channel
        await ctx.send(f"{silenced} https://imgur.com/a/SgeN6L9")
        

    @commands.command()
    async def insulto(self, ctx, members: commands.Greedy[discord.Member]):
        insultos = ["Puto", "Sabandija", "Imbecil", "Piruja", "Troglodita", "Hijo de remilputa", "Conchetumadre",
         "Vieja anacronica con olor a formol y discipula de matusalen", "vieja bruja", "Tramposo", "Pinche vato gay", "Ojala te venda el cubos"]
        insultados = ', '.join(x.mention for x in members)
        await ctx.send(f"{insultados} {random.choice(insultos)}")
    
    @commands.command(aliases=['caracola', '8b'])
    async def caracola_magica(self, ctx, *, question):
        respuestas = ["Tranquis panquis", "ez", "No lo se bro", "No seas puto", "A cambio de una rtx", "Inesquibable", "Cuckeable",
         "veni veni", "ay mano", "El lunes sin falta", "Preguntale a tus amiguitas :upside_down:"]
        await ctx.send(random.choice(respuestas))
    
    @commands.command()
    async def elige (self, ctx, *, cosas = "si|no"):
        items = str(cosas).split('|')
        await ctx.send(random.choice(items))

    @commands.command(aliases=["Tg", "tom_gay", "tg"])
    async def _tomgay (self, ctx):
        await ctx.send("Tom gay", tts=True)
    
    @commands.command()
    async def coca(self, ctx, memeber: discord.Member):
        cocas = ["Sin azúcar", "Gary", "", "de piña"]
        await ctx.send(f"{memeber.mention}, {ctx.author.mention} te ha dado una coca {random.choice(cocas)}")

    @coca.error
    async def coca_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("No te puedes dar una coca a ti mismo!")
        

    # @commands.command()
    # async def simp(self, ctx, member: discord.Member, type: str = "SIMP | Betoso"):
    #     type = str(type).split('|')
    #     await ctx.send(f"{member.mention}, {random.choice(type)}", file = discord.File('Imagenes/betoso.png'))

def setup(bot):
    bot.add_cog(Main(bot))