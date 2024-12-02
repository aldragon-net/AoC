with open('input-2023-05.txt', 'r') as f:
    lines = f.readlines()

class Map:
    def __init__(self, lines) -> None:
        self.ranges = []
        for line in lines:
            dest, source, length = [int(x) for x in line.strip().split()]
            self.ranges.append((dest, source, length))

    def convert(self, x):
        for range in self.ranges:
            dest, source, length = range
            if x >= source and x <= source + length - 1:
                return dest + x - source
        return x

seeds = [int (x) for x in lines[0].split(':')[1].split()]

maps = []

for i in range(2, len(lines)):
    if ':' in lines[i]:
        maplines = []
        continue
    if lines[i].strip() == '':
        maps.append(Map(maplines))
        maplines = []
        continue
    maplines.append(lines[i].strip())
maps.append(Map(maplines))

locations = []
for seed in seeds:
    value = seed
    for map in maps:
        value = map.convert(value)
    locations.append(value)

locations.sort()
print(locations[0])

            