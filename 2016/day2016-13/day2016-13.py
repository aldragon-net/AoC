SEED = 1352
start = (1, 1)
goal = (31, 39)


def is_wall(point):
    x, y = point
    if x < 0 or y < 0:
        return True
    value = x*x + 3*x + 2*x*y + y + y*y + SEED
    binstr = bin(value)
    count = binstr.count('1')
    if count % 2 == 0:
        return False
    return True


field = {start: 0}
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
front = set([start])
move = 0
locations_counter = 1

while goal not in field:
    move += 1
    new_front = set()
    for point in front:
        x, y = point
        for direction in directions:
            dx, dy = direction
            step = (x+dx, y+dy)
            if step in field:
                if field[step] <= move:
                    continue
            if is_wall(step):
                field[step] = -1
                continue
            field[step] = move
            new_front.add(step)
    if move <= 50:
        locations_counter += len(new_front)
    front = new_front

print(field[goal])
print(locations_counter)
