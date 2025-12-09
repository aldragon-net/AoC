import copy

TEST = False
filename = 'test-2025-04.txt' if TEST else 'input-2025-04.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

MAX_Y = len(lines)
MAX_X = len(lines[0].strip())

directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]

field = [['O' for i in range(MAX_X + 2)]]
for line in lines:
    field_line = 'O' + line.strip() + 'O'
    field.append([x for x in field_line])
field.append(['O' for i in range(MAX_X + 2)])


counter = 0
for x in range(1, MAX_X+1):
    for y in range(1, MAX_Y+1):
        if field[y][x] != '@':
            continue
        neighbours = 0
        for shift in directions:
            dx, dy = shift
            if field[y+dy][x+dx] == '@':
                neighbours += 1
        if neighbours < 4:
            counter += 1
print(counter)

total_removed = 0
while True:
    removed = 0
    new_field = copy.deepcopy(field)
    for x in range(1, MAX_X+1):
        for y in range(1, MAX_Y+1):
            if field[y][x] != '@':
                continue
            neighbours = 0
            for shift in directions:
                dx, dy = shift
                if field[y+dy][x+dx] == '@':
                    neighbours += 1
            if neighbours < 4:
                new_field[y][x] = '.'
                removed += 1
    print(removed)
    total_removed += removed
    field = new_field
    if removed == 0:
        break

print(total_removed)
