import discord
from WintonBotFunctions import echo, reverse, yell, owcareer

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@client.event
async def on_ready():
    print("Connected!")

def reverse(s):
    return s[::-1]

@client.event
async def on_message(message):
    contents = message.content
    
    if contents.startswith("!echo"):
        echo()

    if contents.startswith("!reverse"):
        reverse()

    if contents.startswith("!yell"):
        yell()

    if contents.startswith("!owcareer"):
        owcareer()
           
token = get_token()
client.run(token)

