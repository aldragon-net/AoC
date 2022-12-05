import numpy as np
import itertools 

lines = []            
with open('day13input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)

happys = np.zeros((9,9))

sittings = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8]))

for i in range(len(sittings)):
    s = list(sittings[i])
    s.append(s[0])
    s.insert(0, s[8])
    sittings[i] = s
    

print('Various sittings:', len(sittings))
print('First sitting:', sittings[0])
print('Last sitting:', sittings[-1])

k = 0
for i in range(8):
    for j in range(8):
        if j == i:
            continue
        h = int(lines[k].split()[3].strip())
        if lines[k].split()[2] == 'lose':
            h = -h
        happys[i+1,j+1] = h
        k = k + 1

print(happys)
input('Start?')


max_hap = -32768

for i in range(len(sittings)):
    hap = 0
    for j in range(1,10):
        p = sittings[i][j]
        pl = sittings[i][j-1] 
        pr = sittings[i][j+1] 
        hap = hap + happys[p, pl] + happys[p, pr]
    if hap > max_hap:
        max_hap = hap
        opt_i = i
    if i % 100 == 0:
        print('Analyzed sitting', i)

print('Mas happiness is:', max_hap, 'for sitting', sittings[opt_i])
input()



