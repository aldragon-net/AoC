lines = []            
with open('day23input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)

N = len(lines)      
print(N, 'lines of code in file')
  
a = 1
b = 0
  
pos = 0

while True:
    if pos<0 or pos>N-1:
        break
    line = lines[pos]
    print('Executing line', pos, ':', line)
    if line.split()[0] == 'inc':
        if line.split()[1] == 'a':
            a = a + 1
        elif line.split()[1] == 'b':
            b = b + 1
        pos = pos + 1
    elif line.split()[0] == 'tpl':
        if line.split()[1] == 'a':
            a = a*3
        elif line.split()[1] == 'b':
            b = b*3
        pos = pos + 1
    elif line.split()[0] == 'hlf':
        if line.split()[1] == 'a':
            a = a // 2
        elif line.split()[1] == 'b':
            b = b // 2
        pos = pos + 1
    elif line.split()[0] == 'jmp':
        pos = pos + int(line.split()[1])
    elif line.split()[0] == 'jie':
        if line.split()[1].strip(',') == 'a':
            if a % 2 == 0:
                pos = pos + int(line.split()[2])
            else:
                pos = pos + 1
        elif line.split()[1].strip(',') == 'b':
            if b % 2 == 0:
                pos = pos + int(line.split()[2])
            else:
                pos = pos + 1
    elif line.split()[0] == 'jio':
        if line.split()[1].strip(',') == 'a':
            if a == 1:
                pos = pos + int(line.split()[2])
            else:
                pos = pos + 1
        elif line.split()[1].strip(',') == 'b':
            if b == 1:
                pos = pos + int(line.split()[2])
            else:
                pos = pos + 1               
    print('a = ', a, 'b =', b)

print('program stopped, b =', b)    
input()