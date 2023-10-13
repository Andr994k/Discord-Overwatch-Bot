import requests
from bs4 import BeautifulSoup

heroes = {
    "0": "all heroes",
    "1": "ana",
    "2": "ashe",
    "3": "baptiste",
    "4": "bastion",
    "5": "brigitte",
    "6": "cassidy",
    "7": "d.va",
    "8": "doomfist",
    "9": "echo",
    "10": "genji",
    "11": "hanzo",
    "12": "illari",
    "13": "junker queen",
    "14": "junkrat",
    "15": "kiriko",
    "16": "lifeweaver",
    "17": "lucio",
    "18": "mei",
    "19": "mercy",
    "20": "moira",
    "21": "orisa",
    "22": "pharah",
    "23": "ramattra",
    "24": "reaper",
    "25": "reinhardt",
    "26": "roadhog",
    "27": "sigma",
    "28": "sojourn",
    "29": "soldier 76",
    "30": "sombra",
    "31": "symmetra",
    "32": "torbjorn",
    "33": "tracer",
    "34": "widowmaker",
    "35": "winston",
    "36": "wrecking ball",
    "37": "zarya",
    "38": "zenyatta"
}

#String to list converter
def convert(string):
    li = list(string.split(","))
    return li


def get_player_data(careername):

    URL = "https://overwatch.blizzard.com/en-gb/career/" + careername + "/"

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    
    #Make file of raw HTML data, mostly for showing
    f = open("./RawPlayerData/" + careername + " RAW.txt","w+")
    f.write(str(soup))
    f.close()
    #Updating the heroes list to match the one on the website
    heroesdata = soup.find_all(class_="Profile-heroSummary--header")
    heroesdata = heroesdata[2]
    heroesdata = str(heroesdata)
    heroesdata = str(heroesdata.replace('<div class="Profile-heroSummary--header"><h2 class="Profile-heroSummary--heading">Career Stats</h2><select class="Profile-dropdown" data-dropdown-id="hero-dropdown" data-js="hero-select" is="blz-dropdown"><option option-id=',""))
    heroesdata = str(heroesdata.replace('</option><option option-id=',","))
    heroesdata = str(heroesdata.replace(' value=',","))
    heroesdata = str(heroesdata.replace('>',""))
    heroesdata = str(heroesdata.replace('</option</select</div',""))
    heroesdata = str(heroesdata.replace('"',""))
    datanumber = 1
    heroesdata = convert(heroesdata)
    for key in heroesdata[datanumber]:
        for character in key:
            if character.isdigit() or character == '"':
                continue
            else:
                print(character)
                key[] = key.replace(character,"")
    datanumber += 2
    print(heroesdata)
    h = open("Heroesdatatest.txt","w+")
    h.write(f"{heroesdata}")
    h.close()

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
        statlist = convert(statelement)
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

get_player_data("Colaskink-2607")