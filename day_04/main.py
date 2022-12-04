
part1_count = 0
part2_count = 0
all_pairs = []
with open('input.txt') as data_file:
    for li, line in enumerate(data_file):
        pair1, pair2 = line.split(",")
        pair1_start, pair1_end = pair1.split("-")
        pair2_start, pair2_end = pair2.split("-")
        pair1_start = int(pair1_start)
        pair1_end   = int(pair1_end)
        pair2_start = int(pair2_start)
        pair2_end   = int(pair2_end)

        all_pairs.append([[pair1_start, pair1_end], [pair2_start, pair2_end]])

        # test_string_1 = ""
        # for i in range(1, 100):
        #     if pair1_start <= i <= pair1_end:
        #         test_string_1 += f"{i}"
        #     else:
        #         test_string_1 += "."
        # test_string_1 += f"  {pair1_start}-{pair1_end}"

        # If first pair inside second pair or second pair inside first pair
        if  ( pair1_start >= pair2_start and pair1_end <= pair2_end ) or \
            ( pair2_start >= pair1_start and pair2_end <= pair1_end ):
            part1_count += 1

        for i in range(pair1_start, pair1_end+1):
            if i in list(range(pair2_start, pair2_end+1)):
                part2_count +=1
                break


print(f"Part 1: {part1_count}")
print(f"Part 2: {part2_count}")