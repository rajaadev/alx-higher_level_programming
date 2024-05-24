-- Script to print the full description of the table first_table from the database hbtn_0c_0
SELECT TABLE_NAME AS 'Table', CREATE_TABLE AS 'Create Table'
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = '<database_name>'
AND TABLE_NAME = 'first_table';
