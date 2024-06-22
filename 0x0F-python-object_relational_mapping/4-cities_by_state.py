#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa.
The script takes 3 arguments: mysql username, mysql password, and database name.
The results are sorted in ascending order by cities.id.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute the query to get all cities with their corresponding states
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
