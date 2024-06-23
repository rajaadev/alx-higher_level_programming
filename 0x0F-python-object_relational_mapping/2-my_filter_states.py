#!/usr/bin/python3
"""
A script that takes in an argument and 
displays all values in the states
table of hbtn_0e_0_usa 
where name matches the argument.
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
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute the query to get states matching the argument
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY \
            states.id ASC".format(state_name)
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
