import requests
from bs4 import BeautifulSoup
import config

url = config.URL
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
elements = soup.find_all(['p', 'h2','h1'])
with open("output.html", "w", encoding="utf-8") as file:
    for element in elements:
        file.write(element.get_text(strip=True) + "\n\n")

