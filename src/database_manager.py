# -*- coding: utf-8 -*-

import database_driver as db_driver

# Functions to get data from database

# ARTIST #


def get_artists():
    '''Get all meta data about artists
    :return: artists
    '''
    try:
        artists = db_driver.select("SELECT * FROM artists")
        return artists
    except ValueError:
        print("Error while fetching artists :", ValueError)
        return -1


def get_artist_id_from_name(name):
    '''Get Artist id from the artist name.\n
    :return: artist id
    '''
    request = "SELECT artist_id FROM artists AS a WHERE a.name LIKE '%" +name + "%'"
    try:
        id = db_driver.select(request)
        if id != None :
            id = id[0][0] # Get only first result

    except ValueError:
        print("Error while fetching artist_id from name :", ValueError)

    print("artist name", name )
    print("artist id", id )

    return id # if id = None then "artist unknown"


def get_likes_by_artist():
    '''Get number of paintings liked group by artist.\n
    :return: number_likes_by_artist
    '''
    try:
        request = "SELECT a.artist_id, a.name AS artist_name, count(fk_painting_id) AS number_liked \
            FROM history AS h \
            INNER JOIN paintings AS p ON p.painting_id = h.fk_painting_id \
            INNER JOIN artists AS a ON a.artist_id = p.fk_artist_id \
            GROUP BY a.artist_id"
        number_likes_by_artist = db_driver.select(request)
        return number_likes_by_artist
    except ValueError:
        print("Error while fetching paintings liked for each artist :", ValueError)
        return -1


# USER #

def get_users():
    '''Get users from the database.\n
    :return: users.
    '''
    try:
        request = "SELECT u.user_id, u.username, u.email \
        FROM users AS u \
        ORDER BY u.user_id \
        "
        users = db_driver.select(request)
        return users
    except ValueError:
        print("Error while fetching users :", ValueError)
        return -1


def get_users_dashboard():
    '''Get users dashboards and see their number of likes on paintings.\n
    :return: users_dashboard.
    '''
    try:
        request = "SELECT count(h.fk_painting_id) AS paintings_number, u.user_id, u.username \
        FROM users AS u \
        INNER JOIN history AS h ON h.fk_user_id = u.user_id \
        LEFT JOIN preferences AS pf ON pf.preference_id = fk_preferences_id \
        GROUP BY u.user_id \
        "
        users_dashboard = db_driver.select(request)
        return users_dashboard
    except ValueError:
        print("Error while fetching users dashboard :", ValueError)
        return -1


def get_user_history(user_id):
    '''Get user_history with the pictures the user have seen and wich one were liked.\n
    :return: user_history.
    '''
    try:                                   
        request = "SELECT h.favorite, p.painting_id, a.artist_id, a.name, a.century, a.genre, a.nationality, p.date, p.width, p.height, p.orientation, p.flash  \
        FROM history AS h \
        INNER JOIN paintings AS p ON p.painting_id = h.fk_painting_id \
        INNER JOIN artists AS a ON p.fk_artist_id = a.artist_id \
        WHERE h.fk_user_id = " + str(user_id) + " \
        ORDER BY p.painting_id"

        user_history = db_driver.select(request)
        print("user history : ", request)
        return user_history
    except ValueError:
        print("Error while fetching user history :", ValueError)
        return -1


# PAINTING #

def get_paintings():
    '''Get paintings added to the database.\n
    :return: paintings.
    '''
    try:
        request = "SELECT p.painting_id, p.fk_artist_id, p.orientation, p.flash, p.width, p.height, p.date, p.camera_make, p.camera_model \
        FROM paintings AS p ORDER BY painting_id"
        paintings = db_driver.select(request)
        return paintings
    except ValueError:
        print("Error while fetching paintings :", ValueError)
        return -1


def get_paintings_through_time():
    '''Get paintings added to the database though time.\n
    :return: number_paintings_through_time.
    '''
    try:
        request = "SELECT date, count(painting_id), \
            SUM(COUNT(painting_id)) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS cumulative \
            FROM paintings \
            GROUP BY date"

        number_paintings_through_time = db_driver.select(request)
        return number_paintings_through_time
    except ValueError:
        print("Error while fetching paintings through time :", ValueError)
        return -1


def get_painting_metadata(painting_id):
    '''Get paintings added to the database though time.\n
    :return: number_paintings_through_time.
    '''
    try:

        request = "SELECT p.painting_id, a.name, a.century, a.genre, a.nationality, a.number_paintings, p.orientation, p.flash, p.width, p.height, p.date, p.camera_make, p.camera_model \
        FROM paintings AS p WHERE painting_id = " + str(painting_id) + " INNER JOIN artists AS a ON a.artist_id = p.fk_artist_id ORDER BY painting_id"

        # request = "SELECT p.fk_artist_id,  p.orientation, p.flash, p.width, p.height, p.date, p.camera_make, p.camera_model \
        # FROM paintings AS p WHERE painting_id = " + str(painting_id) + " ORDER BY " + str(painting_id)

        paintings = db_driver.select(request)[0]
        return paintings
    except ValueError:
        print("Error while fetching data :", ValueError)
        return -1


if __name__ == "__main__":

    # To test in database_manager
    db_driver.connect_database()

    # Users dashboard
    print("Users Dashboard")
    print(get_users_dashboard())

    # Paintings through time
    print("Number of paintings through time (by date)")
    print(get_paintings_through_time())

    # Paintings through time
    print("Number of likes by artist")
    print(get_likes_by_artist())

    # User history
    user_id = input("fk_user_id = ?\n")

    print("User history : " + str(user_id))
    print(get_user_history(user_id))

    # To test in database_manager
    db_driver.close_connection()
