import numpy as np

with open('day11input.txt') as inpfile:
    field = []
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        row = []
        for ch in line:
            if ch == 'L':
                row.append(0)
            elif ch == '.':
                row.append(16)
            elif ch == '#':
                row.append(1)
        field.append(row)
    field = np.array(field)

d1, d2 = field.shape


def nextstep(field):
    def count1(i,j):
        l1 = max(i-1,0)
        r1 = min(i+1,d1-1)
        l2 = max(j-1,0)
        r2 = min(j+1,d2-1)
        count = ((field[l1:r1+1,l2:r2+1] % 16).sum() - field[i,j])
        return count
    def count2(i,j):
        count = 0
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                l = 1
                while True:
                    di = dx*l
                    dj = dy*l
                    if di == 0 and dj == 0:
                        break
                    if (i+di<0) or (i+di>=d1):
                        break
                    if (j+dj<0) or (j+dj>=d2):
                        break
                    if field[i+di,j+dj] == 16:
                        l += 1
                        continue
                    else:
                        count += field[i+di,j+dj]
                        break
        return count
    n_changes = 0
    mirror = field.copy()
    for i in range(d1):
        for j in range(d2):
            if field[i,j] == 16:
                mirror[i,j] = 16
            else:
                if field[i,j] == 0 and count2(i,j) == 0:
                    mirror[i,j] = 1
                    n_changes += 1
                elif field[i,j] == 1 and count2(i,j)>=5:
                    mirror[i,j] = 0
                    n_changes += 1
    return mirror, n_changes


n_steps = 0
while True:
    field, n_changes = nextstep(field)
    n_steps += 1
    print(n_steps)
    if n_changes == 0:
        break

print('Stopped after {} steps'.format(n_steps))
n_occup = (field == 1).sum()
print(n_occup)

#TODO make it not so horrible