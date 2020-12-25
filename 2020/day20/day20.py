import numpy as np

class Tile:
    def __init__(self, n, arr):
        self.number = n
        self.arr = arr
        self.n = arr[0,:]
        self.s = arr[9,:]
        self.w = arr[:,0]
        self.e = arr[:,9]
        self.nbrs = []
        self.installed = False

    def flip(self):
        self.arr = self.arr.T
        self.n = self.arr[0,:]
        self.s = self.arr[9,:]
        self.w = self.arr[:,0]
        self.e = self.arr[:,9]

    def rotright(self):
        self.flip()
        self.arr = self.arr[:,::-1]
        self.n = self.arr[0,:]
        self.s = self.arr[9,:]
        self.w = self.arr[:,0]
        self.e = self.arr[:,9]

tiles = []

monpattern = np.full((3,20), False)

with open('day20monster.txt', 'r') as monfile:
    lines = [s.strip('\n') for s in monfile.readlines()]
    for i in range(3):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                monpattern[i,j] = True


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

corners = []
sides = []
rest = []

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
                    tile1.nbrs.append(j)
    if n_match == 2:
        corners.append(tile1)
    elif n_match == 3:
        sides.append(tile1)
    elif n_match == 4:
        rest.append(tile1)


mult = 1
for t in corners:
    mult = mult * t.number
print('Multiplication of corners is', mult)

# determine keystone
keystone = corners[0]
tile2, tile3 = [tiles[i] for i in keystone.nbrs]
i = 0
while True:
    n_match = 0
    for b1 in [keystone.e, keystone.s]:
        for b2 in [tile2.n, tile2.s, tile2.w, tile2.e,
                   tile3.n, tile3.s, tile3.w, tile3.e]:
            if all(b1 == b2) or all(b1[::-1] == b2):
                n_match += 1
    if n_match == 2:
        # print('keystone oriented')
        break
    else:
        i += 1
        keystone.rotright()
        if i == 4:
            keystone.flip()

puzzle = np.full((120, 120), False)
for i in range(12):
    for j in range(12):
        if i == 0:
            if j == 0:
                for k in range(10):
                    for r in range(10):
                        puzzle[i*10+k,j*10+r] = keystone.arr[k,r]
                        keystone.installed = True
            else:
                border = puzzle[0+i*10:10+i*10, j*10-1]
                for tile in tiles:
                    if tile.installed:
                        continue
                    n_tries = 0
                    found_tile = False
                    while True:
                        if all(border == tile.w):
                            found_tile = True
                            for k in range(10):
                                for r in range(10):
                                    puzzle[i * 10 + k, j * 10 + r] = tile.arr[k, r]
                            tile.installed = True
                            break
                        n_tries += 1
                        tile.rotright()
                        if n_tries == 4:
                            tile.flip()
                        if n_tries > 8:
                            break
                    if found_tile:
                        break
        else:
            border = puzzle[i*10-1, j*10:(j+1)*10]
            for tile in tiles:
                if tile.installed:
                    continue
                n_tries = 0
                found_tile = False
                while True:
                    if all(border == tile.n):
                        found_tile = True
                        for k in range(10):
                            for r in range(10):
                                puzzle[i * 10 + k, j * 10 + r] = tile.arr[k, r]
                        tile.installed = True
                        break
                    n_tries += 1
                    tile.rotright()
                    if n_tries == 4:
                        tile.flip()
                    if n_tries > 8:
                        break
                if found_tile == True:
                    break

cleanpuzzle = np.full((96,96), False)
for i in range(96):
    for j in range(96):
        cleanpuzzle[i,j] = puzzle[(i // 8) * 10 + i%8 + 1, (j // 8) * 10 +  j%8 + 1]

trarr = np.full((3,20), True)
in_monsters = 0
#searching for monster:
for count in range(8):
    for i in range(93):
        for j in range(76):
            sector = cleanpuzzle[i:i+3,j:j+20]
            match_count = 0
            for k in range(3):
                for r in range(20):
                    if monpattern[k,r] and sector[k,r]:
                        match_count += 1
            if match_count == 15:
                in_monsters += 15
    if in_monsters > 0:
        break
    cleanpuzzle = cleanpuzzle.T
    if not count == 4:
        cleanpuzzle = cleanpuzzle[:,::-1]

print('Among {} \'#\' {} are in monsters and {} not'.format(cleanpuzzle.sum(),
                                                        in_monsters,
                                                        cleanpuzzle.sum() - in_monsters
                                                        )
      )
