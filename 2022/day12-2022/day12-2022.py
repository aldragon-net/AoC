# with open('test.txt', 'r') as f:
with open('input_day12-2022.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

hmap = [[0] * len(lines[0]) for _ in range(len(lines))]
steps = [[1000000] * len(lines[0]) for _ in range(len(lines))]

starts = []

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'S':
            hmap[i][j] = 0
            start_pos = (i, j)
            starts.append((i, j))
        elif lines[i][j] == 'E':
            hmap[i][j] = 25
            end_pos = (i, j)
            steps[i][j] = 0
        else:
            hmap[i][j] = ord(lines[i][j]) - ord('a')
            if lines[i][j] == 'a':
                starts.append((i, j))

while True:
    steps_modified = False
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            for shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                di, dj = shift
                if (0 <= i+di < len(lines)) and (0 <= j+dj < len(lines[0])):
                    if (steps[i][j] > steps[i+di][j+dj] + 1 and
                            hmap[i][j] - hmap[i+di][j+dj] >= -1):
                        steps[i][j] = steps[i+di][j+dj] + 1
                        steps_modified = True
    if not steps_modified:
        break

x, y = start_pos
print(steps[x][y])

a_lengths = []
for start in starts:
    x, y = start
    a_lengths.append(steps[x][y])

a_lengths.sort()
print(a_lengths[0])
