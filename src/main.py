# -*- coding: utf-8 -*-

import database_driver
import download
import enrichment
import insertion
import artist

if __name__ == "__main__":
    images_source = 'ikarus777/best-artworks-of-all-time'
    # Connect to database, return connection

    database_driver.connect_database()
    # Getting all the downloaded images in a list from download.py

    # Choosing random images
    images_list = download.choose_rand_image(images_source, 30)

    # Downloading artists data
    # artist.download_artists(images_source)

    # Seeding all artists data to the database
    # artists = artist.seed_artists()

    # Set insert_table before insertion
    insert_table = 'artists'

    # Go through each artist to insert it's data in the database
    # artist_data_keys = artists.columns.tolist()
    # print(artist_data_keys)

    # print('Artist size :', artists.index)

    for a in artists.index:
        # print(artists.values[a])

        artist_data_values = artists.values[a]
        print(artist_data_values)

        database_driver.insert(
            insert_table, artist_data_keys, artist_data_values)

    # Downloading these images
    download.download_images(images_list)

    # Set insert_table before insertion
    insert_table = 'paintings'

    # Go through each images_list item to get it's meta-data
    for image in images_list:
        print(image["path"])
        img_meta_data = enrichment.set_img_data(image)

        print(img_meta_data)

        if img_meta_data:
            # Inserting these metadata of each image into the table paintings of the database
            meta_data_keys = list(img_meta_data.keys())
            meta_data_values = list(img_meta_data.values())

            database_driver.insert(
                insert_table, meta_data_keys, meta_data_values)
        else:
            print("No insertion available, meta data is None")
    print("End of data extraction, enrichment and load.")
