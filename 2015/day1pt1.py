'''
https://adventofcode.com/2015/day/1

--- Day 1: Not Quite Lisp ---

Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?
'''
import time
start_time = time.time()

# Open text file and convert string to list of integers
with open('./day1_data.txt', 'r') as file:          # Open the file
    lines = file.read()                             # Read the open file
    lines = lines[:-1]                              # Remove the trailing \n
    lines = list(lines)                             # Convert string to list

# (()) = 0 ; ()() = 0 ; ((( = 3 ; (()(()( = 3 ; ))((((( = 3 ; ()) = -1 ; ))( = -1 ; ))) = -3 ; )())()) = -3
test_data = list('(((')

def whichFloor(data):                               # define function
    floor = 0                                       # initialize counter (ground floor)
    for p in data:                                  # loop through each item in the list
        if p == '(':                                # if item is open parentheses, ...
            floor += 1                              # ... then increment floor by 1
        else:                                       # else, ...
            floor -= 1                              # ... then decrement floor by 1
    return floor                                    # return final result (floor)

if __name__ == '__main__':                          # if script run locally

    puzzle_answer = whichFloor(lines)               # call the function with puzzle data
    if puzzle_answer == 74:                         # if the actual result matches the expected result ...
        print(f"Pass! {puzzle_answer}")             # ... print Pass! and the actual result
    else:                                           # else, ...
        print(puzzle_answer)                        # ... print the actual (incorrect) result

    test_answer = whichFloor(test_data)             # call the function with test data
    if test_answer == 3:                            # if the actual result matches the expected result ...
        print(f"Pass! {test_answer}")               # ... print Pass! and the actual result
    else:                                           # else, ...
        print(test_answer)                          # ... print the actual (incorrect) result

    print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
