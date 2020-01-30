'''
https://adventofcode.com/2017/day/6

--- Day 6: Memory Reallocation ---

A debugger program here is having an issue: it is trying to repair a memory reallocation routine, but it keeps getting stuck in an infinite loop.

In this area, there are sixteen memory banks; each memory bank can hold any number of blocks. The goal of the reallocation routine is to balance the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks (ties won by the lowest-numbered memory bank) and redistributes those blocks among the banks. To do this, it removes all of the blocks from the selected bank, then moves to the next (by index) memory bank and inserts one of the blocks. It continues doing this until it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration is produced that has been seen before.

For example, imagine a scenario with only four memory banks:

The banks start with 0, 2, 7, and 0 blocks. The third bank has the most blocks, so it is chosen for redistribution.
Starting with the next bank (the fourth bank) and then continuing to the first bank, the second bank, and so on, the 7 blocks are spread out over the memory banks. The fourth, first, and second banks get two blocks each, and the third bank gets one back. The final result looks like this: 2 4 1 2.
Next, the second bank is chosen because it contains the most blocks (four). Because there are four memory banks, each gets one block. The result is: 3 1 2 3.
Now, there is a tie between the first and fourth memory banks, both of which have three blocks. The first bank wins the tie, and its three blocks are distributed evenly over the other three banks, leaving it with none: 0 2 3 4.
The fourth bank is chosen, and its four blocks are distributed such that each of the four banks receives one: 1 3 4 1.
The third bank is chosen, and the same thing happens: 2 4 1 2.
At this point, we've reached a state we've seen before: 2 4 1 2 was already seen. The infinite loop is detected after the fifth block redistribution cycle, and so the answer in this example is 5.

0 2 7 0 | 0
2 4 1 2 | 1*
3 1 2 3 | 2
0 2 3 4 | 3
1 3 4 1 | 4
2 4 1 2 | 5*

Given the initial block counts in your puzzle input, how many redistribution cycles must be completed before a configuration is produced that has been seen before?
'''
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

### transform a list ###
def redistMemory(data):                             # define function
    maxItem = max(data)                             # variable for the largest integer in list (to be redistributed)
    id = data.index(maxItem)                        # variable for the index of largest int
    length = len(data)                              # variable for length of list
    data[id] = 0                                    # Step 1: removes all of the blocks from the selected bank
    while maxItem > 0:                              # use largest integer as basis for loop
        for i in range(len(data)):                  # Step 2: then moves to the next (by index) memory bank ...
            data[id+i+1-length] += 1                # ... and inserts one of the blocks
            maxItem -= 1                            # ... (and remove one from maxItem - largest int)
            if maxItem == 0:                        # if maxItem reduced to 0, ...
                break                               # ... break out of for + while loops
    return data                                     # return newly transformed list

### track transformed lists and look for duplicates ###
def loopThroughVariants(input):                     # define function
    configurations = ['foo']                        # initialize temp list, seed with input data
    while True:                                     # initialize continuous loop
        input = redistMemory(input)                 # set the return data as input for function call on next cycle
        for i in range(len(input)):                 # loop through each integer in list
            string = "".join(str(i) for i in input) # convert int to string and concatenate
        if string not in configurations:            # if the string is not in temp list ...
            configurations.append(string)           # ... add it to the temp list
        else:                                       # otherwise, ...
            break                                   # ... break out of for + while loops
    return len(configurations)                      # return length of temp list (# of redist cycles)

if __name__ == '__main__':                          # if script run locally

    test_answer = loopThroughVariants(test_data)    # store result in temp variable
    if test_answer == 5:                            # if actual answer matches expected answer ...
        print(f"Pass! {test_answer}")               # ... print "Pass!" and test_answer

    puzzle_answer = loopThroughVariants(puzzleInput)# store result in temp variable
    if puzzle_answer == 7864:                       # if actual answer matches expected answer ...
        print(f"Pass! {puzzle_answer}")             # ... print "Pass!" and puzzle_answer

    print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
