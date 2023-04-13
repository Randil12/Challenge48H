import discord
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help command", description="!ping test", color=discord.Color.blue())
    await ctx.channel.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.reply("pong")    

bot.run("OTAxMzkzNzExNDQxNzcyNjA0.G5YQRm.TmuyTs47KDTEWHOdZ7qPVOYhTrz4e0iEP6XyvM")