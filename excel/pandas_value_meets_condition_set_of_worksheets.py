#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_sheets = [0,1]
threshold = 1900.0

data_frame = pd.read_excel(input_file, sheetname=my_sheets, index_col=None)

row_list = []
for worksheet_name, data in data_frame.items():
	row_list.append(data[data['Sale Amount'].astype(float) > threshold])
filtered_rows = pd.concat(row_list, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='set_of_worksheets', index=False)
writer.save()