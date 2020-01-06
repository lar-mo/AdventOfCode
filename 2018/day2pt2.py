'''
https://adventofcode.com/2018/day/2#part2

--- Part Two ---

Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)
'''
import Levenshtein
import textdistance
import time
start_time = time.time()

# Convert text file to list of strings
with open('./day2_data.txt', 'r') as file:
    lines = file.read().split('\n')
    lines.pop(-1)
# print(lines)

this_len = len(lines[0])
rejects = []
for item in lines:
    if this_len != len(item):
        print(f"error {item}:{len(item)}")
        rejects.append(f"{item}:{len(item)}")
    this_len = len(item)
if len(rejects) == 0:
    print(f"All items have the length of {len(lines[0])}")
else:
    print(rejects)

temp_list = []
for i in range(len(lines)):
    for j in range(len(lines)-2):
        # print(Levenshtein.distance(lines[i],lines[j]))
        td = textdistance.hamming.normalized_similarity(lines[i],lines[j+1])
        print(i, j+1, lines[i], lines[j+1], td)
        # if td < 0.77:
        #     print(i, j+1, lines[i], lines[j+1], td)
#             if lines[i] not in temp_list:
#                 temp_list.append(lines[i])
#             # if lines[j+1] not in temp_list:
#             #     temp_list.append(lines[j+1])
# print(temp_list)

# for i in range(len(temp_list)):
#     for letter in temp_list[i][1]
#         if


# uniques = []
# for i in range(len(temp_list)):
    # print(temp_list[i][4])
    # if temp_list[i][4] not in uniques:
    #     uniques.append(temp_list[i])
# print(uniques)
# print(temp_list[0])

print("--- %s seconds ---" % (time.time() - start_time))
