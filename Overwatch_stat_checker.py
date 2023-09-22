import requests
from bs4 import BeautifulSoup

user = "gedegustav-2101"

URL = "https://overwatch.blizzard.com/en-gb/career/" + user + "/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

stats = soup.find_all(class_="category")

fixedlist = {}

#String to list converter
def Convert(string):
    li = list(string.split(" "))
    return li

herolist = ["Ana", "Ashe", "Baptiste", "Bastion", "Brigitte", "Cassidy",
             "D.va", "Doomfist", "Echo", "Genji", "Hanzo", "Illari",
               "Junker Queen", "Junkrat", "Kiriko", "Lifeweaver",
                 "Lucio", "Mei", "Mercy", "Moira", "Orisa",
                   "Pharah", "Ramattra", "Reaper", "Reinhardt",
                     "Roadhog", "Sigma", "Sojourn", "Soldier: 76",
                       "Sombra", "Symmetra", "Törbjorn", "Tracer",
                         "Widowmaker", "Winston", "Wrecking Ball", "Zarya", "Zenyatta"]

heroes = {
    "0": "Ana",
    "1": "Ashe",
    "2": "Baptiste",
    "3": "Bastion",
    "4": "Brigitte",
    "5": "Cassidy",
    "6": "D.va",
    "7": "Doomfist",
    "8": "Echo",
    "9": "Genji",
    "10": "Hanzo",
    "11": "Illari",
    "12": "Junker Queen",
    "13": "Junkrat",
    "14": "Kiriko",
    "15": "Lifeweaver",
    "16": "Lucio",
    "17": "Mei",
    "18": "Mercy",
    "19": "Moira",
    "20": "Orisa",
    "21": "Pharah",
    "22": "Ramattra",
    "23": "Reaper",
    "24": "Reinhardt",
    "25": "Roadhog",
    "26": "Sigma",
    "27": "Sojourn",
    "28": "Soldier: 76",
    "29": "Sombra",
    "30": "Symmetra",
    "31": "Törbjorn",
    "32": "Tracer",
    "33": "Widowmaker",
    "34": "Winston",
    "35": "Wrecking Ball",
    "36": "Zarya",
    "37": "Zenyatta"
}

for stat in stats:
    statelement = stat.find(class_="content")
    statelement = statelement.contents
    statelement = str(statelement)
    statelement = str(statelement.replace('<div class="header"><p>', ""))
    statelement = str(statelement.replace('</p><p class="value">', ","))
    statelement = str(statelement.replace('</p></div>', ""))
    statelement = str(statelement.replace('<div class="stat-item"><p class="name">', ""))
    statelement = str(statelement.replace("\\", ""))
    statelement = str(statelement.replace("\'", ""))
    statelement = str(statelement.replace("[", ""))
    statelement = str(statelement.replace("]", ""))
    statelement = (statelement.replace("'", ""))
    statlist = Convert(statelement)
    print(statlist)
    for key in statlist:
        print(key)
        if (key == "Best") or (key == "Average") or (key == "Combat") or (key == "Assists") or (key == "Game") or (key == "Match Awards"):
            Title = key
            if Title in fixedlist.keys():
                numbercounter =+ 1
                hero = heroes[numbercounter]
                fixedlist[Title + hero] = Title + hero
                #Things to do:
                #Make a dictionary that contains the dictionary statlist, each character has their own statlist, so it is easily accessed
                #For example, the structure could be {HeroName: {Title: {Key: Value}}}
            else:
                fixedlist[Title + 0] = Title + 0
        elif not key.isdigit():
            if counter == 0:
                Key = key
            else:
                statKey = (statKey + key)
                counter = 1
        else:
            Value = key
            counter = 0
            fixedlist[Key] = Value
    print(statelement)

"""
counter = 0
for key in statlist:
    if (key == "Best") or (key == "Average") or (key == "Combat") or (key == "Assists") or (key == "Game") or (key == "Match Awards") or (key == "Hero Specific"):
        Title = key
        if Title in fixedlist.keys():
            fixedlist[Title] = Title
    elif counter == 0:
        Key = key
        counter = 1
    elif counter == 1:
        Value = key
        counter = 0
        fixedlist[Key] = Value
   """ 

#print(fixedlist)

"""
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
            string = (string + value)
            #if value.isdigit() == False:
"""            
            



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