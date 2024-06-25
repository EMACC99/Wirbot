import os
import random
import gc
import discord
from discord.ext import commands, tasks
from discord import app_commands
from itertools import cycle

with open("token.txt", "r") as f:
    token = f.read()


class Wirbot(commands.Bot):
    def __init__(self) -> None:

        self.status_list = [
            "Mamandosela al admin\n",
            "Viendo fotos de wirluis trapo\n",
            "¿Debería tener Only Fans 🤔?\n",
            "¿Qué me ves cara de pez?\n",
            "Dale el beso Tom\n",
            "Cuckeando\n",
        ]

        random.shuffle(self.status_list)
        self.status_msg = cycle(self.status_list)
        self.default = "\n¡Usa &comandos para ver todo lo que puedo hacer!\n"

        super().__init__(
            command_prefix="&",
            intents=discord.Intents.all(),
            application_id=731570508570689557,
        )

    async def setup_hook(self) -> None:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
        await self.tree.sync()

    async def on_ready(self):
        print(f"Soy yo! El {self.user} de prueba uwu")

    @tasks.loop(minutes=30)
    async def change_status(self):
        await self.change_presence(
            activity=discord.Game(f"{next(self.status_msg)} {self.default}")
        )


bot = Wirbot()
bot.run(token)
