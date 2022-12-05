#puzzle input is 347991
endnumber = 347991
counter = 1
rotcounter = 0
vector = [1,0]
spiral_step = 1
x = 0
y = 0
values = {}
values[(0,0)] = 1
not_yet = True
while True:
    for i in range(spiral_step):
        x = x + vector[0]
        y = y + vector[1]
        counter += 1
        value = 0
        for j in [-1,0,1]:
            for k in [-1,0,1]:
                if (x+j,y+k) in values.keys():
                    value += values[(x+j,y+k)]
        values[(x,y)] = value
        if not_yet and value > endnumber:
            print('First value bigger than puzzle input is', value)
            not_yet = False
        if counter == endnumber:
            print('Number', endnumber, 'reached at', x,y, '| distance is', abs(x)+abs(y))
            input()
            break
    if counter == endnumber:
        break
    vector[0], vector[1] = -vector[1], vector[0] #rotation counterclockwise
    rotcounter +=1
    if rotcounter % 2 == 0:
       spiral_step += 1
