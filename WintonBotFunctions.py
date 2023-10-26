import discord
import random
from Overwatch_stat_checker import get_player_data
from StatImageGenerator import image_generator
from VariousData import counters_data, TankList, DPSList, SuppList

async def get_ow_career(interaction: discord.Interaction, user, hero):
    user = user.replace("#", "-")
    await get_player_data(user)
    await image_generator(user, hero)
    image = discord.File("./PlayerHeroPosters/" + user + "/" + hero + ".png")
    await interaction.followup.send(file=image)

async def get_counter(interaction: discord.Interaction, hero):
    hero = hero.lower()
    if hero in counters_data:
        response = counters_data[hero]
        await interaction.followup.send(response)
    else:
        await interaction.followup.send("Incorrect input, no special characters like ú and ö are needed in the heroname, just use u and o instead")

async def randomize_role(interaction: discord.Interaction, role, roulette):
    rolenumber = "none"
    if roulette != True:
        if role == "all roles":
            rolenumber = random.randint(0,2)
        if role == "tank" or rolenumber == 0:
            await interaction.followup.send("**Your hero is: **" + random.choice(TankList))
        if role == "dps" or role == "damage" or rolenumber == 1:
            await interaction.followup.send("**Your hero is: **" + random.choice(DPSList))
        if role == "support" or role == "healer" or role == "supp" or rolenumber == 2:
            await interaction.followup.send("**Your hero is: **" + random.choice(SuppList))
    else:
        await interaction.followup.send("**__Random Roulettte:__**" + "\n**Tank**: "+random.choice(TankList) + "\n**DPS**: "+random.choice(DPSList) + "\n**DPS**: "+random.choice(DPSList) + "\n**Support**: "+random.choice(SuppList) + "\n**Support**: "+random.choice(SuppList))