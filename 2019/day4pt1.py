'''
--- Day 4: Secure Container ---

You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 246515-739105. (Note: That's 492,591 six digit numbers.)

The correct answer is 1048.
'''
import time
start_time = time.time()

# The value is within the range given in your puzzle input.
puzzle_input = list(range(246515, 739106)) # one more than top end since range is exclusive

# loop through each possible password
possible_passwords = [] # placeholder for password with two identical adjacent digits
for password in puzzle_input:
    # It is a six-digit number. Unnecessary since every int in range is 6 digits by design
    number_to_string = str(password)                    # convert each password from int to string to check length
    if len(number_to_string) != 6:                      # check if the length is not 6 digits
        print(f"{password}: not long enough")           # if so, return error message
        continue                                        # skip to the end

    # Two adjacent digits are the same (like 22 in 122345).
    # Convert digits to list of ints
    list_of_digits = [int(d) for d in str(password)]    # convert the strings to list of integers

    for i in range(len(list_of_digits)):                # loop through each digit
        if i == len(list_of_digits):                    # adjustment for outOfRange error (zero index vs one index)
            break                                       # exit the loop
        if list_of_digits[i-1] == list_of_digits[i]:    # check if previous & current digits are equal
            possible_passwords.append(password)         # if True, add to subset (array) of puzzle input

# Going from left to right, the digits never decrease;
# they only ever increase or stay the same (like 111123 or 135679).

def check_seq(new_list_of_digits):                      # utility function
    prev_j = 0                                          # initialize variable
    for j in new_list_of_digits:                        # loop through each list item
        if prev_j > j:                                  # check if previous digit is greater than current digit
            return False                                # return False
        prev_j = j                                      # set new prev_j for next loop through

#
# Clean up: store list_of_digits instead of original password which has to broken into list of ints, again
#

possible_passwords2 = []                                          # initialize variable
for password2 in possible_passwords:                              # loop through each poss. pwd from subset
    new_list_of_digits = [int(d) for d in str(password2)]         # convert string to list of integers
    if check_seq(new_list_of_digits) == None:                     # check each digit is larger or same as prev digit
        passing_pwd = ''.join(str(x) for x in new_list_of_digits) # concatenate items as one string
        possible_passwords2.append(passing_pwd)                   # add string to new array

### At this point, possible_passwords2 has a lot of duplicates (0 to 6) ###
# Remove duplicates
res = []                                                # initialize variable
for i in possible_passwords2:                           # loop through each item in array
    if i not in res:                                    # check if item is in storage array
        res.append(i)                                   # if not, add to storage array

# Display result
if len(res) == 1048:                                    # if length of result matches the correct answer
    print("Pass!")                                      # print Pass!
print(len(res)) # correct answer is 1048                # print length of result

print("--- %s seconds ---" % (time.time() - start_time))
