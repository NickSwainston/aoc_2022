import numpy as np


def dfs_paths(elevations, start, end, nrows, ncols, unvisted_pos):
    stack = [(start, [start])]
    si = 0
    while stack:
        si += 1
        current, path = stack.pop(0)
        current_row, current_col = current
        current_height = elevations[current_row][current_col]
        left  = (current_row,     current_col - 1)
        right = (current_row,     current_col + 1)
        up    = (current_row - 1, current_col)
        down  = (current_row + 1, current_col)
        # print(f"\nStack {si:03d}  : {current} {path}")
        fi = 0
        for next in [left, right, up, down]:
            fi += 1
            row, col = next
            # new_height = elevations[row][col]
            if 0 > row  or row > nrows - 1 or 0 > col or col > ncols - 1:
                # outside of grid
                # print(f"Stack {si:03d} {fi}: {next} outside")
                continue
            elif elevations[row][col] > current_height + 1:
                # Too high
                # print(f"Stack {si:03d} {fi}: {next} too high")
                # print(elevations[row][col], current_height)
                continue
            elif next in path:
                # Don't loop around
                # print(f"Stack {si:03d} {fi}: {next} previous")
                continue
            elif next not in unvisted_pos:
                # Already been to in a shorter root
                # print(f"Stack {si:03d} {fi}: {next} not short")
                continue
            elif next == end and elevations[row][col] > 24:
                # return the path
                # print(stack + [next])
                yield path + [next]
            else:
                # print(f"Stack {si:03d} {fi}: {next} good")
                unvisted_pos.remove(next)
                stack.append((next, path + [next]))


if __name__ == "__main__":
    elevations = []
    with open('input.txt') as data_file:
        for line in data_file:
            elevations.append([ord(char) - 96 for char in line.strip()])
    elevations = np.array(elevations, dtype=int)

    nrows, ncols = elevations.shape
    print(f"Size : ({nrows}, {ncols})")

    orig_start = np.where(elevations == -27)
    orig_start = (orig_start[0][0],   orig_start[1][0])
    end = np.where(elevations == -27)
    end = (end[0][0],   end[1][0])
    elevations[orig_start[0]][orig_start[1]] = 1
    elevations[end[0]][end[1]] = 26

    possible_starts = []
    for ri in range(nrows):
        for ci in range(ncols):
            if elevations[ri][ci] == 1:
                possible_starts.append((ri, ci))

    possible_lengths = []
    for start in possible_starts:
        unvisted_pos = []
        for ri in range(nrows):
            for ci in range(ncols):
                unvisted_pos.append((ri, ci))

        paths = list(dfs_paths(elevations, start, end, nrows, ncols, unvisted_pos))
        # print(paths)
        if len(paths) == 0:
            continue

        lengths = [ len(i) for i in paths ]
        min_path = min(lengths) - 1
        if start == orig_start:
            print(f"Part 1: {min_path}")
        possible_lengths.append(min_path)

    print(f"Part 2: {min(possible_lengths)}")
