import discord
from discord import app_commands
from discord.ext import commands

from WintonBotFunctions import help, echo, reverse, yell, get_ow_career

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

TOK_FILE = "token.txt"

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@bot.event
async def on_ready():
    print("Connected!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)


@bot.event
async def on_message(message):
    contents = message.content
    channel = message.channel
    
    if contents.startswith("!Help"):
        await help(channel)
    
    if contents.startswith("!echo"):
        await echo(channel, contents)
        
    if contents.startswith("!reverse"):
        await reverse(channel, contents)

    if contents.startswith("!yell"):
        await yell(channel, contents)


@bot.tree.command(name = "ow_career")
@app_commands.describe(user = "The user to get the career of", hero = "The hero to get the stats of")
async def ow_career(interaction: discord.Interaction, user: str, hero: str = "All Heroes"):
    await interaction.response.defer()
    await get_ow_career(interaction, user, hero)
            
token = get_token()
bot.run(token)

