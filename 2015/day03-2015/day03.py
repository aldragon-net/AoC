with open('day03input.txt', 'r') as inpfile:
    line = inpfile.readline()
    inpfile.close()

pos1 = 0 + 0j
pos2 = 0 + 0j
points = []
points.append(pos1)
robomove = False
for i in range(len(line)):
    if not robomove:
        if line[i] == '^':
            pos1 = pos1 + 1j
        if line[i] == 'v':
            pos1 = pos1 - 1j
        if line[i] == '>':
            pos1 = pos1 + 1
        if line[i] == '<':
            pos1 = pos1 - 1
        points.append(pos1)
        robomove = True
    else:
        if line[i] == '^':
            pos2 = pos2 + 1j
        if line[i] == 'v':
            pos2 = pos2 - 1j
        if line[i] == '>':
            pos2 = pos2 + 1
        if line[i] == '<':
            pos2 = pos2 - 1
        points.append(pos2)
        robomove = False
    
unique_points = set(points)

n = len(unique_points)

print(n, 'unique_points')
input()