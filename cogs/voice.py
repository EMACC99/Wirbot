from datetime import date
import discord
import socket
import json
from discord.ext import commands
from discord.utils import get
import datetime
import pytz

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("voice Loaded")

    @commands.command()
    async def habla(self, ctx, called=False):
        
        try:
            channel = ctx.message.author.voice.channel 
            voice = get(self.bot.voice_clients, guild=ctx.guild)

            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()

            await voice.disconnect()

            voice = await channel.connect()

            if called:
                return voice, channel
            else:
                voice.play(discord.FFmpegPCMAudio('voice/kyaa.mp3'), after=lambda e: print('ahh~'))
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.2
        
        except socket.gaierror():
            print(socket.getaddrinfo())
            print(socket.getnameinfo(socket.getaddrinfo()))
            socket.close()



    @commands.command()
    async def adios(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send('adios')
        else:
            await ctx.send('no estoy en un voice channel')

    @commands.command()
    async def pedro(self, ctx):
        # channel = ctx.message.author.voice.channel 
        # voice = get(self.bot.voice_clients, guild=ctx.guild)
        
        # if voice and voice.is_connected():
            # await voice.move_to(channel)
        # else:
            # voice = await channel.connect()

        voice, channel = await self.habla(ctx, called=True)

        voice.play(discord.FFmpegPCMAudio('voice/pedro.mp3'), after=lambda e: print('ya termine de hacer esto'))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.2

    @commands.command()
    async def huevo(self, ctx):
        # channel = ctx.message.author.voice.channel 
        # voice = get(self.bot.voice_clients, guild=ctx.guild)

        # if voice and voice.is_connected():
        #     await voice.move_to(channel)
        # else:
        #     voice = await channel.connect()
        voice, channel = await self.habla(ctx, called = True)
        
        voice.play(discord.FFmpegPCMAudio('voice/mama-huevo.mp3'), after=lambda e: print('mama huevoo'))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.2


    @commands.command(aliases = ["killer, super_mimir"])
    async def mimir_kill(self, ctx, member:discord.Member):
        # print(ctx.author)
        if discord.Guild.get_member(ctx.guild, ctx.author.id) == ctx.guild.owner or ctx.author.name == 'Westbound':
            
        # voice , channel = await self.habla(ctx, called=True)
            try:
            # voice.play(discord.FFmpegPCMAudio('voice/omae-wa-mou-shindeiru.mp3'))
            # voice.source = discord.PCMVolumeTransformer(voice.source)
            # voice.source.volume = 0.2
                await member.move_to(None, reason=f'Porque me lo ordeno le di killer al {member.name}!')
            # await self.adios(ctx)
            except Exception as e:
                await ctx.send('no se pudo')
                print(e)
        
            await ctx.send(f'Ya le di killer al {member.name}')
        else:
            await ctx.send('wiu wiu wiu, el autor no esta en el sudoers file ashe enojada ')
    

    @commands.command(aliases=['mimir'])
    async def mimir_nerfeado(self, ctx, member: discord.Member):
        if datetime.datetime.now(pytz.timezone('America/Mexico_City')).hour >= 21:
            with open('Roles/roles.json') as f:
                roles = json.load(f)

            for role in roles.values():
                if discord.utils.get(ctx.guild.roles, id=role) in ctx.author.roles:
                    voice, channel = await self.habla(ctx, called = True)
                    if member in channel.members:
                        await member.move_to(None, reason= f'{ctx.author.name} mando a oyasumimir a {member.name}')
                        await self.adios(ctx)
                        return
                    else:
                        await ctx.send('no se pudo equis de')
                        await self.adios(ctx)
                        return
            await ctx.send('wiu wiu wiu, el autor no esta en el sudoers file *ashe enojada*, este incidente sera reportado ')
        else:
            await ctx.send(f'{ctx.author.mention}, aun no es la hora de ir a mimir')

    @commands.command()
    async def habla_owo(self, ctx):
        voice, channel = await self.habla(ctx, called = True)
        
        voice.play(discord.FFmpegPCMAudio('voice/owo.mp3'), after=lambda e: print('owo'))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.2


    @commands.command()
    async def brazil(self, ctx):
        voice, channel = await self.habla(ctx, called = True)

        voice.play(discord.FFmpegPCMAudio('voice/brazil.mp3'), after=None)
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volumne = 1.

    @commands.command()
    async def invitame(self, ctx):
        voice, channel = await self.habla(ctx, called = True)

        voice.play(discord.FFmpegPCMAudio('voice/invitame.mp3'), after = None)
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1.


def setup(bot):
    bot.add_cog(Voice(bot))
