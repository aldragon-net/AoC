import re

TEST = False

if TEST:
    filename = 'test-2024-14.txt'
    MAX_X = 11
    MAX_Y = 7
else:
    filename = 'input-2024-14.txt'
    MAX_X = 101
    MAX_Y = 103

TIME = 100


with open(filename, 'r') as f:
    lines = f.readlines()

robots = []
for line in lines:
    data = ([int(x) for x in re.findall(r'-?\d+', line)])
    robots.append(((data[0], data[1]), (data[2], data[3])))


def predict_position(coords, velocity, time):
    x, y = coords
    vx, vy = velocity
    new_x = (x + vx*time) % MAX_X
    new_y = (y + vy*time) % MAX_Y
    return (new_x, new_y)

def count_quadrants(positions):
    q1 = q2 = q3 = q4 = 0
    for position in positions:
        x, y = position
        if x < (MAX_X - 1) / 2:
            if y < (MAX_Y - 1) / 2:
                q1 += 1
            if y > (MAX_Y - 1) / 2:
                q2 += 1
        if x > (MAX_X - 1) / 2:
            if y < (MAX_Y - 1) / 2:
                q3 += 1
            if y > (MAX_Y - 1) / 2:
                q4 += 1
    return (q1, q2, q3, q4)


positions = []
for robot in robots:
    position, velocity = robot
    positions.append(predict_position(position, velocity, TIME))

quadrants = count_quadrants(positions)

result = 1
for q in quadrants:
    result = result*q


moves = 8270
while True:
    field = [[' ' for x in range(MAX_X)] for y in range(MAX_Y)]
    positions = []
    for robot in robots:
        position, velocity = robot
        positions.append(predict_position(position, velocity, moves))
    for position in positions:
        field[position[1]][position[0]] = '#'
    for line in field:
        print(''.join(line) + '|')
    print('time = ', moves)
    input()
    moves += 101 



