with open('input_day08.txt', 'r') as f:
    lines = f.readlines()

screen = [[0] * 6 for _ in range(50)]


def rect(x, y):
    for i in range(x):
        for j in range(y):
            screen[i][j] = 1


def rotate_column(x, shift):
    new_column = [None] * 6
    for i in range(6):
        new_column[i] = screen[x][(i-shift) % 6]
    for i in range(6):
        screen[x][i] = new_column[i]


def rotate_row(y, shift):
    new_row = [None] * 50
    for i in range(50):
        new_row[i] = screen[(i-shift) % 50][y]
    for i in range(50):
        screen[i][y] = new_row[i]


def count_lights():
    count = 0
    for i in range(50):
        for j in range(6):
            count += screen[i][j]
    return count


for line in lines:
    line = line.strip().split()
    if line[0] == 'rect':
        x, y = [int(i) for i in line[1].split('x')]
        rect(x, y)
    elif line[0] == 'rotate':
        shift = int(line[-1])
        if line[1] == 'row':
            y = int(line[2].split('=')[-1])
            rotate_row(y, shift)
        elif line[1] == 'column':
            x = int(line[2].split('=')[-1])
            rotate_column(x, shift)

print(count_lights())
for j in range(6):
    for i in range(50):
        if screen[i][j]:
            print('0', end='')
        else:
            print(' ', end='')
    print()
