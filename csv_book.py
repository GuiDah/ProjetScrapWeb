import csv
import os

from constants import DATA_DIR
from down_img import img_down

def writer_book(data, name_csv, option):
    #the headers of the csv file
    fieldnames = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
                  'price_excluding_tax', 'number_available', 'product_description', 'category',
                  'review_rating', 'image_url']
    #saving csv files of each category at the root of the project
    cat_folder = os.path.join(DATA_DIR, f"{name_csv}.csv")
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    with open(cat_folder, "w", newline="", encoding='utf-8-sig') as csvfile:
        if option == "write":
            file_writer = csv.writer(csvfile)
            file_writer.writerow(fieldnames)
            for cat in data:
                recup_data = [cat['product_page_url'], cat['universal_product_code'], cat['title'], cat['price_including_tax'],
                              cat['price_excluding_tax'], cat['number_available'], cat['product_description'], cat['category'], cat['review_rating'], cat['image_url']]
                file_writer.writerow(recup_data)
                img_down(cat['image_url'])

        elif option == "update":
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)
        else:
            print("une erreur est survenue lors de l'écriture du csv")







