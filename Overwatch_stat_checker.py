import requests
from bs4 import BeautifulSoup

user = "gedegustav-2101"

URL = "https://overwatch.blizzard.com/en-gb/career/" + user + "/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

stats = soup.find_all(class_="category")

statlist = []

for stat in stats:
    statelement = stat.find(class_="content")
    statelement = statelement.contents
    statelement = str(statelement)
    statelement = str(statelement.replace('<div class="header"><p>', ""))
    statelement = str(statelement.replace('</p><p class="value">', ""))
    statelement = str(statelement.replace('</p></div>', ""))
    statelement = str(statelement.replace('<div class="stat-item"><p class="name">', ""))
    statelement = str(statelement.replace("\\", ""))
    statelement = str(statelement.replace("\'", ""))
    statelement = str(statelement.replace("'", ""))
    statlist.append(statelement)


stringcounter = 0
fixedlist = {}
string = ""
numberstringcounter = 0
for key in statlist:
    for value in key:
        if value == ",":
            stringcounter += 1
            if stringcounter == 1:
                Title = string
                Title = Title.replace("[", "")
                string = ""
            if stringcounter >= 2:
                string = string.replace(", ", "")
                fixedlist[string] = numberstorage
                string = ""
                numberstorage = ""
                numberstringcounter = 0
        if value.isdigit() or value == ":":
            if numberstringcounter == 0:
                numberstorage = value
                numberstringcounter += 1
            else:
                numberstorage = (numberstorage + value)
        if value == "]":
            stringcounter = 0
        else:
            if value.isdigit() == False:
                string = (string + value)

"""
# Get a list of the dictionary's items (key-value pairs)
items = list(fixedlist.items())

# Access the item at index 0
index = 0
key, value = items[index]

print(key, value)
"""
f = open("dict" + ".txt","w+")
f.write(f"{fixedlist}")
f.close()