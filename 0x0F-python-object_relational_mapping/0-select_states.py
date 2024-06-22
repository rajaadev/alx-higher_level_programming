#!/usr/bin/python3

import MySQLdb

if __name__ == "__main__":
    # Get credentials and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
        )
    except MySQLdb.Error as err:
        print("Error connecting to database:", err)
        exit(1)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select all states ordered by id
    try:
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        result = cursor.fetchall()
    except MySQLdb.Error as err:
        print("Error retrieving states:", err)
        db.close()
        exit(1)

    # Print the results
    for row in result:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
