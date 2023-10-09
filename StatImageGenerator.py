from PIL import Image, ImageDraw, ImageFont
from Overwatch_stat_checker import heroes
import json
import textwrap
import os

async def image_generator(user, hero):

    #Check if hero exists in dictionary
    #If true, run program
    is_hero = False
    for x in heroes.values():
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
        out = Image.open("./Templates/"+ hero.lower() +".png")

        # get a font
        # font Microsoft Sans Serif Almindelig
        fnt = ImageFont.truetype("./Fonts/configalt-bold.ttf", 32)
        # get a drawing context
        d = ImageDraw.Draw(out)

        async def insert_text_column_auto(x_coord, y_coord, category):
            original_x_coord = x_coord
            element_counter = 0
            for key, value in hero_file[hero][category].items():
                if element_counter == 11:
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
                d.multiline_text((x_coord, y_coord), first_word, font=fnt, fill=(255, 255, 255))
                y_coord += 50
                d.multiline_text((x_coord, y_coord), second_word, font=fnt, fill=(255, 255, 255))
                x_coord += 326
                #Draw value
                d.text((x_coord, y_coord), value, font=fnt, fill=(255, 255, 255), anchor="ra")
                y_coord += 50
                x_coord = original_x_coord
                element_counter += 1

        y_coord = 628
        if hero != "All Heroes":
            x_coord = 129
            for key, value in hero_file[hero]["Hero Specific"].items():
                if "Avg per 10 Min" in key:
                    #Drawing the first key without "Avg per 10 min"
                    key = key.replace("Avg per 10 Min", "")
                    d.text((x_coord, y_coord), key, font=fnt, fill=(255, 255, 255))
                    y_coord += 50
                    #Drawing "Avg per 10 Min"
                    d.text((x_coord, y_coord), " Avg per 10 Min:", font=fnt, fill=(255, 255, 255))
                    #Drawing the first value
                    x_coord += 326
                    d.text((455, y_coord), value, font=fnt, fill=(255, 255, 255), anchor="ra")
                    y_coord += 50
                    x_coord = 129
                else:
                    if "Best in Game" in key:
                        key = key.replace("Best in Game", "")
                        leftover_key = key
                        leftover_value = value
            d.multiline_text((x_coord, y_coord), leftover_key, font=fnt, fill=(255, 255, 255))
            y_coord += 50
            d.multiline_text((x_coord, y_coord), " Best in Game:", font=fnt, fill=(255, 255, 255))
            x_coord += 326
            d.multiline_text((x_coord, y_coord), leftover_value, font=fnt, fill=(255, 255, 255), anchor="ra")
            x_coord = 129
        await insert_text_column_auto(511, 228, "Best")
        await insert_text_column_auto(911, 228, "Average")
        await insert_text_column_auto(1311, 228, "Assists")
        await insert_text_column_auto(1711, 228, "Combat")
        await insert_text_column_auto(2111, 228, "Game")
        d.text((30, 1390), "Stats retrieved from: https://overwatch.blizzard.com/en-gb/career/" + user + "/", font=fnt, fill=(255, 255, 255))
        fnt = ImageFont.truetype("./Fonts/configalt-bold.ttf", 80)
        d.text((550, 80), "Career-profile: " + user.replace("-", "#"), font=fnt, fill=(255, 255, 255))
    # If directory does not exist, create it
    if not os.path.exists("./PlayerHeroPosters/" + user):
        os.mkdir("./PlayerHeroPosters/" + user)

    out.save("./PlayerHeroPosters/" + user + "/" + hero + ".png")

#image_generator("Colaskink-2607", "Ana")