import discord
import os
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from WintonBotFunctions import get_ow_career, get_counter, randomize_role

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

#Load the .env file containing the token of our bot
load_dotenv()
TOKEN = os.getenv("TOKEN")

@bot.event
async def on_ready():
    print("Connected!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name = "ow_career")
@app_commands.describe(user = "The user to get the career of", hero = "The hero to get the stats of")
async def ow_career(interaction: discord.Interaction, user: str, hero: str = "All Heroes"):
    await interaction.response.defer()
    await get_ow_career(interaction, user, hero)

@bot.tree.command(name = "counter")
@app_commands.describe(hero = "The hero you want to counter")
async def counter(interaction: discord.Interaction, hero: str):
    await interaction.response.defer()
    await get_counter(interaction, hero)

@bot.tree.command(name = "random_hero")
@app_commands.describe(role = "The role you want a random hero from", roulette = "Whether or not you want to generate a full team of heroes, the chosen role will have no impact")
async def random_hero(interaction: discord.Interaction, role: str = "all roles", roulette: bool = False):
    await interaction.response.defer()
    await randomize_role(interaction, role, roulette)

bot.run(TOKEN)