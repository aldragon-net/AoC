import numpy as np


lines = []            
with open('day18input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)
        
field = np.zeros((102, 102))
new = np.zeros((102, 102))

for i in range(100):
    for j in range(100):
        if lines[i][j] == '#':
            field[i+1, j+1] = 1
            
print(field)            

def nextiter(field):
    def neibo(i,j):
        N = field[i-1,j+1] + field[i,j+1] + field[i+1,j+1] \
            + field[i-1,j] + field[i+1,j] \
            + field[i-1,j-1] + field[i,j-1] + field[i+1,j-1]
        return N
    for i in range(100):
        for j in range(100):
            N = neibo(i+1,j+1)
            new[i+1,j+1] = field[i+1,j+1]
            if field[i+1,j+1] == 0 and (N == 3):
                new[i+1,j+1] = 1
            if field[i+1,j+1] == 1 and (N < 2 or N > 3):  
                new[i+1,j+1] = 0
    return new
    
niter = 0
while True:
    field[1,1] = 1
    field [1, 100] = 1
    field[100,1] = 1
    field [100, 100] = 1
    N = np.sum(field)
    print(N, 'lights at iteration', niter)
    if niter == 100:
        input()
        break
    new = nextiter(field)
    for i in range(1, 101):
        for j in range(1, 101):
            field[i,j] = new [i,j]
    #print(field[:10,:10])
    #input()
    niter = niter + 1
    
   
    
