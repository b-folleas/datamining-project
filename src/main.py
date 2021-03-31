# -*- coding: utf-8 -*-

import database_driver
import download
import seed

if __name__ == "__main__":
    images_source = 'ikarus777/best-artworks-of-all-time'

    number_images = int(input("Nombre d'images à télécharger :\n"))

    # Choosing random images
    images_list = download.choose_rand_image(images_source, number_images)
    
    # Downloading these images
    download.download_images(images_source, images_list)

    # Launch connection to the database, used for seeding the database
    database_driver.connect_database()

    # Seeding database
    seed.seed_database(images_source, images_list)
    
    # Recommendation

    # Visualization


    # Launch connection to the database, used for seeding the database
    database_driver.close_connection()