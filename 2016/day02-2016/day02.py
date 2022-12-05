lines = []
with open('day02input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)

x,y = 0, 0

decode = {(-1,1):'1', (-1,0):'4', (-1,-1):'7', (0,1):'2', (0,0):'5', (0,-1):'8', (1,1):'3', (1,0):'6', (1,-1):'9'}

code = ''



for line in lines:
    for char in line:
        if char=='U':
            if y<1:
                y = y + 1
        elif char=='D':
            if y>-1:
                y = y - 1            
        elif char=='L':
            if x>-1:
                x = x - 1      
        elif char=='R':
            if x<1:
                x = x + 1       
    code = code + decode[(x,y)]
    
print('Code is', code)
input()
                
