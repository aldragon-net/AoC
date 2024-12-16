TEST = True
filename = 'test-2024-16.txt' if TEST else 'input-2024-16.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
max_x = len(lines[0]) - 1
max_y = len(lines) - 1
field = [[symbol for symbol in line] for line in lines]

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

scores = [[1000000000000 for x in range(len(lines[0]))] for y in range(len(lines))]

for x in range(max_x):
    for y in range(max_y):
        if field[y][x] == 'S':
            start_pos = (x, y)
        if field[y][x] == 'E':
            finish_pos = (x, y)


positions = [(2, start_pos)]
scores[start_pos[1]][start_pos[0]] = 0

while True:
    position = positions.pop()
    dir_num, coords = position
    x, y = coords
    for dir_change in range(-1, 2):
        dx, dy = directions[(dir_num + dir_change) % 4]
        if field[y+dy][x+dx] == '#':
            continue
        if scores[y+dy][x+dx] > scores[y][x] + 1000*abs(dir_change) + 1:
            scores[y+dy][x+dx] = scores[y][x] + 1000*abs(dir_change) + 1
            positions.append(((dir_num + dir_change) % 4, (x+dx, y+dy)))
    if not positions:
        break

best_spots = set(finish_pos)
to_trace = []
for n_dir, direction in enumerate(directions):
    dx, dy = direction
    if scores[finish_pos[1]-dy][finish_pos[0]-dx] == scores[finish_pos[1]][finish_pos[0]] - 1:
        to_trace.append((n_dir, (finish_pos[0]-dx, finish_pos[1]-dy)))
        best_spots.add((finish_pos[0]-dx, finish_pos[1]-dy))



while True:
    position = to_trace.pop()
    dir_num, coords = position
    x, y = coords
    for dir_change in range(-1, 2):
        dx, dy = directions[(dir_num + dir_change) % 4]
        if scores[y-dy][x-dx] == scores[y][x] - 1 or scores[y-dy][x-dx] == scores[y][x] - 1001 or scores[y-dy][x-dx] == scores[y][x] + 999:
            to_trace.append(((dir_num + dir_change) % 4, (x-dx, y-dy)))
            best_spots.add((x-dx, y-dy))
    if not to_trace:
        break

print(len(best_spots))