TEST = False
filename = 'test-2025-09.txt' if TEST else 'input-2025-09.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

points = []
for line in lines:
    line = line.strip()
    points.append((int(line.split(',')[0]), int(line.split(',')[1])))

# PART 1
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


def is_on_border(point):
    x, y = point
    for v_border in v_borders:
        x_border, y1_border, y2_border = v_border
        if x == x_border and y1_border <= y <= y2_border:
            return True
    for h_border in h_borders:
        y_border, x1_border, x2_border = h_border
        if y == y_border and x1_border <= x <= x2_border:
            return True
    return False


def is_inside(point):
    if is_on_border(point):
        return True
    x, y = point
    low_x_count = high_x_count = low_y_count = high_y_count = 0
    for v_border in v_borders:
        x_border, y1_border, y2_border = v_border
        if y1_border < y <= y2_border:
            if x > x_border:
                low_x_count += 1
            if x < x_border:
                high_x_count += 1
    for h_border in h_borders:
        y_border, x1_border, x2_border = h_border
        if x1_border < x <= x2_border:
            if y > y_border:
                low_y_count += 1
            if y < y_border:
                high_y_count += 1
    if low_x_count % 2 == 1 and high_x_count % 2 == 1 and low_y_count % 2 == 1 and high_y_count % 2 == 1:
        return True
    return False


def is_line_inside(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    crossed = False
    if y1 == y2:
        for v_border in v_borders:
            x_border, y1_border, y2_border = v_border
            if x1 < x_border < x2:
                if y1_border < y1 < y2_border:   # должно быть <=, но дает ложные срабатывания
                    crossed = True               # <= требует дополнительных проверок покрытия
                    break
    if x1 == x2:
        for h_border in h_borders:
            y_border, x1_border, x2_border = h_border
            if y1 < y_border < y2:
                if x1_border < x1 < x2_border:   # аналогично
                    crossed = True
                    break
    if crossed:
        return False
    return is_inside(((x1+x2) // 2, (y1+y2) // 2))


max_surface = 0
for i in range(len(points)):
    for j in range(i+1, len(points)):
        dx = abs(points[i][0] - points[j][0]) + 1
        dy = abs(points[i][1] - points[j][1]) + 1
        if dx*dy <= max_surface:
            continue
        rectangle_inside = True
        x1, x2 = points[i][0], points[j][0]
        y1, y2 = points[i][1], points[j][1]
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        for corner in corners:
            if not is_inside(corner):
                rectangle_inside = False
                break
        if not rectangle_inside:
            continue
        # БРУТФОРС с перебором всех элементов на границе прямоугольника
        # border_points = []
        # for x in range(x1+1, x2):
        #     border_points.append((x, y1))
        #     border_points.append((x, y2))
        # for y in range(y1+1, y2):
        #     border_points.append((x1, y))
        #     border_points.append((x2, y))
        # for border_point in border_points:
        #     if not is_inside(border_point):
        #         rectangle_inside = False
        #         break
        ribs = [((x1, y1), (x2, y1)), ((x1, y1), (x1, y2)), ((x1, y2), (x2, y2)), ((x2, y1), (x2, y2))]
        for rib in ribs:
            if not is_line_inside(rib[0], rib[1]):
                rectangle_inside = False
                break
        if rectangle_inside:
            max_surface = dx*dy

print(max_surface)
