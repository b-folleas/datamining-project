from PIL import Image, ExifTags

import numpy
import math
from sklearn.cluster import MiniBatchKMeans


def get_predominant_color(file_path):
    img_file = Image.open(file_path)
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


def get_exif(file_path):
    img_file = Image.open(file_path)
    
    img_exif = img_file._getexif()

    if img_exif:
        exif_data = {
            ExifTags.TAGS[k]: v
            for k, v in img_exif.items()
            if k in ExifTags.TAGS
        }
        return (exif_data)

    return 'no exif'


def enrich_data(exif_data, file_path):
    img_meta_data = {
        "color_primary": '',
        "color_secondary": '',
        "orientation": '',
        "flash": 0,
        "width": 0,
        "height": 0,
        "date": '',
        "camera_make": '',
        "camera_model": '',
        "geo_data": ''
    }

    img_meta_data["color_primary"] = (get_predominant_color(file_path))
    img_meta_data["color_secondary"] = 1
    img_meta_data["orientation"] = 1
    img_meta_data["flash"] = 1

    img_meta_data["width"] = exif_data['ExifImageWidth']
    img_meta_data["height"] = exif_data['ExifImageHeight']
    img_meta_data["date"] = exif_data['DateTimeDigitized']

    img_meta_data["camera_make"] = exif_data['Make']
    img_meta_data["camera_model"] = exif_data['Model']

    return img_meta_data


def set_img_data(file_path):
    img_exif_data = get_exif(file_path)
    img_meta_data = enrich_data(img_exif_data, file_path)

    print("Image meta_data :") # Test phase
    print(img_meta_data) # Test phase
    return img_meta_data


# Setting an img_file_path to get meta_data from 
img_file_path = "./flower.jpg" # Test phase

# Setting img_metada
img_meta_data = set_img_data(img_file_path)

# Then insert this data in database