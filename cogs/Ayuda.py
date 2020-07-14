import discord
from discord.ext import commands

class Ayuda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help loaded")
    
    @commands.command()
    async def comandos(self, ctx):
        author = ctx.author

        embed = discord.Embed(
            colour = discord.Colour.blurple()
        )
        embed.set_author(name='Wirbot')
        # embed.set_image()
        # embed.set_thumbnail()
        embed.add_field(name=f'&hola', value='Te pica la cola!', inline=False)
        embed.add_field(name=f'&insulto @usuario', value='te manda un insulto')
        embed.add_field(name=f'&silencio @usuario' , value='wirbot')
        embed.add_field(name=f'&ping' , value='Pong!')
        embed.add_field(name=f'&elije opc 1|opc 2|...|opc n' , value='elije entre dos o mas cosas separadas por | defualt: si|no')
        embed.add_field(name=f'&caracola_magica <pregunta>' , value='Preguntale a la caracola  alias: &8b, &caracola')
        embed.add_field(name=f'&tom_gay' , value='Tom gay alias: tg, Tg ')
        embed.add_field(name=f'&spam @usuario <mensaje>' , value='Manda entre 15 y 20 mensajes por dm a la persona que lo dirigen')
        embed.add_field(name=f'&desafio <mensaje opcional>' , value='desafia al admin')

        embed.add_field(name=f'&padoru', value='random padoru')
        embed.add_field(name=f'&uwu', value='uwu')
        embed.add_field(name=f'&aaaa', value='aaaa')
        embed.add_field(name=f'&gay_shit', value='gay shit')
        embed.add_field(name=f'&love', value='mona china con corazón')
        embed.add_field(name=f'&angery', value='>:C')
        embed.add_field(name=f'&mamadas', value='no diga mamadas mijo')
        embed.add_field(name=f'&nice', value='noice')
        

        embed.set_footer(text='Si necesitas más ayuda puedes pedirla con el equipo de desarrollo uwu')

        await ctx.author.send(embed=embed)
def setup(bot):
    bot.add_cog(Ayuda(bot))