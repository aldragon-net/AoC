import numpy as np

with open('input_day09.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    f.close()

field = np.zeros((len(lines), len(lines[0])))

for i in range(len(lines)):
    for j in range(len(lines[0])):
        field[i, j] = int(lines[i][j])

sum = 0
basins = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if i-1 >= 0:
            k = i-1
        else:
            k = 0
        if i+1 <= 100:
            L = i+1
        else:
            L = 100
        if j-1 >= 0:
            m = j-1
        else:
            m = 0
        if j+1 <= 100:
            n = j+1
        else:
            n = 100 
        search = field[k:L+1, m:n+1]
        if field[i, j] == search.min():
            sum += field[i, j] + 1
            basins.append((i, j))
print(int(sum))


def scan_basin(basin):
    points = {basin, }
    while True:
        added = []
        for point in points:
            x, y = point
            for i in [-1, 1]:
                if 0 <= (x+i) <= 99 and 0 <= (y+i) <= 99:
                    if ((x+i, y) not in points) and field[x+i, y] != 9:
                        added.append((x+i, y))
                    if ((x, y+i) not in points) and field[x, y+i] != 9:
                        added.append((x, y+i))                         
        if added == []:
            break
        else:
            for point in added:
                points.add(point)
    return len(points)


lengths = []
for basin in basins:
    lengths.append(scan_basin(basin))

lengths.sort(reverse=True)

print(lengths[0]*lengths[1]*lengths[2])
