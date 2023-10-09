import discord
from Overwatch_stat_checker import get_player_data
from StatImageGenerator import image_generator

async def get_ow_career(interaction: discord.Interaction, user, hero):
    user = user.replace("#", "-")
    await get_player_data(user)
    await image_generator(user, hero)
    image = discord.File("./PlayerHeroPosters/" + user + "/" + hero + ".png")
    await interaction.followup.send(file=image)
    