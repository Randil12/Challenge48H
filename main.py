import discord 
from discord.ext import commands
from discord import app_commands
import typing
from geopy.geocoders import Nominatim
from io import BytesIO
import io 
import folium
from selenium.webdriver.chrome.options import Options
import plotly.express as px
import plotly.io as pio


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
names = ""

def create_map(lat, lon):
    m = folium.Map(location=[lat, lon], zoom_start=13)
    return m

@tree.command(name="locate", description="get basic rank infos")
async def self(interation: discord.Interaction,ville:str , adresse:str):
    geolocator = Nominatim(user_agent="my_application")
    location = geolocator.geocode(f'{ville} {adresse}')

    latitude, longitude = location.latitude, location.longitude

    
    fig = px.scatter_mapbox(lat=[latitude], lon=[longitude], zoom=15)  # zoom max 18 min 0
    fig.update_layout(mapbox_style='open-street-map')

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)
    )
    

    # Enregistrer l'image au format PNG
    pio.write_image(fig, 'carte_lyon.png')

    # Charger le fichier d'image
    file = discord.File("carte_lyon.png", filename="carte_lyon.png")

    await interation.response.send_message(file=file)


bot.run('OTAxMzkzNzExNDQxNzcyNjA0.G5YQRm.TmuyTs47KDTEWHOdZ7qPVOYhTrz4e0iEP6XyvM')