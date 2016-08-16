#!/usr/bin/env python3
import csv
import sqlite3
import sys

# Path to and name of a CSV input file
input_file = sys.argv[1]

# Create an in-memory SQLite3 database
# Create a table called sales with four attributes
con = sqlite3.connect(':memory:')
query = """CREATE TABLE IF NOT EXISTS sales
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
for tuple in data:
	print(tuple)
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()
	
# Read the CSV file and update the specific rows
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		data.append(row[column_index])
	print(data)
	con.execute("UPDATE sales SET amount=?, date=? WHERE customer=?;", data)
con.commit()

# Query the sales table
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()
for row in rows:
	output = []
	for column_index in range(len(row)):
		output.append(str(row[column_index]))
	print(output)