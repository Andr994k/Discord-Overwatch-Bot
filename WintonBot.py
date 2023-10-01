import discord
from WintonBotFunctions import help, echo, reverse, yell, owcareer

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


@client.event
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

    if contents.startswith("!owcareer"):
        await owcareer(channel, contents)
        f = open("./MessageData/messagecontent.txt","w+")
        f.write(contents)
        f.close()
            
token = get_token()
client.run(token)

