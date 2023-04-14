import discord 
from discord import app_commands
from typing import List, Literal
from geopy.geocoders import Nominatim
import plotly.express as px
import plotly.io as pio
from PIL import Image, ImageDraw
import BDDManager
import asyncio


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
city = ""

@tree.command(name="locate", description="localise une adresse")
async def self(interation: discord.Interaction,ville:str , adresse:str = None):
    geolocator = Nominatim(user_agent="my_application")
    city = ville

    if adresse is None:
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
    image.save('carte_lyon.png')


    # Charger le fichier d'image
    file = discord.File("carte_lyon.png", filename="carte_lyon.png")

    await interation.response.send_message(file=file)
    

l = BDDManager.get_all_column()
l2 = l[2:]
@tree.command(name="activity", description="toutes les activités")

async def self(interation: discord.Interaction,name:Literal['Bar' , 'Sport'], option:Literal[tuple(l2)] , option2:Literal[tuple(l2)] , option3:Literal[tuple(l2)]):
    embedlist = []
    file = discord.File("carte_lyon.png", filename="carte_lyon.png")
    for i in l2:
        embed = discord.Embed(title="ID :" + str(i))
        
        embedlist.append(embed)
    
    for embed in embedlist:
        await interation.response.send_message(embed=embed , file=file)
        await asyncio.sleep(1)
        

    

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

@tree.command(name="multi_messages", description="Affiche l'aide pour les commandes 'activity' et 'activity2'")
async def self(interation: discord.Interaction):
    messageList = ['Oui' , 'NON' , 'BITE']
    for message in messageList:
        await interation.response.send_message(message)
        await asyncio.sleep(1)

bot.run('OTAxMzkzNzExNDQxNzcyNjA0.G5YQRm.TmuyTs47KDTEWHOdZ7qPVOYhTrz4e0iEP6XyvM')