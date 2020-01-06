# data = [(10602, 'a'), (10704, 'b'), (10632, 'c'), (10650, 'd'), (10686, 'e'), (5094, 'f'), (10688, 'g'), (10664, 'h'), (10670, 'i'), (10656, 'j'), (10726, 'k'), (10698, 'l'), (10630, 'm'), (10626, 'n'), (10644, 'o'), (10648, 'p'), (10656, 'q'), (10650, 'r'), (10664, 's'), (10718, 't'), (10700, 'u'), (10664, 'v'), (10682, 'w'), (10606, 'x'), (10678, 'y'), (10642, 'z')]
#
# # print(min(data)[0])
# winner = list(map(min, zip(*data)))
# print(winner)

# dict = {'a': 10602, 'f': 5094}


import string
# print(string.ascii_lowercase)
dict = {'a': 10602, 'f': 5094}

min = min(dict, key=dict.get)
max = max(dict, key=dict.get)
# print(min)
print(f"Min: {dict[min]}, {min.upper()}{min}")
print(f"Max: {dict[max]}, {max.upper()}{max}")
