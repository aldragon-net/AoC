from functools import cmp_to_key

# with open('test.txt', 'r') as f:
with open('input_day13-2022.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


pairs = []
for i in range(0, len(lines), 3):
    d = {}
    exec('item_1 = ' + lines[i], d)
    exec('item_2 = ' + lines[i+1], d)
    item_1 = d['item_1']
    item_2 = d['item_2']
    pairs.append((item_1, item_2))


def compare(x, y):
    if isinstance(x, int) and isinstance(y, int):
        if x == y:
            return 0
        if x < y:
            return 1
        if x > y:
            return -1
    if isinstance(x, int) and isinstance(y, list):
        x = [x]
        return compare(x, y)
    if isinstance(x, list) and isinstance(y, int):
        y = [y]
        return compare(x, y)
    if isinstance(x, list) and isinstance(y, list):
        i = 0
        while True:
            if i >= len(x) and i >= len(y):
                return 0
            if i >= len(x):
                return 1
            if i >= len(y):
                return -1
            if compare(x[i], y[i]) == 1:
                return 1
            if compare(x[i], y[i]) == -1:
                return -1
            i += 1


count = 0
sum_of_indices = 0
for index, pair in enumerate(pairs):
    left, right = pair
    if compare(left, right) == 1:
        sum_of_indices += index + 1
        count += 1

print(sum_of_indices)

all_items = []
for pair in pairs:
    all_items.append(pair[0])
    all_items.append(pair[1])
all_items.append([[2]])
all_items.append([[6]])

sorted_items = sorted(all_items, key=cmp_to_key(compare), reverse=True)

print((sorted_items.index([[2]]) + 1) * (sorted_items.index([[6]]) + 1))
