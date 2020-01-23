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

# Convert lists of space-delimited strings to lists of strings
for i in range(len(lines)):
    lines[i] = lines[i].split(' ')

test_input = [['aa', 'bb', 'cc', 'dd', 'ee'],['aa', 'bb', 'cc', 'dd', 'aa'],['aa', 'bb', 'cc', 'dd', 'aaa', 'ee', 'ff']]

def countOccurrences(data):
    validCount = 0                                  # initialize temp counter variable (valid passphrases)
    for list in data:                               # loop through each list in data (list of lists)
        itemCount = 0                               # initialize temp counter variable (num of occurrences)
        for item in list:                           # loop through the item in the (current) list
            itemCount += list.count(item)           # keep a running total of num of occurrences for each set (list)
        if itemCount == len(list):                  # if the itemCount matches the length of list (i.e. 1:1)
            validCount += 1                         # mark the list is a valid passphrase (increment counter)
    return validCount                               # when loops are completed, return count of valid passphrases

if __name__ == '__main__':                          # if script run locally

    puzzle_result = countOccurrences(lines)         # call the function with actual puzzle data
    if puzzle_result == 451:                        # if actual result matches expected result, ...
        print(f"Pass! {puzzle_result}")             # ... print "Pass!" and the actual result
    else:                                           # otherwise, ...
        print(puzzle_result)                        # ... print the actual (incorrect) result

    test_result = countOccurrences(test_input)      # call the function with test data
    if test_result == 2:                            # if actual result matches expected result, ...
        print(f"Pass! {test_result}")               # ... print "Pass!" and the actual result
    else:                                           # otherwise, ...
        print(test_result)                          # ... print the actual (incorrect) result

    print("--- %s seconds ---" % (time.time() - start_time)) # print the script execution time
