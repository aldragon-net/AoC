lines = []            
with open('day07input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)

values = {}
        

def getvalue(id, depth):
    global values
    margin = depth*' '
    depth = depth + 1
    try:
        result = values[id]
        return result
    except:
        pass
    try:
        result = int(id)
    except:
        result = -1
    if not result == -1:
        print(margin,'Found', id, 'value:', result)
        values[id] = result
        print(values)
        return result
    keyline = ''
    for line in lines:
        if line.split('->')[-1].strip() == id:
            keyline = line.split('->')[0].strip()
            print(margin, 'For', id, 'found instruction line', line)
            break
    if keyline == '':
        print('Error! No line found for', id)
        input()
    
    if len(keyline.split()) == 1:
        sid = keyline.split()[0]
        result = getvalue(sid, depth)
        print(margin, 'Found', id, 'value:', result)
        values[id] = result
        return getvalue(sid, depth)
    
    if keyline.split()[0] == 'NOT':
        sid = keyline.split()[1]
        result = 65535 - getvalue(sid, depth)
        print(margin,'Found', id, 'value:', result)
        values[id] = result
        return result

    if keyline.split()[1] == 'OR':
        sid1 = keyline.split()[0]
        sid2 = keyline.split()[2]
        result = getvalue(sid1, depth) | getvalue(sid2, depth)
        print(margin, 'Found', id, 'value:', result)
        values[id] = result
        return result
    
    if keyline.split()[1] == 'AND':
        sid1 = keyline.split()[0]
        sid2 = keyline.split()[2]
        result = getvalue(sid1, depth) & getvalue(sid2, depth)
        print(margin, 'Found', id, 'value:', result)
        values[id] = result
        return result
        
    if keyline.split()[1] == 'LSHIFT':
        sid = keyline.split()[0]
        i = int(keyline.split()[2])
        result = getvalue(sid, depth) << i
        print(margin,'Found', id, 'value:', result)
        values[id] = result
        return result

    if keyline.split()[1] == 'RSHIFT':
        sid = keyline.split()[0]
        i = int(keyline.split()[2])
        result = getvalue(sid, depth) >> i
        print(margin, 'Found', id, 'value:', result)
        values[id] = result
        return result     

a = getvalue('a', 0)

print('a value is:', a)
input()

values = {'b': a}

a = getvalue('a', 0)

print('New a value is:', a)
input()
