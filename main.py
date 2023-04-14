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
from PIL import Image, ImageDraw
import plotly.graph_objects as go


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

@tree.command(name="locate", description="localise une adresse")
async def self(interation: discord.Interaction,ville:str , adresse:str):
    geolocator = Nominatim(user_agent="my_application")
    if(adresse == None):
        location = geolocator.geocode(f"{ville}")
    else : 
        location = geolocator.geocode(f"{ville} {adresse}")    

    latitude, longitude = location.latitude, location.longitude

    
    fig = px.scatter_mapbox(lat=[latitude], lon=[longitude], zoom=15)  # zoom max 18 min 0
    
    fig.update_layout(mapbox_style='open-street-map')

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)
    )
    
    # Enregistrer l'image au format PNG
    pio.write_image(fig, 'carte_lyon.png')
    image = Image.open('carte_lyon.png')

    # Obtenir les dimensions de l'image
    width, height = image.size

    # Créer un objet ImageDraw pour dessiner sur l'image
    draw = ImageDraw.Draw(image)

    # Dessiner un cercle rouge au centre de l'image
    center_x = width // 2
    center_y = height // 2
    radius = 5  # ajuster la taille du cercle si nécessaire
    draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill='red')
    image.save('carte_lyon_modifiee.png')


    # Charger le fichier d'image
    file = discord.File("carte_lyon.png", filename="carte_lyon.png")

    await interation.response.send_message(file=file)


@tree.command(name="test", description="test")
async def self(interation: discord.Interaction,name:str):
    await interation.response.send_message(f'Oui + {name}')

bot.run('OTAxMzkzNzExNDQxNzcyNjA0.G5YQRm.TmuyTs47KDTEWHOdZ7qPVOYhTrz4e0iEP6XyvM')