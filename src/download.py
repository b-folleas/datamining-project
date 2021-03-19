import kaggle_settings
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import random


api = KaggleApi()
api.authenticate()


# Select at most <number_of_files> random image urls from a given dataset
def choose_rand_image(dataset, number_of_files):

    random_image_list = []

    # list dataset files
    image_list = api.dataset_list_files(dataset).files
    print("Choosing", number_of_files, "random images from the image list")

    for k in range(number_of_files):
        file = random.choice([i for i in image_list if i.name.startswith('images/')]) # Getting random images
        print("Image", k, file)
        random_image_list.append(file)

    return random_image_list


def download_images(image_list):
    for k in range(len(image_list)):
        file = image_list[0]
        print("Downloading", k, file)
        api.dataset_download_file('ikarus777/best-artworks-of-all-time', str(file), path='../../Assets/images', force=False, quiet=False)
    print("download finished")

image_list = choose_rand_image('ikarus777/best-artworks-of-all-time', 30)
# download_images(image_list)

