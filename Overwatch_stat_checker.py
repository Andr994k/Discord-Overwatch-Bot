import requests
from bs4 import BeautifulSoup

user = "NL2C-2193"

URL = "https://overwatch.blizzard.com/en-gb/career/" + user + "/"

page = requests.get(URL)
#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

stats = soup.find_all(class_="category")

statlist = []

for stat in stats:
    statelement = stat.find(class_="stat-item")
    statelement.find_all("a", class_="name")
    statelement = str(statelement)[39:]    
    statelement = statelement[:-10]
    statelement = statelement.split('</p><p class="value">')
    statlist.append(statelement)

f = open(user + ".txt","w+")
f.write(str(statlist))
f.close()
print(statlist)
"""
souptext = soup.get_text()



f = open("souptext" + ".txt","w+")
f.write(str(souptext))
f.close()
"""