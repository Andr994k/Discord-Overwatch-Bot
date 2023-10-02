from PIL import Image, ImageDraw, ImageFont
from Overwatch_stat_checker import heroes
import json

messagecontent = open("./MessageData/messagecontent.txt", "r")
messagecontent = messagecontent.read()

newmessage = messagecontent.split()
playername = newmessage[1]
heroname = newmessage[2]
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
    counter = 0
    ycoord = 578
    if heroname != "All Heroes":
        for key, value in herofile[heroname]["Hero Specific"].items():
            print(key, value)
            if "Avg per 10 Min" in key:
                #Drawing the first key without "Avg per 10 min"
                key = key.replace("Avg per 10 Min", "")
                d.text((129, ycoord), key, font=fnt, fill=(255, 255, 255))
                ycoord += 50
                #Drawing "Avg per 10 Min"
                d.text((129, ycoord), " Avg per 10 Min:", font=fnt, fill=(255, 255, 255))
                #Drawing the first value
                d.text((400, ycoord), value, font=fnt, fill=(255, 255, 255))
                ycoord += 50
            else:
                if counter == 0:
                    leftoverkey = key
                    leftovervalue = value
                    counter +=1
                    
        d.multiline_text((130, ycoord), leftoverkey, font=fnt, fill=(255, 255, 255))
        d.multiline_text((400, ycoord), leftovervalue, font=fnt, fill=(255, 255, 255))


    # draw multiline text

    out.save("test.png")
    out.show()
