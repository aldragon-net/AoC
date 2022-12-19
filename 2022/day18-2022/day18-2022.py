# with open('test.txt', 'r') as f:
with open('input_day18-2022.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

lava = set()
air = set()
for line in lines:
    x, y, z = [int(i) for i in line.split(',')]
    lava.add((x, y, z))
for x in range(-1, 24):
    for y in range(-1, 24):
        for z in range(-1, 24):
            if (x, y, z) not in lava:
                air.add((x ,y, z))

def surface(cubeset):
    open_sides = set()
    for cube in cubeset:
        x, y, z = cube
        sides = ((x, y, z, 'x'),
                (x, y, z, 'y'),
                (x, y, z, 'z'),
                (x+1, y, z, 'x'),
                (x, y+1, z, 'y'),
                (x, y, z+1, 'z')
                )
        for side in sides:
            if side in open_sides:
                open_sides.remove(side)
            else:
                open_sides.add(side)
    return len(open_sides)

# part 1
print(surface(lava))

# part 2
outside_air = set()
outside_air.add((0,0,0))
layer = outside_air.copy()
while True:
    new_outside = set()
    for cube in layer:
        x, y, z = cube
        for new_cube in ((x-1, y, z),
                         (x+1, y, z),
                         (x, y-1, z),
                         (x, y+1, z),
                         (x, y, z-1),
                         (x, y, z+1)):
            if new_cube in air and new_cube not in outside_air:
                new_outside.add(new_cube)
    if len(new_outside) == 0:
        break
    outside_air = outside_air.union(new_outside)
    layer = new_outside.copy()

print(surface(outside_air) - 25*25*6)



