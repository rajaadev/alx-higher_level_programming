st Databases

This script lists all databases present in the MySQL server.

## Usage

```sh
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

This script uses the `SHOW DATABASES;` command to list all databases. You can execute it by piping the SQL script into the MySQL client on your terminal.

Make sure to have MySQL installed and running on your system before executing the script.

For execution, run:
```sh
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
