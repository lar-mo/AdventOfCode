'''
https://adventofcode.com/2017/day/4#part2

--- Day 4: High-Entropy Passphrases ---
--- Part Two ---

For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?
'''
import time
start_time = time.time()

from day4pt1 import countOccurrences

# Covert data into list of lists (one list per row)
# Convert text file to list of strings
with open('./day4_data.txt', 'r') as file:
    lines = file.read().split('\n')
    lines.pop(-1)

# Convert lists of space-delimited strings to lists of strings
for i in range(len(lines)):
    lines[i] = lines[i].split(' ')

# Test data
test_data = [['abcde', 'xyz', 'ecdab'],['abcde', 'fghij'],['a', 'ab', 'abc', 'abd', 'abf', 'abj'], ['iiii', 'oiii', 'ooii', 'oooi', 'oooo'], ['oiii', 'ioii', 'iioi', 'iiio']]

def countSortedPassphrases(data):
    for passphrase in data:                                 # loop through each passphrase (list) in test input
        for i in range(len(passphrase)):                    # loop through each item in the list (passphrase)
            # passphrase[i] = list(passphrase[i])           # convert each string to a list of items (*unnecess.)
            # passphrase[i] = sorted(passphrase[i])         # sort list items alphabetically
            # passphrase[i] = ''.join(passphrase[i])        # convert list of items back to string
            passphrase[i] = ''.join(sorted(passphrase[i]))  # do both operations in one line of code
    return countOccurrences(data)

if __name__ == '__main__':                            # if script run locally

    puzzle_result = countSortedPassphrases(lines)     # call the function with actual puzzle data
    if puzzle_result == 223:                          # if actual result matches expected result, ...
        print(f"Pass! {puzzle_result}")               # ... print "Pass!" and the actual result
    else:                                             # otherwise, ...
        print(puzzle_result)                          # ... print the actual (incorrect) result

    puzzle_result = countSortedPassphrases(test_data) # call the function with actual puzzle data
    if puzzle_result == 3:                            # if actual result matches expected result, ...
        print(f"Pass! {puzzle_result}")               # ... print "Pass!" and the actual result
    else:                                             # otherwise, ...
        print(puzzle_result)                          # ... print the actual (incorrect) result

    print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
