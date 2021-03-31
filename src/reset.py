# -*- coding: utf-8 -*-

import database_driver
import os


FOLDER_PATH = '../../Assets/images'
LIST_TABLES = ['artists', 'paintings']


def truncate_tables(tables):
    '''Removing all data by truncate the target tables.\n
    :param tables: (string) the target tables.\n
    :return: None.
    '''
    request = "TRUNCATE TABLE " + \
        str(', '.join(tables)) + " CASCADE"
    # Truncate artists and paintings tables
    try:
        print("Execute following request : " + request)
        truncate_result = database_driver.select(request)
    except ValueError:
        print("Error while trying to truncate given tables", ValueError)


def remove_images(dir):
    '''Removing all files in the 'dir' directory.\n
    :param dir: (string) the target directory.\n
    :return: None.
    '''
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


if __name__ == "__main__":

    # Connect to database, return connection
    database_driver.connect_database()

    print("Reseting database...")
    truncate_tables(LIST_TABLES)

    print("Removing images...")
    remove_images(FOLDER_PATH)

    print("Done.")
    # Close database connection at the end of main script
    database_driver.close_connection()
