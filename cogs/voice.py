from datetime import date
import discord
import socket
import json
from discord.ext import commands
from discord.utils import get
import datetime
import pytz


class Voice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("voice Loaded")

    @commands.hybrid_command()
    async def habla(self, ctx: commands.Context, called=False):

        try:
            channel = ctx.message.author.voice.channel
            voice = get(self.bot.voice_clients, guild=ctx.guild)

            if voice and voice.is_connected() and voice.channel != channel:
                await voice.move_to(channel)

            elif voice and voice.is_connected() and voice.channel == channel:
                pass

            else:
                voice = await channel.connect()

            if called:
                return voice, channel

            else:
                voice.play(
                    discord.FFmpegPCMAudio("voice/kyaa.mp3"),
                    after=lambda e: print("ahh~"),
                )
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.2

        except socket.gaierror():
            print(socket.getaddrinfo())
            print(socket.getnameinfo(socket.getaddrinfo()))
            socket.close()
            self.bot.unload_extension("voice")

    @commands.hybrid_command()
    async def adios(self, ctx: commands.Context):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send("adios")
        else:
            await ctx.send("no estoy en un voice channel")

    async def reproducir_wea(self, ctx, filename: str, volume: float = 1.0) -> None:
        voice, channel = await self.habla(ctx, called=True)

        voice.play(discord.FFmpegPCMAudio(filename))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = volume

    @commands.hybrid_command()
    async def pedro(self, ctx):
        await self.reproducir_wea(ctx, "voice/pedro.mp3", volume=0.2)

    @commands.hybrid_command()
    async def huevo(self, ctx):
        await self.reproducir_wea(ctx, "voice/mama-huevo.mp3", 0.2)

    @commands.hybrid_command(aliases=["killer, super_mimir"])
    async def mimir_kill(self, ctx, member: discord.Member):
        # print(ctx.author)
        if (
            discord.Guild.get_member(ctx.guild, ctx.author.id) == ctx.guild.owner
            or ctx.author.name == "West"
        ):

            try:
                await member.move_to(
                    None, reason=f"Porque me lo ordeno le di killer al {member.name}!"
                )
            except Exception as e:
                await ctx.send("no se pudo")
                print(e)

            await ctx.send(f"Ya le di killer al {member.name}")
        else:
            await ctx.send(
                "wiu wiu wiu, el autor no esta en el sudoers file ashe enojada "
            )

    @commands.hybrid_command()
    async def mimir_nerfeado(self, ctx: commands.Context, member: discord.Member):
        if datetime.datetime.now(pytz.timezone("America/Mexico_City")).hour >= 21:
            with open("Roles/roles.json") as f:
                roles = json.load(f)

            for role in roles.values():
                if discord.utils.get(ctx.guild.roles, id=role) in ctx.author.roles:
                    voice, channel = await self.habla(ctx, called=True)
                    if member in channel.members:
                        await member.move_to(
                            None,
                            reason=f"{ctx.author.name} mando a oyasumimir a {member.name}",
                        )
                        await self.adios(ctx)
                        return
                    else:
                        await ctx.send("no se pudo equis de")
                        await self.adios(ctx)
                        return
            await ctx.send(
                "wiu wiu wiu, el autor no esta en el sudoers file *ashe enojada*, este incidente sera reportado "
            )
        else:
            await ctx.send(f"{ctx.author.mention}, aun no es la hora de ir a mimir")

    @commands.hybrid_command()
    async def habla_owo(self, ctx: commands.Context):
        await self.reproducir_wea(ctx, "voice/owo.mp3", volume=0.2)

    @commands.hybrid_command()
    async def brazil(self, ctx: commands.Context):
        await self.reproducir_wea(ctx, "voice/brazil.mp3")

    @commands.hybrid_command()
    async def invitame(self, ctx: commands.Context):
        await self.reproducir_wea(ctx, "voice/invitame.mp3")

    @commands.hybrid_command(aliases=["wirpersecucion", "wirpollo"])
    async def persecucion(self, ctx: commands.Context):
        await self.reproducir_wea(ctx, "voice/persecucion_epica.mp3")

    @commands.hybrid_command(aliases=["ganon"])
    async def suavemente(self, ctx: commands.Context):
        await self.reproducir_wea(ctx, "voice/Cucui_Ganon_-_Suavemente.mp3")

    @commands.hybrid_command()
    async def abrazo(self, ctx: commands.Context):
        await self.reproducir_wea(ctx, "voice/abrazarte.mp3")

    @commands.hybrid_command()
    async def ratas(self, ctx: commands.Context):
        await self.reproducir_wea(ctx, "voice/ratas_judias.mp3")


async def setup(bot: commands.Bot):
    await bot.add_cog(Voice(bot))
