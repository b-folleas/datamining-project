import database_connection


def insert (table, columns, values) :
    # Connect to database
    connection = database_connection.connect_database()
    cursor = database_connection.create_cursor(connection)

    statement = "INSERT INTO " + table + " (" + str(', '.join(columns)) + ") VALUES (" + str(', '.join(['%s'] * len(columns))) + ")"
    
    print(statement)
    
    cursor.execute(statement, values)

    # Then commit changes to the database
    connection.commit() # Very important
    print("Values inserted.")

    # Close the cursor object to avoid memory leaks
    cursor.close()

    # Close the connection as well
    connection.close()


    

    