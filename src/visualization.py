# -*- coding: utf-8 -*-

import database_driver
import pandas as pd
import matplotlib.pyplot as plot

if __name__ == "__main__":

    # To test only visualization
    database_driver.connect_database()

    # Test getting artists
    try:
        artists = database_driver.select("SELECT * FROM artists")
    except ValueError:
        print("Error while fetching artists :", ValueError)

    # Test getting paintings
    try:
        number_paintings_through_time = database_driver.select("SELECT date, count(painting_id), \
            SUM(COUNT(painting_id)) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS cumulative \
            FROM paintings \
            GROUP BY date")
    except ValueError:
        print("Error while fetching artists :", ValueError)

    # Get number of paintings liked by user
    try:
        number_likes_by_user = database_driver.select(
            "SELECT fk_user_id, count(fk_painting_id) FROM history GROUP BY fk_user_id")
    except ValueError:
        print("Error while fetching paintings liked by user :", ValueError)

    # Get number of paintings liked for each artist
    try:
        number_likes_per_artist = database_driver.select("SELECT a.artist_id, a.name AS artist_name, count(fk_painting_id) AS number_liked \
            FROM history AS h \
            INNER JOIN paintings AS p ON p.painting_id = h.fk_painting_id \
            INNER JOIN artists AS a ON a.artist_id = p.fk_artist_id \
            GROUP BY a.artist_id")
    except ValueError:
        print("Error while fetching paintings liked for each artist :", ValueError)
  
    
    # Calling DataFrame from previous SQL statements
    df_likes_per_artist = pd.DataFrame((number_likes_per_artist),columns = ['Artist ID', 'Artist Name', 'Number paintings liked'])
    
    df_paintings_through_time = pd.DataFrame((number_likes_per_artist),columns = ['Date', 'Number of Paintings', 'Cumulative Number of Paintings'])
    plot.plot(df_paintings_through_time)
    plot.title("Number of paintings Evolution Through Time")
    plot.xlabel('date',  fontsize=16)
    plot.ylabel('count',  fontsize=16)
    plot.show()    
    
    df_likes_per_artist.plot(x=0, kind='bar', title="Number of liked images per author")

    # To test only visualization
    database_driver.close_connection(database_driver.CONNECTION)
