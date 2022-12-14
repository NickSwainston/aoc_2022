class true_error(BaseException):
    pass

class false_error(BaseException):
    pass


def get_list(ci, input_list):
    # # print(input_list)
    new_list = []
    left_bracket  = 1
    right_bracket =  0
    # # print(f"ci: {ci}")
    # # print(f"input_list: {input_list}")
    # # print(f"range: {list(range(ci, len(input_list)))}")
    for check_i in range(ci, len(input_list)):
        new_item = input_list[check_i]
        if new_item.startswith("[") and check_i == ci:
            new_item = new_item[1:]

        left_bracket  += new_item.count("[")
        right_bracket += new_item.count("]")
        # # print(f"new item {new_item}")
        #if "]" in input_list[check_i] and "[" not in input_list[check_i]:
        # # print(f"  new_time:      {new_item}")
        # # print(f"  left_bracket:  {left_bracket}")
        # # print(f"  right_bracket: {right_bracket}")
        if left_bracket <= right_bracket:
            # # print(new_list + [new_item[:-1]])
            return new_list + [new_item[:-1]]
        else:
            new_list.append(new_item)

def check_order(left, right, depth):
    # print(f"{(depth - 1) * '  '}Compare [{','.join(left)}] vs [{','.join(right)}] line 29")
    # # print(f"{(depth - 1) * '  '}Compare [{left}] vs [{right}]")
    for ci, chars in enumerate(zip(left, right)):
        lc, rc = chars
        if len(lc) == 0 and len(rc) == 0:
            # print(f"{depth * '  '}Both ran out so continue")
            continue
        elif len(lc) == 0:
            # print(f"{depth * '  '}Left side ran out of items, so inputs are in the right order")
            raise true_error
        elif len(rc) == 0:
            # print(f"{depth * '  '}Right side ran out of items, so inputs are not in the right order")
            raise false_error
        elif left == '[]':
            # print(f"{depth * '  '}Left side ran out of items, so inputs are in the right order")
            raise true_error
        elif right == '[]':
            # print(f"{depth * '  '}Right side ran out of items, so inputs are not in the right order")
            raise false_error
        # print(f"{depth * '  '}Compare {lc} vs {rc}")
        if lc[0] == "[" and rc[0] == "[":
            # both lists so get list and restart fucntion
            new_left  = get_list(ci, left)
            new_right = get_list(ci, right)
            depth += 1
            check_order(new_left, new_right, depth)
            depth -= 1
        elif lc[0] == "[" and rc[0].isdigit():
            # left is list so make right one as well
            new_left  = get_list(ci, left)
            new_right = [rc[0]]
            # print(f"{depth * '  '}Mixed types; convert right to {new_right} and retry comparison")
            depth += 1
            check_order(new_left, new_right, depth)
            depth -= 1
        elif lc[0].isdigit() and rc[0] == "[":
            # right is list so make left one as well
            new_left  = [lc[0]]
            new_right = get_list(ci, right)
            # print(f"{depth * '  '}Mixed types; convert left to {new_left} and retry comparison")
            depth += 1
            check_order(new_left, new_right, depth)
            depth -= 1
        elif "]" in lc or "]" in rc:
            #TODO remove this because probably wrong
            continue
        elif lc[0].isdigit() and rc[0].isdigit():
            # both ints so compare
            if lc == rc:
                continue
            elif int(lc) < int(rc):
                # Right order so exit
                # print(f"{(depth + 1) * '  '}Left side is smaller, so inputs are in the right order")
                raise true_error
            else:
                # right bigger so wrong
                # print(f"{(depth + 1)* '  '}Right side is smaller, so inputs are not in the right order")
                raise false_error
    if len(left) > len(right):
        # print(f"{depth * '  '}Right side ran out of items, so inputs are not in the right order")
        raise false_error
    if depth == 1:
        # Reached end
        # print("  Left side ran out of items, so inputs are in the right order")
        raise true_error

if __name__ == "__main__":
    pairs = []
    pair = []
    packets = []
    with open('example.txt') as data_file:
        for line in data_file:
            if line == '\n':
                pairs.append(pair)
                pair = []
            else:
                pair.append(line.strip())
                packets.append(line.strip()[1:-1].split(","))
        pairs.append(pair)
    part1_sum = 0
    for pi, pair in enumerate(pairs):
        left, right = pair
        # remove outermost bracket
        left = left[1:-1].split(",")
        right = right[1:-1].split(",")

        # print(f"\nPair {pi+1}:")
        depth = 1
        try:
            check_order(left, right, depth)
        except true_error:
            # print(True)
            part1_sum += pi + 1
        except false_error:
            # print(False)
            continue

    # print(f"Part1: {part1_sum}")

    first_input  = "[[2]]"[1:-1].split(",")
    second_input = "[[6]]"[1:-1].split(",")
    packets.append(first_input)
    packets.append(second_input)
    # still_sorting = True
    # run_i = 1
    # while still_sorting:
    #     # print(f"\nRun {run_i}")
    #     # for pack in packets:
    #     #     # print(pack)
    #     still_sorting = False
    #     for pi in range(1, len(packets)):
    #         # Check if infront of next
    #         first  = packets[pi-1]
    #         second = packets[pi]
    #         try:
    #             # # print("")
    #             check_order(first, second, depth)
    #         except true_error:
    #             # Right order so do nothing
    #             continue
    #         except false_error:
    #             # Switch them
    #             packets[pi-1] = second
    #             packets[pi] = first
    #             # Not done yet
    #             still_sorting = True
    #     run_i += 1

    still_sorting = True
    run_i = 1
    while still_sorting:
        still_sorting = False
        print(f"\nRun {run_i}")
        for i in range(1, len(packets)):
            # print(f"  Packet {i}")
            current_pos = packets[i]
            j = i - 1
            unordered = True
            while j >= 0 and unordered:
                # print(f"    J: {j}")
                packets[j + 1] = packets[j]
                j = j -1

                try:
                    check_order(current_pos, packets[j], depth)
                except true_error:
                    # Right order so do nothing
                    continue
                except false_error:
                    # Switch them
                    unordered = False
            packets[j + 1] = current_pos

        # Check if it's in the right order now
        for pi in range(1, len(packets)):
            # Check if infront of next
            first  = packets[pi-1]
            second = packets[pi]
            try:
                check_order(first, second, depth)
            except true_error:
                # Right order so do nothing
                continue
            except false_error:
                # Not done yet
                still_sorting = True
        run_i += 1
        if run_i%10 == 0:
            packets = packets[-1] + packets[:-1]
        for pack in packets:
            print(pack)

    for pi, pack in enumerate(packets):
        if pack == first_input:
            first_loc = pi + 1
        elif pack == second_input:
            second_loc = pi + 1
        print(pack)
    print(f"Part 2: {first_loc * second_loc}")
