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



DataDict = {}

Title = True
IsKey = False

for key in statlist:
    if Title == True:
        bing = key
        IsKey = True
        Title = False
    else:
        if IsKey == True:
            DataDict[key] = {}
            IsKey = False
        if IsKey == False:
            DataDict[key] = statlist[1:]
            IsKey = True
                    
print("\n")
print(DataDict)
























"""

# Get a list of the dictionary's items (key-value pairs)
items = list(fixedlist.items())

# Access the item at index 0
index = 0
key, value = items[index]

print(key, value)

#f = open("dict" + ".txt","w+")
#f.write(f"{fixedlist}")
#f.close()

"""