import numpy as np

TEST = False
filename = 'test-2024-10.txt' if TEST else 'input-2024-10.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines = lines[::-1]

max_x = len(lines[0]) - 1
max_y = len(lines) - 1

field = np.zeros((max_x+1, max_y+1))

for y, line in enumerate(lines):
    for x, symbol in enumerate(line):
        field[x, y] = int(symbol)


def trace_routes(pos):

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def out_of_field(coords):
        x, y = coords
        return (x < 0 or x > max_x or y < 0 or y > max_y)

    def step(pos):
        nonlocal count
        x, y = pos
        value = field[x, y]
        if value == 9:
            uniq_nines.add((x, y))
            count += 1
            return
        for direction in directions:
            dx, dy = direction
            if out_of_field((x+dx, y+dy)):
                continue
            if field[x+dx, y+dy] == value + 1:
                step((x+dx, y+dy))
        return

    uniq_nines = set()
    count = 0
    step(pos)
    return len(uniq_nines), count


scoresum_1 = 0
scoresum_2 = 0
for x in range(max_x+1):
    for y in range(max_y+1):
        if field[x, y] == 0:
            score_1, score_2 = trace_routes((x, y))
            scoresum_1 += score_1
            scoresum_2 += score_2

print(scoresum_1)
print(scoresum_2)
