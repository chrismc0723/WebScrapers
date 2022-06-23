from bs4 import BeautifulSoup
import requests
import re

search_term = input("Input: ")

url = "https://www.marvel.com/search"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

page_text = doc.find(class_="pagination")
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

for page in range(0, pages + 20):
    url = f"https://www.marvel.com/search?limit=20&query={search_term}&offset={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    ul = doc.find(class_="search-list__cards")
    items = ul.find_all(text=re.compile(search_term))

    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue

        link = parent['href']
        next_parent = item.find_parent(class_="mvl-card__search-wrapper--featured")
        print(item)
        print(link)

