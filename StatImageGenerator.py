from PIL import Image, ImageDraw, ImageFont
from Overwatch_stat_checker import heroes
import json

messagecontent = open("./MessageData/messagecontent.txt", "r")
messagecontent = messagecontent.read()

newmessage = messagecontent.split()
playername = newmessage[1]
if len(newmessage) >= 3:
    heroname = newmessage[2]
else:
    heroname = "All Heroes"

#Check if hero exists in dictionary
#If true, run program
ishero = False
for x in heroes.values():
    if x == heroname:
        ishero = True
    else:
        continue



if ishero:
    herofile = open("./PlayerData/" + playername + ".txt", "r")
    herofile = herofile.read()
    herofile = herofile.replace("'", '"')
    herofile = herofile.replace(" -", "")
    herofile = json.loads(herofile)
    # create an image
    out = Image.open("./Templates/"+ heroname.lower() +".png")

    # get a font
    # font Microsoft Sans Serif Almindelig
    fnt = ImageFont.truetype("./Fonts/configalt-bold.otf", 32)
    # get a drawing context
    d = ImageDraw.Draw(out)

    def insert_text_column_with_specifications(xcoord, ycoord, category, keysentence, secondarysentence):
        originalxcoord = xcoord
        for key, value in herofile[heroname][category].items():
            if keysentence in key:
                print(key, value)
                #Drawing the first key without "Best in Game"
                key = key.replace(keysentence, "")
                d.text((xcoord, ycoord), key, font=fnt, fill=(255, 255, 255))
                ycoord += 50
                #Drawing "Best in Game"
                d.text((xcoord, ycoord), " "+ keysentence + ":", font=fnt, fill=(255, 255, 255))
                xcoord += 326
                #Drawing the first value
                d.text((xcoord, ycoord), value, font=fnt, fill=(255, 255, 255), anchor="ra")
                ycoord += 50
                xcoord = originalxcoord
            else:
                if secondarysentence in key:
                    key = key.replace(secondarysentence, "")
                    leftoverkey = key
                    leftovervalue = value
        d.multiline_text((xcoord, ycoord), leftoverkey, font=fnt, fill=(255, 255, 255))
        ycoord += 50
        d.multiline_text((xcoord, ycoord), " " + secondarysentence + ":", font=fnt, fill=(255, 255, 255))
        xcoord += 326
        d.multiline_text((xcoord, ycoord), leftovervalue, font=fnt, fill=(255, 255, 255), anchor="ra")
        xcoord = 129
    def insert_text_column_auto(xcoord, ycoord, category):
        originalxcoord = xcoord
        linecounter = 0
        secondcounter = 0
        counter = 0
        nextline = False
        for key, value in herofile[heroname][category].items():
            for x in key:
                if nextline == True:
                    secondline = x
                    
                    
                if x == " ":
                    linecounter += 1
                    if linecounter == 3: 
                        nextline = True
                else:
                    if counter == 0:
                        firstline = x
                        counter += 1
                    elif counter == 1:
                        firstline = firstline + x
                    else:
                        if secondcounter == 0:
                            secondline = x
                            secondcounter += 1
                        else:
                            secondline = secondline + x

                    
            print(firstline,secondline)
            if keysentence in key:
                print(key, value)
                #Drawing the first key without "Best in Game"
                key = key.replace(keysentence, "")
                d.text((xcoord, ycoord), key, font=fnt, fill=(255, 255, 255))
                ycoord += 50
                #Drawing "Best in Game"
                d.text((xcoord, ycoord), " "+ keysentence + ":", font=fnt, fill=(255, 255, 255))
                xcoord += 326
                #Drawing the first value
                d.text((xcoord, ycoord), value, font=fnt, fill=(255, 255, 255), anchor="ra")
                ycoord += 50
                xcoord = originalxcoord
            else:
                if secondarysentence in key:
                    key = key.replace(secondarysentence, "")
                    leftoverkey = key
                    leftovervalue = value
        d.multiline_text((xcoord, ycoord), leftoverkey, font=fnt, fill=(255, 255, 255))
        ycoord += 50
        d.multiline_text((xcoord, ycoord), " " + secondarysentence + ":", font=fnt, fill=(255, 255, 255))
        xcoord += 326
        d.multiline_text((xcoord, ycoord), leftovervalue, font=fnt, fill=(255, 255, 255), anchor="ra")
        xcoord = 129


    ycoord = 628
    if heroname != "All Heroes":
        xcoord = 129
        for key, value in herofile[heroname]["Hero Specific"].items():
            if "Avg per 10 Min" in key:
                #Drawing the first key without "Avg per 10 min"
                key = key.replace("Avg per 10 Min", "")
                d.text((xcoord, ycoord), key, font=fnt, fill=(255, 255, 255))
                ycoord += 50
                #Drawing "Avg per 10 Min"
                d.text((xcoord, ycoord), " Avg per 10 Min:", font=fnt, fill=(255, 255, 255))
                #Drawing the first value
                xcoord += 326
                d.text((455, ycoord), value, font=fnt, fill=(255, 255, 255), anchor="ra")
                ycoord += 50
                xcoord = 129
            else:
                if "Best in Game" in key:
                    key = key.replace("Best in Game", "")
                    leftoverkey = key
                    leftovervalue = value
        d.multiline_text((xcoord, ycoord), leftoverkey, font=fnt, fill=(255, 255, 255))
        ycoord += 50
        d.multiline_text((xcoord, ycoord), " Best in Game:", font=fnt, fill=(255, 255, 255))
        xcoord += 326
        d.multiline_text((xcoord, ycoord), leftovervalue, font=fnt, fill=(255, 255, 255), anchor="ra")
        xcoord = 129
    insert_text_column_with_specifications(511,228,"Best", "Best in Game", "Most in Life")
    insert_text_column_auto(129, 228, "Combat")




# draw multiline text

out.save("test.png")
out.show()
