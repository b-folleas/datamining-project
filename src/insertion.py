import database_connection

CONNEXION = ''


def db_open():
    global CONNEXION
    CONNEXION = database_connection.connect_database()


def db_close():
    global CONNEXION
    # Close the connection as well
    CONNEXION.close()


def insert(table, columns, values):
    global CONNEXION

    db_open()

    # Connect to database

    cursor = database_connection.create_cursor(CONNEXION)

    statement = "INSERT INTO " + table + " (" + str(', '.join(columns)) + ") VALUES (" + str(
        ', '.join(['%s'] * len(columns))) + ")"
    print(statement)

    try:

        cursor.execute(statement, values)

        # Then commit changes to the database
        CONNEXION.commit()
        print("Values inserted.")
    except ValueError:

        print("Error while inserting datas :", ValueError)

    # Close the cursor object to avoid memory leaks
    cursor.close()

    db_close()
