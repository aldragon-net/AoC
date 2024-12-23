TEST = False
filename = 'test-2024-23.txt' if TEST else 'input-2024-23.txt'
with open(filename, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

connections = []
for line in lines:
    c1, c2 = line.split('-')
    connections.append((c1, c2))

computers = {}
for connection in connections:
    c1, c2 = connection
    if c1 not in computers:
        computers[c1] = [c2]
    else:
        computers[c1].append(c2)
    if c2 not in computers:
        computers[c2] = [c1]
    else:
        computers[c2].append(c1)

# part 1
threes = set()
for first_computer, first_linked_with in computers.items():
    for second_computer in first_linked_with:
        for third_computer in computers[second_computer]:
            if third_computer in first_linked_with:
                three = [first_computer, second_computer, third_computer]
                three.sort()
                threes.add(tuple(three))
sum = 0
for three in threes:
    if three[0][0] == 't' or three[1][0] == 't' or three[2][0] == 't':
        sum += 1
print(sum)

# part 2
# brutforce (improved)
groups = threes
while True:
    larger_groups = set()
    for group in groups:
        neighbours = set()
        for computer in group:
            for neighbour in computers[computer]:
                neighbours.add(neighbour)
        for computer in neighbours:
            linked_with = computers[computer]
            if computer in group:
                continue
            if set(group).issubset(linked_with):
                larger_group = [*group, computer]
                larger_group.sort()
                larger_groups.add(tuple(larger_group))
    if len(larger_groups) == 0:
        break
    groups = larger_groups

print(','.join(groups.pop()))
