import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Greetings loaded")

    # async def on_member_join(self, member):
    #     channel = member.guild.system_channel
    #     if channel is not None:
    #         await channel.send(f"Bienvenido al server {member.mention}!!")

    @commands.hybrid_command()
    async def hola(self, ctx: commands.Context):
        await ctx.send("Te pica la cola!")

    @commands.hybrid_command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(
            f"Pong! Son las bolas de king kong! {round(self.bot.latency *1000)} ms"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Greetings(bot))
