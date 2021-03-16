import pandas as pandas
import kaggle_settings

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# option to print all datas
pandas.set_option('display.max_columns', None)


def download_artists():
    api.dataset_download_file('ikarus777/best-artworks-of-all-time', 'artists.csv', path='../../Assets', force=False,
                              quiet=False)


def seed_artists():
    print('Seeding artists...')

    def get_century(years):
        years_list = years.split(' ')
        mean = (int(years_list[0].strip()) + int(years_list[2].strip())) / 2
        return (mean // 100 + 1)
    def get_first(genre):
        genre = genre.split(',')[0]
        return (genre)

    dataframe = pandas.read_csv('../../Assets/artists.csv')

    dataframe = dataframe[["name", "years", "genre", "nationality", "paintings"]]

    dataframe['years'] = dataframe['years'].apply(get_century) # get century from years
    dataframe['genre'] = dataframe['genre'].apply(get_first) # select first Genre only

    # add type for columns
    dataframe = dataframe.astype(dtype={"name": "<U200",
                                        "years": "int64",
                                        "genre": "<U200",
                                        "nationality": "<U200",
                                        "paintings": "int64"})
    # column rename
    dataframe = dataframe.rename(columns={"years": "century"})
    return dataframe # TODO send to database

download_artists()
seed_artists()

print(seed_artists().head())
