# -*- coding: utf-8 -*-

# Import the connect library from psycopg2
from psycopg2 import connect


def connect_database():

    # Declare connection instance
    connection = connect(
        dbname = "data-mining-project",
        user = "root",
        host = "127.0.0.1",
        password = "root"
    )

    return connection


def create_cursor(connection):
    # Declare a cursor object from the connection
    try :
        cursor = connection.cursor()
    except :
        print("Error :" + sys.exc_info()[0])

    return cursor


if __name__ == "__main__" :

    connection = connect_database()
    cursor = create_cursor(connection)

    # Test phase
    print("Testing schema")
    cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'")    # execute 'SHOW TABLES' (but data is not returned)
    tables = cursor.fetchall() # return data from last query
    print(tables)
    # End Test phase

    # Close the cursor object to avoid memory leaks
    cursor.close()

    # Close the connection as well
    connection.close()