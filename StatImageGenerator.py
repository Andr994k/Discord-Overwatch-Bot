from PIL import Image, ImageDraw, ImageFont
from Overwatch_stat_checker import herodict
import json
import textwrap
import os

async def image_generator(user, hero):
    hero = hero.lower()
    #Check if hero exists in dictionary
    #If true, run program
    is_hero = False
    for x in herodict.values():
        if x == hero:
            is_hero = True
        else:
            continue

    if is_hero:
        hero_file = open("./PlayerData/" + user + ".txt", "r")
        hero_file = hero_file.read()
        hero_file = hero_file.replace("'", '"')
        hero_file = hero_file.replace(" -", "")
        hero_file = json.loads(hero_file)
        # create an image
        image = Image.open("./Templates/"+ hero +".png")

        # get a font
        # font Microsoft Sans Serif Almindelig
        fnt = ImageFont.truetype("./Fonts/configalt-bold.ttf", 32)
        # get a drawing context
        d = ImageDraw.Draw(image)

        async def insert_text_column_auto(x_coord, y_coord, category, max_elements):
            original_x_coord = x_coord
            element_counter = 0
            for key, value in hero_file[hero][category].items():
                if element_counter == max_elements:
                    break
                #Using textwrap library to automatically break up string if too long
                if len(key) > 18:
                    key = textwrap.wrap(key, width=18, break_long_words=False)
                    if key[1] in key:
                        first_word = key[0]
                        second_word = " " + key[1]

                    #Convert back to string from list
                    key = (str(key))
                    key = key.replace(",", "\n")
                    key = key.replace("[", "")
                    key = key.replace("]", "")
                    key = key.replace("'", "")
                else:
                    first_word = key
                    second_word = ""
                #Draw key
                d.text((x_coord, y_coord), first_word, font=fnt, fill=(255, 255, 255))
                y_coord += 50
                d.text((x_coord, y_coord), second_word, font=fnt, fill=(255, 255, 255))
                x_coord += 326
                #Draw value
                d.text((x_coord, y_coord), value, font=fnt, fill=(255, 255, 255), anchor="ra")
                y_coord += 50
                x_coord = original_x_coord
                element_counter += 1

        if hero != "all heroes":
            await insert_text_column_auto(129, 628, "Hero Specific", 7)
        #Insert text columns for each category
        await insert_text_column_auto(511, 228, "Best", 11)
        await insert_text_column_auto(911, 228, "Average", 11)
        await insert_text_column_auto(1311, 228, "Assists", 11)
        await insert_text_column_auto(1711, 228, "Combat", 11)
        await insert_text_column_auto(2111, 228, "Game", 11)

        #insert source text
        d.text((30, 1390), "Stats retrieved from: https://overwatch.blizzard.com/en-gb/career/" + user + "/", font=fnt, fill=(255, 255, 255))
        d.text((2530, 1390), "Career-profile: " + user.replace("-", "#"), font=fnt, fill=(255, 255, 255), anchor="ra")
        #insert title text
        fnt = ImageFont.truetype("./Fonts/configalt-bold.ttf", 80)
        d.text((550, 80), hero.title(), font=fnt, fill=(255, 255, 255))

    # If directory does not exist for player, create it
    if not os.path.exists("./PlayerHeroPosters/" + user):
        os.mkdir("./PlayerHeroPosters/" + user)

    #save image inside player folder
    image.save("./PlayerHeroPosters/" + user + "/" + hero + ".png")