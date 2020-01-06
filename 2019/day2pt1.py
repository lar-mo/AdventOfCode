'''
--- Day 2: 1202 Program Alarm ---

On the way to your gravity assist around the Moon, your ship computer beeps angrily about a "1202 program alarm". On the radio, an Elf is already explaining how to handle the situation: "Don't worry, that's perfectly norma--" The ship computer bursts into flames.

You notify the Elves that the computer's magic smoke seems to have escaped. "That computer ran Intcode programs like the gravity assist program it was working on; surely there are enough spare parts up there to build a new Intcode computer!"

An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.

For example, suppose you have the following program:

1,9,10,3,2,3,11,0,99,30,40,50
For the purposes of illustration, here is the same program split into multiple lines:

1,9,10,3,
2,3,11,0,
99,
30,40,50
The first four integers, 1,9,10,3, are at positions 0, 1, 2, and 3. Together, they represent the first opcode (1, addition), the positions of the two inputs (9 and 10), and the position of the output (3). To handle this opcode, you first need to get the values at the input positions: position 9 contains 30, and position 10 contains 40. Add these numbers together to get 70. Then, store this value at the output position; here, the output position (3) is at position 3, so it overwrites itself. Afterward, the program looks like this:

1,9,10,70,
2,3,11,0,
99,
30,40,50
Step forward 4 positions to reach the next opcode, 2. This opcode works just like the previous, but it multiplies instead of adding. The inputs are at positions 3 and 11; these positions contain 70 and 50 respectively. Multiplying these produces 3500; this is stored at position 0:

3500,9,10,70,
2,3,11,0,
99,
30,40,50
Stepping forward 4 more positions arrives at opcode 99, halting the program.

Here are the initial and final states of a few more small programs:

1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?
'''
import time
start_time = time.time()

# original values for intcode[1] and intcode[2] are 0 & 0, respectively.
# intcode = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,1,31,5,35,1,9,35,39,2,13,39,43,1,43,10,47,1,47,13,51,2,10,51,55,1,55,5,59,1,59,5,63,1,63,13,67,1,13,67,71,1,71,10,75,1,6,75,79,1,6,79,83,2,10,83,87,1,87,5,91,1,5,91,95,2,95,10,99,1,9,99,103,1,103,13,107,2,10,107,111,2,13,111,115,1,6,115,119,1,119,10,123,2,9,123,127,2,127,9,131,1,131,10,135,1,135,2,139,1,10,139,0,99,2,0,14,0]

with open('./day2_data.txt', 'r') as file:
    intcode = file.read() # read from file
    intcode = intcode.strip() # strip new lines \n (just the last list item)
    intcode = intcode.split(',') # split on commas
    intcode = [ int(x) for x in intcode ] # list comprehension to convert strings to ints in list
    intcode[1] = 12 # change list item at pos1 to '12' per instructions
    intcode[2] = 2  # change list item at pos2 to  '2' per instructions

'''
           0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
intcode = [1,0,0,3,1,1,2,3,1,3, 4, 3, 1, 5, 0, 3, 2,10, 1,19, 1, 5,19,23, 1,23, 5,27, 1,27,13,31,99]

1,0,0,3  , add 1+1=2 => 1,0,0,2,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,99
1,1,2,3  , add 0+0=0 => 1,0,0,0,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,99
1,3,4,3  , add 0+1=1 => 1,0,0,1,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,99
1,5,0,3  , add 1+1=2 => 1,0,0,2,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,99
2,10,1,19, mlt 4x0=0 => 1,0,0,2,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,0,1,5,19,23,1,23,5,27,1,27,13,31,99
1,5,19,23, add 1+0=0 => 1,0,0,2,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,0,1,5,19,0,1,23,5,27,1,27,13,31,99
1,23,5,27, add 1+1=2 => 1,0,0,2,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,0,1,5,19,1,1,23,5,2,1,27,13,31,99
1,27,13,31 add 2+5=7 => 1,0,0,2,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,0,1,5,19,1,1,23,5,2,1,27,13,7,99
99 exit

'''

j = 0
for i in range(len(intcode) // 4):    # divide len of intcode list by four since each block has 4 integers/positions
    chunk = intcode[j:j+4]            # grab a slice of four ints on every loop through
    j += 4                            # increment counter (start of block) by four on every loop through
    if chunk[0] == 1:                 # per rules, if pos0 of block(chunk) is 1, do 'additon'
        intcode[chunk[3]] = intcode[chunk[1]] + intcode[chunk[2]] # add values @ pos1+pos1, put result in pos3
    elif chunk[0] == 2:               # per rules, if pos0 of block(chunk) is 2, do 'multiplication'
        intcode[chunk[3]] = intcode[chunk[1]] * intcode[chunk[2]] # multiply values @pos1*pos2, put result in pos3
    elif chunk[0] == 99:              # per rules, if pos0 of block(chunk) is 99, ...
        break                         # ... exit the for loop
    else:                             # otherwise, if pos0 is not one of the above, ...
        print("something went wrong") # ... print "something went wrong" and ...
        break                         # ... exit the for loop
if intcode[0] == 3562624:             # if calculation matches the correct answer
    print("Pass")                     # print "Pass"
print(f"You got [intcode[0]]: {intcode[0]}") # Display the calculation

print("--- %s seconds ---" % (time.time() - start_time))
