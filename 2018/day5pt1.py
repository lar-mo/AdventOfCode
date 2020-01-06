'''
https://adventofcode.com/2018/day/5

--- Day 5: Alchemical Reduction ---

You've managed to sneak in to the prototype suit manufacturing lab. The Elves are making decent progress, but are still struggling with the suit's size reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their problem eventually, you can do better. You scan the chemical composition of the suit's material and discover that it is formed by extremely long polymers (one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.

For example:

In aA, a and A react, leaving nothing behind.
In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
In abAB, no two adjacent units are of the same type, and so nothing happens.
In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
Now, consider a larger example, dabAcCaCBAcCcaDA:

dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.
After all possible reactions, the resulting polymer contains 10 units.

How many units remain after fully reacting the polymer you scanned? (Note: in this puzzle and others, the input is large; if you copy/paste your input, make sure you get the whole thing.)
'''
import time
start_time = time.time()

# Convert text file to list of strings
with open('./day5_data.txt', 'r') as file:
    lines = file.read()
    lines = lines[:-1]

puzzleInput = list(lines)

# This function removes one mixed-case pair of letters at a time
def removePairs(list_of_units):
    for i in range(len(list_of_units)-1):                                     # loop through all the list items
        if list_of_units[i].lower() == list_of_units[i+1].lower():            # look for letter pairs
            if list_of_units[i].islower() and list_of_units[i+1].isupper():   # check pairs are mixed case (aA)
                del list_of_units[i:i+2]                                      # if so, remove pair of items from list
                return list_of_units                                          # return remaining list
            elif list_of_units[i].isupper() and list_of_units[i+1].islower(): # check pair are mixed case (Aa)
                del list_of_units[i:i+2]                                      # if so, remove pair of items from list
                return list_of_units                                          # return remaining list
    return False                                                              # return False if no more letter pairs

# This function loops through all letters in the puzzle input
def reducePolymer(puzzle_input):
    while True:                                                               # start infinite loop
        res = removePairs(puzzle_input)                                       # submit list to removePairs() function
        if res == False:                                                      # if no pair found by removePairs()
            return last_res                                                   # return last saved list
        last_res = res                                                        # create/update saved list

if __name__ == '__main__':                                                    # if script run directly

    result = len(reducePolymer(puzzleInput))                                  # get the len of the final list
    if result == 11108:                                                       # if result matches correct answer
        print("Pass! ")                                                       # print "Pass!"
    print(result)                                                             # print result

    print("--- %s seconds ---" % (time.time() - start_time)) # ~55 secs
