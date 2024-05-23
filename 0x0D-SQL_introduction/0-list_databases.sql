#!/bin/bash

# Create a temporary SQL script file
echo "SHOW DATABASES;" > /tmp/temp_list_databases.sql

# Execute the SQL script using the MySQL client
mysql -hlocalhost -uroot -p < /tmp/temp_list_databases.sql

# Remove the temporary SQL script file
rm /tmp/temp_list_databases.sql
