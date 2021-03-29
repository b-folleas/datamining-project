# -*- coding: utf-8 -*-

import database_driver


if __name__ == "__main__" :

    # Test getting artists
    try :
        artists = database_driver.select("")
    except ValueError :
        print("Error while fetching artists :", ValueError)
    
    # Test getting paintings
    try :
        number_paintings = database_driver.select("SELECT COUNT(painting_id) AS number_paintings FROM paintings")
    except ValueError :
        print("Error while fetching artists :", ValueError)
    
    # Get number of paintings liked by user
    try :
        number_likes_by_user = database_driver.select("SELECT fk_user_id, count(fk_painting_id) FROM history GROUP BY fk_user_id")
    except ValueError:
        print("Error while fetching paintings liked by user :", ValueError)

    # Get number of paintings liked for each artist
    try :
        number_likes_per_artist = database_driver.select("SELECT a.artist_id, a.name AS artist_name, count(fk_painting_id) AS number_liked \
            FROM history AS h \
            INNER JOIN paintings AS p ON p.painting_id = h.fk_painting_id \
            INNER JOIN artists AS a ON a.artist_id = p.fk_artist_id \
            GROUP BY a.artist_id")
    except ValueError :
        print("Error while fetching paintings liked for each artist :", ValueError)


        