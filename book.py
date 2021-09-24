import requests
from bs4 import BeautifulSoup

def book(url):

    """find all data of books"""

    response = requests.get(url)
    book_informations = {
        "product_page_url": "",
        "titre": "",
        "universal_product_code": 0,
        "price_including_tax": 0,
        "price_excluding_tax": 0,
        "number_available": "",
        "product_description": "",
        "category": "",
        "review_rating": "",
    }

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        book_informations["titre"] = soup.find("h1").text
        book_informations["universal_product_code"] = soup.find_all("td")[0].text
        book_informations["price_excluding_tax"] = soup.find_all("td")[2].text.replace("Â", "")
        book_informations["price_including_tax"] = soup.find_all("td")[3].text.replace("Â", "")
        book_informations["product_description"] = soup.find("div", class_="sub-header").next_sibling.next_sibling.text
        #book_informations["category"] = soup.find("ul", class_="breadcrumb").find("li").find("a")["href"]

        book_informations["number_available"] = soup.find_all("td")[6].text

        return book_informations
    else:
        print("une erreur est survenue")

infos = book(url = "http://books.toscrape.com/catalogue/soumission_998/index.html")
print(infos)