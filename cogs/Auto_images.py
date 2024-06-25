import random
import discord
import os
import shutil
import requests
from discord.ext import commands
from random import choice
from PIL import Image, ImageDraw, ImageFont
from nhentai_scrapper import nscrapper
from pet import headpats


class Auto_Images(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def make_auto_meme(self):
        pass

    @commands.Cog.listener()
    async def on_ready(self):
        print("Auto Images Loaded")

    @commands.hybrid_command()
    async def mason(self, ctx: commands.Context, *, args=""):

        if isinstance(ctx.channel, discord.DMChannel) or ctx.channel.is_nsfw():
            im = Image.open("./numbers/numbers_blank_template.png")
            draw = ImageDraw.Draw(im)
            image_width, image_height = im.size
            font = ImageFont.truetype(
                font="./numbers/Roboto/Roboto-Bold.ttf", size=int(image_height / 20)
            )

            # with open("./numbers/Mason.txt", "r") as f:
            #     contents = f.read()

            # contents = contents.split()
            if len(args) == 0:
                contents = nscrapper.get_front_page()
            else:
                contents = nscrapper.search(args)

            if type(contents) == int:
                await ctx.send(f"No se pudo, la pagina regreso {contents}")
                return

            if len(contents) == 0:
                await ctx.send(
                    f"No hay nada tan especifico para tus marranadas, viejx cochinx"
                )
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
                draw.text((x[i], y[i]), numbers[i], font=font, fill="red")

            os.chdir("numbers")
            file_name = "the_numbers_mason.png"
            im.save("the_numbers_mason.png")
            await ctx.send(file=discord.File(f"{file_name}"))
            os.remove(file_name)
            os.chdir("..")

        else:
            await ctx.send("Marrano")
            await ctx.send(file=discord.File(f"./Imagenes/spanish_inquisition.gif"))

    @commands.hybrid_command()
    async def simp(
        self, ctx: commands.Context, member: discord.Member, content="SIMP|Betoso"
    ):
        content = str(content).split("|")
        content = [_.upper() for _ in content]
        # print(content)
        content = random.choice(content)
        # print(content)
        im = Image.open("Imagenes/betoso_resized.png")
        draw = ImageDraw.Draw(im)
        image_width, image_height = im.size
        font = ImageFont.truetype(
            font="./numbers/Roboto/Roboto-Bold.ttf", size=int(image_height / 7)
        )
        x, y = 100, 250
        draw.text((x, y), content, font=font, fill="white")
        file_name = "imagen.png"
        im.save(file_name)
        await ctx.send(file=discord.File(file_name))

    @commands.hybrid_command()
    async def perfil(self, ctx: commands.Context, user: discord.User):
        await ctx.send(f"Mira, la imagen de {user} {user.avatar}")

    @commands.hybrid_command()
    async def pet(self, ctx: commands.Context, user: discord.User):
        profile_pic = user.avatar.replace(format="png")
        response = requests.get(profile_pic, stream=True)

        if response.status_code == 200:
            response.raw.decode_content = True
            # os.chdir("pet")
            try:
                os.remove("pet/profile.png")
            except:
                pass

            with open("pet/profile.png", "wb") as f:
                shutil.copyfileobj(response.raw, f)
                headpats.head_pats()

                await ctx.send(file=discord.File("output.gif"))

                os.chdir("..")
        else:
            await ctx.send("A ocurrido un error :c")
        # await ctx.send(profile_pic)


async def setup(bot: commands.Bot):
    await bot.add_cog(Auto_Images(bot))
