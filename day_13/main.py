import functools

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


def check_order_wrapper(left, right, depth=1):
    try:
        check_order(left, right, depth)
    except true_error:
        # print(True)
        return -1
    except false_error:
        # print(False)
        return 1


def parse_inputs(packet, depth, verbose=True):
    # print(f"{(depth - 1) * '  '}Compare [{','.join(left)}] vs [{','.join(right)}] line 29")
    # # print(f"{(depth - 1) * '  '}Compare [{left}] vs [{right}]")
    parsed_packet = []
    skip = 0
    for ci, part in enumerate(packet):
        if len(part) == 0:
            # print(f"{depth * '  '} empty {part}")
            continue
        if skip > 0:
            # print(f"{depth * '  '} skip {part} {skip}")
            skip -= 1
            continue
        if part[0] == "[":
            # both lists so get list and restart fucntion
            new_part  = get_list(ci, packet)
            skip = len(new_part) - 1
            # print(f"{depth * '  '} new_part {new_part}")
            depth += 1
            parsed_part = parse_inputs(new_part, depth)
            depth -= 1
            parsed_packet.append(parsed_part)
            continue
        # print(f"{depth * '  '}{part}")
        parsed_packet.append(int(part))
    return parsed_packet


def check_order(left, right, depth, verbose=False):
    # print(f"{(depth - 1) * '  '}Compare [{','.join(left)}] vs [{','.join(right)}] line 29")
    if verbose:
        print(f"{(depth - 1) * '  '}Compare {left} vs {right}")

    for ci, chars in enumerate(zip(left, right)):
        lc, rc = chars
        if type(lc) == list and type(rc) == list:
            # Perform double list checks
            # both lists so get list and restart fucntion
            depth += 1
            check_order(lc, rc, depth)
            depth -= 1
            continue
        if verbose:
            print(f"{depth * '  '}Compare {lc} vs {rc}")
        if type(lc) == list and type(rc) == int:
            # left is list so make right one as well
            if verbose:
                print(f"{depth * '  '}Mixed types; convert right to [{rc}] and retry comparison")
            depth += 1
            check_order(lc, [rc], depth)
            depth -= 1
        elif type(lc) == int and type(rc) == list:
            # right is list so make left one as well
            if verbose:
                print(f"{depth * '  '}Mixed types; convert left to [{lc}] and retry comparison")
            depth += 1
            check_order([lc], rc, depth)
            depth -= 1
        elif type(lc) == int and type(rc) == int:
            # both ints so compare
            if lc == rc:
                continue
            elif lc < rc:
                # Right order so exit
                if verbose:
                    print(f"{(depth + 1) * '  '}Left side is smaller, so inputs are in the right order")
                raise true_error
            else:
                # right bigger so wrong
                if verbose:
                    print(f"{(depth + 1)* '  '}Right side is smaller, so inputs are not in the right order")
                raise false_error


    if len(left) == 0 and len(right) == 0:
        if verbose:
            print(f"{(depth + 1)  * '  '}Both ran out so continue")
        return
    elif len(left) == 0:
        if verbose:
            print(f"{depth * '  '}Left side ran out of items, so inputs are in the right order")
        raise true_error
    elif len(right) == 0:
        if verbose:
            print(f"{depth * '  '}Right side ran out of items, so inputs are not in the right order")
        raise false_error
    elif len(right) < len(left):
        if verbose:
            print(f"{depth * '  '}Right side ran out of items, so inputs are not in the right order")
        raise false_error

    if depth == 1:
        # Reached end
        if verbose:
            print("  Left side ran out of items, so inputs are in the right order")
        raise true_error

if __name__ == "__main__":
    pairs = []
    pair = []
    packets = []
    with open('input.txt') as data_file:
        for line in data_file:
            if line == '\n':
                pairs.append(pair)
                pair = []
            else:
                parsed = parse_inputs(line.strip()[1:-1].split(","), 1)
                pair.append(parsed)
                packets.append(parsed)
        pairs.append(pair)
    part1_sum = 0
    for pi, pair in enumerate(pairs):
        left, right = pair

        print(f"\n== Pair {pi + 1} ==")
        depth = 1
        try:
            check_order(left, right, depth)
        except true_error:
            # print(True)
            print(pi + 1)
            part1_sum += pi + 1
        except false_error:
            # print(False)
            continue

    print(f"Part 1: {part1_sum}")

    first_input  = [[2]]
    second_input = [[6]]
    packets.append(first_input)
    packets.append(second_input)
    packets = sorted(packets, key=functools.cmp_to_key(check_order_wrapper))

    for pi, pack in enumerate(packets):
        if pack == first_input:
            first_loc = pi + 1
        elif pack == second_input:
            second_loc = pi + 1
        # print(pack)
    print(f"Part 2: {first_loc * second_loc}")
