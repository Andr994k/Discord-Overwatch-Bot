import requests
from bs4 import BeautifulSoup

user = "gedegustav-2101"

URL = "https://overwatch.blizzard.com/en-gb/career/" + user + "/"

page = requests.get(URL)
#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

stats = soup.find_all(class_="category")

statlist = []

for stat in stats:
    statelement = stat.find(class_="content")
    statelement = statelement.contents
    statelement = str(statelement)
    statelement = str(statelement.split('<div class="header"><p>'))
    statelement = str(statelement.split('</p><p class="value">'))
    statelement = str(statelement.split('</p></div>'))
    statelement = str(statelement.split('<div class="stat-item"><p class="name">'))
    raw = "\\"
    print(raw)
    statelement = str(statelement.replace(raw, ""))
    statelement = str(statelement.replace("\'", ""))
    statelement = str(statelement.replace("'", ""))
    statelement = str(statelement.replace(",", ""))
    statlist.append(statelement)


f = open(user + ".py","w+")
f.write(str(statlist))
f.close()
print(statlist)

"""
souptext = soup.get_text()



f = open("souptext" + ".txt","w+")
f.write(str(souptext))
f.close()
"""