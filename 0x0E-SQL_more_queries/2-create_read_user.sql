-- Creates database hbtn_0d_2
-- Creates a user user_0d_2
-- Grants SELECT privilege to database
-- Script should not fail if either database or user does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
 IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
