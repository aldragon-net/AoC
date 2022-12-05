code = []
with open('day05input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        code.append(int(line))
L = len(code)

step = 0
pos = 0

while True:
    step += 1
    jump = code[pos]
    if code[pos] >=3:
        code[pos] -= 1
    else:
        code[pos] +=1
    pos += jump
    if pos<0 or pos>L-1:
        print('Out of code at step:', step)
        input()
        break
    
