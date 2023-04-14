import plotly.express as px
import plotly.io as pio
import discord
from discord.ext import commands
import plotly.graph_objects as go



# Créer un bot Discord
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Définir une commande pour envoyer l'image
@bot.event
async def on_ready():
    print('Bot is ready')


@bot.command()
async def send_image(ctx,  lat: str, lon: str, zoom: int):


    fig = px.scatter_mapbox(lat=[lat], lon=[lon], zoom=zoom)  # zoom max 18 min 0
    fig.update_layout(mapbox_style='open-street-map')

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)
    )
    fig.add_trace(go.Scattermapbox(
        lat=[lat],
        lon=[lon],
        mode='markers',
        marker=dict(size=10, color='red', symbol='marker')
    ))

    # Enregistrer l'image au format PNG
    pio.write_image(fig, 'carte_lyon.png')

    # Charger le fichier d'image
    file = discord.File("carte_lyon.png", filename="carte_lyon.png")

    await ctx.send(file=file)
    

bot.run('OTAxMzkzNzExNDQxNzcyNjA0.G5YQRm.TmuyTs47KDTEWHOdZ7qPVOYhTrz4e0iEP6XyvM')    