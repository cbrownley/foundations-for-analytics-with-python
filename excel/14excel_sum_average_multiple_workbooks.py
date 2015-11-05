#!/usr/bin/env python3
import glob
import os
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_folder = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('sums_and_averages')

all_data = []
sales_column_index = 3

header = ['workbook', 'worksheet', 'worksheet_total', 'worksheet_average',\
 					'workbook_total', 'workbook_average']
all_data.append(header)

for input_file in glob.glob(os.path.join(input_folder, '*.xls*')):
	with open_workbook(input_file) as workbook:
		list_of_totals = []
		list_of_numbers = []
		workbook_output = []
		for worksheet in workbook.sheets():
			total_sales = 0
			number_of_sales = 0
			worksheet_list = []
			worksheet_list.append(os.path.basename(input_file))
			worksheet_list.append(worksheet.name)
			for row_index in range(1,worksheet.nrows):
				try:
					total_sales += float(str(worksheet.cell_value(row_index,sales_column_index)).strip('$').replace(',',''))
					number_of_sales += 1.
				except:
					total_sales += 0.
					number_of_sales += 0.
			average_sales = '%.2f' % (total_sales / number_of_sales)
			worksheet_list.append(total_sales)
			worksheet_list.append(float(average_sales))
			list_of_totals.append(total_sales)
			list_of_numbers.append(float(number_of_sales))
			workbook_output.append(worksheet_list)
		workbook_total = sum(list_of_totals)
		workbook_average = sum(list_of_totals)/sum(list_of_numbers)
		for list_element in workbook_output:
			list_element.append(workbook_total)
			list_element.append(workbook_average)
		all_data.extend(workbook_output)
		
for list_index, output_list in enumerate(all_data):
	for element_index, element in enumerate(output_list):
		output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)