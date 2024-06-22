#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)from 
the database hbtn_0e_0_usa sorted in ascending order by states.id.
"""

import MySQLdb
import sys

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
            charset="utf8"
        )
     except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'\
            ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
