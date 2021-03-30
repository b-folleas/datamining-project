# -*- coding: utf-8 -*-

import database_driver
import pandas as pd
import matplotlib.pyplot as plot

if __name__ == "__main__":

    # To test only visualization
    database_driver.connect_database()

    '''
    # Test getting artists
    try:
        artists = database_driver.select("SELECT * FROM artists")
    except ValueError:
        print("Error while fetching artists :", ValueError)

    

    # Get paintings added to the database thought time
    try:
        request = "SELECT date, count(painting_id), \
            SUM(COUNT(painting_id)) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS cumulative \
            FROM paintings \
            GROUP BY date"

        # print(request)
        number_paintings_through_time = database_driver.select(request)

        df_paintings_through_time = pd.DataFrame(number_paintings_through_time,
                                                 columns=['date', 'painting_number', 'all_painting'])

        df_paintings_through_time['date'] = pd.to_datetime(df_paintings_through_time['date'], format='%Y-%m-%d')
        df_paintings_through_time = df_paintings_through_time.astype(dtype={"painting_number": "int64",
                                                                            "all_painting": "int64"})

        # print(number_paintings_through_time)

        df_paintings_through_time.plot(kind='line', x='date', y='all_painting', color='red')
        plot.title("Number of paintings Evolution Through Time")
        plot.xlabel('date', fontsize=16)
        plot.ylabel('count', fontsize=16)


    except ValueError:
        print("Error while fetching artists :", ValueError)

    # Get number of paintings liked by user
    try:
        number_likes_by_user = database_driver.select(
            "SELECT fk_user_id, count(fk_painting_id) FROM history GROUP BY fk_user_id")
    except ValueError:
        print("Error while fetching paintings liked by user :", ValueError)

    '''

    # Get number of paintings liked for each artist
    try:
        request = "SELECT a.artist_id, a.name AS artist_name, count(fk_painting_id) AS number_liked \
            FROM history AS h \
            INNER JOIN paintings AS p ON p.painting_id = h.fk_painting_id \
            INNER JOIN artists AS a ON a.artist_id = p.fk_artist_id \
            GROUP BY a.artist_id"

        number_likes_per_artist = database_driver.select(request)

        df_likes_per_artist = pd.DataFrame(number_likes_per_artist,
                                           columns=['artist_id', 'artist_name', 'n_likes'])

        df_likes_per_artist = df_likes_per_artist.astype(dtype={"artist_name": "<U200",
                                                                "n_likes": "int64"})
        print(df_likes_per_artist)

        df_likes_per_artist.plot(kind='bar', x='artist_name', y='n_likes', color='blue')
        plot.title("Artists and liked paintings")
        plot.xlabel('Artists', fontsize=16)
        plot.ylabel('likes', fontsize=16)

    except ValueError:
        print("Error while fetching paintings liked for each artist :", ValueError)

    # Calling DataFrame from previous SQL statements

    plot.show()

    # df_likes_per_artist.plot(x=0, kind='bar', title="Number of liked images per author")

    # To test only visualization
    database_driver.close_connection(database_driver.CONNECTION)
