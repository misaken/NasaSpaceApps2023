#main.py
from bs4 import BeautifulSoup
import requests

query = "mars weather"

url = "https://www.google.com/search?q=" + query
url = "http://www.google.com/"
url = "https://data.nasa.gov/"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

print(soup)
search_input = soup.find("input", {"name": "q"})
search_input["value"] = query
print(soup.prettify)