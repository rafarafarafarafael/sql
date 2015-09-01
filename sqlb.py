# import sqlite3 module
import sqlite3 as sql

# opens connection to database
connection = sql.connect("new.db")
# create 
c = connection.cursor()
c.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
c.execute ("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

# commit the changes
connection.commit()

# close the database
connection.close()