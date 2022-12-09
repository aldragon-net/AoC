with open('input_day09-2022.txt', 'r') as f:
# with open('test.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


directions = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0
tail_pos = set()
tail_pos.add((tail_x, tail_y))

knots = [[0,0] for _ in range(10)]

# def move_tail(head_x, head_y, tail_x, tail_y):
#     print(head_x, head_y, tail_x, tail_y)
#     if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
#         return False, tail_x, tail_y
#     if abs(head_x - tail_x) > 0:
#         tail_x += (head_x - tail_x) // abs(head_x - tail_x)
#     if abs(head_y - tail_y) > 0:
#         tail_y += (head_y - tail_y) // abs(head_y - tail_y)
#     tail_pos.add((tail_x, tail_y))
#     return True, tail_x, tail_y


# for line in lines:
#     direction, steps = line.split()
#     steps = int(steps)
#     dx, dy = directions[direction]
#     for step in range(steps):
#         head_x += dx
#         head_y += dy
#         while True:
#             moved, tail_x, tail_y = move_tail(head_x, head_y, tail_x, tail_y)
#             if not moved:
#                 break


def move_knots(head_x, head_y):
    knots[0] = [head_x, head_y]
    for i in range(1, 10):
        if (abs(knots[i][0] - knots[i-1][0]) <= 1 and 
                abs(knots[i][1] - knots[i-1][1]) <= 1):
            continue
        if abs(knots[i][0] - knots[i-1][0]) > 0:
            knots[i][0] += (knots[i-1][0] - knots[i][0]) // abs(knots[i-1][0] - knots[i][0])
        if abs(knots[i][1] - knots[i-1][1]) > 0:
            knots[i][1] += (knots[i-1][1] - knots[i][1]) // abs(knots[i-1][1] - knots[i][1])
        tail_pos.add((tail_x, tail_y))
    return True, tail_x, tail_y


for line in lines:
    direction, steps = line.split()
    steps = int(steps)
    dx, dy = directions[direction]
    for step in range(steps):
        head_x += dx
        head_y += dy
        move_knots(head_x, head_y)
        tail_pos.add((knots[-1][0], knots[-1][1]))

print(len(tail_pos))
