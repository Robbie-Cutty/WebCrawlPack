from bs4 import BeautifulSoup
import pandas as pd
import requests
import config

url = config.URL
output = requests.get(url)
soup = BeautifulSoup(output.text, 'html.parser')
table = soup.find_all('table')
tables = pd.read_html(str(table))[0]
tables.to_csv('url.csv')

print("Success")
