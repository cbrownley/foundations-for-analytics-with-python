#!/usr/bin/env python3
import csv
import MySQLdb
import sys

# Path to and name of a CSV output file
output_file = sys.argv[1]

# Connect to a MySQL database
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', \
user='root', passwd='my_password')
c = con.cursor()

# Create a file writer object and write the header row
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['Supplier Name','Invoice Number','Part Number','Cost','Purchase Date']
filewriter.writerow(header)

# Query the Suppliers table and write the output to a CSV file
c.execute("""SELECT * 
		FROM Suppliers 
		WHERE Cost > 700.0;""")
rows = c.fetchall()
for row in rows:
	filewriter.writerow(row)
