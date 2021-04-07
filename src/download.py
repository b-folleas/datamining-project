# -*- coding: utf-8 -*-

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
    '''Define a list of random images from the dataset.
    :param dataset: (set) A dataset containing the files which will be given into a list of images.
    :param number_of_files: (int) Int to define the number of files to pick from the dataset.
    :return: The list of images
    '''
    random_images_list = []

    # list dataset files
    images_list = api.dataset_list_files(dataset).files
    print("Source :", dataset)

    print("Choosing", number_of_files, "random images from the image list :")

    for k in range(number_of_files):
        image = {"name": '', "path": '', "file": '', "artist": ''}
        image_file = random.choice(
            [i for i in images_list if i.name.startswith('images/')])  # Getting random images
        image["name"] = ntpath.basename(str(image_file))
        image["path"] = FOLDER_PATH + '/' + image["name"]
        image["file"] = image_file
        print("Image", k, image["name"])
        artist_key = image_file.name.replace("images/images/", "").replace(
            "/" + ntpath.basename(str(image_file)), "").replace(".jpg", "")
        image["artist"] = artist_key
        random_images_list.append(image)

    return random_images_list


def download_images(dataset, images_list):
    '''Download a list of images.
    :param images_list: (list) A standard list containing images object.
    :return: None.
    '''
    for image in images_list:
        api.dataset_download_file(dataset,
                                  str(image["file"]), path=FOLDER_PATH, force=False, quiet=False)
    print("Downloading images over.\n")


if __name__ == "__main__":

    images_source = 'ikarus777/best-artworks-of-all-time'

    # Getting all the downloaded images in a list from download.py

    # Choosing random images
    images_list = choose_rand_image(images_source, 30)
