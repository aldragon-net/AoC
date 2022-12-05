import numpy as np

key = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]

indices  = {
            "children": 0,
            "cats": 1,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 4,
            "vizslas": 5,
            "goldfish": 6,
            "trees": 7,
            "cars": 8,
            "perfumes": 9  
            }

print(indices)

lines = []            
with open('day16input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline()
        if line == '':
            break
        line = line[line.find(':')+1:].strip()
        lines.append(line)

data = np.zeros((500,11))

data[:,:10] = data[:,:10] - 1

print(data)

for i in range(500):
    line = lines[i]
    print(line)
    slines = line.split(',')
    print(slines)
    for j in range(3):
        index = indices[slines[j].split(':')[0].strip()]
        data[i,index] = int(slines[j].split(':')[1])

for i in range(500):
    match = True
    for j in range(10):
        if not ((data[i, j] == -1) or data[i,j] == key[j]):
            match = False
    if match:
        print('This aunt Sue fits:', i+1)
        
        
for i in range(500):
    match = True
    for j in range(10):
        if j == 1 or j == 7:
            if not ((data[i, j] == -1) or data[i,j] > key[j]):
                match = False
        elif j == 3 or j == 6:
            if not ((data[i, j] == -1) or data[i,j] < key[j]):
                match = False
        else:
            if not ((data[i, j] == -1) or data[i,j] == key[j]):
                match = False
    if match:
        print('[Corrected]: This aunt Sue fits:', i+1)
