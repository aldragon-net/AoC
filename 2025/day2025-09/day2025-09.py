TEST = True
filename = 'test-2025-09.txt' if TEST else 'input-2025-09.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

points = []
for line in lines:
    line = line.strip()
    points.append((int(line.split(',')[0]), int(line.split(',')[1])))


# max_surface = 0
# for i in range(len(points)):
#     for j in range(i+1, len(points)):
#         dx = abs(points[i][0] - points[j][0]) + 1
#         dy = abs(points[i][1] - points[j][1]) + 1
#         if dx*dy > max_surface:
#             max_surface = dx*dy

h_borders = []
v_borders = []
prev = points[-1]
for point in points:
    x1, y1 = prev
    x2, y2 = point
    if x1 == x2:
        y1, y2 = sorted([y1, y2])
        v_borders.append((x1, y1, y2))
    if y1 == y2:
        x1, x2 = sorted([x1, x2])
        h_borders.append((y1, x1, x2))
    prev = point

print(v_borders)
print(h_borders)

# def is_inside(x, y):
#     for v_border in v_borders:
#         x_border, y1_border, y2_border = v_border
#         if y
