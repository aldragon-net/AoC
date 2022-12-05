import numpy as np
import itertools 

lines = []            
with open('day14input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)


deers = []

for i in range(len(lines)):
    v, tf, tr = int(lines[i].split()[3]),\
                int(lines[i].split()[6]),\
                int(lines[i].split()[-2])
    deers.append([v, tf, tr])

print('Deers parameters:')
print(deers)

def dist(deers, t):
    dist = []
    for i in range(len(deers)):
        v, tf, tr = deers[i][0], deers[i][1], deers[i][2]
        period = tf + tr
        full = t // period
        rest = t % period
        if rest >= tf:
            rest = tf
        L = (full*tf + rest)*v
        dist.append(L)
    return dist

distances = dist(deers, 2503)

distances.sort()

print('Best deer distance is:', distances[-1])


scores = [0 for deer in deers]

for t in range(1, 2504):
    distances = dist(deers, t)
    best_dist = max(distances)
    for i in range(len(distances)):
        if distances[i] == best_dist:
            scores[i] =  scores[i] + 1

scores.sort()
print('Best deer score is:', scores[-1])
input()



