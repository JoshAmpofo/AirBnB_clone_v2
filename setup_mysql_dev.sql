-- This script will create an MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create new user if already non-existent
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant user privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant select privileges on `performance_schema`
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
