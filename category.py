import csv
import os

import requests
from bs4 import BeautifulSoup
from math import ceil

from book import book
from down_img import img_down
from csv_book import writer_book

def lien_html(lien):

    nouveau_lien = "http://books.toscrape.com/catalogue/"+lien.replace("../", "")
    return nouveau_lien

def link_url_catgegory(lienCat):

    """cette fonction prends en paramétres lienCat qui est rajoutée au lien du site"""

    link_cat = "http://books.toscrape.com/"+lienCat
    return link_cat

def list_pages_in_category(cat_index_url):
    """
    Calculates the number of pages in a category
    and generates the list of pages of this category.
    :param cat_index_url: The index page of the category.
    :return: A list of all pages of the category.
    """
    response = requests.get(cat_index_url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        cat_total_book_number = soup.select_one(
        '.form-horizontal > strong').text
        nb_pages = ceil(int(cat_total_book_number) / 20)

        # Add index.html first category page to the list
        all_url_of_one_category = [cat_index_url]

        # Append other pages if needed (page-x.html)
        for nb_page in range(2, nb_pages + 1):
            all_url_of_one_category.append(
                cat_index_url.replace("index", f"page-{str(nb_page)}")
            )
        return all_url_of_one_category


def scrap_one_categories(url):
    """find one categories"""
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
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

def scrap_all_categories(url):
    """find all url categories"""
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        liste_all_books = soup.find("div", class_="side_categories")
        find_all_books = liste_all_books.find_all("li")[1:]
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
        all_pages = list_pages_in_category(cont)
        name_csv = page_cat.split('/')[-2]
        for pages in all_pages:
            cat_book += scrap_one_categories(pages)
        writer_book(cat_book, name_csv, option="write")
        cat_book = []
        """print(cat_book)"""
    return cat_book

if __name__ == "__main__":
    main()
    """infos = scrap_one_categories(url="http://books.toscrape.com/catalogue/category/books/classics_6/index.html")"""
    """print(infos)"""










