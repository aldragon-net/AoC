wlhs = []
with open('day02input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline()
        line.strip()
        dimstrings = line.split('x')
        if line == '':
            inpfile.close()
            break
        wlhs.append([int(dimstring) for dimstring in dimstrings])
print(len(wlhs), 'sizes in input')
total_S = 0
total_L = 0
for i in range(len(wlhs)):
    wlh = wlhs[i]
    w, l, h = wlh[0], wlh[1], wlh[2]
    S1 = l*w
    S2 = w*h  
    S3 = h*l
    P1 = 2*l+2*w
    P2 = 2*l+2*h
    P3 = 2*w+2*h
    volume = w*l*h
    surfaces = [S1, S2, S3]
    perimeters = [P1, P2, P3]
    surfaces.sort()
    perimeters.sort()
    smallest = surfaces[0]
    ribbon = perimeters[0]
    S = 2*S1 + 2*S2 + 2*S3 + smallest
    riblength = ribbon + volume
    total_S = total_S + S
    total_L = total_L + riblength
print('Total surface is :', total_S)
print('Total length is :', total_L)
input()
    
    