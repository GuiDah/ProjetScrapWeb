## Importing Necessary Modules
import os
import requests  # to get image from the web
import shutil  # to save it locally

def img_down(image_url):
    #the images are saved at the root of the project in the image folder.
    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    IMG_DIR = os.path.join(CUR_DIR, "images")
    ## Set up the image URL and filename
    filename =image_url.split("/")[-1]

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        img_folder = os.path.join(IMG_DIR, filename)
        if not os.path.exists(IMG_DIR):
            os.makedirs(IMG_DIR)
        # Open a local file with wb ( write binary ) permission.
        with open(img_folder, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')