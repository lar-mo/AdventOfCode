'''
--- Part Two ---

During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence. Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)
'''
import time
start_time = time.time()

# Convert text file to list
with open('./day1_data.txt', 'r') as file:
    lines = file.read().split('\n')
    lines.pop(-1)

# calculate the fuel requirement for each module, repeat until mass is 0
# F = M / 3 , then round down and subtract 2
fuel_requirements = []
for mass in lines:
    fuel_requirement = []
    while int(mass) >= 0:
        fuel_req = int(mass) // 3 - 2
        fuel_requirement.append(fuel_req)
        mass = fuel_req
    fuel_requirement.pop()

    # add all items in the list to get the TOTAL
    grand_total = 0
    for totals in fuel_requirement:
        grand_total += totals
    fuel_requirements.append(grand_total)

# add all items in the list to get the TOTAL
grand_total = 0
for totals in fuel_requirements:
    grand_total += totals

if grand_total == 5122170:
    print("Pass! ")
print(grand_total) # correct answer is 5122170

print("--- %s seconds ---" % (time.time() - start_time))
