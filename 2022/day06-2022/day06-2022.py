with open('input_day06-2022.txt', 'r') as f:
    line = f.readline().strip()


def first_marker(line, n):
    for i in range(n, len(line)):
        subline = line[i-n:i]
        if len(set(subline)) == n:
            return i


print('Part 1:', first_marker(line, 4))
print('Part 2:', first_marker(line, 14))
