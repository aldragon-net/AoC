from collections import deque


class Monkey():
    def __init__(self, number, items, operation,
                 divalue, truepass, falsepass) -> None:
        self.number = number
        self.items = deque(items)
        self.operation = operation
        self.divalue = divalue
        self.truepass = truepass
        self.falsepass = falsepass
        self.inspect_count = 0


monkeys = []

with open('input_day11-2022.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
for i in range(8):
    j = i*7
    number = int(lines[j].split()[1].strip(':'))
    items = [int(x) for x in lines[j+1].split(':')[1].strip().split(', ')]
    operation = lines[j+2].split(':')[1].strip()
    divalue = int(lines[j+3].split()[-1])
    truepass = int(lines[j+4].split()[-1])
    falsepass = int(lines[j+5].split()[-1])
    monkey = Monkey(number, items, operation, divalue, truepass, falsepass)
    monkeys.append(monkey)

divider = 1
for monkey in monkeys:
    divider *= monkey.divalue


def process(monkey):
    while monkey.items:
        item = monkey.items.popleft()
        monkey.inspect_count += 1
        d = {'old': item}
        exec(monkey.operation, d)
        new = d['new']
        new = new // 3  # part 1
        # new = new % divider  # part 2
        if new % monkey.divalue == 0:
            monkeys[monkey.truepass].items.append(new)
        else:
            monkeys[monkey.falsepass].items.append(new)


CYCLES = 20  # part 1
# CYCLES = 10000  # part 2

for i in range(CYCLES):
    for monkey in monkeys:
        process(monkey)

counts = [monkey.inspect_count for monkey in monkeys]
counts.sort(reverse=True)

print(counts[0] * counts[1])
