

creates_starting_input = []
moves = []
input_still = True
with open('input.txt') as data_file:
    for li, line in enumerate(data_file):
        print(line)
        if input_still:
            if line == "\n":
                # finished
                input_still = False
                continue
            else:
                creates_starting_input.append(line[:-1])
        else:
            each_item = line.split()
            moves.append( (each_item[1], each_item[3], each_item[5]))

# print(creates_starting_input)
# print(moves)

creates = {}
# make creates
max_creates = len(creates_starting_input) - 1
for n in creates_starting_input[-1].split():
    create_list = []
    for ci in range(max_creates-1, -1, -1):
        # Grab the create
        strn_n = 4*(int(n)-1)+1
        if strn_n > len(creates_starting_input[ci]):
            continue
        if creates_starting_input[ci][strn_n] != " ":
            create_list.append(creates_starting_input[ci][strn_n])
    creates[n] = create_list

# print("Part 1")
# creates2 = creates
# print(creates)
# for number, mfrom, mto in moves:
#     for ni in range(int(number)):
#         create_to_move = creates[mfrom][-1]
#         # remove
#         creates[mfrom] = creates[mfrom][:-1]
#         # add
#         creates[mto].append(create_to_move)
#     #print(creates)
# print(creates)

# part1_output = ""
# for ck in creates.keys():
#     part1_output += creates[ck][-1]
# print(f"Part 1: {part1_output}")


print("Part 2")
print(creates)
for number, mfrom, mto in moves:
    create_to_move = creates[mfrom][-int(number):]
    # remove
    creates[mfrom] = creates[mfrom][:-int(number)]
    # add
    creates[mto] += create_to_move
    print(creates)
print(creates)

part2_output = ""
for ck in creates.keys():
    part2_output += creates[ck][-1]
print(f"Part 2: {part2_output}")