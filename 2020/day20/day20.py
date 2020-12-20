import numpy as np

class Tile:
    def __init__(self, n, arr):
        self.number = n
        self.arr = arr
        self.n = arr[0,:]
        self.s = arr[9,:]
        self.w = arr[:,0]
        self.e = arr[:,9]

tiles = []

with open('day20input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline()
        if line == '':
            break
        elif line == '\n':
            continue
        elif line[:4] == 'Tile':
            n = int(line.strip().split()[1].strip(':'))
            arr = np.full((10,10), False)
            for i in range(10):
                line = inpfile.readline()
                for j in range(10):
                    if line[j] == '#':
                        arr[i,j] = True
            t = Tile(n, arr)
            tiles.append(t)

print(len(tiles))

print(tiles[0].number, tiles[0].e)

print(tiles[-1].number, tiles[-1].w)

mult = 1
for i in range(len(tiles)):
    tile1 = tiles[i]
    n_match = 0
    for j in range(len(tiles)):
        if i == j:
            continue
        tile2 = tiles[j]
        for b1 in [tile1.n, tile1.s, tile1.w, tile1.e]:
            for b2 in [tile2.n, tile2.s, tile2.w, tile2.e]:
                if all(b1 == b2) or all(b1[::-1] == b2):
                    n_match += 1
    if n_match == 2:
        mult = mult * tile1.number
    print(i, n_match)

print(mult)