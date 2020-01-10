'''
https://adventofcode.com/2018/day/2

--- Day 2: Inventory Management System ---

You stop falling through time, catch your breath, and check the screen on the device. "Destination reached. Current Year: 1518. Current Location: North Pole Utility Closet 83N10." You made it! Now, to find those anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not sure either. But now that so many people have chimneys, maybe he could sneak in that way?" Another voice responds, "Actually, we've been working on a new kind of suit that would let him fit through tight spaces like that. But, I heard that a few days ago, they lost the prototype fabric, the design plans, everything! Nobody on the team can even seem to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd be stored together, so the box IDs should be similar. Too bad it would take forever to search the warehouse for two similar box IDs..." They walk too far away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were discovered - and use your fancy wrist device to quickly scan every box and produce a list of the likely candidates (your puzzle input).

To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?
'''
import time
start_time = time.time()

# Convert text file to list of strings
with open('./day2_data.txt', 'r') as file:
    lines = file.read().split('\n')
    lines.pop(-1)

# puzzle_input = ['luojygedpvsthptkxiwnaorzmq', 'lucjqgedppsbhftkxiwnaorlmq', 'lucjmgeffvsbhftkxiwnaorziq']
puzzle_input = lines

# print(puzzle_input)
# print(puzzle_input[0].count('o'))

# counting those with exactly 2 of any letter
counts_2 = []
for i in range(len(puzzle_input)):
    for letter in puzzle_input[i]:
        count = puzzle_input[i].count(letter)
        if count == 2:
            counts_2.append(puzzle_input[i])
# print(counts_2)

counts2unique = []                                              # initialize variable
for i in counts_2:                                              # loop through each item in array
    if i not in counts2unique:                                  # check if item is in storage array
        counts2unique.append(i)                                 # if not, add to storage array
# print(len(counts2unique))

counts_3 = []
for i in range(len(puzzle_input)):
    for letter in puzzle_input[i]:
        count = puzzle_input[i].count(letter)
        if count == 3:
            counts_3.append(puzzle_input[i])
# print(counts_3)

counts3unique = []                                              # initialize variable
for i in counts_3:                                              # loop through each item in array
    if i not in counts3unique:                                  # check if item is in storage array
        counts3unique.append(i)                                 # if not, add to storage array
# print(len(counts3unique))

total = len(counts2unique) * len(counts3unique)
if total == 4712:
    print("Pass! ")
print(f"{len(counts2unique)} x {len(counts3unique)} = {total}")

print("--- %s seconds ---" % (time.time() - start_time))
