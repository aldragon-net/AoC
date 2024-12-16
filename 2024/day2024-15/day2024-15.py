TEST = False
field_file = 'test-field-2024-15.txt' if TEST else 'input-field-2024-15.txt'
moves_file = 'test-moves-2024-15.txt' if TEST else 'input-moves-2024-15.txt'

with open(field_file, 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
max_x = len(lines[0]) - 1
max_y = len(lines) - 1
field = [[symbol for x, symbol in enumerate(line)] for y, line in enumerate(lines)]

for x in range(max_x):
    for y in range(max_y):
        if field[y][x] == '@':
            robot_pos = (x, y)
            break

with open(moves_file, 'r') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
moves = ''.join(lines)

directions = {
    '<': (-1, 0),
    'v': (0, 1),
    '>': (1, 0),
    '^': (0, -1)
}

for move in moves:
    direction = directions[move]
    dx, dy = direction
    robot_x, robot_y = robot_pos
    to_move = [robot_pos]
    i = 1
    while True:
        next_x, next_y = robot_x + i*dx, robot_y + i*dy
        if field[next_y][next_x] == '#':
            to_move = False
            break
        if field[next_y][next_x] == '.':
            break
        if field[next_y][next_x] == 'O':
            to_move.append((next_x, next_y))
        i += 1
    if to_move:
        field[robot_y][robot_x] = '.'
        robot_pos = (robot_x + dx, robot_y + dy)
        for n, shift in enumerate(to_move):
            x, y = shift
            x, y = x + dx, y + dy
            field[y][x] = '@' if n == 0 else 'O'

sum = 0
for x in range(max_x+1):
    for y in range(max_y+1):
        if field[y][x] == 'O':
            sum += 100*y + x
print(sum)

# part 2

with open(field_file, 'r') as f:
    lines = f.readlines()

lines = [line.strip().replace('#', '##')
                     .replace('.', '..')
                     .replace('O', '[]')
                     .replace('@', '@.') for line in lines]
max_x = len(lines[0]) - 1
max_y = len(lines) - 1
field = [[symbol for x, symbol in enumerate(line)] for y, line in enumerate(lines)]

for x in range(max_x+1):
    for y in range(max_y+1):
        if field[y][x] == '@':
            robot_pos = (x, y)
            break

for y in range(max_y+1):
    print(''.join(field[y]))


for move in moves:
    direction = directions[move]
    dx, dy = direction
    robot_x, robot_y = robot_pos
    to_move = [('@', robot_pos)]

    if move in ['<', '>']:
        i = 1
        while True:
            next_x, next_y = robot_x + i*dx, robot_y + i*dy
            if field[next_y][next_x] == '#':
                to_move = False
                break
            if field[next_y][next_x] == '.':
                break
            if field[next_y][next_x] in ['[', ']']:
                to_move.append((field[next_y][next_x], (next_x, next_y)))
            i += 1
        if to_move:
            field[robot_y][robot_x] = '.'
            robot_pos = (robot_x + dx, robot_y + dy)
            for shift in to_move:
                symbol, pos = shift
                x, y = pos
                x, y = x + dx, y + dy
                field[y][x] = symbol
    
    if move in ['^', 'v']:
        blocked = False
        front_positions = [robot_pos]
        while True:
            clear = True
            new_front = []
            for front_pos in front_positions:
                front_x, front_y = front_pos
                next_front_x, next_front_y = front_x + dx, front_y + dy
                if field[next_front_y][next_front_x] == '#':
                    to_move = False
                    blocked = True
                    clear = False
                    break
                if field[next_front_y][next_front_x] == '.':
                    new_front.append((front_x, front_y))
                    continue
                if field[next_front_y][next_front_x] == ']':
                    new_front.append((next_front_x, next_front_y))
                    to_move.append((']', (next_front_x, next_front_y)))
                    new_front.append((next_front_x-1, next_front_y))
                    to_move.append(('[', (next_front_x-1, next_front_y)))
                    clear = False
                if field[next_front_y][next_front_x] == '[':
                    new_front.append((next_front_x, next_front_y))
                    to_move.append(('[', (next_front_x, next_front_y)))
                    new_front.append((next_front_x+1, next_front_y))
                    to_move.append((']', (next_front_x+1, next_front_y)))
                    clear = False
                if blocked:
                    break
            if blocked or clear:
                break
            front_positions = new_front[:]
        if to_move:
            robot_pos = (robot_x + dx, robot_y + dy)
            for shift in to_move:
                symbol, pos = shift
                x, y = pos
                field[y][x] = '.'
            for shift in to_move:
                symbol, pos = shift
                x, y = pos
                x, y = x + dx, y + dy
                field[y][x] = symbol
    
    # for y in range(max_y+1):
    #     print(''.join(field[y]))
    # print('after', move)
    # input()

sum = 0
for x in range(max_x+1):
    for y in range(max_y+1):
        if field[y][x] == '[':
            sum += 100*y + x
print(sum)