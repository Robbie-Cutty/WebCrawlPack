import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import config
os.makedirs("images", exist_ok=True)
url = config.URL
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
soup = BeautifulSoup(requests.get(url, headers=headers).content, "html.parser")
for i, img in enumerate(soup.find_all("img")):
    try:
        r = requests.get(urljoin(url, img.get("src")), headers=headers)
        with open(f"images/image_{i}.jpg", 'wb') as f:
            f.write(r.content)
    except:
        pass