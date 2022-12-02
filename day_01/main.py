
total_cals = []
with open('input.txt') as data_file:
    current_cal = 0
    for line in data_file:
        if line == "\n":
            total_cals.append(current_cal)
            current_cal = 0
        else:
            current_cal += int(line[:-1])
# print(total_cals)
print(f"Part 1 : {max(total_cals)}")

total_cals.sort()
#print(total_cals)
print(f"Part 2 : {total_cals[-1] + total_cals[-2] + total_cals[-3]}")