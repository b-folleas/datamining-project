# -*- coding: utf-8 -*-

import pandas as pandas
import kaggle_settings
from kaggle.api.kaggle_api_extended import KaggleApi
import database_manager as db_manager
import database_driver as db_driver


api = KaggleApi()
api.authenticate()

FOLDER_PATH = '../../Assets'

# option to print all datas
pandas.set_option('display.max_columns', None)

# downloading artists.csv file into ../../Assets that contains all metadata for each artist


def download_artists(images_source):
    '''Download a artists.csv file from source API.
    :param images_source: (string) indicates the source from which download the artists.csv file.
    :return: none
    '''
    print('Dowloading artists csv file...')

    api.dataset_download_file(images_source, 'artists.csv', path=FOLDER_PATH, force=False,
                              quiet=False)


def get_artists_from_csv():
    '''Get Artists from the artists.csv file.
    Get the artist meta data, ennrich some of them.
    :return: dataframe object
    '''

    def get_century(years):
        '''Get century based on the mean of a list of years (start, end) given in parameter.\n
        :param years: (list) A list of two elements : the starting year and ending year.\n
        :return: (int) century
        '''
        years_list = years.split(' ')
        mean = (int(years_list[0].strip()) + int(years_list[2].strip())) / 2
        return (mean // 100 + 1)

    def get_first(items):
        '''Get first element of a list.\n
        :param items: (list) The list of items.\n
        :return: (object) item.
        '''
        item = items.split(',')[0]
        return (item)

    def get_last_name(items):
        '''Get only lastname from a string containing the firstname and lastname.\n
        :param items: (string) The string composed of the firstname and lastname.\n
        :return: (string) lastname.
        '''
        item = items.split(' ')[-1]
        return (item)

    dataframe = pandas.read_csv('../../Assets/artists.csv')

    dataframe = dataframe[["name", "years",
                           "genre", "nationality", "paintings"]]

    dataframe['years'] = dataframe['years'].apply(
        get_century)  # get century from years
    dataframe['genre'] = dataframe['genre'].apply(
        get_first)  # select first Genre only


    # add type for columns
    dataframe = dataframe.astype(dtype={"name": "<U200",
                                        "years": "int64",
                                        "genre": "<U200",
                                        "nationality": "<U200",
                                        "paintings": "int64"})
    # column rename
    dataframe = dataframe.rename(columns={"years": "century"})
    dataframe = dataframe.rename(columns={"paintings": "number_paintings"})
    return dataframe


if __name__ == "__main__":
    db_driver.connect_database()
    # download_artists()
    # seed_artists()

    # print(seed_artists())
    # print(seed_artists().head())

    #print(seed_artists())
