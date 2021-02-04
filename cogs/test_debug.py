import discord
from discord.ext import commands

class debug_time(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ya puedes hacer debug")

    
    @commands.command()
    async def member_name(self,ctx, member: discord.Member):
        print (member.name)
        print (member.mention)
        print (member.id)
        print (discord.Guild.get_member(ctx.guild, ctx.author.id))
        print (ctx.guild.owner_id)
        print(discord.Guild.get_member(ctx.guild, member.id) == ctx.guild.owner)
    
    @commands.command()
    async def role_name(self,ctx):
        for role in ctx.guild.roles:
            print (role.name)
            print (role.mention)
            print (role.id)
            print (type(role.id))
            print (discord.utils.get(ctx.guild.roles, id = role.id))


def setup(bot):
    bot.add_cog(debug_time(bot))