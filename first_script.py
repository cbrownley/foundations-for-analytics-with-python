#!/usr/bin/env python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
from math import exp, log, sqrt
from string import split, join, strip, replace, lower, upper, capitalize
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
import glob
import os

# Print a simple string
print "Output #1: I'm excited to learn Python"

# This line and the next line are comment lines
# Add two numbers together
x = 4
y = 5
z = x + y
#print "Four plus five equals %d" % (z)
print "Output #2: Four plus five equals " + str(z)

# This line and the next line are comment lines
# Add two lists together
a = [1, 2, 3, 4]
b = ["first", "second", "third", "fourth"]
c = a + b
print "Output #3:", a, b, c

# INTEGERS
# x equals 9
x = 9
print "Output #4: " + str(x)

# 3*3*3*3 = 81
print "Output #5: " + str(3**4)

# 8/2 equals 4, then 8.3/2.7 equals approximately 3.074
print "Output #6: " + str(int(8.3)/int(2.7))
print "Output #7: " + str(8.3/2.7)

# 7/2 equals 3 because of truncation, then 7/2.0 and 7.0/2 both equal 3.5
print "Output #8: " + str(7/2)
print "Output #9: " + str(7/2.0)
print "Output #10: " + str(7.0/2)

# FLOATING-POINT NUMBERS
# 2.5 multiplied by 4.8 equals 12.0
y = 2.5*4.8
print "Output #11: " + str(y)

# 8/float(3) equals 2.666667
r = 8/float(3)
print "Output #12: " + str(r)
# 8/3 equals 2 because of truncation
print "Output #13: " + str(8/3)

# Show how to format output in print statements
print "Output #14: %d" % (8.3/2.7)
print "Output #15: %0.2f" % (8.3/2.7)
s = 8/float(3)
print "Output #16: %.4f" % (s)

# Some mathematical functions available in the math module
print "Output #17: " + str(exp(3))
print "Output #18: " + str(log(4))
print "Output #19: " + str(sqrt(81))

# STRINGS
# A string with single quotations, therefore include a backslash before
# the single quotation in the contraction "I'm" to print the single quotation
print "Output #20:", 'I\'m enjoying learning Python'

# A one-line string, but if the string is long and running off the page on the right
# you can use a "\" to separate the long string into smaller strings on separate lines
print "Output #21:", "This is a long string.  Without the backslash it would run off of the page \
on the right in the text editor and be very difficult to read and edit.  By using \
the backslash you can split the long string into smaller strings on separate lines \
so that the whole string is easy to view in the text editor."

# Use triple single or double quotes if you want the string to span multiple lines
# and you don't want to use the "\"
print "Output #22:", '''You can use triple single quotations
for multi-line comment strings'''

# Use triple single or double quotes if you want the string to span multiple lines
# and you don't want to use the "\"
print "Output #23:", """You can also use triple double quotations
for multi-line comment strings"""

# Add two strings together
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print "Output #24: " + sentence

# Repeat a string four times
print "Output #25: She is" + " " + "very "*4 + "beautiful."

# Determine the number of characters in a string, including spaces and punctuation
m = len(sentence)
print "Output #26: " + str(m)

# split()
string1 = "My deliverable is due in May"
string1_list = string1.split()
print "Output #27: " + str(string1_list)
print "Output #28: " + str(string1_list[0])

string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print "Output #29: " + str(string2_list)
print "Output #30: " + str(string2_list[5]) + str( string2_list[-1])

# join()
new_string = join(string1_list, ' ')
print "Output #31: "+ new_string
print "Output #32: " + ','.join(string2_list)

# strip()
string3 = "   Remove unwanted characters from this string\t\t    \n"
print "Output #33: string3:",string3
string3_lstrip = string3.lstrip()
print "Output #34: lstrip:",string3_lstrip
string3_rstrip = string3.rstrip()
print "Output #35: rstrip:",string3_rstrip
string3_strip = string3.strip()
print "Output #36: strip:",string3_strip

string4 = "$$Here's another string that has unwanted characters__---++"
print "Output #37: " + string4
string4_strip = string4.strip('$_-+')
print "Output #38: " + string4_strip

# replace()
string3_replace = string3_strip.replace(" ", "!@!")
print "Output #39: " + string3_replace
string4_replace = string4_strip.replace(" ", ",")
print "Output #40: " + string4_replace

# lower()
string5 = "Here's WHAT Happens WHEN You Use lower"
print "Output #41: " + string5.lower()

# upper()
string5 = "Here's what Happens when You Use UPPER"
print "Output #42: " + string5.upper()

# capitalize()
string5 = "here's WHAT Happens WHEN you use Capitalize"
print "Output #43: " + string5.capitalize()
string5_list = string5.split()
print "Output #44:",
for word in string5_list:
    print word.capitalize(),

# REGULAR EXPRESSIONS / PATTERN MATCHING
# Count the number of times a pattern appears in a string
print ""
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
    	count += 1
print "Output #45: " + str(count)

# Print the pattern each time it is found in the string
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I)
print "Output #46:",
for word in string_list:
    if pattern.search(word):
		print pattern.search(word).group('match_word'),

# Substitute the letter "a" for the word "the" in the string
print ""
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print "Output #47: " + pattern.sub("a", string)

# DATES
# Print today's date, as well as the year, month, and day elements
today = date.today()
print "Output #48: today: %s" % (today)
print "Output #49: " + str(today.year)
print "Output #50: " + str(today.month)
print "Output #51: " + str(today.day)
current_datetime = datetime.today()
print "Output #52: " + str(current_datetime)

# Calculate a new date using a timedelta
one_day = timedelta(days=-1)
yesterday = today + one_day
print "Output #53: yesterday: %s" % (yesterday)
eight_hours = timedelta(hours=-8)
print "Output #54: %s, %s" % (eight_hours.days, eight_hours.seconds)

# Calculate the amount of time between two dates and grab the first element, the number of days
date_diff = today - yesterday
print "Output #55: " + str(date_diff)
print "Output #56: " + str(date_diff).split()[0]

# Create a string with a specific format from a date object
print "Output #57: " + str(today.strftime('%m/%d/%Y'))
print "Output #58: " + str(today.strftime('%b %d, %Y'))
print "Output #59: " + str(today.strftime('%Y-%m-%d'))
print "Output #60: " + str(today.strftime('%B %d, %Y'))

# Create a datetime object with a specific format from a string representing a date
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')
print "Output #61: " + str(datetime.strptime(date1, '%m/%d/%Y'))
print "Output #62: " + str(datetime.strptime(date2, '%b %d, %Y'))
print "Output #63: " + str(datetime.date(datetime.strptime(date3, '%Y-%m-%d'))) # include the date portion, not time
print "Output #64: " + str(datetime.date(datetime.strptime(date4, '%B %d, %Y'))) # include the date portion, not time

# LISTS
# Use square brackets to create a list
# len() counts the number of elements in a list
# max() and min() find the maximum and minimum numbers in numeric lists
# count() counts the number of times a value appears in a list
a_list = [1, 2, 3]
print "Output #65: " + str(a_list)
print "Output #66: a_list has %d elements" % len(a_list)
print "Output #67: the maximum value in a_list is %d" % max(a_list)
print "Output #68: the minimum value in a_list is %d" % min(a_list)
another_list = ['printer', 5, ['star', 'circle', 9]]
print "Output #69: " + str(another_list)
print "Output #70: another_list also has %d elements" % len(another_list)
print "Output #71: 5 is in another_list %d time" % another_list.count(5)

# Use list indices to access specific values in a list
# [0] is the first value; [-1] is the last value
print "Output #72: " + str(a_list[0])
print "Output #73: " + str(a_list[1])
print "Output #74: " + str(a_list[2])
print "Output #75: " + str(a_list[-1])   # to get the last value in a list
print "Output #76: " + str(a_list[-2])
print "Output #77: " + str(a_list[-3])
print "Output #78: " + str(another_list[2])
print "Output #79: " + str(another_list[-1])

# Use list slices to access a subset of list values
# Do not include the starting indice to start from the beginning
# Do not include the ending indice to go all of the way to the end
print "Output #80: " + str(a_list[0:2])
print "Output #81: " + str(another_list[:2])
print "Output #82: " + str(a_list[1:3])
print "Output #83: " + str(another_list[1:])

# Use [:] to make a copy of a list
a_new_list = a_list[:]    # to copy a list
print "Output #84: " + str(a_new_list)

# Use + to add two or more lists together
a_longer_list = a_list + another_list    # to add lists together
print "Output #85: " + str(a_longer_list)

# Use 'in' and 'not in' to check whether specific values are or are not in a list
a = 2 in a_list    # use 'in' to check whether a value is in a list
print "Output #86: " + str(a)
b = 6 not in a_list    # use 'not in' to check whether a value is not in a list
print "Output #87: " + str(b)

# Use append() to add additional values to the end of the list
# Use remove() to remove specific values from the list
# Use pop() to remove values from the end of the list
a_list.append(4)
a_list.append(5)
a_list.append(6)
print "Output #88: " + str(a_list)
a_list.remove(5)
print "Output #89: " + str(a_list)
a_list.pop()
a_list.pop()
print "Output #90: " + str(a_list)

# Use reverse() to reverse a list, in-place, meaning it changes the list
a_list.reverse()
print "Output #91: " + str(a_list)
a_list.reverse()
print "Output #92: " + str(a_list)

# Use sort() to sort a list, in-place, meaning it changes the list
# To sort a list without changing the original list, make a copy first
unordered_list = [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
print "Output #93: " + str(unordered_list)
list_copy = unordered_list[:]
list_copy.sort()
print "Output #94: " + str(list_copy)
print "Output #95: " + str(unordered_list)

# Use sorted() to sort a collection of lists by a position in the lists
my_lists = [[1,2,3,4], [4,3,2,1], [2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
print "Output #96: " + str(my_lists_sorted_by_index_3)

# Use itemgetter() to sort a collection of lists by two index positions
my_lists = [[123,2,2,444], [22,6,6,444], [354,4,4,678], 
       [236,5,5,678], [578,1,1,290], [461,1,1,290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3,0))
print "Output #97: " + str(my_lists_sorted_by_index_3_and_0)

# TUPLES
# Use parentheses to create a tuple
my_tuple = ('x', 'y', 'z')
print "Output #98: " + str(my_tuple)
print "Output #99: my_tuple has %d elements" % len(my_tuple)
print "Output #100: " + str(my_tuple[1])
longer_tuple = my_tuple + my_tuple
print "Output #101: " + str(longer_tuple)

# Unpack tuples with the left-hand side of an assignment operator
one, two, three = my_tuple
print "Output #102:", one, two, three
var1 = 'red'
var2 = 'robin'
print "Output #103:", var1, var2
# Swap values between variables
var1, var2 = var2, var1
print "Output #104:", var1, var2

# Convert tuples to lists and lists to tuples
my_list = [1, 2, 3]
my_tuple = ('x', 'y', 'z')
print "Output #105: " + str(tuple(my_list))
print "Output #106: " + str(list(my_tuple))

# DICTIONARIES
# Use curly braces to create a dictionary
# len() counts the number of key-value pairs in a dictionary
empty_dict = { }
a_dict = {'one':1, 'two':2, 'three':3}
print "Output #107: " + str(a_dict)
print "Output #108: a_dict has %d elements" % len(a_dict)
another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}
print "Output #109: " + str(another_dict)
print "Output #110: another_dict also has %d elements" % len(another_dict)

# Use keys to access specific values in a dictionary
print "Output #111: " + str(a_dict['two'])
print "Output #112: " + str(another_dict['z'])

# Use copy() to make a copy of a dictionary
a_new_dict = a_dict.copy()    # to copy a dictionary
print "Output #113: " + str(a_new_dict)

# Use keys(), values(), and items() to access
# a dictionary's keys, values, and key-value pairs, respectively
print "Output #114: " + str(a_dict.keys())
a_dict_keys = a_dict.keys()
print "Output #115: " + str(a_dict_keys)
print "Output #116: " + str(a_dict.values())
print "Output #117: " + str(a_dict.items())

# Use has_key(), 'in' / 'not in', or get() to test
# whether a key is in a dictionary
print "Output #118: " + str(a_dict.has_key('three'))

if 'y' in another_dict: print "Output #119: IN!"
if 'y' in another_dict:
	print("Output #114: y is a key in another_dict: {}.".format(another_dict.keys()))

if 'c' not in another_dict: print "Output #120: NOT IN!"
if 'c' not in another_dict:
	print("Output #115: c is not a key in another_dict: {}.".format(another_dict.keys()))

print "Output #121: " + str(a_dict.get('three'))
print "Output #122: " + str(a_dict.get('four'))
print "Output #123: " + str(a_dict.get('four', 'Not in dict'))

# Use sorted() to sort a dictionary
# To sort a dictionary without changing the original dictionary, make a copy first
print "Output #124: " + str(a_dict)
dict_copy = a_dict.copy()
ordered_dict1 = sorted(dict_copy.items(), key=lambda item: item[0])
print "Output #125 (order by keys): " + str(ordered_dict1)
ordered_dict2 = sorted(dict_copy.items(), key=lambda item: item[1])
print "Output #126 (order by values): " + str(ordered_dict2)
ordered_dict3 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=True)
print "Output #127 (order by values, descending): " + str(ordered_dict3)
ordered_dict4 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=False)
print "Output #128 (order by values, ascending): " + str(ordered_dict4)

# CONTROL FLOW
# if-else statement
x = 5
if x > 4 or x != 9:
    print "Output #129: " + str(x)
else:
    print "Output #129: x is not greater than 4"

# if-elif-else statement
if x > 6:
    print "Output #130: x is greater than six"
elif x > 4 and x == 5:
    print "Output #130: " + str(x*x)
else:
    print "Output #130: x is not greater than 4"
    
# for loop
y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
z = ['nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one']
print "Output #131:",
for number in y:
    print number,
print ""

print "Output #132: "
for i in range(len(z)):
    print i, z[i]

print "Output #133:",
for j in range(len(z)):
    if y[j] > 4:
        print y[j],
print ""

print "Output #134: "
for key, value in another_dict.items():
    print str(key) + " " + str(value)

# compact for loops
# list, set, and dictionary comprehensions
# Select specific rows using a list comprehension
my_data = [[1,2,3], [4,5,6], [7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print "Output #135: " + str(rows_to_keep)

# Select a set of unique tuples in a list using a set comprehension
my_data = [(1,2,3), (4,5,6), (7,8,9), (7,8,9)]
set_of_tuples1 = {x for x in my_data}
print "Output #136: " + str(set_of_tuples1)
set_of_tuples2 = set(my_data)
print "Output #137: " + str(set_of_tuples2)

# Select specific key-value pairs using a dictionary comprehension
my_dictionary = {'customer1': 7, 'customer2': 9, 'customer3': 11}
my_results = {key : value for key, value in my_dictionary.items() if value > 10}
print "Output #138: " + str(my_results)

# while loop
print "Output #139:",
x = 0
while x < 11:
    print x,
    x += 1
print ""

# FUNCTIONS
# Calculate the mean of a sequence of numeric values
def getMean(numericValues):
    return float(sum(numericValues))/len(numericValues) if len(numericValues) > 0 else float('nan')

my_list = [2, 2, 4, 4, 6, 6, 8, 8]
print "Output #140: " + str(getMean(my_list))

#import numpy as np
#print np.mean(my_list)

# Calcuate the median of a sequence of numeric values
def getMedian(numericValues):
    theValues = sorted(numericValues)
    if len(theValues) % 2 == 1:
        return theValues[(len(theValues)+1)/2-1]
    else:
        lower = theValues[len(theValues)/2-1]
        upper = theValues[len(theValues)/2]
        return (float(lower + upper))/2

my_list1 = [2, 3, 4, 5, 6]
my_list2 = [4, 6, 8, 10, 12, 14]
#print getMedian(my_list1)
#print getMedian(my_list2)

# EXCEPTIONS
# Calculate the mean of a sequence of numeric values
def getMean(numericValues):
    return float(sum(numericValues))/len(numericValues)

my_list1 = [2, 2, 4, 4, 6, 6, 8, 8]
my_list2 = [ ]
# Short version
try:
    print "Output #141: " + str(getMean(my_list2))
except ZeroDivisionError as detail:
    print "Output #141 (Error): " + str(float('nan'))
    print "Output #141 (Error):", detail

# Long version
try:
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print "Output #142 (Error): " + str(float('nan'))
    print "Output #142 (Error):", detail
else:
    print "Output #142 (The mean is):", result
finally:
    print "Output #142 (Finally): The finally block is executed every time"

# READ A FILE
# Read a single text file
#input_file = sys.argv[1]

#print "Output #143: "
#filereader = open(input_file, 'r')
#for row in filereader:
#    print row.strip()
#filereader.close()

#print "Output #144: "
#with open(input_file, 'r') as filereader:
#    for row in filereader:
#        print row.strip()

#print "Output #145: "
# READ MULTIPLE FILES
# Read multiple text files
#inputPath = sys.argv[1]
#for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
#    filereader = open(input_file, 'r')
#    for row in filereader:
#        print row.strip()

"""
# WRITE TO A FILE
# Write to a text file
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print "Output #146: Output written to file"

# Write to a CSV file
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_index = len(my_numbers)
output_file = sys.argv[1]
filewriter = open(output_file, 'a')
for index_value in range(len(my_numbers)):
    if index_value < (max_index-1):
        filewriter.write(str(my_numbers[index_value])+',')
    else:
        filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()
print "Output #147: Output appended to file"
"""