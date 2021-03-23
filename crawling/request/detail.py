import requests
from bs4 import BeautifulSoup

raw = requests.get("https://soomgo.com/search/pro")
html = BeautifulSoup(raw.text, "html.parser")

container = html.select("div.search-pro--item")
num = 1