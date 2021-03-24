import pandas as pandas
import kaggle_settings
from kaggle.api.kaggle_api_extended import KaggleApi


api = KaggleApi()
api.authenticate()

FOLDER_PATH = '../../Assets'

# option to print all datas
pandas.set_option('display.max_columns', None)

# downloading artists.csv file into ../../Assets that contains all metadata for each artist
def download_artists():
    print('Dowloading artists csv file...')

    api.dataset_download_file('ikarus777/best-artworks-of-all-time', 'artists.csv', path=FOLDER_PATH, force=False,
                              quiet=False)


def seed_artists():
    print('Seeding artists...')

    def get_century(years):
        years_list = years.split(' ')
        mean = (int(years_list[0].strip()) + int(years_list[2].strip())) / 2
        return (mean // 100 + 1)

    def get_first(items):
        item = items.split(',')[0]
        return (item)

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
    dataframe = dataframe.rename(columns={"paintings": "number_paintings"})
    return dataframe # TODO send to database

if __name__ == "__main__" :

    download_artists()
    seed_artists()

    print(seed_artists())
    print(seed_artists().head())
