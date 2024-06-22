#!/usr/bin/python3
"""
A script that lists all cities of a given state from the database hbtn_0e_4_usa.
The script takes 4 arguments: mysql username, mysql password, database name, and state name (SQL injection free!)
The results are sorted in ascending order by cities.id.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials, database name, and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute the query to get all cities of the given state
    query = """
    SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC)
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    """
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()[0]

    # Print the result
    if result:
        print(result)
    else:
        print("No cities found for the given state.")

    # Close the cursor and database connection
    cursor.close()
    db.close()

