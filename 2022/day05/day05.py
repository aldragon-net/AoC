with open('input_day05.txt', 'r') as f:
    lines = f.readlines()

stacks = [[] for _ in range(9)]

for i in range(9):
    stacks[i].extend(list(lines[i].strip()))


def make_move(n, fr, t):
    fr -= 1
    t -= 1
    for i in range(n):
        item = stacks[fr].pop()
        stacks[t].append(item)


def make_move_2(n, fr, t):
    fr -= 1
    t -= 1
    intermediate = []
    for i in range(n):
        item = stacks[fr].pop()
        intermediate.append(item)
    intermediate = intermediate[::-1]
    stacks[t].extend(intermediate)


for i in range(10, len(lines)):
    instruction = lines[i].strip().split()
    n = int(instruction[1])
    fr = int(instruction[3])
    t = int(instruction[5])
    make_move_2(n, fr, t)

tops = [stack[-1] for stack in stacks]

print(''.join(tops))
