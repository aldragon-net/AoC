import hashlib

SEED = 'bwnlcvfs'

directions = {'U': (0, -1),
              'D': (0, 1),
              'L': (-1, 0),
              'R': (1, 0)
              }


def get_ways(cell, path):
    x, y = cell
    hash = hashlib.md5((SEED+path).encode()).hexdigest()
    ways = set()
    for i, way in enumerate(['U', 'D', 'L', 'R']):
        if hash[i] in ['b', 'c', 'd', 'e', 'f']:
            ways.add(way)
    if 'U' in ways and y == 0:
        ways.remove('U')
    if 'D' in ways and y == 3:
        ways.remove('D')
    if 'L' in ways and x == 0:
        ways.remove('L')
    if 'R' in ways and x == 3:
        ways.remove('R')
    return ways


front = [((0, 0), '')]
move = 0
path_found = False
while not path_found:
    if not front:
        print('Locked!')
        break
    move += 1
    new_front = []
    for state in front:
        cell, path = state
        x, y = cell
        ways = get_ways(cell, path)
        for way in ways:
            dx, dy = directions[way]
            if (x+dx, y+dy) == (3, 3):
                print('Path found of length', len(path+way), ':', path+way)
                continue
            new_front.append(((x+dx, y+dy), path+way))
    front = new_front
