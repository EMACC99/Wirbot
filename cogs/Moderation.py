import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        # id_bruce = 123
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation class loaded")

    @commands.command()
    async def desafio(self, ctx, *, reason=""):
        # admin = discord.utils.get(ctx.guild.roles, id=696406564730568705) #admin admin
        admin = discord.utils.get(ctx.guild.roles, id=662153290594648094) #los lords
        print(type(admin))
        print (admin)
        await ctx.send(f"{ctx.author.mention} ha desafiado al Admin {admin.mention} {reason}")

    # @commands.command(aliases = ["no_bruce", "shadow_bruce"]) #comando para banear al bruce
    # @commands.has_permissions(kick_members=True)
    # async def rip_bruce(self, ctx, member: discord.Member, *, reason="por mis huevos"):
    #     # member = discord.utils.get(ctx.guild.member, id = self.id_bruce)
    #     if member.name == "Locorraco":
    #         await member.kick(reason = reason)
    #         await ctx.send(f"{ctx.author.mention} ha kickeado al bruce, recuerda que tienes la obligacion de mandarle la invitacion")
    #     elif member.name is not "Locorraco":
    #         await ctx.send(f"{ctx.author.mention} No puedes kickear a alguien que no sea bruce")
    #     else:
    #         await ctx.send(f"{ctx.author.mention} intento banear a alguien, notifiquenle al {ctx.guild.owner.mention}")

def setup(bot):
    bot.add_cog(Moderation(bot))    