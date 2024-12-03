import re

TEST = False

filename = 'test-2024-03.txt' if TEST else 'input-2024-03.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

# part 1
muls = []
for line in lines:
    muls.extend(re.findall(r'mul\([0-9]+,[0-9]+\)', line))
sumexp = 0
for mul in muls:
    x1, x2 = [int(x) for x in re.findall(r'[0-9]+', mul)]
    sumexp += x1*x2
print(sumexp)

# part 2
muls = []
for line in lines:
    muls.extend(re.findall(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', line))
sumexp = 0
active = True
for mul in muls:
    if mul == 'do()':
        active = True
        continue
    if mul == 'don\'t()':
        active = False
        continue       
    x1, x2 = [int(x) for x in re.findall(r'[0-9]+', mul)]
    if active:
        sumexp += x1*x2

print(sumexp)
