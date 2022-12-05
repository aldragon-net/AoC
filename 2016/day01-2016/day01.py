with open('day01input.txt', 'r') as inpfile:
    line = inpfile.readline().strip()

commands = [item.strip(',') for item in line.split()]

x = 0
y = 0
d = 'N'

visited = set()
visited.add((x,y))

for i in range(len(commands)):
    turn = commands[i][0]
    move = int(commands[i][1:])
    if turn == 'R':
        if d == 'N':
            d = 'E'
        elif d == 'E':
            d = 'S'
        elif d == 'S':
            d = 'W'
        elif d == 'W':
            d = 'N'
    elif turn == 'L':
        if d == 'N':
            d = 'W'
        elif d == 'W':
            d = 'S'
        elif d == 'S':
            d = 'E'
        elif d == 'E':
            d = 'N'
    if d == 'N':
        for i in range(move):
            y = y + 1
            point = (x,y)
            if not point in visited:
                visited.add(point)
            else:
                print('you visited', x, y, 'before, distance is', abs(x)+abs(y))
    elif d == 'S':
        for i in range(move):
            y = y - 1
            point = (x,y)
            if not point in visited:
                visited.add(point)
            else:
                print('you visited', x, y, 'before, distance is', abs(x)+abs(y))
    elif d == 'E':
        for i in range(move):
            x = x + 1
            point = (x,y)
            if not point in visited:
                visited.add(point)
            else:
                print('you visited', x, y, 'before, distance is', abs(x)+abs(y))
    elif d == 'W':
        for i in range(move):
            x = x - 1
            point = (x,y)
            if not point in visited:
                visited.add(point)
            else:
                print('you visited', x, y, 'before, distance is', abs(x)+abs(y))
    
       
print('Final distance is', abs(x)+abs(y), 'x,y:', x, y)
input()        
