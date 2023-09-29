from PIL import Image, ImageDraw, ImageFont
from Overwatch_stat_checker import heroes

messagecontent = open("./MessageData/messagecontent.txt", "r")
messagecontent = messagecontent.read()

newmessage = messagecontent.split()
newmessage = newmessage[2]
print(heroes.values())
for x in heroes.values():
    if x == newmessage:
        print("yes")
    else:
        print("no")

"""
# create an image
out = Image.open("./Templates/Ana.png")

# get a font
# font Microsoft Sans Serif Almindelig
fnt = ImageFont.truetype("./Fonts/configalt-bold.otf", 40)
# get a drawing context
d = ImageDraw.Draw(out)

wordlist = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten"}


ycoord = 10
for number, word in wordlist.items():
    d.multiline_text((10, ycoord), number + "  " + word, font=fnt, fill=(0, 0, 0))
    ycoord += 40

# draw multiline text

out.save("test.png")
out.show()
"""