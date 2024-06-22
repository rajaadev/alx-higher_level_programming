#!/usr/bin/python3
"""
This script lists all databases of a MySQL server.
"""

import MySQLdb
import sys

def list_databases(hostname, username, password):
    """
    Connects to a MySQL server and lists all databases.

    Args:
        hostname (str): The host name or IP address of the MySQL server.
        username (str): The MySQL username to use for the connection.
        password (str): The password for the MySQL user.
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host=hostname,
            user=username,
            passwd=password
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query to get the list of databases
        cursor.execute("SHOW DATABASES")

        # Fetch all the rows from the executed query
        databases = cursor.fetchall()

        # Print each database name
        for database in databases:
            print(database[0])

        # Close the cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-list_databases.py <hostname> <username> <password>")
    else:
        list_databases(sys.argv[1], sys.argv[2], sys.argv[3])
