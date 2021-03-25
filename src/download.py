import random
import ntpath
import kaggle_settings
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi


api = KaggleApi()
api.authenticate()

FOLDER_PATH = '../../Assets/images'


# Select at most <number_of_files> random image urls from a given dataset
def choose_rand_image(dataset, number_of_files):

    random_images_list = []

    # list dataset files
    images_list = api.dataset_list_files(dataset).files
    print(dataset)
    print(images_list[0])

    print("Choosing", number_of_files, "random images from the image list")

    for k in range(number_of_files):
        image = {"name": '', "path": '', "file": '', "artist": ''}
        image_file = random.choice([i for i in images_list if i.name.startswith('images/')]) # Getting random images
        image["name"] = ntpath.basename(str(image_file))
        image["path"] = FOLDER_PATH + '/' + image["name"]
        image["file"] = image_file
        print("Image", k, image["name"])
        artist_key = image_file.name.replace("images/images/", "").replace("/" + ntpath.basename(str(image_file)), "").replace(".jpg", "")
        image["artist"] = artist_key
        random_images_list.append(image)

    return random_images_list


def download_images(images_list):
    for image in images_list :
        print("Downloading", image["name"])
        api.dataset_download_file('ikarus777/best-artworks-of-all-time', str(image["file"]), path=FOLDER_PATH, force=False, quiet=False)
    print("download finished")


if __name__ == "__main__" :

    images_source = 'ikarus777/best-artworks-of-all-time'

    # Getting all the downloaded images in a list from download.py
    
    # Choosing random images
    images_list = choose_rand_image(images_source, 30)

