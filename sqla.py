# Create a SQLite3 database and table
# import the sqlite3 library
import sqlite3 as sql

# create a new database if the database doesnt exist already
conn = sql.connect("new.db")

# get a cursor object used to execute sql commands
cursor = conn.cursor()

# create a table
cursor.execute("CREATE TABLE population(city TEXT, state TEXT, population INT)")

# close database connection 
conn.close()
