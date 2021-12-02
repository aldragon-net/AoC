with open('input_day02.txt', 'r') as f:
    lines = f.readlines()
    f.close()

# part 1
pos = 0
depth = 0

for line in lines:
    comm, val = line.strip().split()[0], int(line.strip().split()[1])
    if comm == 'forward':
        pos += val
    elif comm == 'up':
        depth -= val
    elif comm == 'down':
        depth += val
print(pos*depth)
# end of part 1

# part 2
pos = 0
depth = 0
aim = 0

for line in lines:
    comm, val = line.strip().split()[0], int(line.strip().split()[1])
    if comm == 'forward':
        pos += val
        depth += val * aim
    elif comm == 'up':
        aim -= val
    elif comm == 'down':
        aim += val

print(pos*depth)
# end of part 2
