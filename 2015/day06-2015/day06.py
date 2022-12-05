import numpy as np

lights = np.ones((1000,1000))

lights = lights -1 #- 2

# with open('day06input.txt', 'r') as inpfile:
    # while True:
        # line = inpfile.readline().strip()
        # if line == '':
            # break
        # if line.split()[0] == 'toggle':
            # i1 = int(line.split()[1].split(',')[0])
            # j1 = int(line.split()[1].split(',')[1])
            # i2 = int(line.split()[3].split(',')[0])
            # j2 = int(line.split()[3].split(',')[1])
            # lights[i1:i2+1,j1:j2+1] = lights[i1:i2+1,j1:j2+1] * -1
        # if line.split()[0] == 'turn' and line.split()[1] == 'on':
            # i1 = int(line.split()[2].split(',')[0])
            # j1 = int(line.split()[2].split(',')[1])
            # i2 = int(line.split()[4].split(',')[0])
            # j2 = int(line.split()[4].split(',')[1])
            # lights[i1:i2+1,j1:j2+1] = 1
        # if line.split()[0] == 'turn' and line.split()[1] == 'off':
            # i1 = int(line.split()[2].split(',')[0])
            # j1 = int(line.split()[2].split(',')[1])
            # i2 = int(line.split()[4].split(',')[0])
            # j2 = int(line.split()[4].split(',')[1])
            # lights[i1:i2+1,j1:j2+1] = -1

#lights = lights + 1
#lights = lights / 2
            
with open('day06input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        if line.split()[0] == 'toggle':
            i1 = int(line.split()[1].split(',')[0])
            j1 = int(line.split()[1].split(',')[1])
            i2 = int(line.split()[3].split(',')[0])
            j2 = int(line.split()[3].split(',')[1])
            lights[i1:i2+1,j1:j2+1] = lights[i1:i2+1,j1:j2+1] + 2 
        if line.split()[0] == 'turn' and line.split()[1] == 'on':
            i1 = int(line.split()[2].split(',')[0])
            j1 = int(line.split()[2].split(',')[1])
            i2 = int(line.split()[4].split(',')[0])
            j2 = int(line.split()[4].split(',')[1])
            lights[i1:i2+1,j1:j2+1] = lights[i1:i2+1,j1:j2+1] + 1
        if line.split()[0] == 'turn' and line.split()[1] == 'off':
            i1 = int(line.split()[2].split(',')[0])
            j1 = int(line.split()[2].split(',')[1])
            i2 = int(line.split()[4].split(',')[0])
            j2 = int(line.split()[4].split(',')[1])
            lights[i1:i2+1,j1:j2+1] = lights[i1:i2+1,j1:j2+1] - 1
            for i in range(i1, i2+1):
                for j in range (j1, j2+1):
                    if lights[i,j] < 0:
                        lights[i,j] = 0
       

N = lights.sum() #/ 2


print('Total brgitness:', N)
