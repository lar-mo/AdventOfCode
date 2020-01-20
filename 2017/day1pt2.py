'''
https://adventofcode.com/2017/day/1#part2

--- Day 1: Inverse Captcha ---
--- Part Two ---

You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a star as encouragement. The instructions change:

Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.
What is the solution to your new captcha?

'''

import time
start_time = time.time()

# Convert text file to list of strings
with open('./day1_data.txt', 'r') as file:
    lines = file.read()
    lines = lines[:-1]

puzzleInput = list(lines)
for i in range(0, len(puzzleInput)):
    puzzleInput[i] = int(puzzleInput[i])

def sumMatchingDigitsv2(listOfInts):
    winners = []
    for i in range(len(listOfInts)):
        if listOfInts[i] == listOfInts[i+len(listOfInts)//2-len(listOfInts)]:
            winners.append(listOfInts[i])
    return sum(winners)

# Unit tests
if sumMatchingDigitsv2([1,2,1,2]) == 6: print("Pass!") # produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
if sumMatchingDigitsv2([1,2,2,1]) == 0: print("Pass!") # produces 0, because every comparison is between a 1 and a 2.
if sumMatchingDigitsv2([1,2,3,4,2,5]) == 4: print("Pass!") # produces 4, because both 2s match each other, but no other digit has a match.
if sumMatchingDigitsv2([1,2,3,1,2,3]) == 12: print("Pass!") # produces 12.
if sumMatchingDigitsv2([1,2,1,3,1,4,1,5]) == 4: print("Pass!") # produces 4.

# Solve the puzzle
result = sumMatchingDigitsv2(puzzleInput)           # call the function with actual puzzle input from day1_data.txt
if result == 1152:                                  # if (correct) result is 1152
    print(f"Pass! {result}")                        # print "Pass! and the result"

print("--- %s seconds ---" % (time.time() - start_time))
