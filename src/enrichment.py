from PIL import Image, ExifTags

import numpy
import math
import datetime
from sklearn.cluster import MiniBatchKMeans
from pathlib import Path
import artist


def get_predominant_color(image):
    img_file = Image.open(image["path"])
    numarray = numpy.array(img_file.getdata(), numpy.uint8)

    cluster_count = 1  # Numbers of clusters

    # MiniBatch execution
    clusters = MiniBatchKMeans(n_clusters=cluster_count)
    clusters.fit(numarray)

    # Get primary color
    primary_color = '#%02x%02x%02x' % (
        math.ceil(clusters.cluster_centers_[0][0]),
        math.ceil(clusters.cluster_centers_[0][1]),
        math.ceil(clusters.cluster_centers_[0][2]))

    print("Primary color :") # Test phase
    print(primary_color) # Test phase
    return primary_color


def get_exif(image):
    img_file = Image.open(image["path"])
    img_exif = img_file._getexif()

    if img_exif:
        exif_data = {
            ExifTags.TAGS[k]: v
            for k, v in img_exif.items()
            if k in ExifTags.TAGS
        }
        return exif_data

    return None


def enrich_data(exif_data, image):
    img_meta_data = {
        "painting_path": '',
        "fk_artist_id": '',
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

    img = Image.open(image["path"])
    width, height = img.size

    img_meta_data["painting_path"] = image["path"] # To change, done here beacause of not null constraint
    print(image["artist"])
    img_meta_data["fk_artist_id"] = artist.get_artist_from_name(image["artist"])

    # Getting painting primary color
    img_meta_data["color_primary"] = (get_predominant_color(image))
    img_meta_data["color_secondary"] = 1
    
    img_meta_data["width"] = width
    img_meta_data["height"] = height
    
    img_meta_data["date"] = datetime.date.today().strftime("%m/%d/%Y")

    # Adding meta_data through exif_data
    if exif_data != None :
        # Date of creation of the image, if not, use today's date
        img_meta_data["date"] = datetime.datetime.strptime(exif_data['DateTimeDigitized'], '%Y:%m:%d %H:%M:%S').date().strftime("%m/%d/%Y")

        img_meta_data["orientation"] = exif_data["Orientation"]
        img_meta_data["flash"] = exif_data["Flash"]
        img_meta_data["camera_make"] = exif_data['Make']
        img_meta_data["camera_model"] = exif_data['Model']

    print(img_meta_data)
    return img_meta_data


def set_img_data(image):
    img_exif_data = get_exif(image)
    img_meta_data = enrich_data(img_exif_data, image)

    return img_meta_data

    return 1

if __name__ == "__main__" :

    image = {}
    # Setting an img_file_path to get meta_data from 
    image["path"] = "./flower.jpg" # Test phase
    image["artist"] = "Monet"

    # Setting img_metada
    img_meta_data = set_img_data(image)
