'''
https://adventofcode.com/2017/day/2

--- Day 2: Corruption Checksum ---

As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?
'''
import time
start_time = time.time()

# Covert data into list of lists (one list per row)
# Convert text file to list of strings
with open('./day2_data.txt', 'r') as file:
    rows = file.read().split('\n')
    rows.pop(-1)

# Convert lists of tab-delimited strings to lists of strings
for i in range(len(rows)):
    rows[i] = rows[i].split('\t')

puzzle_input = rows                             # renamed variable for easier reading

# Convert lists of strings to lists of integers
for list in puzzle_input:                       # loop through each list in (big) list
    for i in range(0, len(list)):               # loop through each item in list
        list[i] = int(list[i])                  # convert each item (str) to integer

# Calculate the checksum for spreadsheet
def findSpeadsheetChecksum(input):
    ranges = []                                 # initialize temp list
    for list in input:                          # loop through each list of ints
        minInt = min(list)                      # find lowest number
        maxInt = max(list)                      # find highest number
        diff = maxInt-minInt                    # find diff between highest and lowest
        ranges.append(diff)                     # add result to temp list
    return sum(ranges)                          # return the sum of all items in temp list

# Result: Sum of all integers in temp list
real = findSpeadsheetChecksum(puzzle_input)     # call function with actual puzzle data
if real == 32121:                               # if result matches correct answer: 32121
    print(f"Pass! {real}")                      # print Pass! and the result
else:                                           # otherwise,
    print(real)                                 # print the incorrect result

test = findSpeadsheetChecksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) # call function with test data
if test == 18:                                  # if result matches correct answer: 18
    print(f"Pass! {test}")                      # print Pass! and the result
else:                                           # otherwise,
    print(test)                                 # print the incorrect result

print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
