#!/usr/bin/python3
"""
A script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
This script is safe from SQL injection.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute the query to get states matching the argument using parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
