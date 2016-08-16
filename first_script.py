#!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
import glob
import os

# Print a simple string
print("Output #1: I'm excited to learn Python.")

# Add two numbers together
x = 4
y = 5
z = x + y
print("Output #2: Four plus five equals {0:d}.".format(z))

# Add two lists together
a = [1, 2, 3, 4]
b = ["first", "second", "third", "fourth"]
c = a + b
print("Output #3: {0}, {1}, {2}".format(a, b, c))

# INTEGERS
x = 9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
print("Output #6: {0}".format(int(8.3)/int(2.7)))

# FLOATING-POINT NUMBERS
print("Output #7: {0:.3f}".format(8.3/2.7))
y = 2.5*4.8
print("Output #8: {0:.1f}".format(y))
r = 8/float(3)
print("Output #9: {0:.2f}".format(r))
print("Output #10: {0:.4f}".format(8.0/3))

# Some mathematical functions available in the math module
print("Output #11: {0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.1f}".format(sqrt(81)))

# STRINGS
# A string with single quotes, so include a backslash before the single quote
print("Output #14: {0:s}".format('I\'m enjoying learning Python'))

# A one-line string, but if the string is long and running off the page on the right
# you can use a "\" to separate the long string into smaller strings on separate lines
print("Output #15: {0:s}".format("This is a long string.  Without the backslash \
it would run off of the page on the right in the text editor and be very \
difficult to read and edit.  By using the backslash you can split the long \
string into smaller strings on separate lines so that the whole string is easy \
to view in the text editor."))

# Use triple single or double quotes if you want the string to span multiple lines
# and you don't want to use the "\"
print("Output #16: {0:s}".format('''You can use triple single quotes
for multi-line comment strings'''))

print("Output #17: {0:s}".format("""You can also use triple double quotations
for multi-line comment strings"""))

# Add two strings together
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("Output #18: {0:s}".format(sentence))

# Repeat a string four times
print("Output #19: {0:s} {1:s}{2:s}".format("She is", "very "*4, "beautiful."))

# Determine the number of characters in a string, including spaces and punctuation
m = len(sentence)
print("Output #20: {0:d}".format(m))

# split()
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ", 2)
print("Output #21: {0}".format(string1_list1))
print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
.format(string1_list2[0], string1_list2[1], string1_list2[2])

string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1], string2_list[5], string2_list[-1]))

# join()
print("Output #25: {0}".format(','.join(string2_list)))

# strip()
string3 = "   Remove unwanted characters from this string\t\t    \n"
print("Output #26: string3: {0:s}".format(string3))
string3_lstrip = string3.lstrip()
print("Output #27: lstrip: {0:s}".format(string3_lstrip))
string3_rstrip = string3.rstrip()
print("Output #28: rstrip: {0:s}".format(string3_rstrip))
string3_strip = string3.strip()
print("Output #29: strip: {0:s}".format(string3_strip))

string4 = "$$Here's another string that has unwanted characters.__---++"
print("Output #30: {0:s}".format(string4))
string4 = "$$The unwanted characters have been removed.__---++"
string4_strip = string4.strip('$_-+')
print("Output #31: {0:s}".format(string4_strip))

# replace()
string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ", "!@!")
print("Output #32 (with !@!): {0:s}".format(string5_replace))
string5_replace = string5.replace(" ", ",")
print("Output #33 (with commas): {0:s}".format(string5_replace))

# lower(), upper(), capitalize()
string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))

string7 = "Here's what Happens when You Use UPPER."
print("Output #35: {0:s}".format(string7.upper()))

string8 = "here's WHAT Happens WHEN you use Capitalize."
print("Output #36: {0:s}".format(string8.capitalize()))
string8_list = string8.split()
print("Output #37 (on each word):")
for word in string8_list:
    print("{0:s}".format(word.capitalize()))

# REGULAR EXPRESSIONS / PATTERN MATCHING
# Count the number of times a pattern appears in a string
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
    	count += 1
print("Output #38: {0:d}".format(count))

# Print the pattern each time it is found in the string
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I)
print("Output #39:")
for word in string_list:
    if pattern.search(word):
		print("{:s}".format(pattern.search(word).group('match_word')))

# Substitute the letter "a" for the word "the" in the string
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print("Output #40: {:s}".format(pattern.sub("a", string)))

# DATES
# Print today's date, as well as the year, month, and day elements
today = date.today()
print("Output #41: today: {0!s}".format(today))
print("Output #42: {0!s}".format(today.year))
print("Output #43: {0!s}".format(today.month))
print("Output #44: {0!s}".format(today.day))
current_datetime = datetime.today()
print("Output #45: {0!s}".format(current_datetime))

# Calculate a new date using a timedelta
one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output #46: yesterday: {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

# Calculate the amount of time between two dates and grab the first element, the number of days
date_diff = today - yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split()[0]))

# Create a string with a specific format from a date object
print("Output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("Output #51: {:s}".format(today.strftime('%b %d, %Y')))
print("Output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {:s}".format(today.strftime('%B %d, %Y')))

# Create a datetime object with a specific format
# from a string representing a date
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')

# Two datetime objects and two date objects
# based on the four strings that have different date formats
print("Output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))

# Show the date portion only
print("Output #56: {!s}".format(datetime.date(datetime.strptime\
(date3, '%Y-%m-%d')))
print("Output #57: {!s}".format(datetime.date(datetime.strptime\
(date4, '%B %d, %Y')))

# LISTS
# Use square brackets to create a list
# len() counts the number of elements in a list
# max() and min() find the maximum and minimum numbers in numeric lists
# count() counts the number of times a value appears in a list
a_list = [1, 2, 3]
print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elements.".format(len(a_list)))
print("Output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}.".format(min(a_list)))
another_list = ['printer', 5, ['star', 'circle', 9]]
print("Output #62: {}".format(another_list))
print("Output #63: another_list also has {} elements.".format(len(another_list)))
print("Output #64: 5 is in another_list {} time.".format(another_list.count(5)))

# Use list indices to access specific values in a list
# [0] is the first value; [-1] is the last value
print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[1]))
print("Output #67: {}".format(a_list[2]))
print("Output #68: {}".format(a_list[-1]))
print("Output #69: {}".format(a_list[-2]))
print("Output #70: {}".format(a_list[-3]))
print("Output #71: {}".format(another_list[2]))
print("Output #72: {}".format(another_list[-1]))

# Use list slices to access a subset of list values
# Do not include the starting indice to start from the beginning
# Do not include the ending indice to go all of the way to the end
print("Output #73: {}".format(a_list[0:2]))
print("Output #74: {}".format(another_list[:2]))
print("Output #75: {}".format(a_list[1:3]))
print("Output #76: {}".format(another_list[1:]))

# Use [:] to make a copy of a list
a_new_list = a_list[:]
print("Output #77: {}".format(a_new_list))

# Use + to add two or more lists together
a_longer_list = a_list + another_list    # to add lists together
print("Output #78: {}".format(a_longer_list))

# Use 'in' and 'not in' to check whether specific values are or are not in a list
a = 2 in a_list
print("Output #79: {}".format(a))
if 2 in a_list:
    print("Output #80: 2 is in {}.".format(a_list))
b = 6 not in a_list
print("Output #81: {}".format(b))
if 6 not in a_list:
    print("Output #82: 6is not in {}.".format(a_list))

# Use append() to add additional values to the end of the list
# Use remove() to remove specific values from the list
# Use pop() to remove values from the end of the list
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))
a_list.remove(5)
print("Output #84: {}".format(a_list))
a_list.pop()
a_list.pop()
print("Output #85: {}".format(a_list))

# Use reverse() to reverse a list, in-place, meaning it changes the list
# To reverse a list without changing the original list, make a copy first
a_list.reverse()
print("Output #86: {}".format(a_list))
a_list_copy = a_list[:]
a_list_copy.reverse()
print("Output #87: {}".format(a_list_copy))

# Use sort() to sort a list, in-place, meaning it changes the list
# To sort a list without changing the original list, make a copy first
unordered_list = [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
print("Output #88: {}".format(unordered_list))
list_copy = unordered_list[:]
list_copy.sort()
print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unordered_list))

# Use sorted() to sort a collection of lists by a position in the lists
my_lists = [[1,2,3,4], [4,3,2,1], [2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
print("Output #91: {}".format(my_lists_sorted_by_index_3))

# Use itemgetter() to sort a collection of lists by two index positions
my_lists = [[123,2,2,444], [22,6,6,444], [354,4,4,678], [236,5,5,678], \
[578,1,1,290], [461,1,1,290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3,0))
print("Output #92: {}".format(my_lists_sorted_by_index_3_and_0))

# TUPLES
# Use parentheses to create a tuple
my_tuple = ('x', 'y', 'z')
print("Output #93: {}".format(my_tuple))
print("Output #94: my_tuple has {} elements".format(len(my_tuple)))
print("Output #95: {}".format(my_tuple[1]))
longer_tuple = my_tuple + my_tuple
print("Output #96: {}".format(longer_tuple))

# Unpack tuples with the left-hand side of an assignment operator
one, two, three = my_tuple
print("Output #97: {0} {1} {2}".format(one, two, three))
var1 = 'red'
var2 = 'robin'
print("Output #98: {} {}".format(var1, var2))
# Swap values between variables
var1, var2 = var2, var1
print("Output #99: {} {}".format(var1, var2))

# Convert tuples to lists and lists to tuples
my_list = [1, 2, 3]
my_tuple = ('x', 'y', 'z')
print("Output #100: {}".format(tuple(my_list)))
print("Output #101: {}".format(list(my_tuple)))

# DICTIONARIES
# Use curly braces to create a dictionary
# Use a colon between keys and values in each pair
# len() counts the number of key-value pairs in a dictionary
empty_dict = { }
a_dict = {'one':1, 'two':2, 'three':3}
print("Output #102: {}".format(a_dict))
print("Output #103: a_dict has {!s} elements".format(len(a_dict)))
another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}
print("Output #104: {}".format(another_dict))
print("Output #105: another_dict also has {!s} elements"\
.format(len(another_dict)))

# Use keys to access specific values in a dictionary
print("Output #106: {}".format(a_dict['two']))
print("Output #107: {}".format(another_dict['z']))

# Use copy() to make a copy of a dictionary
a_new_dict = a_dict.copy()
print("Output #108: {}".format(a_new_dict))

# Use keys(), values(), and items() to access
# a dictionary's keys, values, and key-value pairs, respectively
print("Output #109: {}".format(a_dict.keys()))
a_dict_keys = a_dict.keys()
print("Output #110: {}".format(a_dict_keys))
print("Output #111: {}".format(a_dict.values()))
print("Output #112: {}".format(a_dict.items()))

# Use in, not in, and get to test
# whether a key is in a dictionary
if 'y' in another_dict:
	print("Output #114: y is a key in another_dict: {}."\
    .format(another_dict.keys()))

if 'c' not in another_dict:
	print("Output #115: c is not a key in another_dict: {}."\
    .format(another_dict.keys()))

print("Output #116: {!s}".format(a_dict.get('three')))
print("Output #117: {!s}".format(a_dict.get('four')))
print("Output #118: {!s}".format(a_dict.get('four', 'Not in dict')))

# Use sorted() to sort a dictionary
# To sort a dictionary without changing the original dictionary, 
# make a copy first
print("Output #119: " + str(a_dict)
dict_copy = a_dict.copy()
ordered_dict1 = sorted(dict_copy.items(), key=lambda item: item[0])
print("Output #120 (order by keys): {}".format(ordered_dict1))
ordered_dict2 = sorted(dict_copy.items(), key=lambda item: item[1])
print("Output #121 (order by values): {}".format(ordered_dict2))
ordered_dict3 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=True)
print("Output #122 (order by values, descending): {}".format(ordered_dict3))
ordered_dict4 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=False)
print("Output #123 (order by values, ascending): {}".format(ordered_dict4))

# CONTROL FLOW
# if-else statement
x = 5
if x > 4 or x != 9:
    print("Output #124: {}".format(x))
else:
    print("Output #125: x is not greater than 4")

# if-elif-else statement
if x > 6:
    print("Output #126: x is greater than six")
elif x > 4 and x == 5:
    print("Output #127: {}".format(x*x))
else:
    print("Output #128: x is not greater than 4")
    
# for loop
y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', \
'Nov', 'Dec']
z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta', \
'Holly', 'Isabel', 'Jenny']

print("Output #129:")
for month in y:
    print("{!s".format(month))

print("Output #130: (index value: name in list)")
for i in range(len(z)):
    print("{0!s}: {1:s}".format(i, z[i]))

print("Output #131: (access elements in y with z's index values)")
for j in range(len(z)):
    if y[j].startswith('J'):
        print("{!s}".format(y[j]))

print("Output #132:")
for key, value in another_dict.items():
    print("{0:s}, {1}".format(key, value))

# compact for loops
# list, set, and dictionary comprehensions
# Select specific rows using a list comprehension
my_data = [[1,2,3], [4,5,6], [7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print("Output #133 (list comprehension): {}".format(rows_to_keep))

# Select a set of unique tuples in a list using a set comprehension
my_data = [(1,2,3), (4,5,6), (7,8,9), (7,8,9)]
set_of_tuples1 = {x for x in my_data}
print("Output #134 (set comprehension): {}".format(set_of_tuples1))
set_of_tuples2 = set(my_data)
print("Output #135 (set function): {}".format(set_of_tuples2))

# Select specific key-value pairs using a dictionary comprehension
my_dictionary = {'customer1': 7, 'customer2': 9, 'customer3': 11}
my_results = {key : value for key, value in my_dictionary.items() if \
value > 10}
print("Output #136 (dictionary comprehension): {}".format(my_results))

# while loop
print("Output #137:")
x = 0
while x < 11:
    print("{!s}".format(x))
    x += 1

# FUNCTIONS
# Calculate the mean of a sequence of numeric values
def getMean(numericValues):
    return sum(numericValues)/len(numericValues) if len(numericValues) > 0 \
    else float('nan')

my_list = [2, 2, 4, 4, 6, 6, 8, 8]
print("Output #138 (mean): {!s}".format(getMean(my_list)))

#import numpy as np
#print np.mean(my_list)

# EXCEPTIONS
# Calculate the mean of a sequence of numeric values
def getMean(numericValues):
    return sum(numericValues)/len(numericValues)

my_list2 = [ ]
# Short version
try:
    print("Output #139: {}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
    print("Output #139 (Error): {}".format(float('nan')))
    print("Output #139 (Error): {}".format(detail))

# Long version
try:
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print("Output #140 (Error): {}".format(float('nan')))
    print("Output #140 (Error): {}".format(detail))
else:
    print("Output #140 (The mean is): {}".format(result))
finally:
    print("Output #140 (Finally): The finally block is executed every time")

# READ A FILE
# Read a single text file
#input_file = sys.argv[1]

## Read a text file (older method) ##
#print("Output #141:")
#filereader = open(input_file, 'r', newline='')
#for row in filereader:
#    print("{}".format(row.strip()))
#filereader.close()

## Read a text file (newer method) ##
#print("Output #142:")
#with open(input_file, 'r', newline='') as filereader:
#    for row in filereader:
#        print("{}".format(row.strip()))

#print("Output #143:")
# READ MULTIPLE FILES
# Read multiple text files
#inputPath = sys.argv[1]
#for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
#    with open(input_file, 'r', newline='') as filereader:
#       for row in filereader:
#           print("{}".format(row.strip()))

# WRITE TO A FILE
# Write to a text file
#my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#max_index = len(my_letters)
#output_file = sys.argv[1]
#filewriter = open(output_file, 'w')
#for index_value in range(len(my_letters)):
#    if index_value < (max_index-1):
#        filewriter.write(my_letters[index_value]+'\t')
#    else:
#        filewriter.write(my_letters[index_value]+'\n')
#filewriter.close()
#print("Output #144: Output written to file")

# Write to a CSV file
#my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#max_index = len(my_numbers)
#output_file = sys.argv[1]
#filewriter = open(output_file, 'a')
#for index_value in range(len(my_numbers)):
#    if index_value < (max_index-1):
#        filewriter.write(str(my_numbers[index_value])+',')
#    else:
#        filewriter.write(str(my_numbers[index_value])+'\n')
#filewriter.close()
#print("Output #145: Output appended to file")