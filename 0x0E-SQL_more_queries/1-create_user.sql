-- Create user user_0d_1 IF NOT EXISTS
echo "CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';" | mysql -hlocalhost -uroot -p

-- GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';"| mysql -hlocalhost -uroot -p
