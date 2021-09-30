import requests
from bs4 import BeautifulSoup
from book import book

def lien_html(lien):

    nouveau_lien = lien.replace("../../../", "http://books.toscrape.com/catalogue/")
    return nouveau_lien


def scrap_one_categories(url):
    """find one categories"""
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        liste_book = soup.find("ol", class_="row")
        find__book = liste_book.find_all("li")


        all_books = []
        for elements_livre in find__book:
            div_contenair = lien_html(elements_livre.find("div", class_="image_container").find("a")["href"])
            book_infos = book(div_contenair)
            all_books.append(book_infos)
        return all_books
    else:
        print("une erreur est survenue")

""""infos = scrap_one_categories(url="http://books.toscrape.com/catalogue/category/books/classics_6/index.html")"""
"""print(infos)"""

def scrap_all_categories(url):
    """find all categories"""
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        liste_all_books = soup.find("div", class_="side_categories")
        find_all_books = liste_all_books.find_all("li")

        for all_categories in find_all_books:
            all_contenair = all_categories.find("a")["href"]
            print(all_contenair)
        return all_contenair
    else:
        print("une erreur est survenue lors scrap du site")
        
infos_books = scrap_all_categories(url="http://books.toscrape.com/index.html")
print(infos_books)

