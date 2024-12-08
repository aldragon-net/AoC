TEST = False
filename = 'test-2024-08.txt' if TEST else 'input-2024-08.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines = lines[::-1]

max_x = len(lines[0]) - 1
max_y = len(lines) - 1


def out_of_field(coords):
    x, y = coords
    return (x < 0 or x > max_x or y < 0 or y > max_y)


antennas = {}
for y, line in enumerate(lines):
    for x, symbol in enumerate(line):
        if symbol == '.':
            continue
        if symbol not in antennas:
            antennas[symbol] = [(x, y)]
        else:
            antennas[symbol].append((x, y))

pairs = []
for type, antennas_of_type in antennas.items():
    for i in range(len(antennas_of_type)):
        for j in range(i+1, len(antennas_of_type)):
            pairs.append((antennas_of_type[i], antennas_of_type[j]))

antinodes = set()

for pair in pairs:
    coords_1, coords_2 = pair
    x1, y1 = coords_1
    x2, y2 = coords_2
    dx = x2 - x1
    dy = y2 - y1
    antinode_1, antinode_2 = (x1-dx, y1-dy), (x2+dx, y2+dy)
    if not out_of_field(antinode_1):
        antinodes.add(antinode_1)
    if not out_of_field(antinode_2):
        antinodes.add(antinode_2)

print(len(antinodes))

antinodes = set()

for pair in pairs:
    antinode_1, antinode_2 = pair
    antinodes.add(antinode_1)
    antinodes.add(antinode_2)
    x1, y1 = antinode_1
    x2, y2 = antinode_2
    dx = x2 - x1
    dy = y2 - y1
    i = 1
    while not all((out_of_field(antinode_1), out_of_field(antinode_2))):
        antinode_1, antinode_2 = (x1-i*dx, y1-i*dy), (x2+i*dx, y2+i*dy)
        if not out_of_field(antinode_1):
            antinodes.add(antinode_1)
        if not out_of_field(antinode_2):
            antinodes.add(antinode_2)
        i += 1
print(len(antinodes))
