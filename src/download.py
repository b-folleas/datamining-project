import settings
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import random


api = KaggleApi()
api.authenticate()

number_of_file = 30

# list dataset files
image_list = api.dataset_list_files('ikarus777/best-artworks-of-all-time').files

print("choosing " , number_of_file, "random images from  the image list")

for k in range(number_of_file):
    file = random.choice(image_list)
    print("downloading ", file)
    api.dataset_download_file('ikarus777/best-artworks-of-all-time', str(file), path='../../Assets/images', force=False, quiet=False)

print("download finished")
