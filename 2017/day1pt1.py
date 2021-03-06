'''
https://adventofcode.com/2017/day/1

--- Day 1: Inverse Captcha ---

The night before Christmas, one of Santa's Elves calls you in a panic. "The printer's broken! We can't print the Naughty or Nice List!" By the time you make it to sub-basement 17, there are only a few minutes until midnight. "We have a big problem," she says; "there must be almost fifty bugs in this system, but nothing else can print The List. Stand in this square, quick! There's no time to explain; if you can convince them to pay you in stars, you'll be able to--" She pulls a lever and the world goes blurry.

When your eyes can focus again, everything seems a lot more pixelated than before. She must have sent you inside the computer! You check the system clock: 25 milliseconds until midnight. With that much time, you should be able to collect all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day millisecond in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're standing in a room with "digitization quarantine" written in LEDs along one wall. The only door is locked, but it includes a small interface. "Restricted Area - Strictly No Digitized Users Allowed."

It goes on to explain that you may only leave by solving a captcha to prove you're not a human. Apparently, you only get one millisecond to solve the captcha: too fast for a normal human, but it feels like hours to you.

The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
What is the solution to your captcha?
'''

import time
start_time = time.time()

# Open text file and convert string to list of integers
with open('./day1_data.txt', 'r') as file:          # Open the file
    lines = file.read()                             # Read the open file
    lines = lines[:-1]                              # Remove the trailing \n
puzzleInput = list(lines)                           # convert string to list of strings
for i in range(0, len(puzzleInput)):                # loop through each item in list
    puzzleInput[i] = int(puzzleInput[i])            # convert each item (str) to integer

# Function to compare adjacent items (integers)
def sumMatchingDigits(listOfInts):
    winners = []                                    # initialize temp list
    for i in range(len(listOfInts)-1):              # loop through each list item
        if listOfInts[i] == listOfInts[i+1]:        # if adjacent ints are the same, ...
            winners.append(listOfInts[i])           # ... add to temp list

    if listOfInts[0] == listOfInts[-1]:             # standalone comparison: if first and last are the same, ...
        winners.append(listOfInts[0])               # ... add to temp list

    return sum(winners)                             # return the sum of all item (ints) in list

# Unit tests
if sumMatchingDigits([1,1,2,2]) == 3: print("Pass!")         # expected result: 3 (unit test 1)
if sumMatchingDigits([1,1,1,1]) == 4: print("Pass!")         # expected result: 4 (unit test 2)
if sumMatchingDigits([1,2,3,4]) == 0 : print("Pass!")        # expected result: 0 (unit test 3)
if sumMatchingDigits([9,1,2,1,2,1,2,9]) == 9: print("Pass!") # expected result: 9 (unit test 4)

# Solve the puzzle
result = sumMatchingDigits(puzzleInput)             # call the function with actual puzzle input from day1_data.txt
if result == 1182:                                  # if (correct) result is 1182
    print(f"Pass! {result}")                        # print "Pass! and the result"

print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
