import random
import discord
from discord.ext import commands
from typing import List


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Main commands loaded")

    @commands.hybrid_command()
    async def silencio(
        self, ctx: commands.Context, members: commands.Greedy[discord.Member]
    ):
        silenced = ", ".join(x.mention for x in members)
        # hacer que se mutee si estan en voice channel
        await ctx.send(f"{silenced} https://imgur.com/a/SgeN6L9")

    @commands.hybrid_command()
    async def insulto(
        self, ctx: commands.Context, members: commands.Greedy[discord.Member]
    ):
        insultos = [
            "Puto",
            "Sabandija",
            "Imbecil",
            "Piruja",
            "Troglodita",
            "Hijo de remilputa",
            "Conchetumadre",
            "Vieja anacronica con olor a formol y discipula de matusalen",
            "vieja bruja",
            "Tramposo",
            "Pinche vato gay",
            "Ojala te venda el cubos",
        ]
        insultados = ", ".join(x.mention for x in members)
        await ctx.send(f"{insultados} {random.choice(insultos)}")

    @commands.hybrid_command()
    async def caracola(self, ctx: commands.Context, *, question):
        respuestas = [
            "Tranquis panquis",
            "ez",
            "No lo se bro",
            "No seas puto",
            "A cambio de una rtx",
            "Inesquibable",
            "Cuckeable",
            "veni veni",
            "ay mano",
            "El lunes sin falta",
            "Preguntale a tus amiguitas :upside_down:",
            "mejor desinstala",
        ]
        await ctx.send(random.choice(respuestas))

    @commands.hybrid_command()
    async def eigthlox(self, ctx: commands.Context, *, question):
        palomo_respuestas = [
            "Cielos, que basado",
            "Pedro basado, Pedro basado",
            "Eso me recuerda a Scary Movie",
            "Cuando el Niño del Pedro tenga manos",
            "Server buena onda, server buena onda",
            "A limpiar papas, campesino",
            "Claro que soy prieto, soy peruano",
            "Wirluiiiiiiiiiiiisssss!",
            "Akasita pete",
            "Habla bien indio",
        ]
        await ctx.send(random.choice(palomo_respuestas))

    @commands.hybrid_command()
    async def elige(self, ctx: commands.Context, *, cosas="si|no"):
        items = str(cosas).split("|")
        await ctx.send(random.choice(items))

    @commands.hybrid_command()
    async def tom_gay(self, ctx: commands.Context):
        await ctx.send("Tom gay", tts=True)

    @commands.hybrid_command()
    async def ugu(self, ctx: commands.Context):
        await ctx.send(
            "ugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugugu",
            tts=True,
        )

    @commands.hybrid_command()
    async def coca(self, ctx: commands.Context, memeber: discord.Member):
        cocas = ["Sin azúcar", "Gary", "", "de piña"]
        await ctx.send(
            f"{memeber.mention}, {ctx.author.mention} te ha dado una coca {random.choice(cocas)}"
        )

    @coca.error
    async def coca_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("No te puedes dar una coca a ti mismo!")

    @commands.hybrid_command()
    async def tombola(self, ctx: commands.Context):
        role_id = 301519670840655882
        role = discord.utils.get(ctx.guild.roles, id=role_id)
        # members_list = [member for member in ctx.guild.members if role in member.roles]
        members_list: List[discord.Member] = []
        for member in ctx.message.guild.members:
            if role in member.roles:
                members_list.append(member)

        pendejo = random.choice(random.sample(members_list, len(members_list)))
        await ctx.send(
            f"Has sido seleccionado para la TOMbola {pendejo.mention}, sientete como quieras"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))
