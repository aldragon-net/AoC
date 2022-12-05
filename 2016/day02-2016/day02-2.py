lines = []
with open('day02input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)

x,y = -2, 0

decode = {(-1,1):'2', (-1,0):'6', (-1,-1):'A', (0,1):'3', (0,0):'4', (0,-1):'B', (1,1):'4', (1,0):'8', (1,-1):'C', (0,2):'1', (-2,0):'5', (2,0):'9', (0,-2):'D'}

code = ''

for line in lines:
    for char in line:
        if char=='U':
            y = y + 1
            if abs(x)+abs(y)>2:
                y = y - 1
        elif char=='D':
            y = y - 1
            if abs(x)+abs(y)>2:
                y = y + 1            
        elif char=='L':
            x = x - 1 
            if abs(x)+abs(y)>2:
                x = x + 1      
        elif char=='R':
            x = x + 1
            if abs(x)+abs(y)>2:
                x = x - 1    
    code = code + decode[(x,y)]
    
print('Code is', code)
input()
                
