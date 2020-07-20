import textwrap
import discord
import os
from discord.ext import commands
from random import choice
from PIL import Image, ImageDraw, ImageFont

class Auto_Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Auto Images Loaded")

    @commands.command(aliases=['numbers', 'Mason'])
    async def mason(self,ctx):
        im = Image.open("./numbers/numbers_blank_template.png")
        draw = ImageDraw.Draw(im)
        image_width, image_height = im.size
        font = ImageFont.truetype(font="./numbers/Roboto/Roboto-Bold.ttf", size=int(image_height/20))
        
        with open("./numbers/Mason.txt", "r") as f:
            contents = f.read()
        
        contents = contents.split()
        numbers = []
        for i in range(5):
            item = choice(contents)
            numbers.append(item)
            contents.remove(item)

        char_width, char_height = font.getsize('A')

        y = [145, 145, 149, 148, 45]
        x = [84, 180, 289, 404, 403]
        for i in range(len(numbers)):
            draw.text((x[i], y[i]), numbers[i], font=font, fill='red')
        
        os.chdir('numbers')
        file_name = "the_numbers_mason.png"
        im.save("the_numbers_mason.png")
        await ctx.send(file=discord.File(f"{file_name}"))
        os.remove(file_name)
        os.chdir('..')



def setup(bot):
    bot.add_cog(Auto_Images(bot))
