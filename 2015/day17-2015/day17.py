import numpy as np

total_V = 150

volumes = []            
with open('day17input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline()
        if line == '':
            break
        line = line.strip()
        volumes.append(int(line))

volumes = np.array(volumes)        
print(volumes)
input()

in_use = np.zeros((len(volumes))) 

N = 0
for i in range(2**len(volumes)):
    for j in range(len(volumes)):
        in_use[j] = (i >> j) % 2
    V = np.dot(volumes, in_use)
    if V == total_V:
        N = N + 1
    if i % 8192 == 0:
        print(i, 'combinations analyzed')
        
print(N, 'combinations fit')
input()

N = 0
min_vols = len(volumes)
for i in range(2**len(volumes)):
    for j in range(len(volumes)):
        in_use[j] = (i >> j) % 2
    V = np.dot(volumes, in_use)
    if V == total_V:
        vols = np.sum(in_use)
        if vols == min_vols:
            N = N + 1
        if vols<min_vols:
            N = 1
            min_vols = vols
    if i % 8192 == 0:
        print(i, 'combinations analyzed')
        
print(N, 'combinations fit of', min_vols, 'containers')
input()
