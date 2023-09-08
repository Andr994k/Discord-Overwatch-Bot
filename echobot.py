import os
import discord
import requests
from bs4 import BeautifulSoup

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
        rem = contents[5:]
        reply = "Du sendte: " + rem
        await message.channel.send(reply)

    if contents.startswith("!reverse"):
        rem = contents[8:]
        reverse_rem = reverse(rem)
        reply = "Du sendte: " + reverse_rem
        await message.channel.send(reply)

    if contents.startswith("!yell"):
      rem = contents[5:]
      reply = rem + "!"
      await message.channel.send(reply)

    if contents.startswith("!owcareer"):
       global careername
       careername = contents[10:]
       URL = "https://overwatch.blizzard.com/en-gb/career/" + careername.replace("#","-") + "/"
       print(URL)
       page = requests.get(URL)
       soup = BeautifulSoup(page.content, "html.parser")
       soupstr = str(soup)
       
       f = open(careername + ".txt","w+")
       f.write(soupstr)
       f.close()
       await message.channel.send(file=discord.File(careername + ".txt"))
           
token = get_token()
client.run(token)

