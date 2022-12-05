import numpy as np
import itertools 

lines = []            
with open('day09input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)

distances = np.zeros((8,8))


routes = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7]))

print('Various routes:', len(routes))

k = 0
for i in range(8):
    for j in range(i+1,8):
        L = int(lines[k].split('=')[-1].strip())
        distances[i,j] = L
        distances[j,i] = L
        k = k + 1

L_min = 1000000
L_max = 0
for route in routes:
    L = 0
    for point in range(7):
        i = route[point]
        j = route[point+1]
        L = L + distances[i,j]
    #print('L =', L, 'for route', route)
    if L < L_min:
        L_min = L
        min_route = route
    if L > L_max:
        L_max = L
        max_route = route

print('Min distance', L_min, 'for route', min_route)
print('Max distance', L_max, 'for route', max_route)
input()



