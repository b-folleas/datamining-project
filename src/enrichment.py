from PIL import Image, ExifTags

import numpy
import math
from sklearn.cluster import MiniBatchKMeans


def get_predominant_color(file_path):
    imgfile = Image.open(file_path)
    numarray = numpy.array(imgfile.getdata(), numpy.uint8)

    cluster_count = 1  # Numbers of clusters

    # MiniBatch execution
    clusters = MiniBatchKMeans(n_clusters=cluster_count)
    clusters.fit(numarray)

    # get color
    primary_color = '#%02x%02x%02x' % (
        math.ceil(clusters.cluster_centers_[0][0]),
        math.ceil(clusters.cluster_centers_[0][1]),
        math.ceil(clusters.cluster_centers_[0][2]))

    return primary_color


# print(get_predominant_color("../Assets/images/flower.jpg"))

def get_exif(file_path):
    imgfile = Image.open(file_path)
    width, height = imgfile.size

    print(width, height)

    img_exif = imgfile._getexif()

    if img_exif:
        exif_data = {
            ExifTags.TAGS[k]: v
            for k, v in img_exif.items()
            if k in ExifTags.TAGS
        }
        return (exif_data)

    return 'no exif'


def enrich_data():
    image_metadata = {
        "color_primary": '',
        "color_secondary": '',
        "size_x": 0,
        "size_y": 0,
        "orientation": '',
        "flash": 0,
        "exif_painting_width": 0,
        "exif_painting_height": 0,
        "date": '',
        "camera_make": '',
        "camera_model": '',
        "geo_data": ''
    }

'''
image_metadata["color_primary"] = 1
image_metadata["color_secondary"] = 1
image_metadata["orientation"] = 1
image_metadata["flash"] = 1

image_metadata["exif_painting_width"] = exif_data['ExifImageWidth']
image_metadata["exif_painting_height"] = exif_data['ExifImageHeight']
image_metadata["date"] = exif_data['DateTimeDigitized']


image_metadata["size_x"] = width
image_metadata["size_y"] = height
image_metadata["camera_make"] = exif_data['Make']
image_metadata["camera_model"] = exif_data['Model']

print(image_metadata)
'''
print(get_exif("../../Assets/images/flower.jpg"))
