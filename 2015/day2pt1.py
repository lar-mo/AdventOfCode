'''

--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
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
test_data = [[1,1,10], [2,3,4]]                     # test data

def calculateArea(data):
    all_packages = []                               # initialize temp list
    for set in data:                                # loop through each set in function input (data)
        l, w, h = set[0], set[1], set[2]            # define the l, w, h variables for easier reading
        base_area = 2*l*w + 2*w*h + 2*h*l           # calculate base area for each set from list
        extra = min([l*w, w*h, h*l])                # calculate smallest side using min(list) method
        all_packages.append(base_area + extra)      # add sum of base_area and extra to temp list (all_packages)
    sum_of_all_packages = sum(all_packages)         # calculate sum of all items in all_packages
    return sum_of_all_packages                      # return total (sum)

if __name__ == '__main__':                          # if script run locally

    test_answer = calculateArea(test_data)          # call calculateArea function with test_data
    if test_answer == 101:                          # if actual result matches expected result, ...
        print(f"Pass! {test_answer}")               # ... print Pass! and actual result
    else:                                           # else, ...
        print(f"Fail: {test_answer}")               # ... print Fail: and actual (incorrect) result

    puzzle_answer = calculateArea(puzzle_input)     # call calculateArea function with puzzle_input
    if puzzle_answer == 1598415:                    # if actual result matches expected result, ...
        print(f"Pass! {puzzle_answer}")             # ... print Pass! and actual result
    else:                                           # else, ...
        print(f"Fail: {puzzle_answer}")             # ... print Fail: and actual (incorrect) result

    print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
