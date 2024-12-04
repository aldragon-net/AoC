TEST = False
filename = 'test-2024-04.txt' if TEST else 'input-2024-04.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

rawlines = ['...' + line.strip() + '...' for line in lines]
blankline = '.' * len(rawlines[0])
lines = [blankline] * 3
lines.extend(rawlines)
lines.extend([blankline] * 3)


directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)]
XMAS = 'XMAS'

xmas_count = 0
for i in range(3, len(lines) - 3):
    for j in range(len(lines[0]) - 3):
        for direction in directions:
            isxmas = True
            dx, dy = direction
            for shift in range(4):
                if lines[i + dx*shift][j + dy*shift] != XMAS[shift]:
                    isxmas = False
                    break
            if isxmas:
                xmas_count += 1
print(xmas_count)

xmas_count = 0
for i in range(3, len(lines) - 3):
    for j in range(len(lines[0]) - 3):
        if lines[i][j] == 'A':
            word1 = ''.join([lines[i-1][j-1], 'A', lines[i+1][j+1]])
            word2 = ''.join([lines[i-1][j+1], 'A', lines[i+1][j-1]])
        else:
            continue
        if (word1 == 'MAS' or word1 == 'SAM') and (word2 == 'MAS' or word2 == 'SAM'):
            xmas_count += 1
print(xmas_count)
