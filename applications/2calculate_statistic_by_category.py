#!/usr/bin/env python3
import csv
import sys
from datetime import date, datetime

def date_diff(date1, date2):
	try:
		diff = str(datetime.strptime(date1, '%m/%d/%Y') - \
				datetime.strptime(date2, '%m/%d/%Y')).split()[0]
	except:
		diff = 0
	if diff == '0:00:00':
		diff = 0
	return diff
	
input_file = sys.argv[1]
output_file = sys.argv[2]

packages = {}
previous_name = 'N/A'
previous_package = 'N/A'
previous_package_date = 'N/A'
first_row = True
today = date.today().strftime('%m/%d/%Y')

with open(input_file, 'r', newline='') as input_csv_file:
	filereader = csv.reader(input_csv_file)
	header = next(filereader)
	for row in filereader:
		current_name = row[0]
		current_package = row[1]
		current_package_date = row[3]
		if current_name not in packages:
			packages[current_name] = {}
		if current_package not in packages[current_name]:
			packages[current_name][current_package] = 0
		if current_name != previous_name:
			if first_row:
				first_row = False
			else:
				diff = date_diff(today, previous_package_date)
				if previous_package not in packages[previous_name]:
					packages[previous_name][previous_package] = int(diff)
				else:
					packages[previous_name][previous_package] += int(diff)
		else:
			diff = date_diff(current_package_date, previous_package_date)
			packages[previous_name][previous_package] += int(diff)
		previous_name = current_name
		previous_package = current_package
		previous_package_date = current_package_date

header = ['Customer Name', 'Category', 'Total Time (in Days)']
with open(output_file, 'w', newline='') as output_csv_file:
	filewriter = csv.writer(output_csv_file)
	filewriter.writerow(header)
for customer_name, customer_name_value in packages.items():
	for package_category, package_category_value in packages[customer_name].items():
		row_of_output = []
		print(customer_name, package_category, package_category_value)
		row_of_output.append(customer_name)
		row_of_output.append(package_category)
		row_of_output.append(package_category_value)
		filewriter.writerow(row_of_output)