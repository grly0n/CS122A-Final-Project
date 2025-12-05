DROP DATABASE IF EXISTS cs122a;
CREATE DATABASE cs122a;

DROP USER IF EXISTS 'test'@'localhost';
CREATE USER 'test'@'localhost' IDENTIFIED BY 'password';
GRANT ALL on cs122a.* to 'test'@'localhost';