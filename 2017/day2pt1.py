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

# Convert text file to list of strings
with open('./day2_data.txt', 'r') as file:
    rows = file.read().split('\n')
    rows.pop(-1)
# print(rows)

for i in range(len(rows)):
    rows[i] = rows[i].split('\t')

puzzle_input = rows
# print(f"Puzzle Input: {puzzle_input}")

for list in puzzle_input:
    for i in range(0, len(list)):                # loop through each item in list
        list[i] = int(list[i])                   # convert each item (str) to integer

# print(puzzle_input)

# row = '121\t59\t141\t21\t120\t67\t58\t49\t22\t46\t56\t112\t53\t111\t104\t130'
# print(row.split('\t'))

# Covert data into list of lists (one list per row)
# puzzle_input = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]

def findSpeadsheetChecksum(input):
    # for each list:
    ranges = []
    for list in input:
        # (a) find lowest number
        minInt = min(list)
        # print(minInt)
        # (b) find highest number
        maxInt = max(list)
        # print(maxInt)
        # (c) subtract lowest from highest
        diff = maxInt-minInt
        # print(diff)
        # (d) add result to temp list
        ranges.append(diff)
    return sum(ranges)

# Result: Sum of all integers in temp list
real = findSpeadsheetChecksum(puzzle_input) # correct answer: 32121
if real == 32121:
    print(f"Pass! {real}")
else:
    print(real)
test = findSpeadsheetChecksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) # 18
if test == 18:
    print(f"Pass! {test}")
else:
    print(test)

print("--- %s seconds ---" % (time.time() - start_time))
