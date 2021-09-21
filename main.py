import csv
import os

import requests
from bs4 import BeautifulSoup

from constants import DATA_DIR

url = 'http://books.toscrape.com/'
response = requests.get(url)
categorie_element = []
if response.ok:

    soup = BeautifulSoup(response.text, 'html.parser')
    categories_elements = soup.find_all("div", class_="side_categories")

    for categorie_element in categories_elements:
        categorie_element = categorie_element.find('li')
        print(categorie_element.text)










