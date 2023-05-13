import numpy as np

def move_head(head_pos, direction):
    row, col = head_pos
    if direction == 'L':
        col -= 1
    elif direction == 'R':
        col += 1
    elif direction == 'D':
        row -= 1
    elif direction == 'U':
        row += 1
    return (row, col)

def output_stage(knot_pos, size=5, nknots=10):
    print("")
    for ri in range(size-1, -1, -1):
        row = ""
        for ci in range(size):
            result = "."
            if knot_pos[0][0] == ri and knot_pos[0][1] == ci:
                result = 'H'
            for ki in range(1,nknots):
                if knot_pos[ki][0] == ri and knot_pos[ki][1] == ci and result != 'h':
                    result = f"{ki}"
            row += result
        print(row)

def update_tail(head_pos, tail_pos):
    row_dist = head_pos[0] - tail_pos[0]
    col_dist = head_pos[1] - tail_pos[1]
    distance = np.sqrt(col_dist**2 + row_dist**2)

    if distance > np.sqrt(2):
        # Needs to move
        if abs(col_dist) > abs(row_dist):
            # move to same row
            row = head_pos[0]
            if col_dist > 0:
                col = head_pos[1] - 1
            else:
                col = head_pos[1] + 1
        elif abs(col_dist) == abs(row_dist):
            # move to diagonal
            if col_dist > 0:
                col = head_pos[1] - 1
            else:
                col = head_pos[1] + 1
            if row_dist > 0:
                row = head_pos[0] - 1
            else:
                row = head_pos[0] + 1
        else:
            # move to same col
            col = head_pos[1]
            if row_dist > 0:
                row = head_pos[0] - 1
            else:
                row = head_pos[0] + 1
    else:
        row, col = tail_pos
    return (row, col)


if __name__ == "__main__":
    move_pos = []
    with open('input.txt') as data_file:
        for line in data_file:
            move_pos.append( (line.split()[0], int(line.split()[1])) )

    size = 1000
    knot_pos = [(size//2, size//2)] * 2

    tail_count = np.zeros((size, size))
    for direction, distance in move_pos:
        print(knot_pos[0])
        for di in range(distance):
            knot_pos[0] = move_head(knot_pos[0], direction)
            knot_pos[-1] = update_tail(knot_pos[0], knot_pos[-1])
            #output_stage(knot_pos[0], knot_pos[-1], size)
            tail_count[knot_pos[-1][0], knot_pos[-1][1]] += 1

    part1_count = tail_count > 0
    print(f"Part 1: {part1_count.sum()}")

    knot_pos = [(size//2, size//2)] * 10
    tail_count = np.zeros((size, size))
    for direction, distance in move_pos:
        for di in range(distance):
            # move head
            knot_pos[0] = move_head(knot_pos[0], direction)
            for ti in range(1,10):
                # update each knot
                knot_pos[ti] = update_tail(knot_pos[ti-1], knot_pos[ti])
            tail_count[knot_pos[-1][0], knot_pos[-1][1]] += 1
        #output_stage(knot_pos, size)
    part2_count = tail_count > 0
    print(f"Part 2: {part2_count.sum()}")
