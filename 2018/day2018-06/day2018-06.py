TEST = False
filename = 'test-2018-06.txt' if TEST else 'input-2018-06.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

centers = [tuple([int(x) for x in line.strip().split(', ')]) for line in lines]


def mdistance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def ownship(point):
    distances = [mdistance(point, center) for center in centers]
    ordered_distances = sorted(distances)
    if ordered_distances[0] == ordered_distances[1]:
        return None
    return distances.index(ordered_distances[0])


def count_area(center):
    area = 1
    i = 1
    x0, y0 = center
    center_index = ownship(center)
    while True:
        new_area = 0
        points = [(x0+i, y0+j) for j in range(-i, i+1)]
        points.extend([(x0-i, y0+j) for j in range(-i, i+1)])
        points.extend([(x0+j, y0+i) for j in range(-i+1, i)])
        points.extend([(x0+j, y0-i) for j in range(-i+1, i)])
        for point in points:
            if ownship(point) == center_index:
                new_area += 1
        if new_area == 0:
            return area
        area += new_area
        i += 1
        if i == 100:
            return None

# part 1
# areas = []
# for center in centers:
#     area = count_area(center)
#     if area:
#         areas.append(area)

# areas.sort(reverse=True)
# print(areas)

# part 2


middle_x = sum([p[0] for p in centers])/len(centers)
middle_y = sum([p[1] for p in centers])/len(centers)
start = (round(middle_x), round(middle_y))
print(start)


def count_area_2(start):
    area = 1
    i = 0
    x0, y0 = start
    while True:
        i += 1
        new_area = 0
        points = [(x0+i, y0+j) for j in range(-i, i+1)]
        points.extend([(x0-i, y0+j) for j in range(-i, i+1)])
        points.extend([(x0+j, y0+i) for j in range(-i+1, i)])
        points.extend([(x0+j, y0-i) for j in range(-i+1, i)])
        for point in points:
            if sum([mdistance(point, center) for center in centers]) < 10000:
                new_area += 1
        if new_area == 0:
            return area
        area += new_area
        print(i, new_area)


print('result p2:', count_area_2(start))
