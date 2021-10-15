import csv
import os

import requests
from bs4 import BeautifulSoup

from book import book

from csv_book import writer

def lien_html(lien):

    nouveau_lien = "http://books.toscrape.com/catalogue/"+lien.replace("../", "")
    return nouveau_lien


def link_url_catgegory(lienCat):

    """cette fonction prends en paramétres lienCat qui est rajoutée au lien du site"""

    link_cat = "http://books.toscrape.com/"+lienCat
    return link_cat



def scrap_one_categories(url):
    """find one categories"""
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        liste_book = soup.find("ol", class_="row")
        find__book = liste_book.find_all("li")
        name_csv = soup.find("h1").text
        print(name_csv)
        all_books = []
        for elements_livre in find__book:
            div_contenair = lien_html(elements_livre.find("div", class_="image_container").find("a")["href"])

            book_infos = book(div_contenair)
            all_books.append(book_infos)

        writer(all_books, name_csv, option="write")
        quit(56878)

        return all_books

    else:
        print("une erreur est survenue")




def scrap_all_categories(url):
    """find all url categories"""
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        liste_all_books = soup.find("div", class_="side_categories")
        find_all_books = liste_all_books.find_all("li")
        all_url_cat = []
        for all_categories in find_all_books:
            all_contenair = all_categories.find("a")["href"]
            all_url_cat.append(all_contenair)
        return all_url_cat
    else:
        print("une erreur est survenue lors scrap du site")
"""infos_books = scrap_all_categories(url="http://books.toscrape.com/index.html")"""
"""print(infos_books)"""


def main():

    infos_books = scrap_all_categories(url="http://books.toscrape.com/index.html")
    cat_book = []
    for page_cat in infos_books:
        cont = link_url_catgegory(page_cat)
        cat_book.append(scrap_one_categories(cont))
        print(cat_book)
    return cat_book

if __name__ == "__main__":
    main()
    """infos = scrap_one_categories(url="http://books.toscrape.com/catalogue/category/books/classics_6/index.html")"""
    """print(infos)"""










