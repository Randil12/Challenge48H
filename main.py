import plotly.express as px
import plotly.io as pio
import discord
from discord.ext import commands
import typing
from discord.ext import commands
from discord import app_commands
from discord import File

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await tree.sync()
        self.synced = True
        print("Bot is online")

bot = abot()
tree = app_commands.CommandTree(bot)

@tree.command(name="locate", description="jsp")
async def send_image(interation,  lat: str, lon: str, zoom: int):
    
    fig = px.scatter_mapbox(lat=[lat], lon=[lon], zoom=zoom)  # zoom max 18 min 0
    fig.update_layout(mapbox_style='open-street-map')

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)
    )

    pio.write_image(fig, 'carte_lyon.png')

    file = discord.File("carte_lyon.png", filename="carte_lyon.png")
    await interation.send(file=file)

@tree.command(name="activity", description="jsp")
async def self1(interation: discord.Interaction,activité:str , region: typing.Literal["EUW","EUNE","NA","BR","JP","KR","LA","LAS","OC","TR","RU"], queue: typing.Literal["SoloQ","FelxQ"]):
    await interation.response.send_message("str à la con activity")

bot.run('OTAxMzkzNzExNDQxNzcyNjA0.G5YQRm.TmuyTs47KDTEWHOdZ7qPVOYhTrz4e0iEP6XyvM')    