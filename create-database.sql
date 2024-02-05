CREATE DATABASE boat_database;

CREATE USER boat_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE boat_database TO boat_admin;

 ALTER DATABASE boat_database OWNER TO boat_admin;

--execute by running psql -f create-database.sql 