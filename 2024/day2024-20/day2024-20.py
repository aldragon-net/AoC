TEST = False
filename = 'test-2024-20.txt' if TEST else 'input-2024-20.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

MIN_CHEAT = 50 if TEST else 100

lines = [line.strip() for line in lines]
max_x = len(lines[0]) - 1
max_y = len(lines) - 1
field = [[symbol for symbol in line] for line in lines]


def out_of_field(coords):
    x, y = coords
    return (x < 0 or x > max_x or y < 0 or y > max_y)


for x in range(max_x):
    for y in range(max_y):
        if field[y][x] == 'S':
            start_pos = (x, y)
        if field[y][x] == 'E':
            finish_pos = (x, y)

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

scores = [[1000000000000 for x in range(len(lines[0]))] for y in range(len(lines))]

positions = [start_pos]
scores[start_pos[1]][start_pos[0]] = 0

for x in range(max_x):
    for y in range(max_y):
        if field[y][x] == 'S':
            start_pos = (x, y)
        if field[y][x] == 'E':
            finish_pos = (x, y)

while True:
    position = positions.pop()
    x, y = position
    for direction in directions:
        dx, dy = direction
        if field[y+dy][x+dx] == '#':
            continue
        if scores[y+dy][x+dx] > scores[y][x] + 1:
            scores[y+dy][x+dx] = scores[y][x] + 1
            positions.append((x+dx, y+dy))
    if not positions:
        break

# backtrack:
cheatdir = [(-2, 0), (0, -2), (2, 0), (0, 2)]
cheats = []

x, y = finish_pos
while scores[y][x] > 0:
    for direction in cheatdir:
        dx, dy = direction
        if out_of_field((x+dx, y+dy)):
            continue
        diff = scores[y][x] - scores[y+dy][x+dx]
        if diff > MIN_CHEAT:
            cheats.append((diff-2, (x, y)))
    for direction in directions:
        dx, dy = direction
        if out_of_field((x+dx, y+dy)):
            continue
        if scores[y][x] - scores[y+dy][x+dx] == 1:
            x = x + dx
            y = y + dy
            break

# cheats.sort(key=lambda x: x[0], reverse=True)
# # print(cheats)
print(len(cheats))


cheat_shifts = set()
for dx in range(-20, 21):
    for dy in range(-20, 21):
        length = abs(dx) + abs(dy)
        if length <= 20:
            cheat_shifts.add((length, (dx, dy)))

cheats = []
x, y = finish_pos
while scores[y][x] > 0:
    for shift in cheat_shifts:
        cost, coords = shift
        dx, dy = coords
        if out_of_field((x+dx, y+dy)):
            continue
        diff = scores[y][x] - scores[y+dy][x+dx]
        if diff >= MIN_CHEAT + cost:
            cheats.append((diff-cost, (x, y)))
    for direction in directions:
        dx, dy = direction
        if out_of_field((x+dx, y+dy)):
            continue
        if scores[y][x] - scores[y+dy][x+dx] == 1:
            x = x + dx
            y = y + dy
            break

# cheats.sort(key=lambda x: x[0], reverse=True)
# print(cheats)
print(len(cheats))
