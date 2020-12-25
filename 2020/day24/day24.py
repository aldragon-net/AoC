with open('day24input.txt', 'r') as inpfile:
    lines = [line.strip() for line in inpfile.readlines()]

def traceline(line):
    x = 0
    y = 0
    i = 0
    while i<len(line):
        char = line[i]
        if char == 'e':
            x += 2
        elif char == 'w':
            x -= 2
        elif char == 'n':
            y += 1
            i += 1
            char = line[i]
            if char == 'e':
                x += 1
            elif char == 'w':
                x -= 1
        elif char == 's':
            y -= 1
            i += 1
            char = line[i]
            if char == 'e':
                x += 1
            elif char == 'w':
                x -= 1
        i += 1
    return (x, y)


def neighbours_count(blacked):
    def addto(nbrstat, point, value):
        if point in nbrstat.keys():
            nbrstat[point] = nbrstat[point] + value
        else:
            nbrstat[point] = value
        return nbrstat
    nbrstat = {}
    for tile in blacked:
        x, y = tile
        nbrs = [(x+2, y), (x-2,y), (x+1,y+1), (x+1,y-1), (x-1,y+1), (x-1,y-1)]
        nbrstat = addto(nbrstat, (x, y), 0)
        for nbr in nbrs:
            x, y = nbr
            nbrstat = addto(nbrstat, (x, y), 1)
    return nbrstat

blacked = set()
for line in lines:
    point = traceline(line)
    if point in blacked:
        blacked.remove(point)
    else:
        blacked.add(point)

print('part 1: number of black tiles is:', len(blacked))

n_moves = 0
while n_moves < 100:
    nbrstat = neighbours_count(blacked)
    for point in nbrstat.keys():
        if (point in blacked) and not 0 < nbrstat[point] <= 2:
            blacked.remove(point)
        elif (point not in blacked) and nbrstat[point] == 2:
            blacked.add(point)
    n_moves += 1
    # print(n_moves, len(blacked))

print('part 2: number of black tiles after 100th move is:', len(blacked))
