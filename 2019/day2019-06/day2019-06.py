TEST = False
filename = 'test-2019-06.txt' if TEST else 'input-2019-06.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

structure = {}
for line in lines:
    center, orbiter = line.strip().split(')')
    structure[orbiter] = center


def count_p1(orbiter):
    return 1 if structure[orbiter] == 'COM' else count_p1(structure[orbiter]) + 1


def get_centers(point):
    centers = []
    while point != 'COM':
        point = structure[point]
        centers.append(point)
    return centers


result = sum([count_p1(orbiter) for orbiter in structure])
print(result)

san_orbits = get_centers('SAN')
you_orbits = get_centers('YOU')

for planet in san_orbits:
    if planet in you_orbits:
        print(san_orbits.index(planet) + you_orbits.index(planet))
        break
