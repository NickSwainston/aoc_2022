def get_priority(duplicate):
    if duplicate.isupper():
        prority = ord(duplicate) - 64 + 26
    else:
        prority = ord(duplicate) - 96
    return prority

sum1 = 0
sum2 = 0
with open('input.txt') as data_file:
    lines_list = list(data_file)
    for li, line in enumerate(lines_list):
        size = len(line) // 2
        first = line[:size]
        second = line[size:]
        for f in first:
            for s in second:
                if f == s:
                    duplicate = f
                    break
        # print(duplicate)
        # print(prority)
        sum1 += get_priority(duplicate)

        if li%3 == 0:
            for c in line:
                if c in lines_list[li+1] and c in lines_list[li+2]:
                    duplicate = c
                    break
            sum2 += get_priority(duplicate)

print(f"Part 1: {sum1}")
print(f"Part 2: {sum2}")
