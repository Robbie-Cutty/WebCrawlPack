import requests
from bs4 import BeautifulSoup
import config

url = config.URL



response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
file_name = 'output.html'
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
