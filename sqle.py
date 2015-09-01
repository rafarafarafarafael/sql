# insert command with Error Handler

# import sqlite3 module
import sqlite3 as sql

# opens connection to database
conn = sql.connect("new.db")
# create 
c = conn.cursor()

try:
	# insert data
	c.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
	c.execute ("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")

	# commit the changes
	conn.commit()

except sql.OperationalError as e:
	print "Oops! Something went wrong. Try again..."
	print e
# close the database
conn.close()