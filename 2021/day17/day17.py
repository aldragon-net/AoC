# target area:
LOW_X = 179
HIGH_X = 201
LOW_Y = -109
HIGH_Y = -63

LONGSHOT = -2*LOW_Y + 1


def check_target(x, y):
    return (LOW_X <= x <= HIGH_X) and (LOW_Y <= y <= HIGH_Y)


def next_step(x, y, vx, vy):
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    vy -= 1
    return x, y, vx, vy


x_success = [[] for i in range(LONGSHOT)]
y_success = [[] for i in range(LONGSHOT)]

for v0x in range(HIGH_X+1):
    x = 0
    y = 0
    vx = v0x
    vy = 0
    step = 0
    while True:
        step += 1
        x, y, vx, vy = next_step(x, y, vx, vy)
        if check_target(x, LOW_Y):
            x_success[step].append(v0x)
        if x > HIGH_X or step == LONGSHOT-1:
            break
for v0y in range(LOW_Y, -LOW_Y):
    x = 0
    y = 0
    vx = 0
    vy = v0y
    step = 0
    while True:
        step += 1
        x, y, vx, vy = next_step(x, y, vx, vy)
        if check_target(LOW_X, y):
            y_success[step].append(v0y)
        if y < LOW_Y:
            break

distinct_vs = set()
for i in range(LONGSHOT):
    if len(x_success[i]) * len(y_success[i]) != 0:
        for vx in x_success[i]:
            for vy in y_success[i]:
                distinct_vs.add((vx, vy))

print(len(distinct_vs))
