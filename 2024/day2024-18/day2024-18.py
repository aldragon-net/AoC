import numpy as np

TEST = False
filename = 'test-2024-18.txt' if TEST else 'input-2024-18.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

FIELD_X = 6 if TEST else 70
FIELD_Y = 6 if TEST else 70
MOVES = 12 if TEST else 1024

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def out_of_field(coords):
    x, y = coords
    return (x < 0 or x > FIELD_X or y < 0 or y > FIELD_Y)


def make_field(moves):
    field = np.zeros((FIELD_X+1, FIELD_Y+1))
    for i in range(moves):
        x, y = [int(x) for x in lines[i].strip().split(',')]
        field[x, y] = 1
    return field


def solve(field):
    scores = [[1000000000000 for x in range(FIELD_X+1)] for y in range(FIELD_Y+1)]
    positions = [(0, 0)]
    scores[0][0] = 0
    while True:
        position = positions.pop()
        x, y = position
        for direction in directions:
            dx, dy = direction
            if out_of_field((x+dx, y+dy)) or field[x+dx, y+dy] == 1:
                continue
            if scores[x+dx][y+dy] > scores[x][y] + 1:
                scores[x+dx][y+dy] = scores[x][y] + 1
                positions.append((x+dx, y+dy))
        if not positions:
            break
    if scores[FIELD_X][FIELD_Y] == 1000000000000:
        return False
    return scores[FIELD_X][FIELD_Y]


bytes = len(lines)
delta = len(lines) // 2 + 1
old_result = False
while True:
    print(f'solving with {bytes} bytes; byte {bytes-1} is {lines[bytes-1].strip()}')
    field = make_field(bytes)
    result = solve(field)
    if result:
        bytes = bytes + delta
        print(f'Solved, result {result}\n')
    else:
        print('Unsolvable\n')
        bytes = bytes - delta
    if result != old_result and delta == 1:
        break
    old_result = result
    delta = delta // 2 if delta > 1 else 1
