#!/usr/bin/python3
"""
A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
     except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute query to get states with names starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'\
            ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
