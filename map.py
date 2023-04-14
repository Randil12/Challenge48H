import plotly.express as px
import plotly.io as pio
import discord
from discord.ext import commands
import typing
from discord.ext import commands
from discord import app_commands

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await tree.sync()
        self.synced = True
        print("Bot is online")

def get_map(lat, lon, zoom):
    fig = px.scatter_mapbox(lat=[lat], lon=[lon], zoom=zoom)
    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)
    )
    pio.write_image(fig, 'carte_lyon.png')
    file = discord.File("carte_lyon.png", filename="carte_lyon.png")
    return file

bot = abot()
tree = app_commands.CommandTree(bot)


# Définir une commande pour envoyer l'image
@bot.event
async def on_ready():
    print('Bot is ready')


@tree.command(name="location", description="jsp")
async def self1(ctx, lat: str, lon: str, zoom: int):
    file = get_map(lat, lon, zoom)
    await ctx.send(file=file)



bot.run('OTAxMzkzNzExNDQxNzcyNjA0.G5YQRm.TmuyTs47KDTEWHOdZ7qPVOYhTrz4e0iEP6XyvM')    
