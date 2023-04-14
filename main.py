import discord 
from discord.ext import commands
from discord import app_commands
import typing
from geopy.geocoders import Nominatim
from io import BytesIO
import io 
import folium
from selenium.webdriver.chrome.options import Options


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
async def self(interation: discord.Interaction,name:str , region: typing.Literal["EUW","EUNE","NA","BR","JP","KR","LA","LAS","OC","TR","RU"]):
    geolocator = Nominatim(user_agent="my_application")
    location = geolocator.geocode('La Feria Lyon')

    latitude, longitude = location.latitude, location.longitude
    map_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"


    map = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker(location=[latitude, longitude], popup='Lyon').add_to(map)

    # Save map as HTML
    
    embed = discord.Embed(title="Oui", description=f"[Click here for map]({map})", color=discord.Color.blue())
    #embed = discord.Embed(title="Oui", description=map_url, color=discord.Color.blue())
    names = region
    await interation.response.send_message(f"str à la con {region}" , embed=embed)


@tree.command(name="test", description="test")
async def self(interation: discord.Interaction,name:str):
    await interation.response.send_message(f'Oui + {name}')

bot.run('OTAxMzkzNzExNDQxNzcyNjA0.G5YQRm.TmuyTs47KDTEWHOdZ7qPVOYhTrz4e0iEP6XyvM')    