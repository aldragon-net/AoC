import re

TEST = False
filename = 'test-2025-03.txt' if TEST else 'input-2025-03.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

LENGTH = len(lines[0].strip())
print(LENGTH)

all_positions = []
for rawline in lines:
    line = rawline.strip()
    positions = []
    for i in range(9, 0, -1):
        j = str(i)
        matches = re.finditer(j, line)
        indices = [match.start() for match in matches]
        positions.append((j, indices))
    all_positions.append(positions)

sum2 = 0
DIG_NUM = 12
for positions in all_positions:
    min = -1
    digits = []
    for dig_pos in range(DIG_NUM):
        for number in positions:
            chosen = False
            indices = number[1]
            for ind in indices:
                if ind > min and ind <= LENGTH - DIG_NUM + dig_pos:
                    digits.append(number[0])
                    min = ind
                    chosen = True
                    break
            if chosen:
                break
    digits = ''.join(digits)
    sum2 += int(digits)

print(sum2)
