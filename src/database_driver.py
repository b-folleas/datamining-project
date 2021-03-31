# -*- coding: utf-8 -*-

# Import the connect library from psycopg2

from psycopg2 import connect

CONNECTION = None


def connect_database():
    """Standard method to connect to the database.\n
    The dbname, user, host, password are the specific attributes to specify.\n
    :return: None.
    """

    global CONNECTION

    # Declare connection instance
    CONNECTION = connect(
        dbname="data-mining-project",
        user="root",
        host="127.0.0.1",
        password="root"
    )


def create_cursor(connection):
    """Declare a cursor object from the connection.\n
    :return: cursor.
    """
    try:
        cursor = connection.cursor()
    except ConnectionError:
        print("Error :", ConnectionError)

    return cursor


def close_connection():
    '''Close the connection to the database.\n
    :return: None.
    '''
    CONNECTION.close()


def close_cursor(cursor):
    '''Close the cursor for the database operations.\n
    :param cursor: cursor.\n
    :return: None.
    '''
    # Close the cursor object to avoid memory leaks
    cursor.close()


def insert(table, columns, values):
    '''Insert data into the table indicated for the current connection database.\n
    :param table: table in which insert data.\n
    :param columns: list of columns of the table.\n
    :param values: list of values corresponding to the columns.\n
    :return: None.
    '''
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


def select(statement): #TODO: Rename to execute(statement)
    '''Execute the statement and print the returning rows.\n
    :param statement: the SQL query to execute.\n
    :return: Requested rows or None.
    '''
    # Create cursor
    cursor = create_cursor(CONNECTION)

    try:
        cursor.execute(statement)
        CONNECTION.commit()
        print("statement executed")
        if cursor.rowcount > 0 :
            result = cursor.fetchall() # return data from last query
        else :
            return None    
    except ValueError:
        print("Error while fetching data :", ValueError)

    # Close the cursor object to avoid memory leaks
    cursor.close()

    return result

def prepared_execute(statement, name, args):
    # Create cursor
    cursor = create_cursor(CONNECTION)

    try:
        query = "PREPARE " + name + " AS " + statement

        print(query)
        cursor.execute(query)

        cursor.execute("EXECUTE " + name + ' (' + args + ')')
        if cursor.rowcount > 0 :
            result = cursor.fetchall() # return data from last query
        else :
            return None
    except ValueError:
        print("Error while fetching data :", ValueError)

    # Close the cursor object to avoid memory leaks
    cursor.close()

    return result


if __name__ == "__main__":

    # Test phase
    connect_database()
    cursor = create_cursor(CONNECTION)

    print("Testing schema")
    # execute 'SHOW TABLES' (but data is not returned)
    cursor.execute(
        "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'")
    tables = cursor.fetchall()  # return data from last query
    print(tables)

    close_cursor(cursor)

    # Close the connection as well
    close_connection()

    # End Test phase
