from bs4 import BeautifulSoup
import requests
import re

user_input = input("What Character: ")

url = f"https://www.marvel.com/search?limit=20&query={user_input}&offset=0"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

div = doc.find(class_="flex-col-auto two-column__content")
items = div.find_all(text=re.compile(user_input))

for item in items:
    parent = item.parent
    if parent.name != "a":
        continue

    link = parent['href']
    next_parent = item.find_parent(class_="mvl-card__search-wrapper--featured")
    name = next_parent.find(class_="card-body__headline")
    print(name)
    print(link)
