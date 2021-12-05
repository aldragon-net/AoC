import numpy as np

with open('input_day05.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    f.close()

field = np.zeros((1000, 1000))

for line in lines:
    x1, y1 = line.split(' -> ')[0].split(',')
    x2, y2 = line.split(' -> ')[1].split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if x1 == x2:
        line_points = []
        start_y = min(y1, y2)
        end_y = max(y1, y2)
        for i in range(start_y, end_y + 1):
            field[x1, i] = field[x1, i] + 1
    if y1 == y2:
        line_points = []
        start_x = min(x1, x2)
        end_x = max(x1, x2)
        for i in range(start_x, end_x + 1):
            field[i, y1] = field[i, y1] + 1
    if x1 != x2 and y1 != y2:
        line_points = []
        start_x = min(x1, x2)
        end_x = max(x1, x2)
        sign = 1
        if start_x == x1:
            start_y = y1
            if y2 < y1:
                sign = -1
        else:
            start_y = y2
            if y1 < y2:
                sign = -1
        for i in range(end_x - start_x + 1):
            field[start_x+i, start_y + i*sign] = field[start_x+i,
                                                       start_y + i*sign] + 1

cells = field >= 2
print(cells.sum())
