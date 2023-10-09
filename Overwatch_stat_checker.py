import requests
from bs4 import BeautifulSoup

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

#String to list converter
async def convert(string):
    li = list(string.split(","))
    return li

async def get_player_data(careername):

    URL = "https://overwatch.blizzard.com/en-gb/career/" + careername + "/"

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    
    #Make file of raw HTML data, mostly for showing
    f = open("./RawPlayerData/" + careername + " RAW.txt","w+")
    f.write(str(soup))
    f.close()

    stats = soup.find_all(class_="category")
    DataDict = {}
    for key, value in heroes.items():
        DataDict[value] = {}

    HeroCounter = 0
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
        statlist = await convert(statelement)
        for key in statlist:
            if key == "Hero Specific":
                HeroCounter += 1
            if (key == "Hero Specific") or (key == "Best") or (key == "Average") or (key == "Combat") or (key == "Assists") or (key == "Game") or (key == "Match Awards"):
                StatCounter = 0
            if StatCounter == 0:
                Title = key
                if HeroCounter < len(heroes):
                    DataDict[heroes[str(HeroCounter)]][Title] = {}
                StatCounter += 1
            else:
                if StatCounter == 1:
                    StatKey = key
                    StatCounter += 1
                else:
                    StatValue = key 
                    StatCounter = 1
                    if HeroCounter < len(heroes):
                        DataDict[heroes[str(HeroCounter)]][Title][StatKey] = StatValue

    f = open("./PlayerData/" + careername + ".txt","w+")
    f.write(f"{DataDict}")
    f.close()