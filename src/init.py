import pandas as pandas

import settings

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# option to print all datas
pandas.set_option('display.max_columns', None)

# artists = api.dataset_download_file('ikarus777/best-artworks-of-all-time', 'artists.csv', path='../../Assets',force=False, quiet=False)
# print(artists)

dataframe = pandas.read_csv('../../Assets/artists.csv')
# name, years, genre, nationality, paintings

dataframe = dataframe[["name", "years", "genre",  "nationality", "paintings"]]

dataframe = dataframe.astype(dtype={"name": "<U200",
                                    "years": "<U200",
                                    "genre": "<U200",
                                    "nationality": "<U200",
                                    "paintings": "int64"})


dataframe['years'] = dataframe['years'].apply(lambda x: x + 1)

print(dataframe.head())
