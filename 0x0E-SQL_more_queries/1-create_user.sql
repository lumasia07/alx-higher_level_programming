-- Creates a server user user_0d_1
-- Grants all privileges to the user
-- Flushes privileges to apply changes
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
 IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;

