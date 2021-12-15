import numpy as np

with open('input_day15.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    f.close()

field = np.zeros((100,100), dtype=np.int16)

search = np.ones((100,100), dtype=np.int16) * 9999
search[0,0] = 0

for i in range(100):
    for j in range(100):
        field[i ,j] = int(lines[i][j])

print(field)
print(search)

def get_min(i,j):
    if 0<i<99 and 0<j<99:
        return min(search[i-1,j], search[i+1,j],
                   search[i, j-1], search[i, j+1])
    elif i == 0 and j == 0:
        return min(search[i+1, j], search[i, j+1])
    elif i == 99 and j == 99:
        return min(search[i-1, j], search[i, j-1])
    elif i == 0 and j == 99:
        return min(search[i+1, j], search[i, j-1])
    elif i == 99 and j == 0:
        return min(search[i-1, j], search[i, j+1])
    elif i == 0:
        return min(search[i+1, j], search[i, j+1], search[i, j-1])
    elif j == 0:
        return min(search[i+1, j], search[i-1, j], search[i, j+1])
    elif i == 99:
        return min(search[i-1, j], search[i, j+1], search[i, j-1])
    elif j == 99:
        return min(search[i+1, j], search[i-1, j], search[i, j-1])

while True:
    changes = 0
    for i in range(100):
        for j in range(100):
            if search[i,j] > field[i,j] + get_min(i, j):
                search[i,j] = field[i, j] + get_min(i, j)
                changes += 1
    print(changes)
    print(search)
    input()
