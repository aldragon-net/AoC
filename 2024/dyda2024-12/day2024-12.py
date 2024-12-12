import numpy as np

TEST = False
filename = 'test-2024-12.txt' if TEST else 'input-2024-12.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines = lines[::-1]

max_x = len(lines[0]) - 1
max_y = len(lines) - 1

field = [[symbol for x, symbol in enumerate(line)] for y, line in enumerate(lines)]

def out_of_field(coords):
    x, y = coords
    return (x < 0 or x > max_x or y < 0 or y > max_y)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


regions = {}
traced = set()


def calculate_sides(borders):
    sides = []
    analyzed = set()
    for border in borders:
        if border in analyzed:
            continue
        side = set()
        side.add(border)
        x, y, direction = border
        direction_i = directions.index(direction)
        side_dir_1, side_dir_2 = directions[(direction_i + 1)%4], directions[(direction_i - 1)%4]
        dx1, dy1 = side_dir_1
        dx2, dy2 = side_dir_2
        i = 1
        tracing_1, tracing_2 = True, True
        while tracing_1 or tracing_2:
            if tracing_1 and (x + dx1*i, y+dy1*i, direction) in borders:
                side.add((x + dx1*i, y+dy1*i, direction))
                analyzed.add((x + dx1*i, y+dy1*i, direction))
            else:
                tracing_1 = False
            if tracing_2 and (x + dx2*i, y+dy2*i, direction) in borders:
                side.add((x + dx2*i, y+dy2*i, direction))
                analyzed.add((x + dx2*i, y+dy2*i, direction))
            else:
                tracing_2 = False
            i += 1                             
        sides.append(side)
    return len(sides)

def trace_region(coords):
    x, y = coords
    type = field[x][y]
    traced.add(coords)
    cells = set()
    cells.add(coords)
    borders = set()
    for direction in directions:
        borders.add((x, y, direction))

    def step(pos):
        x, y = pos
        for direction in directions:
            dx, dy = direction
            new_x, new_y = x + dx, y + dy
            if out_of_field((new_x,new_y)):
                continue
            if field[new_x][new_y] == type:
                if (new_x, new_y) in traced or (new_x, new_y) in cells:
                    continue
                traced.add((new_x, new_y))
                cells.add((new_x, new_y))
                for i, border_direction in enumerate(directions):
                    antidirection = directions[(i+2) % 4]
                    nei_dx, nei_dy = border_direction
                    nei_x, nei_y = new_x + nei_dx, new_y + nei_dy
                    if (nei_x, nei_y, antidirection) in borders:
                        borders.remove(((nei_x, nei_y, antidirection)))
                    else:
                        borders.add((x+dx, y+dy, border_direction))
                step((x+dx, y+dy))
        return
    step(coords)
    return type, len(cells), len(borders), calculate_sides(borders)


cost_1 = 0
cost_2 = 0
for x in range(max_x+1):
    for y in range(max_y+1):
        if (x, y) not in traced:
            type, area, perimeter, sides = trace_region((x, y))
            cost_1 += area * perimeter
            cost_2 += area * sides

print(cost_1)
print(cost_2)
