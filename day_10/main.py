
def output_crt(cycle_i, x, row_buffer):
    # Row buffer stuff
    # print(f"\nCycle:       {cycle_i}")
    # print(f"Sprite:      {x}")
    if x + 1>= (cycle_i % 40) - 1 >= x - 1:
        # on
        row_buffer += "#"
    else:
        # off
        row_buffer += "."
    # print(f"Current row: {row_buffer[-1]}")
    if cycle_i % 40 == 0:
        print(row_buffer)
        row_buffer = ""
    return row_buffer

def check_signal_strength(cycle_i, x):
    # Signal stregth stuff
    if cycle_i % 40 == 20:
        #print(cycle_i * x, cycle_i, x)
        return cycle_i * x
    else:
        return 0


if __name__ == "__main__":
    cycle_i = 0
    x = 1
    signal_strength = 0
    row_buffer = ""
    with open('input.txt') as data_file:
        for line in data_file:
            if line.startswith("noop"):
                cycle_i += 1
                row_buffer = output_crt(cycle_i, x, row_buffer)
                signal_strength += check_signal_strength(cycle_i, x)
            else:
                addx = int(line.split()[1])
                # Nothing on first cycle
                cycle_i += 1
                row_buffer = output_crt(cycle_i, x, row_buffer)
                signal_strength += check_signal_strength(cycle_i, x)
                # add on second
                cycle_i += 1
                row_buffer = output_crt(cycle_i, x, row_buffer)
                signal_strength += check_signal_strength(cycle_i, x)
                x += addx

    print(f"Part 1: {signal_strength}")
