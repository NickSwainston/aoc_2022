shape_score = {
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3, # Scissors
}
# A rock
# B Paper
# C Scissors

outcome_score = {
    # Draws
    "AX": 3,
    "BY": 3,
    "CZ": 3,
    # Wins
    "AY": 6,
    "BZ": 6,
    "CX": 6,
    # Loses
    "AZ": 0,
    "BX": 0,
    "CY": 0,
}

needed_score = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

part1_total = 0
part2_total = 0
with open('input.txt') as data_file:
    for line in data_file:
        # Part 1
        them, me = line.split()
        score = shape_score[me] + outcome_score[f"{them}{me}"]
        part1_total += score
        # print(them, me, score)

        # Part 2
        them, need = line.split()
        goal_score = needed_score[need]
        for pair in outcome_score.keys():
            # print(pair, them, outcome_score[pair], goal_score),
            if pair.startswith(them) and outcome_score[pair] == goal_score:
                goal_shape = shape_score[pair[-1]]
        score = goal_shape + goal_score
        print(score)
        part2_total += score
print(f"Part 1: {part1_total}")
print(f"Part 2: {part2_total}")