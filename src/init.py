import pandas as pandas
import kaggle_settings

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

def get_century(years):
    years_list = years.split(' ')
    mean = (int(years_list[0].strip()) + int(years_list[2].strip()))/2
    return( mean//100 + 1)

def get_first(genre):
    genre = genre.split(',')[0]
    return(genre)


dataframe['years'] = dataframe['years'].apply(get_century)

dataframe['genre'] = dataframe['genre'].apply(get_first)

dataframe = dataframe.astype(dtype={"name": "<U200",
                                    "years": "int64",
                                    "genre": "<U200",
                                    "nationality": "<U200",
                                    "paintings": "int64"})

dataframe = dataframe.rename(columns={"years": "century"})

print(dataframe.head())
