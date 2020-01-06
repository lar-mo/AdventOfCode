'''
--- Day 4: Secure Container ---

--- Part Two ---

An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle input is 246515-739105. (Note: That's 492,591 six digit numbers.)

The correct answer is 677.
'''
import time
start_time = time.time()

# The value is within the range given in your puzzle input.
puzzle_input = list(range(246515, 739106)) # one more than top end since range is exclusive

# loop through each possible password
possible_passwords = [] # placeholder for password with two identical adjacent digits
for password in puzzle_input:
    # It is a six-digit number. Unnecessary since every int in range is 6 digits by design
    number_to_string = str(password)
    if len(number_to_string) != 6:
        print(f"{password}: not long enough")
        break

    # Two adjacent digits are the same (like 22 in 122345).
    # Convert digits to list of ints
    list_of_digits = [int(d) for d in str(password)]
    for i in range(len(list_of_digits)):
        if i == len(list_of_digits)-1:
            break
        elif list_of_digits[i] == list_of_digits[i+1]:
            count = list_of_digits.count(list_of_digits[i])
            if count == 2:
                possible_passwords.append(password)

# Going from left to right, the digits never decrease;
# they only ever increase or stay the same (like 111123 or 135679).

def check_seq(new_list_of_digits):
    prev_j = 0
    for j in new_list_of_digits:
        if prev_j > j:
            return False
        prev_j = j

possible_passwords2 = []
for password2 in possible_passwords:
    new_list_of_digits = [int(d) for d in str(password2)]
    if check_seq(new_list_of_digits) == None:
        passing_pwd = ''.join(str(x) for x in new_list_of_digits)
        possible_passwords2.append(passing_pwd)

res = []
for i in possible_passwords2:
    if i not in res:
        res.append(i)

for pwds in res:
    res_digits = [int(d) for d in str(pwds)]

if len(res) == 677:
    print("Pass! ")
print(len(res)) # correct answer is 677

print("--- %s seconds ---" % (time.time() - start_time))
