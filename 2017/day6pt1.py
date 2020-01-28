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
    rows = file.read().strip().split('\t')      # strip \n first, then split on tabs (\t)

puzzleInput = rows                             # renamed variable for easier reading
for i in range(0, len(puzzleInput)):                # loop through each item in list
    puzzleInput[i] = int(puzzleInput[i])            # convert each item (str) to integer
# print(puzzleInput)

test_data = [0, 2, 7, 0]
# print(test_data)

def redistMemory(data1):
    maxItem = max(data1)
    id = data1.index(maxItem)
    length = len(data1)
    data1[id] = 0
    while maxItem > 0:
        for i in range(len(data1)):
            data1[id+i+1-length] += 1
            maxItem -= 1
            if maxItem == 0:
                break
    return data1

def loopThroughVariants(data):
    configurations = []
    while True:
        data = redistMemory(data)
        for i in range(len(data)):
            b = "".join(str(i) for i in data)
        if b not in configurations:
            configurations.append(b)
        else:
            break
    # print(configurations)
    return len(configurations) + 1

print(loopThroughVariants(test_data)) # 5

print(loopThroughVariants(puzzleInput)) # 7864

if __name__ == '__main__':                                   # if script run locally

    print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
