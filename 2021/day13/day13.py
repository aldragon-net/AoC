with open('input_day13.txt', 'r') as f:
    dots = []
    line = f.readline().strip()
    while line != '':
        x, y = [int(n) for n in line.split(',')]
        dots.append((x,y))
        line = f.readline().strip()
    folds = []
    line = f.readline().strip()
    while line != '':
        fold_pos = int(line.split('=')[1])
        fold_dir = line.split('=')[0].split()[-1]
        folds.append((fold_dir,fold_pos))
        line = f.readline().strip()
    f.close()

dots = set(dots)


def make_a_fold(dots, fold):
    new_dots = set()
    fold_dir, fold_pos = fold
    for dot in dots:
        x, y = dot
        if fold_dir == 'x':
            new_y = y
            if x < fold_pos:
                new_x = x
            else:
                new_x = fold_pos - (x-fold_pos)
        elif fold_dir == 'y':
            new_x = x
            if y < fold_pos:
                new_y = y
            else:
                new_y = fold_pos - (y-fold_pos)
        new_dots.add((new_x, new_y))
    return new_dots


print(len(dots), 'dots before fold')
for fold in folds:
    dots = make_a_fold(dots, fold)
    print('dots after fold:', len(dots))


output = []
for i in range(6):
    outstr = [' ' for n in range(40)]
    for j in range(37):
        for dot in dots:
            x, y = dot
            if y == i:
                outstr[x] = '#'
    outstr = ''.join(outstr)
    output.append(outstr)

for line in output:
    print(line)