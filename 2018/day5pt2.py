'''
https://adventofcode.com/2018/day/5#part2

--- Day 5: Alchemical Reduction ---
--- Part Two ---

Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should. Your goal is to figure out which unit type is causing the most problems, remove all instances of it (regardless of polarity), fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?
'''
from day5pt1 import reducePolymer # imports main function from Day 5, part 1 (implies use of removePairs())
import string                     # import for input data
import time

start_time = time.time()

letters = string.ascii_lowercase                # generate data for input: a-z
results = {}                                    # initialize temp list
for letter in letters:                          # loop through every lowercase ltter
    with open('./day5_data.txt', 'r') as file:  # get fresh copy of puzzle input (open file as raw)
        lines = file.read()                     # (read file)
        lines = lines[:-1]                      # (trim last character \n)
    lines = lines.replace(letter, "")           # remove lowercase of target unit
    lines = lines.replace(letter.upper(), "")   # remove uppercase of target unit
    puzzleInput = list(lines)                   # convert string to list of items
    length = len(reducePolymer(puzzleInput))    # get the length of each reduction
    print(f"{length}:{letter.upper()}{letter}") # print result to terminal
    results[letter] = length                    # save result to dictionary

min = min(results, key=results.get)             # find the lowest 'score' (i.e. shortest polymer) in the dictionary
print(f"The winner is {min.upper()}{min}. Minified size is {results[min]}.") # Correct: Ff, 5094

print("--- %s seconds ---" % (time.time() - start_time))
