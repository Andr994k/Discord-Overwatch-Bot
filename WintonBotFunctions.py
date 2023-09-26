import discord
from Overwatch_stat_checker import Everything

async def echo():
    rem = contents[5:]
    reply = "Du sendte: " + rem
    await message.channel.send(reply)


async def reverse():
    rem = contents[8:]
    reverse_rem = reverse(rem)
    reply = "Du sendte: " + reverse_rem
    await message.channel.send(reply)

async def yell():
    rem = contents[5:]
    reply = rem + "!"
    await message.channel.send(reply)

async def owcareer():
    global careername
    careername = contents[10:]
    careername = careername.replace("#", "-")
    careername = careername.replace(" ", "")
    Everything(careername)
    await message.channel.send(file=discord.File(careername + ".txt"))
    