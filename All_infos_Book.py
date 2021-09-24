import requests
from bs4 import BeautifulSoup
from book import book
from category import *

def scrap_book(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        liste_book = soup.find("ol", class_="row")
        find__book = liste_book.find("li")

        all_books = []
        for elements_livre in find__book:
            div_contenair = lien_html(elements_livre.find("div", class_="image_container").find("a")["href"])
            book_infos = book(div_contenair)
            all_books.append(book_infos)

        return all_books
    else:
        print("une erreur est survenue")


infos = scrap_one_categories(url="http://books.toscrape.com/catalogue/category/books/classics_6/index.html")
print(infos)