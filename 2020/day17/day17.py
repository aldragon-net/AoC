import numpy as np

N_STEPS = 6

with open('day17input.txt', 'r') as inpfile:
    lines = inpfile.readlines()

active_x = len(lines) + 2
max_x = active_x + 2*N_STEPS
shift_x = (max_x - active_x) // 2
active_y = len(lines[0].strip()) + 2
max_y = active_y + 2*N_STEPS
shift_y = (max_y - active_y) // 2
active_z = 3
max_z = active_z + 2*N_STEPS
shift_z = max_z  // 2
max_w, shift_w = max_z, shift_z

shape = (max_x, max_y, max_z, max_w)
print(shape, shift_z)

field = np.full(shape, False)
mirror = field.copy()

for x in range(len(lines)):
    for y in range(len(lines[x].strip())):
        if lines[x][y] == '#':
            field[x+shift_x][y+shift_y][shift_z][shift_w] = True


def count(field, x,y,z):
    count = np.sum(field[x-1:x+2,
                        y-1:y+2,
                        z-1:z+2,
                        w-1:w+2])
    if field[x,y,z,w]: count -= 1
    return count

step = 0
while True:
    step +=1
    for x in range(max_x):
        for y in range(max_y):
            for z in range(max_z):
                for w in range(max_w):
                    n = count(field,x,y,z)
                    if field[x,y,z,w] == True:
                        if 2 <= n <= 3:
                            mirror[x,y,z,w] = True
                        else:
                            mirror[x,y,z,w] = False
                    else:
                        if n == 3:
                            mirror[x,y,z,w] = True
                        else:
                            mirror[x,y,z,w] = False
    for x in range(max_x):
        for y in range(max_y):
            for z in range(max_z):
                for w in range(max_w):
                    field[x,y,z,w] = mirror[x,y,z,w]
    print('step', step)
    if step == N_STEPS:
        break

n_active = np.sum(field)

print('there are {} active cubes after 6th step'.format(n_active))
