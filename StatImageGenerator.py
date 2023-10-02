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
    print(herofile)
    herofile = json.loads(herofile)
    
    # create an image
    out = Image.open("./Templates/"+ heroname.lower() +".png")

    # get a font
    # font Microsoft Sans Serif Almindelig
    fnt = ImageFont.truetype("./Fonts/configalt-bold.otf", 35)
    # get a drawing context
    d = ImageDraw.Draw(out)



    ycoord = 578
    if heroname != "All Heroes":
        for key in herofile[heroname]["Hero Specific"]:
            if "Avg per 10 Min" in key:
                key = key.replace("Avg per 10 Min", "")
                d.multiline_text((129, ycoord), key + "\n" + "Avg per 10 Min", font=fnt, fill=(255, 255, 255))
                ycoord += 100
            else:
                leftovers = key
        d.multiline_text((130, ycoord), leftovers, font=fnt, fill=(255, 255, 255))



    # draw multiline text

    out.save("test.png")
    out.show()
