import discord
from Overwatch_stat_checker import Everything

def reversemessage(s):
    return s[::-1]

async def help(channel):
    await channel.send(file=discord.File("./Templates/!help image (den er ikke done, så du må ikke være ond andreas. jeg skal nok gøre den flot, på et tidspunkt).png"))

async def echo(channel, contents):
    rem = contents[5:]
    reply = "Du sendte: " + rem
    await channel.send(reply)

async def reverse(channel, contents):
    rem = contents[8:]
    reverse_rem = reversemessage(rem)
    reply = "Du sendte: " + reverse_rem
    await channel.send(reply)

async def yell(channel, contents):
    rem = contents[5:]
    reply = rem + "!"
    await channel.send(reply)

async def owcareer(channel, contents):
    global careername
    careername = contents[10:]
    careername = careername.replace("#", "-")
    careername = careername.replace(" ", "")
    Everything(careername)
    await channel.send(file=discord.File("./PlayerData/"+ careername + ".txt"))
    