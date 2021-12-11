import numpy as np

with open('input_day11.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    f.close()

field = np.zeros((10, 10), dtype=np.int16)

for i in range(len(lines)):
    for j in range(len(lines[0])):
        field[i, j] = int(lines[i][j])


N_STEPS = 100

n = 0
sum_flashes = 0

while True:
    n += 1
    # increasing
    field = field + 1
    # flashing
    flashed = []
    while True:
        new_flashed = []
        for x in range(10):
            for y in range(10):
                if field[x, y] > 9:
                    if (x, y) not in flashed:
                        new_flashed.append((x, y))
        if len(new_flashed) == 0:
            break
        flashed.extend(new_flashed)
        for point in new_flashed:
            x, y = point
            x1 = max(x-1, 0)
            x2 = min(x+1, 10)
            y1 = max(y-1, 0)
            y2 = min(y+1, 10)
            field[x1:x2+1, y1:y2+1] = field[x1:x2+1, y1:y2+1] + 1
    for point in flashed:
        x, y = point
        field[x, y] = 0
    sum_flashes += len(flashed)
    if n == N_STEPS:
        print(sum_flashes, 'flashes after step', N_STEPS)
    if len(flashed) == 100:
        print('all flashed at step', n)
        break
