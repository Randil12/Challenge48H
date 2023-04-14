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

@tree.command(name="locatebar", description="localise un nom de bar")
async def self(interation: discord.Interaction,ville:str):
    bar = BDDManager.get_bar_by_city(ville)
    print(bar)
    message = ""
    for i in bar[:120]:
        message += i + "\n"
    await interation.response.send_message(message)
    
@tree.command(name="activitybar", description="toutes les activités")
async def self(interation: discord.Interaction,name:str, city:Literal['lyon' , 'lille' , 'clermont-ferrand']):
    info = BDDManager.get_all_info_by_name_and_city(city , name)
    
    embed = discord.Embed(title=f'Bar : {name} sur {city}' , description=f'Terrasse : {info[0][2]}\n Restauration : {info[0][3]}\n Vente à emporté : {info[0][4]}\n Wifi gratuit : {info[0][5]}\n Diffusion de mathc : {info[0][6]}\n Air Climatisé : {info[0][7]}\n Acces au toilette handicapé : {info[0][8]}\n Billard : {info[0][9]}\n Fléchette :{info[0][10]}\n Babyfoot : {info[0][11]}\n Flipper : {info[0][12]}\n Concert et Musique live : {info[0][13]}\n DJ Mix : {info[0][14]}\n Chien accepté : {info[0][15]}\n Jeux de société : {info[0][16]}\n')
   
    await interation.response.send_message(embed=embed)


@tree.command(name="locate", description="localise une adresse et renvoie une carte")
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

    width, height = image.size

    draw = ImageDraw.Draw(image)

    center_x = width // 2
    center_y = height // 2
    radius = 5  # ajuster la taille du cercle si nécessaire
    draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill='red')
    image.save('carte_lyon_modifiee.png')


    file = discord.File("carte_lyon_modifiee.png", filename="carte_lyon_modifiee.png")

    await interation.response.send_message(file=file)
        

@tree.command(name="help", description="Affiche l'aide pour les commandes")
async def help_command(interation: discord.Interaction):
    help_message = """
    **Aide pour les commandes 'locatebar', 'locate' et 'locatesportplace' :**

    `locatebar` : localise un nom de bar

    Syntaxe : `/locatebar ville`

    - `ville` (obligatoire) : localise les bar dans la ville passer en parametre'.

    `locate` : localise une adresse et renvoie une carte

    Syntaxe : `/locate ville:str lieu : str`

    - `ville` (obligatoire) : Le nom de la ville ou chercher le lieu.
    - `lieu` (facultatif) : Le nom du lieu à localiser.

    `locatesportplace` : localise tout les sport

    Syntaxe : `/locatesportplace lieu : str`

    - `lieu` (obligatoire) : Le nom du lieu à localiser.

    `activitybar` : toutes les activités

    Syntaxe : `/activitybar city : str name : str`

    - `city` (obligatoire) : Le nom de la ville du lieu à localiser.
    - `name` (obligatoire) : Le nom du bar.
    """

    await interation.response.send_message(help_message)


l = BDDManager.get_all_place()

@tree.command(name="locatesportplace", description="localise tout les sport")

async def self(interation: discord.Interaction,lieu:Literal[tuple(l)]):
    lieu = BDDManager.get_name_by_place(lieu)
    message = ""
    for i in lieu[:50]:
        message += i + "\n"
    await interation.response.send_message(message)
    

bot.run('METTRE LE TOKEN')