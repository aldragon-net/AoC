with open('input_day01.txt', 'r') as f:
    lines = f.readlines()

elves = []
elf = 0
for line in lines:
    if line.strip() == '':
        elves.append(elf)
        elf = 0
        continue
    elf += int(line.strip())

elves.sort()

print('Part 1 (top elf):', elves[-1])
print('Part 2 (top 3 elves):', sum(elves[-3:]))
