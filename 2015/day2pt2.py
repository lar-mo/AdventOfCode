'''
https://adventofcode.com/2015/day/2#part2

--- Part Two ---

The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
How many total feet of ribbon should they order?
'''
import time
start_time = time.time()

# Open text file and convert string to list of integers
with open('./day2_data.txt', 'r') as file:          # Open the file
    lines = file.read().split('\n')                 # Read the open file
    lines = lines[:-1]                              # Remove the trailing \n
    lines = list(lines)                             # Convert string to list

for i in range(len(lines)):                         # loop through each set in list
    lines[i] = lines[i].split('x')                  # split on the 'x' e.g. 1x1x10

for item in lines:                                  # loop through each set (item) in list
    for i in range(len(item)):                      # loop through each item in set (item)
        item[i] = int(item[i])                      # convert string to int (in order to do math)

puzzle_input = lines                                # rename puzzle data for easier reading

test_data = [[2,3,4], [1,1,10]]                     # test data

def calculateRibbon(data):
    all_packages = []                               # initialize temp list
    for set in data:                                # loop through each set in function input (data)
        l, w, h = set[0], set[1], set[2]            # define the l, w, h variables for easier reading
        set.pop(set.index(max(set)))                # remove the highest value in set
        wrap = 2*set[0] + 2*set[1]                  # calculate wrap for each set from list
        bow = l*w*h                                 # calculate bow using min(l*w*h) method
        all_packages.append(wrap + bow)             # add sum of wrap and bow to temp list (all_packages)
    sum_of_all_packages = sum(all_packages)         # calculate sum of all items in all_packages
    return sum_of_all_packages                      # return total (sum)

if __name__ == '__main__':                          # if script run locally

    test_answer = calculateRibbon(test_data)        # call calculateRibbon function with test_data
    if test_answer == 48:                           # if actual result matches expected result, ...
        print(f"Pass! {test_answer}")               # ... print Pass! and actual result
    else:                                           # else, ...
        print(f"Fail: {test_answer}")               # ... print Fail: and actual (incorrect) result

    puzzle_answer = calculateRibbon(puzzle_input)   # call calculateRibbon function with puzzle_input
    if puzzle_answer == 3812909:                    # if actual result matches expected result, ... 
        print(f"Pass! {puzzle_answer}")             # ... print Pass! and actual result
    else:                                           # else, ...
        print(f"Fail: {puzzle_answer}")             # ... print Fail: and actual (incorrect) result

    print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
