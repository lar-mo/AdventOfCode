'''
https://adventofcode.com/2015/day/1#part2

--- Day 1: Not Quite Lisp ---
--- Part Two ---

Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character that causes Santa to first enter the basement?
'''
import time
start_time = time.time()

# Open text file and convert string to list of integers
with open('./day1_data.txt', 'r') as file:          # Open the file
    lines = file.read()                             # Read the open file
    lines = lines[:-1]                              # Remove the trailing \n
    lines = list(lines)                             # Convert string to list

test_data = list('()())')                           # answer is 5

def whichFloor(data):                               # define function
    counter = 1                                     # initialize counter, starting at 1 due to break on line 35
    floor = 0                                       # initialize floor (0 = ground floor)
    for p in data:                                  # loop through each item in the list
        if p == '(':                                # if item is open parentheses, ...
            floor += 1                              # ... then increment floor by 1
        else:                                       # else, ...
            floor -= 1                              # ... then decrement floor by 1
            if floor == -1:                         # if floor reaches -1 (basement), ...
                break                               # ... break out of for loop
        counter += 1                                # ... and increment counter by 1
    return counter                                  # return counter

if __name__ == '__main__':                          # if script run locally

    puzzle_answer = whichFloor(lines)               # call the function with puzzle data
    if puzzle_answer == 1795:                       # if the actual result matches the expected result ...
        print(f"Pass! {puzzle_answer}")             # ... print Pass! and the actual result
    else:                                           # else, ...
        print(puzzle_answer)                        # ... print the actual (incorrect) result

    test_answer = whichFloor(test_data)             # call the function with test data
    if test_answer == 5:                            # if the actual result matches the expected result ...
        print(f"Pass! {test_answer}")               # ... print Pass! and the actual result
    else:                                           # else, ...
        print(test_answer)                          # ... print the actual (incorrect) result

    print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
