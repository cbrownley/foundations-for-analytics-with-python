#!/usr/bin/python
import string
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

messages = {}
notes = []
with open(input_file, 'rU') as text_file:
	for row in text_file:
		if '[Note]' in row:
			n = 2
			groups = row.split(' ')
			date_time = ' '.join(groups[:n])
			rest_of_line_string = ' '.join(groups[n:])
			rest_of_line_list = rest_of_line_string.split(' ', 2)
			note = rest_of_line_list[2].strip('\n').strip()
			row_list = []
			row_list.append(date_time)
			row_list.append(note)
			print row_list
			
			day = row_list[0]
			note = row_list[1]
			if note not in notes:
				notes.append(note)
			if day not in messages:
				messages[day] = {}
			if note not in messages[day]:
				messages[day][note] = 1
			else:
				messages[day][note] += 1

#filewriter = open(output_file, 'wb')
header = ['Date']
header.extend(notes)
header = ','.join(map(str,header)) + '\n'
print header
#filewriter.write(header)
for day, day_value in messages.items():
	row_of_output = []
	row_of_output.append(day)	
	for index in range(len(notes)):
		if notes[index] in day_value.keys():
			row_of_output.append(day_value[notes[index]])
		else:
			row_of_output.append(0)
	output = ','.join(map(str,row_of_output)) + '\n'
	print output
	#filewriter.write(output)
#filewriter.close()