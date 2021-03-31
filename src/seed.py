# -*- coding: utf-8 -*-

import database_driver as db_driver
import database_manager as db_manager
import pandas as pd
import download
import enrichment
import artist
import random


def seed_artists(images_source):

    print("Seeding artists...")

    # Downloading artists data
    artist.download_artists(images_source)

    # Seeding all artists data to the database
    artists = artist.seed_artists()

    # Set insert_table before insertion
    insert_table = 'artists'

    # Go through each artist to insert it's data in the database
    artist_data_keys = artists.columns.tolist()
    # print(artist_data_keys)

    # print('Artist size :', artists.index)

    for a in artists.index:
        # print(artists.values[a])

        artist_data_values = artists.values[a]
        print(artist_data_values)

        db_driver.insert(
            insert_table, artist_data_keys, artist_data_values)


def seed_paintings(images_list):

    print("Seeding paintings...")
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

            db_driver.insert(
                insert_table, meta_data_keys, meta_data_values)
        else:
            print("No insertion available, meta data is None")
    print("End of data extraction, enrichment and load of paintings.")


def seed_history(number_rows):
    '''Inserting random rows in the history table with the paintings seen by users.
    '''
    print("Seeding history...")
    # Set insert_table before insertion
    insert_table = 'history'

    # Initialisation keys and values
    data_keys = ['fk_user_id', 'fk_painting_id', 'favorite']
    try :
        users = db_manager.get_users()
    except TypeError:
        print("Error while randomly picking user :", TypeError)
    try :
        paintings = db_manager.get_paintings()
    except TypeError:
        print("Error while randomly picking painting :", TypeError)
    try :
        favorite_choice = ['true', 'false']
    except TypeError:
        print("Error while randomly picking favorite choice:", TypeError)

    # Go through each images_list item to get it's meta-data
    for i in range(number_rows):
        user_id = random.choice(users)[0] # Getting one random user
        painting_id = random.choice(paintings)[0] # Getting one random painting
        favorite = random.choice(favorite_choice)
        
        db_driver.insert(insert_table, data_keys, [user_id, painting_id, favorite])
    
    # Inserting these data
    print("End of insertion for history.")


def seed_database(images_source, images_list, number_rows):
    """Seeding database and downloading files
    """
    seed_artists(images_source)

    seed_paintings(images_list)

    seed_history(number_rows)


if __name__ == "__main__":
    # Launch connection to the database, used for seeding the database
    database_driver.connect_database()

    seed_history(2)

   


    # Launch connection to the database, used for seeding the database
    database_driver.close_connection()

    # images_source = 'ikarus777/best-artworks-of-all-time'
    # number_paintings = 30

    # # Choosing random images
    # images_list = download.choose_rand_image(images_source, paintings_number)

    # # Downloading these images
    # download.download_images(images_source, images_list)


