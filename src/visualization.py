# -*- coding: utf-8 -*-

import database_manager as db_manager
import database_driver as db_driver
import pandas as pd
import matplotlib.pyplot as plot


REPORT_FOLDER = '../../Report'

def plot_users_dashboard():
    # Building a dataframe from users_dashboard
    
    users_dashboard_array = db_manager.get_users_dashboard()
    print('plot_users_dashboard')
    print(users_dashboard_array)
    if users_dashboard_array != None or len(users_dashboard_array) > 1 :

        df_users_dashboard = pd.DataFrame(users_dashboard_array,
                                        columns=['paintings_number', 'user_id', 'username'])

        df_users_dashboard = df_users_dashboard.astype(dtype={"paintings_number": "int64",
                                                            "user_id": "<U200",
                                                            "username": "<U200"})

        print("Users Dashboard")
        # print(df_users_dashboard)
        
        df_users_dashboard.plot(0, frame_on=False) # no visible frame
        df_users_dashboard.xaxis.set_visible(False) # hide the x axis
        df_users_dashboard.yaxis.set_visible(False) # hide the y axis

        table(df_users_dashboard)

        filename = "users_dashboard"
        plot.savefig(REPORT_FOLDER + filename + ".png")

    else :
        print(users_dashboard_array)
        print('No data for users dashboard.')
    

def plot_paintings_through_time():
    # Building a dataframe from paintings through time
    df_paintings_through_time = pd.DataFrame(db_manager.get_paintings_through_time(),
                                             columns=['date', 'paintings_number', 'all_painting'])

    df_paintings_through_time['date'] = pd.to_datetime(
        df_paintings_through_time['date'], format='%Y-%m-%d')
    df_paintings_through_time = df_paintings_through_time.astype(dtype={"paintings_number": "int64",
                                                                        "all_painting": "int64"})
    print("Number of paintings through time (by date)")
    print(df_paintings_through_time)

    # Displaying a graph from this dataframe (paintings through time)

    df_paintings_through_time.plot(
        kind='line', x='date', y='all_painting', color='red')
    plot.title("Number of paintings Evolution Through Time")
    plot.xlabel('date', fontsize=16)
    plot.ylabel('count', fontsize=16)

    filename = "paintings_through_time"
    plot.savefig(REPORT_FOLDER + filename + ".png")

def plot_likes_by_artist():
    # Building a dataframe from likes group by artist

    df_likes_by_artist = pd.DataFrame(db_manager.get_likes_by_artist(),
                                      columns=['artist_id', 'artist_name', 'n_likes'])

    df_likes_by_artist = df_likes_by_artist.astype(dtype={"artist_name": "<U200",
                                                          "n_likes": "int64"})
    print("Number of likes by artist")
    print(df_likes_by_artist)

    df_likes_by_artist.plot(kind='bar', x='artist_name',
                            y='n_likes', color='blue')
    plot.title("Number of liked images by artist")
    plot.xlabel('Artists', fontsize=16)
    plot.ylabel('likes', fontsize=16)

    filename = "likes_by_artist"
    plot.savefig(REPORT_FOLDER + filename + ".png")


def plot_user_history(user_id):
    '''Display a table of the information about a user given in parameter.\n
    :param user_id: (int) the id of the user to display the information.\n
    :return: None.
    '''
    user_history_array = db_manager.get_user_history(user_id)
    print('plot_users_dashboard')
    print(user_history_array)
    if user_history_array != None or len(user_history_array) > 1 :
        df_user_history = pd.DataFrame(user_history_array,
                                    columns=['fav', 'painting_id', 'artist_id', 'artist_name', 'artist_century', 'artist_genre', 'artist_nationality', 'painting_date', 'painting_width', 'painting_height', 'painting_orientation', 'painting_flash'])

        df_user_history = df_user_history.astype(dtype={'fav': 'bool',
                                                        'painting_id': 'int64',
                                                        'artist_id': 'int64',
                                                        'artist_name': "<U200",
                                                        'artist_century': "<U200",
                                                        'artist_genre': "<U200",
                                                        'artist_nationality': "<U200",
                                                        'painting_date': 'datetime64',
                                                        'painting_width': 'int64',
                                                        'painting_height': 'int64',
                                                        'painting_orientation': 'int64',
                                                        'painting_flash': 'int64'
                                                        })
        print("User history : " + str(user_id))
        # print(df_user_history)

        df_user_history.plot(1, frame_on=False) # no visible frame
        df_user_history.xaxis.set_visible(False) # hide the x axis
        df_user_history.yaxis.set_visible(False) # hide the y axis

        table(df_user_history)


        filename = "users_dashboard"
        plot.savefig(REPORT_FOLDER + filename + ".png")
    else :
        print(user_history_array)
        print('No data for this user.')

if __name__ == "__main__":

    # To test only visualization
    db_driver.connect_database()

    # Building a dataframe from users_dashboard
    df_users_dashboard = pd.DataFrame(db_manager.get_users_dashboard(),
                                      columns=['paintings_number', 'user_id', 'username'])

    df_users_dashboard = df_users_dashboard.astype(dtype={"paintings_number": "int64",
                                                          "user_id": "<U200",
                                                          "username": "<U200"})

    print("Users Dashboard")
    print(df_users_dashboard)

    ax = plot(111, frame_on=False) # no visible frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis

    table(ax, df_users_dashboard)

    filename = "users_dashboard"
    plot.savefig(REPORT_FOLDER + filename + ".png")


    # Building a dataframe from paintings through time
    df_paintings_through_time = pd.DataFrame(db_manager.get_paintings_through_time(),
                                             columns=['date', 'paintings_number', 'all_painting'])

    df_paintings_through_time['date'] = pd.to_datetime(
        df_paintings_through_time['date'], format='%Y-%m-%d')
    df_paintings_through_time = df_paintings_through_time.astype(dtype={"paintings_number": "int64",
                                                                        "all_painting": "int64"})
    print("Number of paintings through time (by date)")
    print(df_paintings_through_time)

    # Displaying a graph from this dataframe (paintings through time)

    df_paintings_through_time.plot(
        kind='line', x='date', y='all_painting', color='red')
    plot.title("Number of paintings Evolution Through Time")
    plot.xlabel('date', fontsize=16)
    plot.ylabel('count', fontsize=16)

    filename = "paintings_through_time"
    plot.savefig(REPORT_FOLDER + filename + ".png")

    # Building a dataframe from likes group by artist

    df_likes_by_artist = pd.DataFrame(db_manager.get_likes_by_artist(),
                                      columns=['artist_id', 'artist_name', 'n_likes'])

    df_likes_by_artist = df_likes_by_artist.astype(dtype={"artist_name": "<U200",
                                                          "n_likes": "int64"})
    print("Number of likes by artist")
    print(df_likes_by_artist)

    df_likes_by_artist.plot(kind='bar', x='artist_name',
                            y='n_likes', color='blue')
    plot.title("Number of liked images by artist")
    plot.xlabel('Artists', fontsize=16)
    plot.ylabel('likes', fontsize=16)

    filename = "likes_by_artist"
    plot.savefig(REPORT_FOLDER + filename + ".png")

    # Building a dataframe from users and their history
    user = input("fk_user_id = ?\n")

    df_user_history = pd.DataFrame(db_manager.get_user_history(user),
                                   columns=['fav', 'painting_id', 'artist_id', 'artist_name', 'painting_date', 'painting_width', 'painting_height'])

    df_user_history = df_user_history.astype(dtype={'fav': 'bool',
                                                    'painting_id': 'int64',
                                                    'artist_id': 'int64',
                                                    'artist_name': "<U200",
                                                    'painting_date': 'datetime64',
                                                    'painting_width': 'int64',
                                                    'painting_height': 'int64'})
    print("User history : " + str(user))
    print(df_user_history)

    # To test only visualization
    db_driver.close_connection()
