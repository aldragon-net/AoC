# with open('test.txt', 'r') as f:
with open('input_day17-2022.txt', 'r') as f:
    jets = f.readline().strip()

rocks = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (0, 1), (1, 0), (1, 1))
]


def glass_height(glass):
    max_y = 0
    for block in glass:
        x, y = block
        if y > max_y:
            max_y = y
    return max_y


glass = set()

floor = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
for block in floor:
    glass.add(block)


rock_count = 0
moves = 0

while rock_count < 2022:
    rock_pattern = rocks[rock_count % 5]
    rock_count += 1
    rock = []
    for block in rock_pattern:
        x, y = block
        start_y = glass_height(glass) + 4
        rock.append([x+2, y+start_y])
    falling = True
    while falling:
        if jets[moves] == '>':
            dx = 1
        elif jets[moves] == '<':
            dx = -1
        moves = (moves + 1) % len(jets)
        for block in rock:
            x, y = block
            if x+dx < 0 or x+dx > 6 or (x+dx, y) in glass:
                break
        else:
            for block in rock:
                block[0] += dx
        for block in rock:
            x, y = block
            if (x, y-1) in glass:
                for block in rock:
                    glass.add(tuple(block))
                falling = False
                break
        else:
            for block in rock:
                block[1] -= 1

print(glass_height(glass))
