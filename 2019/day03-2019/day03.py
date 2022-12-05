lines = []
with open('day03input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)

commands1 = [item for item in lines[0].split(',')]
commands2 = [item for item in lines[1].split(',')]

x = 0
y = 0

visited = {}
visited[(0,0)] = 0

stepcounter1 = 0
for i in range(len(commands1)):
    d = commands1[i][0]
    move = int(commands1[i][1:])
    if d == 'U':
        for i in range(move):
            stepcounter1 = stepcounter1 + 1
            y = y + 1
            point = (x,y)
            if not point in visited.keys():
                visited[(x,y)] = stepcounter1
            else:
                print('Selfcross of 1st wire at', x, y, 'distance is', abs(x)+abs(y))
    elif d == 'D':
        for i in range(move):
            stepcounter1 = stepcounter1 + 1
            y = y - 1
            point = (x,y)
            if not point in visited.keys():
                visited[(x,y)] = stepcounter1
            else:
                print('Selfcross of 1st wire at', x, y, 'distance is', abs(x)+abs(y))
    elif d == 'R':
        for i in range(move):
            stepcounter1 = stepcounter1 + 1
            x = x + 1
            point = (x,y)
            if not point in visited.keys():
                visited[(x,y)] = stepcounter1
            else:
                print('Selfcross of 1st wire at', x, y, 'distance is', abs(x)+abs(y))
    elif d == 'L':
        for i in range(move):
            stepcounter1 = stepcounter1 + 1
            x = x - 1
            point = (x,y)
            if not point in visited.keys():
                visited[(x,y)] = stepcounter1
            else:
                print('Selfcross of 1st wire at', x, y, 'distance is', abs(x)+abs(y))

    
min_distance = 1000000
min_stepsum = 10000000


x = 0
y = 0

stepcounter2 = 0


for i in range(len(commands2)):
    d = commands2[i][0]
    move = int(commands2[i][1:])
    if d == 'U':
        for i in range(move):
            stepcounter2 = stepcounter2 + 1
            y = y + 1
            point = (x,y)
            if not point in visited.keys():
                pass
            else:
                dist = abs(x)+abs(y)
                stepsum = stepcounter2 + visited[(x,y)]
                print('Wires crossing at', x, y, 'distance is', dist, 'and stepsum is', stepsum)
                if dist <= min_distance:
                    min_distance = dist
                if stepsum <= min_stepsum:
                    min_stepsum = stepsum
                
    elif d == 'D':
        for i in range(move):
            stepcounter2 = stepcounter2 + 1
            y = y - 1
            point = (x,y)
            if not point in visited.keys():
                pass
            else:
                dist = abs(x)+abs(y)
                stepsum = stepcounter2 + visited[(x,y)]
                print('Wires crossing at', x, y, 'distance is', dist, 'and stepsum is', stepsum)
                if dist <= min_distance:
                    min_distance = dist
                if stepsum <= min_stepsum:
                    min_stepsum = stepsum
    elif d == 'R':
        for i in range(move):
            stepcounter2 = stepcounter2 + 1
            x = x + 1
            point = (x,y)
            if not point in visited.keys():
                pass
            else:
                dist = abs(x)+abs(y)
                stepsum = stepcounter2 + visited[(x,y)]
                print('Wires crossing at', x, y, 'distance is', dist, 'and stepsum is', stepsum)
                if dist <= min_distance:
                    min_distance = dist
                if stepsum <= min_stepsum:
                    min_stepsum = stepsum
    elif d == 'L':
        for i in range(move):
            stepcounter2 = stepcounter2 + 1
            x = x - 1
            point = (x,y)
            if not point in visited.keys():
                pass
            else:
                dist = abs(x)+abs(y)
                stepsum = stepcounter2 + visited[(x,y)]
                print('Wires crossing at', x, y, 'distance is', dist, 'and stepsum is', stepsum)
                if dist <= min_distance:
                    min_distance = dist
                if stepsum <= min_stepsum:
                    min_stepsum = stepsum

print('Minimal distance of crossing is:', min_distance)
print('Minimal stepsum is:', min_stepsum)
print('Press any key')       
input()        
