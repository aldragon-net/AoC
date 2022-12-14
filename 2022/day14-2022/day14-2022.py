# with open('test.txt', 'r') as f:
with open('input_day14-2022.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

field = [[0] * 400 for _ in range(200)]
XSHIFT = 300

max_y = 0
for line in lines:
    pairs = line.split(' -> ')
    for i in range(1, len(pairs)):
        x1, y1 = pairs[i-1].split(',')
        x1 = int(x1) - XSHIFT
        y1 = int(y1)
        x2, y2 = pairs[i].split(',')
        x2 = int(x2) - XSHIFT
        y2 = int(y2)
        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2
        if x1 == x2:
            if y2 < y1:
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                field[y][x1] = 1
        if y1 == y2:
            if x2 < x1:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                field[y1][x] = 1

# part 2; comment for part 1
FLOOR_LEVEL = max_y + 2
for i in range(len(field[FLOOR_LEVEL])):
    field[FLOOR_LEVEL][i] = 1
# end of part 2 block


sand_count = 0


def simulate_sand():
    x = 200
    y = 0
    abyss = False
    source_blocked = False
    while True:
        if field[y+1][x] == 0:
            y += 1
        elif field[y+1][x-1] == 0:
            y += 1
            x -= 1
        elif field[y+1][x+1] == 0:
            y += 1
            x += 1
        else:
            field[y][x] = 2
            if y == 0 and x == 200:
                source_blocked = True
            break
        if y > 198:
            abyss = True
            break
    return abyss, source_blocked


while True:
    sand_count += 1
    abyss, source_blocked = simulate_sand()
    if source_blocked:  # use for part 2
        print(sand_count)
        break
    # if abyss:  # use for part 1
    #     print(sand_count-1)
    #     break
