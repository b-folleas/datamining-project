# -*- coding: utf-8 -*-

# Import the connect library from psycopg2

from psycopg2 import connect

CONNECTION = None

def connect_database():

    global CONNECTION

    # Declare connection instance
    CONNECTION = connect(
        dbname = "data-mining-project",
        user = "root",
        host = "127.0.0.1",
        password = "root"
    )

def create_cursor(connection):
    # Declare a cursor object from the connection
    try :
        cursor = connection.cursor()
    except ConnectionError:
        print("Error :", ConnectionError)

    return cursor

def close_connection(connection):
    # Close the connection as well
    connection.close()

def close_cursor(cursor):
    # Close the cursor object to avoid memory leaks
    cursor.close()


def insert(table, columns, values):

    # Create cursor
    cursor = create_cursor(CONNECTION)

    statement = "INSERT INTO " + table + " (" + str(', '.join(columns)) + ") VALUES (" + str(
        ', '.join(['%s'] * len(columns))) + ")"
    print(statement)

    try:
        cursor.execute(statement, values)

        # Then commit changes to the database
        CONNECTION.commit()
        print("Values inserted.")
    except ValueError:

        print("Error while inserting data :", ValueError)

    # Close the cursor object to avoid memory leaks
    cursor.close()


def select(statement):

    # Create cursor
    cursor = create_cursor(CONNECTION)

    try:
        cursor.execute(statement)
        result = cursor.fetchall() # return data from last query
        print(result)
    except ValueError:
        print("Error while fetching data :", ValueError)

    # Close the cursor object to avoid memory leaks
    cursor.close()

    return result


if __name__ == "__main__" :
    
    # Test phase
    connect_database()
    cursor = create_cursor(CONNECTION)

    print("Testing schema")
    cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'")    # execute 'SHOW TABLES' (but data is not returned)
    tables = cursor.fetchall() # return data from last query
    print(tables)

    close_cursor(cursor)

    # Close the connection as well
    close_connection(connection)

    # End Test phase
