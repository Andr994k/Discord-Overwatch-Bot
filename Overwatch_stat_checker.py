import requests
from bs4 import BeautifulSoup

URL = "https://overwatch.blizzard.com/en-gb/career/Colaskink-2607/"

page = requests.get(URL)
#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

stats = soup.find_all(class_="category")

statlist = []

for stat in stats:
    statelement = stat.find(class_="stat-item")
    statelement.find_all("a", class_="name")

f = open("test2" + ".txt","w+")
f.write(str(statlist))
f.close()
print(statlist)
"""
souptext = soup.get_text()



f = open("souptext" + ".txt","w+")
f.write(str(souptext))
f.close()
"""