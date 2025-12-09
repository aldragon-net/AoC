import math

TEST = False
filename = 'test-2025-06.txt' if TEST else 'input-2025-06.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

clean_lines = []
for line in lines:
    line = line.strip()
    line = [x.replace(' ', '').strip() for x in line.split(' ')]
    clean = []
    for item in line:
        if item:
            clean.append(item)
    clean_lines.append(clean)

grand_total = 0
for i in range(len(clean_lines[-1])):
    if clean_lines[-1][i] == "+":
        total = 0
        for j in range(len(clean_lines)-1):
            total += int(clean_lines[j][i])
    if clean_lines[-1][i] == "*":
        total = 1
        for j in range(len(clean_lines)-1):
            total = total*int(clean_lines[j][i])
    grand_total += total

print(grand_total)

operands = []
total = 0
for i in range(len(lines[0])-2, -1, -1):
    number = ''.join([lines[j][i].replace(' ', '') for j in range(len(lines))])
    if not number:
        continue
    if number[-1] == '+' or number[-1] == '*':
        operator = number[-1]
        operands.append(int(number[:-1]))
        print(operands)
        if operator == '+':
            total += sum(operands)
        if operator == '*':
            total += math.prod(operands)
        operands = []
        operator = ''
        continue
    operands.append(int(number))

print(total)
