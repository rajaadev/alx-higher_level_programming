#!/usr/bin/python3

"""
This script connects to a MySQL server and retrieves all states from the
database hbtn_0e_0_usa. The results are sorted by id and displayed.

Usage: ./0-select_states.py <username> <password> <database_name>
"""

import MySQLdb


def main():
    """
    Main function to connect to MySQL, retrieve states, and display results.
    """

    # Get credentials and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        # Create a cursor object
        cursor = db.cursor()

        # Execute query to select states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        result = cursor.fetchall()

        # Print results
        for row in result:
            print(row)

    except MySQLdb.Error as err:
        print("Error connecting to database:", err)
    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    main()
