filename = 'input-2018-10.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

dots = []
for line in lines:
    x, y, vx, vy = int(line[10:16]), int(line[18:24]), int(line[36:38]), int(line[40:42])
    dots.append([x, y, vx, vy])

time = 0
while True:
    time += 1
    for dot in dots:
        dot[0] += dot[2]
        dot[1] += dot[3]
    xs = [dot[0] for dot in dots]
    ys = [dot[1] for dot in dots]
    max_xs, min_xs = max(xs), min(xs)
    max_ys, min_ys = max(ys), min(ys)
    spread_x = max_xs - min_xs
    spread_y = max_ys - min_ys
    if spread_y == 9:  # min value from sequence
        field = [[' ' for i in range(62)] for j in range(10)]
        for dot in dots:
            x, y = dot[0]-min_xs, dot[1]-min_ys
            field[y][x] = '#'
        for line in field:
            print(''.join(line))
        print('time =', time)
        break
