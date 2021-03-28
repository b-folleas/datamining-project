import pandas as pandas
import kaggle_settings
from kaggle.api.kaggle_api_extended import KaggleApi
import database_connection

'''
Get Artists data
'''


api = KaggleApi()
api.authenticate()

FOLDER_PATH = '../../Assets'

# option to print all datas
pandas.set_option('display.max_columns', None)

# downloading artists.csv file into ../../Assets that contains all metadata for each artist
def download_artists(images_source):
    print('Dowloading artists csv file...')

    api.dataset_download_file(images_source, 'artists.csv', path=FOLDER_PATH, force=False,
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
    return dataframe


def get_artist_from_name(name):
    # Connect to database
    connection = database_connection.connect_database()
    cursor = database_connection.create_cursor(connection)

    statement = "SELECT artist_id FROM artists AS a WHERE a.name LIKE '%"+ name + "%'" # ajouter une limite 1 ?
    
    print(statement)
    
    cursor.execute(statement)
    id = cursor.fetchone()[0] # return data from last query

    # Close the cursor object to avoid memory leaks
    cursor.close()

    # Close the connection
    connection.close()

    return id

if __name__ == "__main__" :

    download_artists()
    seed_artists()

    print(seed_artists())
    print(seed_artists().head())
