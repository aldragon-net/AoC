from collections import Counter

with open('input_day06.txt', 'r') as f:
    lines = f.readlines()

length = len(lines[0].strip())

positions = [[] for _ in range(length)]

for line in lines:
    for i in range(length):
        positions[i].append(line[i])

for i in range(length):
    counter = Counter(positions[i])
    # print(counter.most_common(1)[0][0], end='')   # part 1
    print(counter.most_common()[-1][0], end='')     # part 2
