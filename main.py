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
    file = discord.File("carte_lyon_modifiee.png", filename="carte_lyon_modifiee.png")

    await interation.response.send_message(file=file)

# @tree.command(name="activity", description="trouver une activité")
# async def self(interation: discord.Interaction, activité:typing.Literal["Bar"], 
#               restauration: typing.Optional[bool]=False, 
#               terrasse: typing.Optional[bool]=False):
#     await interation.response.send_message("ok")
   
@tree.command(name="help", description="Affiche l'aide pour les commandes 'activity' et 'activity2'")
async def help_command(interation: discord.Interaction):
    help_message = """
    **Aide pour les commandes 'activity' et 'activity2' :**

    `activity` : Localise une adresse pour une activité spécifique.

    Syntaxe : `/activity activité:Bar [restauration:bool] [terrasse:bool]`

    - `activité` (obligatoire) : Le type d'activité à localiser. Les options possibles sont : 'Bar'.
    - `option` (facultatif, exemple : terrasse, emporter, ...) : Option pour indiquer si le bar possede l'option choisie.

    `location` : Localise une adresse pour une autre activité.

    Syntaxe : `/location ville:str lieu : str`

    - `ville` (obligatoire) : Le nom de la ville ou chercher le lieu. Vous pouvez spécifier n'importe quelle chaîne de caractères.
    - `lieu` (facultatif) : Le nom du lieu à localiser. Vous pouvez spécifier n'importe quelle chaîne de caractères.
    """

    await interation.response.send_message(help_message)

bot.run('OTAxMzkzNzExNDQxNzcyNjA0.G5YQRm.TmuyTs47KDTEWHOdZ7qPVOYhTrz4e0iEP6XyvM')