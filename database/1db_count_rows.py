#!/usr/bin/env python3
import sqlite3

# Create an in-memory SQLite3 database
# Create a table called sales with four attributes
con = sqlite3.connect(':memory:')
query = """CREATE TABLE sales
			(customer VARCHAR(20), 
			 product VARCHAR(40),
			 amount FLOAT,
			 date DATE);"""
con.execute(query)
con.commit()

# Insert a few rows of data into the table
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
		('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
		('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
		('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()

# Query the sales table
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

# Count the number of rows in the output
row_counter = 0
for row in rows:
	print(row)
	row_counter += 1
print('Number of rows: {}'.format(row_counter))
