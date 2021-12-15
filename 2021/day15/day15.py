import numpy as np

with open('input_day15.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    f.close()


def get_min(i, j):
    try:
        near_1 = search[i-1, j]
    except:
        near_1 = 99999
    try:
        near_2 = search[i+1, j]
    except:
        near_2 = 99999
    try:
        near_3 = search[i, j-1]
    except:
        near_3 = 99999
    try:
        near_4 = search[i, j+1]
    except:
        near_4 = 99999
    return min(near_1, near_2, near_3, near_4)


# part 1

field = np.zeros((100, 100), dtype=np.int16)

search = np.ones((100, 100), dtype=np.int32) * 99999
search[0, 0] = 0

for i in range(100):
    for j in range(100):
        field[i, j] = int(lines[i][j])

while True:
    changes = 0
    for i in range(100):
        for j in range(100):
            if search[i, j] > field[i, j] + get_min(i, j):
                search[i, j] = field[i, j] + get_min(i, j)
                changes += 1
    if changes == 0:
        break

print('part 1:', search[99, 99])

# part 2

field = np.zeros((500, 500), dtype=np.int16)

search = np.ones((500, 500), dtype=np.int32) * 99999
search[0, 0] = 0

for i in range(500):
    for j in range(500):
        field[i, j] = (int(lines[i % 100][j % 100]) + i//100 + j//100 - 1) % 9 + 1

print(field)

while True:
    changes = 0
    for i in range(500):
        for j in range(500):
            if search[i,j] > field[i,j] + get_min(i, j):
                search[i,j] = field[i, j] + get_min(i, j)
                changes += 1
    print(changes)
    if changes == 0:
        break

print('part 2:', search[499, 499])
