import requests
from bs4 import BeautifulSoup

#String to list converter
async def convert(string):
    li = list(string.split(","))
    return li

herodict = {}

async def get_player_data(careername):

    URL = "https://overwatch.blizzard.com/en-gb/career/" + careername + "/"

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    
    #Make file of raw HTML data, mostly for showing
    f = open("./RawPlayerData/" + careername + " RAW.txt","w+")
    f.write(str(soup))
    f.close()
    
    #Updating the heroes list to match the one on the website
    herodata = soup.find_all(class_="Profile-heroSummary--header")
    herodata = herodata[2]
    herodata = str(herodata)
    herodata = str(herodata.replace('<div class="Profile-heroSummary--header"><h2 class="Profile-heroSummary--heading">Career Stats</h2><select class="Profile-dropdown" data-dropdown-id="hero-dropdown" data-js="hero-select" is="blz-dropdown"><option option-id=',""))
    herodata = str(herodata.replace('</option><option option-id=',","))
    herodata = str(herodata.replace(' value=',","))
    herodata = str(herodata.replace('>',""))
    herodata = str(herodata.replace('</option</select</div',""))
    herodata = str(herodata.replace('"',""))
    herodata = str(herodata.replace('ö',"o"))
    herodata = str(herodata.replace('ú',"u"))
    herodata = herodata.lower()
    herodata = await convert(herodata)
    herodata = herodata[::2]
    index = 0
    for key in herodata:
        herodict[str(index)] = key
        index += 1

    #Create empty dictionaries in datadict to be filled with stats
    stats = soup.find_all(class_="category")
    DataDict = {}
    for key, value in herodict.items():
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
                if HeroCounter < len(herodict):
                    DataDict[herodict[str(HeroCounter)]][Title] = {}
                StatCounter += 1
            else:
                if StatCounter == 1:
                    StatKey = key
                    StatCounter += 1
                else:
                    StatValue = key 
                    StatCounter = 1
                    if HeroCounter < len(herodict):
                        DataDict[herodict[str(HeroCounter)]][Title][StatKey] = StatValue

    f = open("./PlayerData/" + careername + ".txt","w+")
    f.write(f"{DataDict}")
    f.close()