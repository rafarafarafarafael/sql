# import from CSV

# import the csv module
import csv
import sqlite3 as sql

with sql.connect("new.db") as conn:
	c = conn.cursor()

	# open the csv file and assign it to a variable
	employees = csv.reader(open("employees.csv", "rU"))

	# create a new table called employees
	c.execute("CREATE TABLE IF NOT EXISTS employees(firstname TEXT, lastname TEXT)")
	
	# insert data into table
	c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)

