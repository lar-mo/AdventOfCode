'''
https://adventofcode.com/2017/day/2#part2

--- Day 2: Corruption Checksum ---
--- Part Two ---

"Great work; looks like we're on the right track after all. Here's a star for your effort." However, the program seems a little worried. Can programs be worried?

"Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5
In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?
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
for list in puzzle_input:
    for i in range(0, len(list)):               # loop through each item in list
        list[i] = int(list[i])                  # convert each item (str) to integer

def evenlyDivided(input):
    division_results = []                       
    for list in input:
        winning_pair = []
        list = sorted(list)
        for num in list:
            for i in range(len(list)-1):
                if i < list.index(num):
                    remainder = num % list[i]
                    if remainder == 0:
                        winning_pair = [num, list[i]]

        result = winning_pair[0] // winning_pair[1]
        division_results.append(result)
    return sum(division_results)

answer = evenlyDivided(puzzle_input)
if answer == 197:
    print(f"Pass! {answer}")
else:
    print(answer)

test_data = [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]
test_answer = evenlyDivided(test_data)
if test_answer == 9:
    print(f"Pass! {test_answer}")
else:
    print(test_answer)

print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
