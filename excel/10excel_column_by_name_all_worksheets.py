#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('selected_columns_all_worksheets')

my_columns = ['Customer Name', 'Sale Amount']
	
first_worksheet = True
with open_workbook(input_file) as workbook:
	data = [my_columns]
	index_of_cols_to_keep = []
	for worksheet in workbook.sheets():
		if first_worksheet:
			header = worksheet.row_values(0)
			for column_index in range(len(header)):
				if header[column_index] in my_columns:
					index_of_cols_to_keep.append(column_index)
			first_worksheet = False
		for row_index in range(1, worksheet.nrows):
			row_list = []
			for column_index in index_of_cols_to_keep:	
				cell_value = worksheet.cell_value(row_index, column_index)
				cell_type = worksheet.cell_type(row_index, column_index)
				if cell_type == 3:
					date_cell = xldate_as_tuple(cell_value,workbook.datemode)
					date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
					row_list.append(date_cell)
				else:
					row_list.append(cell_value)
			data.append(row_list)

	for list_index, output_list in enumerate(data):
		for element_index, element in enumerate(output_list):
			output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)