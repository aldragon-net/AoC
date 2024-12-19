TEST = False
filename = 'test-2024-19.txt' if TEST else 'input-2024-19.txt'

designs = []
with open(filename, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    towels = lines[0].split(', ')
    designs = lines[2:]

analyzed = {}


def check_design(design, towels):
    if len(design) == 0:
        return 1
    if design in analyzed:
        return analyzed[design]
    count = 0
    for towel in towels:
        if design[-len(towel):] != towel:
            continue
        count += check_design(design[:-len(towel)], towels)
    analyzed[design] = count
    return count


sum = 0
sum_var = 0
for design in designs:
    count = check_design(design, towels)
    sum = sum + 1 if count else sum
    sum_var += count

print(sum)
print(sum_var)
