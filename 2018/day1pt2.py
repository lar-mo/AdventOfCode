'''
https://adventofcode.com/2018/day/1#part2

--- Day 1: Chronal Calibration ---
--- Part Two ---

You notice that the device repeats the same frequency change list over and over. To calibrate the device, you need to find the first frequency it reaches twice.

For example, using the same list of changes above, the device would loop as follows:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
(At this point, the device continues from the start of the list.)
Current frequency  3, change of +1; resulting frequency  4.
Current frequency  4, change of -2; resulting frequency  2, which has already been seen.
In this example, the first frequency reached twice is 2. Note that your device might need to repeat its list of frequency changes many times before a duplicate frequency is found, and that duplicates might be found while in the middle of processing the list.

Here are other examples:

+1, -1 first reaches 0 twice.
+3, +3, +4, -2, -4 first reaches 10 twice.
-6, +3, +8, +5, -6 first reaches 5 twice.
+7, +7, -2, -7, -4 first reaches 14 twice.
What is the first frequency your device reaches twice?
'''

import time
start_time = time.time()

# Convert text file to list of strings
with open('./day1_data.txt', 'r') as file:
    lines = file.read().split('\n')
    lines.pop(-1)

# convert input (freq variations) to integers
puzzle_input = []
for value in lines:
    if value[0] == "+":
        puzzle_input.append(int(value[1:]))
    else:
        puzzle_input.append(int(value))

### this is TOTALLY INEFFICIENT *** takes ~150-170 secs
# start a running total using same input until a duplicate freq is found
freq = 0                            # initialize var for base freq
freqs = []                          # initialize temp list for running totals
i = 0                               # set init value for while loop
while i == 0:                       # set repeating loop
    for var in puzzle_input:        # loop through each value in puzzle_input list
        freq += var                 # add positive or negative int to running total
        if freq in freqs:           # if result is in the list already ...
            i = 1                   # ... break while loop by setting i to non-zero and ...
            break                   # ... break out of for loop
        else:                       # otherwise, ...
            freqs.append(freq)      # ... add new running total to temp list

if freq == 413:
    print("Pass! ")
print(freq)

print("--- %s seconds ---" % (time.time() - start_time))
