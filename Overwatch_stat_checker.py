import requests
from bs4 import BeautifulSoup

URL = "https://overwatch.blizzard.com/en-gb/career/Colaskink-2607/"

page = requests.get(URL)
#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.h1['class'].string)