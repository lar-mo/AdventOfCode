'''
https://adventofcode.com/2017/day/4

--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
'''
import time
start_time = time.time()

# Covert data into list of lists (one list per row)
# Convert text file to list of strings
with open('./day4_data.txt', 'r') as file:
    lines = file.read().split('\n')
    lines.pop(-1)

# Convert lists of tab-delimited strings to lists of strings
for i in range(len(lines)):
    lines[i] = lines[i].split(' ')

test_input = [['aa', 'bb', 'cc', 'dd', 'ee'],['aa', 'bb', 'cc', 'dd', 'aa'],['aa', 'bb', 'cc', 'dd', 'aaa']]

def countOccurrences(data):
    validCount = 0
    for list in data:
        itemCount = 0
        for item in list:
            itemCount += list.count(item)
        if itemCount == len(list):
            validCount += 1
    return validCount

puzzle_result = countOccurrences(lines)
if puzzle_result == 451:
    print(f"Pass! {puzzle_result}")
else:
    print(puzzle_result)

test_result = countOccurrences(test_input)
if test_result == 2:
    print(f"Pass! {test_result}")
else:
    print(test_result)

print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
