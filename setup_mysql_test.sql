-- create test server for project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create new user for db
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all priviliges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant select privileges to performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
