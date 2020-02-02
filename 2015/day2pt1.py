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

for i in range(len(lines)):
    lines[i] = lines[i].split('x')

for item in lines:
    for i in range(len(item)):
        item[i] = int(item[i])

# print(lines)
puzzle_input = lines

test_data = [[1,1,10], [2,3,4]]
# test_data = [[2,3,4]]

def calculateArea(data):

    all_packages = []
    for set in data:
        # l=2, w=3, h=4
        l = set[0]
        w = set[1]
        h = set[2]
        # 2*l*w + 2*w*h + 2*h*l
        base_area = 2*l*w + 2*w*h + 2*h*l

        find_smallest_side = []
        find_smallest_side.append(l*w)
        find_smallest_side.append(w*h)
        find_smallest_side.append(h*l)
        extra = min(find_smallest_side)

        all_packages.append(base_area + extra)

    sum_of_all_packages = sum(all_packages)

    return sum_of_all_packages

if __name__ == '__main__':                          # if script run locally

    test_answer = calculateArea(test_data)
    if test_answer == 101:
        print(f"Pass! {test_answer}")
    else:
        print(test_answer)

    puzzle_answer = calculateArea(puzzle_input)
    if puzzle_answer == 1598415:
        print(f"Pass! {puzzle_answer}")
    else:
        print(puzzle_answer)

    print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
