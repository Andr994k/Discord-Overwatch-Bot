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
    li = list(string.split(","))
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
    "0": "All Heroes",
    "1": "Ana",
    "2": "Ashe",
    "3": "Baptiste",
    "4": "Bastion",
    "5": "Brigitte",
    "6": "Cassidy",
    "7": "D.va",
    "8": "Doomfist",
    "9": "Echo",
    "10": "Genji",
    "11": "Hanzo",
    "12": "Illari",
    "13": "Junker Queen",
    "14": "Junkrat",
    "15": "Kiriko",
    "16": "Lifeweaver",
    "17": "Lucio",
    "18": "Mei",
    "19": "Mercy",
    "20": "Moira",
    "21": "Orisa",
    "22": "Pharah",
    "23": "Ramattra",
    "24": "Reaper",
    "25": "Reinhardt",
    "26": "Roadhog",
    "27": "Sigma",
    "28": "Sojourn",
    "29": "Soldier: 76",
    "30": "Sombra",
    "31": "Symmetra",
    "32": "Törbjorn",
    "33": "Tracer",
    "34": "Widowmaker",
    "35": "Winston",
    "36": "Wrecking Ball",
    "37": "Zarya",
    "38": "Zenyatta"
}

DataDict = {}
for key in heroes:
    DataDict[key] = {}


#Make a dictionary that contains the dictionary statlist, each character 
#has their own statlist, so it is easily accessed
#For example, the structure could be {HeroName: {Title: {Key: Value}}}

print(DataDict)
HeroCounter = -1
StatCounter = 0
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

    for key in statlist:
        if key == "Best":
            HeroCounter += 1
        if (key == "Best") or (key == "Average") or (key == "Combat") or (key == "Assists") or (key == "Game") or (key == "Match Awards"):
            StatCounter = 0
        if StatCounter == 0:
            Title = key
            StatCounter += 1
        else:
            if StatCounter == 1:
                StatKey = key
                StatCounter += 1
            else:
                StatValue = key 
                StatCounter = 1
                if HeroCounter < len(heroes):
                    DataDict[str(HeroCounter)][Title] = {StatKey: StatValue}

print(DataDict)





"""
    for key in statlist:
        print(key)
        if (key == "Best") or (key == "Average") or (key == "Combat") or (key == "Assists") or (key == "Game") or (key == "Match Awards"):
            Title = key
            if Title in fixedlist.keys():
                numbercounter =+ 1
                hero = heroes[numbercounter]
                fixedlist[Title + hero] = Title + hero
                #Things to do:
            else:
                fixedlist[Title + 0] = Title + 0
        elif not key.isdigit():
            if counter == 0:
                statKey = key
            else:
                statKey = (statKey + key)
                counter = 1
        else:
            Value = key
            counter = 0
            fixedlist[statKey] = Value
            """

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
#f = open("dict" + ".txt","w+")
#f.write(f"{fixedlist}")
#f.close()