# -*- coding: utf-8 -*-

import database_driver
import os


FOLDER_PATH = '../../Assets/images'
LIST_TABLES = ['artists', 'paintings']

def truncate_tables(tables):

    request = "TRUNCATE TABLE " + \
        str(', '.join(tables)) + " CASCADE"
    # Truncate artists and paintings tables
    try:
        print(request)
        truncate_result = database_driver.select(request)
        print(truncate_result)
    except ValueError:
        print("Error while trying to truncate given tables", ValueError)

def remove_images(dir):

    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


if __name__ == "__main__":

    print("Reseting database and files...")

    # Connect to database, return connection
    database_driver.connect_database()

    truncate_tables(LIST_TABLES)

    remove_images(FOLDER_PATH)

    # Close database connection at the end of main script
    database_driver.close_connection()
