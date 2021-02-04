import asyncio
import os
import random
import discord
from discord.ext import commands
from discord.utils import get
from discord import Embed
from Bank import user_operations

reactions = ['<:kirbyculo:631698681506168871>', '<:wahaha:651897822186176515>']

class Bank(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bank loaded")


    @commands.command()
    async def register(self, ctx):
        m = await ctx.send("Te gustaria registrarte en el servicio bancario?")
        for reaction in reactions:
            await m.add_reaction(reaction)

        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) in reactions

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout = 60, check = check)
        except asyncio.TimeoutError:
            # await ctx.send(reactions[1])
            await ctx.send(f'Se acabo el tiempo mi chavo {reactions[1]}')

        else:
            # print(reaction.emoji.id)
            # print(type(reaction.emoji.id))
            # print(type(reactions[0][1:-1].split(':')[-1]))
            if reaction.emoji.id == int(reactions[0][1:-1].split(':')[-1]):
                member = ctx.message.author.id
                msg, ok = user_operations.register_user(member, init_balance=50)
                if ok:
                    await ctx.send(f'{msg}')
                    await ctx.send(f'bienvenido al wirbanco')
                elif not ok:
                    await ctx.send(f'ocurrio un error, contacte al admin')
                    await ctx.send(f'{msg}')

            elif reaction.emoji.id == int(reactions[1][1:-1].split(':')[-1]):
                await ctx.send(f'al cabo que ni queria')
                
                


    @commands.command()
    async def balance(self, ctx):
        member = ctx.message.author.id
        balance = user_operations.balance(member)
        if type(balance) == str:
            await ctx.send(f'ocurrio un error: {balance}')
        else:
            await ctx.send(f'Tu balance es de <:fedebrush:786993930217455616> {balance} brushcoins')


    @commands.command()
    async def wirwalet(self, ctx):
        raise NotImplementedError

    @commands.command()
    async def transfer(self, ctx, member:discord.Member, brush_coin:int):
        raise NotImplementedError

    @commands.command()
    async def wirbet(self, ctx, brush_coin:int, win_porcentaje:float):
        loss = 0.5
        member = ctx.message.author.id
        balance = user_operations.balance(member)
        if type(balance) != float:
            await ctx.send(f'Ha ocurrido un error: {balance}')
        else:
            if brush_coin > balance:
                await ctx.send(f'Ponte a chambear para conseguir mas brushcoins <:fedebrush:786993930217455616>')
            else:
                num = 0
                for chance in range(3):
                    num = random.random()
                if num < 0.5:
                    await ctx.send(f'Te la pleaste, pierdes {loss * 100:.2f}% de tus brushcoins')
                    ok, message = user_operations.update_balance(member, balance * loss)
                    if ok:
                        await ctx.send('operacion completada!')
                    else:
                        await ctx.send(f'Ha ocurrido un error pero tus brushcoins que tenias antes del wirbet se pierden (o eso espero :P), {message}')
                elif num >= 0.5:
                    await ctx.send(f'Has ganado el wirbet y ahora tu balance aumenta {win_porcentaje *100:.2f}%')
                    ok, message = user_operations.update_balance(member, balance + (balance * win_porcentaje))
                    if ok:
                        await ctx.send('operacion completada!')
                    else: 
                        await ctx.send(f'Ha ocurrido un error pero tus brushcoins que tenias antes del wirber no se pierden (o eso espero :P), {message}')

def setup(bot):
    bot.add_cog(Bank(bot))