from PIL import Image
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


print(get_predominant_color("../Assets/images/flower.jpg"))
