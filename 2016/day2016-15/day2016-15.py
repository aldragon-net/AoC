TEST = False
filename = 'test-2016-15.txt' if TEST else 'input-2016-15.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

disks = []
for line in lines:
    words = line.strip().split()
    positions, start = int(words[3]), int(words[-1].strip('.'))
    disks.append((positions, start))

# part 2:
disks.append((11, 0))

time = 0
step = 1
disks_passed = []
while len(disks_passed) < len(disks):
    time += step
    for i in range(len(disks)):
        if i in disks_passed:
            continue
        positions, start = disks[i]
        if (start + time + i + 1) % positions == 0:
            disks_passed.append(i)
            step = step*positions

print(time)
