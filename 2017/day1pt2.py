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
with open('./day1_data.txt', 'r') as file:          # Open the file
    lines = file.read()                             # Read the data in the file
    lines = lines[:-1]                              # Remove the trailing \n
puzzleInput = list(lines)                           # convert string to list of strings
for i in range(0, len(puzzleInput)):                # loop through each item in list
    puzzleInput[i] = int(puzzleInput[i])            # convert each item (str) to integer

def sumMatchingDigitsv2(listOfInts):
    winners = []                                    # initialize temp list
    # variables for easier reading
    length = len(listOfInts)                        # length of list
    half = length // 2                              # half the length
    for i in range(len(listOfInts)):                # loop through each list item
        # use modulus and subtraction to ensure indices are always positive integers
        # comparisons (lines 48-55)
            # index 0 1 2 3
            # list [1,2,1,2]
            #   0:2 (1, 1) (0+2%4=2) => 0<2
            #   1:3 (2, 2) (1+2%4=3) => 1<2
            #   2:0 (1, 1) (2+2-4=0) => 2!<2
            #   3:1 (2, 2) (3+2-4=1) => 3!<2
        # if i < half:
        #     # use modulus to find index of corresponding digit half way from circular list
        #     if listOfInts[i] == listOfInts[i+half%length]: # if current digit matches corresponding digit ...
        #         winners.append(listOfInts[i])              # ... add to temp list
        # else:
        #     # use subtraction to find index of corresponding digit half way from circular list
        #     if listOfInts[i] == listOfInts[i+half-length]: # if current digit matches corresponding digit ...
        #         winners.append(listOfInts[i])              # ... add to temp list

        '''
        use subtraction only; uses mix of positive and negative index numbers
        e.g. comparisons (lines 66-67)
            index 0 1 2 3
            list [1,2,1,2]
              0:2 (1, 1) (0+2-4=-2)
              1:3 (2, 2) (1+2-4=-1)
              2:0 (1, 1) (2+2-4=0)
              3:1 (2, 2) (3+2-4=1)
        '''
        # use subtraction to find index of corresponding digit half way from circular list
        if listOfInts[i] == listOfInts[i+half-length]: # if current digit matches corresponding digit ...
            winners.append(listOfInts[i])              # ... add to temp list

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
