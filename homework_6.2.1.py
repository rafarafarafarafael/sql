import sqlite3 as sql

with sql.connect("cars.db") as connct:
	c = connct.cursor()

	c.execute("CREATE TABLE cars(Make TEXT, Model TEXT, Quantity INT)")
	c.execute("INSERT INTO cars VALUES('Honda', 'Fit', 1)")
