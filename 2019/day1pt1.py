'''
--- Day 1: The Tyranny of the Rocket Equation ---

Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
'''
import time
start_time = time.time()

# Convert text file to list
with open('./day1_data.txt', 'r') as file:
    lines = file.read().split('\n')
    lines.pop(-1)
    # print(lines)

# calculate the fuel requirement for each module
# F = M / 3 round down subtract 2
fuel_requirements = []
for mass in lines:
    fuel_req = int(mass) // 3 - 2 # parentheses are unnecessary, i.e. (int(mass) // 3) - 2
    # populate new list
    fuel_requirements.append(fuel_req)
# print(fuel_requirements)

# add all items in the list to get the TOTAL
grand_total = 0
for totals in fuel_requirements:
    grand_total += totals

if grand_total == 3416712:
    print("Pass! ")
print(grand_total) # correct answer is 3416712

print("--- %s seconds ---" % (time.time() - start_time))
