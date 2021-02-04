import random
import discord
import os
import shutil
import requests
from discord.ext import commands
from random import choice
from PIL import Image, ImageDraw, ImageFont

class Auto_Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    def make_auto_meme(self):
        pass


    @commands.Cog.listener()
    async def on_ready(self):
        print("Auto Images Loaded")


    @commands.command(aliases=['numbers', 'Mason'])
    async def mason(self,ctx, *, args = ''):
        import nhentai_scrapper.nhentai_scrapper_bot_version as nhentai
        if isinstance(ctx.channel, discord.DMChannel) or ctx.channel.is_nsfw():
            im = Image.open("./numbers/numbers_blank_template.png")
            draw = ImageDraw.Draw(im)
            image_width, image_height = im.size
            font = ImageFont.truetype(font="./numbers/Roboto/Roboto-Bold.ttf", size=int(image_height/20))

            # with open("./numbers/Mason.txt", "r") as f:
            #     contents = f.read()

            # contents = contents.split()
            if len(args) == 0:
                contents = nhentai.get_front_page()
            else:
                contents = nhentai.search(args)

            if type(contents) == int:
                await ctx.send(f"No se pudo, la pagina regreso {contents}")
                return

            if len(contents) == 0:
                await ctx.send(f"No hay nada tan especifico para tus marranadas, viejx cochinx")
                return

            numbers = []
            n = 5
            if len(contents) < 5:
                n = len(contents)

            for i in range(n):
                item = choice(contents)
                numbers.append(item)
                contents.remove(item)

            # char_width, char_height = font.getsize('A')

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

        else:
            await ctx.send("Marrano")
            await ctx.send(file=discord.File(f"./Imagenes/spanish_inquisition.gif"))


    @commands.command(aliases = ['mano'])
    async def simp(self, ctx, member: discord.Member, content = "SIMP|Betoso"):
        content = str(content).split('|')
        content = [_.upper() for _ in content]
        # print(content)
        content = random.choice(content)
        # print(content)
        im = Image.open('./Imagenes/betoso_resized.png')
        draw = ImageDraw.Draw(im)
        image_width, image_height = im.size
        font = ImageFont.truetype(font="./numbers/Roboto/Roboto-Bold.ttf", size=int(image_height/7))
        x,y = 100,250
        draw.text((x,y), content, font=font, fill = 'white')
        file_name = "imagen.png"
        im.save(file_name)
        await ctx.send(file = discord.File(file_name))


    @commands.command(aliases=['fotito'])
    async def perfil(self, ctx, user: discord.User):
        await ctx.send(f"Mira, la imagen de {user} {user.avatar_url}")


    @commands.command(aliases=['pet'])
    async def head_pat(self,ctx,user: discord.User):
        # profile_pic = user.avatar_url
        profile_pic = user.avatar_url_as(format='png')
        response = requests.get(profile_pic, stream = True)

        if response.status_code == 200:
            response.raw.decode_content = True
            os.chdir('pet')    
            try:
                os.remove('profile.png')
            except:
                pass

            with open('profile.png', 'wb') as f:
                shutil.copyfileobj(response.raw, f)
                import pet.head_pats
                pet.head_pats.main()
               
                await ctx.send(file=discord.File('output.gif'))
                
                os.chdir('..')
        else:
            await ctx.send("A ocurrido un error :cry:")
        # await ctx.send(profile_pic)


def setup(bot):
    bot.add_cog(Auto_Images(bot))
