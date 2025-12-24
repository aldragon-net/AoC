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

    def convert_diapasone_set(self, diapasone_set):
        new_diapasone_set = set()
        while diapasone_set:
            diapasone = diapasone_set.pop()
            fragments = set()
            fragments.add(diapasone)
            while fragments:
                fragment = fragments.pop()
                d_start, d_end = fragment
                changed = False
                for range in self.ranges:
                    dest, source, length = range
                    if d_start >= source and d_end <= source + length - 1:
                        new_diapasone_set.add((dest + d_start - source, dest + d_end - source))
                        changed = True
                    elif d_start < source and source <= d_end <= source + length - 1:
                        fragments.add((d_start, source - 1))
                        new_diapasone_set.add((dest, dest + d_end - source))
                        changed = True
                    elif source <= d_start <= source + length - 1 and d_end > source + length - 1:
                        new_diapasone_set.add((dest + d_start - source, dest + length - 1))
                        fragments.add((source + length, d_end))
                        changed = True
                    elif d_start < source and d_end > source + length - 1:
                        fragments.add((d_start, source - 1))
                        fragments.add((source + length, d_end))
                        new_diapasone_set.add((dest, dest + length - 1))
                        changed = True
                if not changed:
                    new_diapasone_set.add(fragment)
        return new_diapasone_set


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


# part 1

seeds = [int(x) for x in lines[0].split(':')[1].split()]
locations = []
for seed in seeds:
    value = seed
    for map in maps:
        value = map.convert(value)
    locations.append(value)

locations.sort()
print(locations[0])

# part 2

boundaries = lines[0].split(':')[1].split()
seeds = set([(int(boundaries[i*2]), int(boundaries[i*2])+int(boundaries[i*2+1])-1) for i in range(len(boundaries)//2)])

for map in maps:
    seeds = map.convert_diapasone_set(seeds)

low_values = [seed[0] for seed in seeds]
print(min(low_values))
