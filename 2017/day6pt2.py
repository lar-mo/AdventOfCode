'''
https://adventofcode.com/2017/day/6#part2

--- Day 6: Memory Reallocation ---
--- Part Two ---

Out of curiosity, the debugger would also like to know the size of the loop: starting from a state that has already been seen, how many block redistribution cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the answer in that example would be 4.

How many cycles are in the infinite loop that arises from the configuration in your puzzle input?
'''
from day6pt1 import redistMemory
import time
start_time = time.time()

# Covert data into list of lists (one list per row)
# Convert text file to list of strings
with open('./day6_data.txt', 'r') as file:
    rows = file.read().strip().split('\t')          # strip \n first, then split on tabs (\t)

puzzleInput = rows                                  # renamed variable for easier reading
for i in range(0, len(puzzleInput)):                # loop through each item in list
    puzzleInput[i] = int(puzzleInput[i])            # convert each item (str) to integer

test_data = [0, 2, 7, 0]

### track transformed lists and look for duplicates ###
def loopThroughVariants(input):                     # define function
    configurations = []                             # initialize temp list for redist result for each cycle
    lengths = []                                    # initialize temp list for length of configurations list
    while True:                                     # initialize continuous loop
        input = redistMemory(input)                 # set the return data as input for function call on next cycle
        for i in range(len(input)):                 # loop through each integer in list
            string = "".join(str(i) for i in input) # convert int to string and concatenate
        configurations.append(string)               # ... add it to the temp list
        if configurations.count(string) == 2:       # if the variant repeats the first time (count=2), ...
            lengths.append(len(configurations))     # ... add length of list (cycles)
        if configurations.count(string) == 3:       # if the variant repeats for the second time (count=3), ...
            lengths.append(len(configurations))     # ... add length of list (cycles) ...
            break                                   # ... then, break out of while loop
    return lengths[-1] - lengths[0]                 # return result of last item minus first item from lengths list
                                                    # i.e. how many block redistribution cycles must be performed before that same state is seen again

if __name__ == '__main__':                          # if script run locally

    test_answer = loopThroughVariants(test_data)    # store result in temp variable
    if test_answer == 4:                            # if actual answer matches expected answer ...
        print(f"Pass! {test_answer}")               # ... print "Pass!" and test_answer
    else:                                           # otherwise, ...
        print(test_answer)                          # ... print the actual result

    puzzle_answer = loopThroughVariants(puzzleInput)# store result in temp variable
    if puzzle_answer == 1695:                       # if actual answer matches expected answer ...
        print(f"Pass! {puzzle_answer}")             # ... print "Pass!" and puzzle_answer
    else:                                           # otherwise, ...
        print(puzzle_answer)                        # ... print the actual result

    print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
