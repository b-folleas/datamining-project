# -*- coding: utf-8 -*-

from PIL import Image, ExifTags

import numpy
import math
import datetime
from sklearn.cluster import MiniBatchKMeans
from pathlib import Path
import database_manager as db_manager


def get_predominant_color(img):
    """Get the predominant color of an image using MiniBatchKMeans clusterisation.
    :param img: An image file which has been already opened.
    :return: The predominant color as a string with the format #hexadecimal.
    """
    numarray = numpy.array(img.getdata(), numpy.uint8)

    #numarray.reshape(-1, 1)

    cluster_count = 1  # Numbers of clusters

    # MiniBatch execution
    clusters = MiniBatchKMeans(n_clusters=cluster_count)
    clusters.fit(numarray)

    # Get primary color
    primary_color = '#%02x%02x%02x' % (
        math.ceil(clusters.cluster_centers_[0][0]),
        math.ceil(clusters.cluster_centers_[0][1]),
        math.ceil(clusters.cluster_centers_[0][2]))

    return primary_color


def get_exif(image):
    """Get exif data from an image object.
    :param image: (object) An image object stored in the images_list.
    :return: exif data or None.
    """
    img_exif = None
    try:
        img_file = Image.open(image["path"])
        img_exif = img_file._getexif()
    except FileNotFoundError:
        print("Error :", FileNotFoundError)

    if img_exif:
        exif_data = {
            ExifTags.TAGS[k]: v
            for k, v in img_exif.items()
            if k in ExifTags.TAGS
        }
        return exif_data

    return None


def set_img_data(image):
    """Set the meta data to be inserted in database of an image object.
    :param images_list: A standard list containing images object.
    :return: Object of the image meta data.
    """
    img_exif_data = get_exif(image)

    img_meta_data = {
        "painting_path": '',
        "fk_artist_id": 0,
        "color_primary": '',
        "color_secondary": '',
        "orientation": 0,
        "flash": 0,
        "width": '',
        "height": '',
        "date": '',
        "camera_make": '',
        "camera_model": '',
        "geo_data": ''
    }

    try:
        img = Image.open(image["path"])
        width, height = img.size

        # To change, done here beacause of not null constraint
        img_meta_data["painting_path"] = image["path"]
        print(image["artist"])


        img_meta_data["fk_artist_id"] = db_manager.get_artist_id_from_name(
            image["artist"])



        # Getting painting primary color
        img_meta_data["color_primary"] = get_predominant_color(img)
        img_meta_data["color_secondary"] = 1

        img_meta_data["width"] = width
        img_meta_data["height"] = height

        img_meta_data["date"] = datetime.date.today().strftime("%m/%d/%Y")

        # Adding meta_data through img_exif_data
        if img_exif_data != None:
            # Date of creation of the image, if not, use today's date
            img_meta_data["date"] = datetime.datetime.strptime(
                img_exif_data['DateTimeDigitized'], '%Y:%m:%d %H:%M:%S').date().strftime("%m/%d/%Y")

            img_meta_data["orientation"] = img_exif_data["Orientation"]
            img_meta_data["flash"] = img_exif_data["Flash"]
            img_meta_data["camera_make"] = img_exif_data['Make']
            img_meta_data["camera_model"] = img_exif_data['Model']

        return img_meta_data

    except FileNotFoundError:
        print("Error :", FileNotFoundError)

        return None


if __name__ == "__main__":

    image = {}
    # Setting an img_file_path to get meta_data from
    image["path"] = "./flower.jpg"  # Test phase
    img_file = Image.open(image["path"])

    print(get_predominant_color(img_file))

    #image["artist"] = "Monet"

    # Setting img_metada
    #img_meta_data = set_img_data(image)
