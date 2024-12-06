import numpy as np

TEST = False
filename = 'test-2024-06.txt' if TEST else 'input-2024-06.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines = lines[::-1]

max_x = len(lines[0]) - 1
max_y = len(lines) - 1

field = np.zeros((max_x+1, max_y+1))
visited = set()


def rotate_right(direction):
    x, y = direction
    x, y = y, -x
    return (x, y)


def rotate_left(direction):
    x, y = direction
    x, y = -y, x
    return (x, y)


def move(x, y, direction):
    dx, dy = direction
    x += dx
    y += dy
    return (x, y)


def out_of_field(x, y):
    return (x < 0 or x > max_x or y < 0 or y > max_y)


def check_cycle(x, y, direction, x_obs, y_obs):
    visited = set()
    while True:
        if (x, y, direction) in visited:
            return True
        visited.add((x, y, direction))
        next_x, next_y = move(x, y, direction)
        if out_of_field(next_x, next_y):
            return False
        if field[next_x, next_y] != 0 or (next_x == x_obs and next_y == y_obs):
            direction = rotate_right(direction)
            continue
        x, y = next_x, next_y


for y, line in enumerate(lines):
    for x, symbol in enumerate(line):
        if line[x] == '^':
            start_x, start_y = x, y
            pos_x, pos_y = x, y
            direction = (0, 1)
            continue
        if line[x] == '#':
            field[x, y] = 1

obstacles = set()

while True:
    visited.add((pos_x, pos_y))
    next_x, next_y = move(pos_x, pos_y, direction)

    if (not out_of_field(next_x, next_y)
            and field[next_x, next_y] == 0
            and (next_x, next_y) not in visited
            and not (next_x == start_x and next_y == start_y)):

        if check_cycle(pos_x, pos_y, direction, next_x, next_y):
            obstacles.add((next_x, next_y))

    if out_of_field(next_x, next_y):
        break
    if field[next_x, next_y] != 0:
        direction = rotate_right(direction)
        continue

    pos_x, pos_y = next_x, next_y

print(len(visited))
print(len(obstacles))
