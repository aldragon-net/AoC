# with open('test.txt', 'r') as f:
with open('input_day15-2022.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

sensors = []
beacons = []
min_x = 99999999
max_x = 0
max_range = 0
for line in lines:
    x = int(line.split()[2].split('=')[1].strip(','))
    y = int(line.split()[3].split('=')[1].strip(':'))
    xb = int(line.split()[-2].split('=')[1].strip(','))
    yb = int(line.split()[-1].split('=')[1])
    srange = abs(x - xb) + abs(y- yb)
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if srange > max_range:
        max_range = srange
    sensors.append((x, y, srange))
    beacons.append((xb, yb))

# y=10
y=2000000
forbidden = set()

# for sensor in sensors:
#     xs, ys, srange = sensor
#     for x in range(0, srange-abs(ys-y)+1):
#         forbidden.add(xs+x)
#         forbidden.add(xs-x)

# for beacon in beacons:
#     xb, yb = beacon
#     if yb == y and xb in forbidden:
#         forbidden.remove(xb)

# print(len(forbidden))

squares_to_search = [(54, 1792), (54, 1793), (510, 999), (510, 1000), (1276, 1467), (1277, 1467), (1473, 855), (1473, 856), (1474, 854), (1474, 855), (1475, 853), (1475, 854), (1476, 852), (1476, 853), (1477, 851), (1477, 852), (1478, 850), (1478, 851), (1479, 849), (1479, 850), (1480, 848), (1480, 849), (1481, 847), (1481, 848), (1482, 846), (1482, 847), (1483, 845), (1483, 846), (1484, 844), (1484, 845), (1485, 843), (1485, 844), (1486, 842), (1486, 843), (1487, 841), (1487, 842), (1562, 944), (1562, 945), (1563, 943), (1563, 944), (1564, 942), (1564, 943), (1565, 941), (1565, 942), (1566, 940), (1566, 941), (1567, 939), (1567, 940), (1568, 938), (1568, 939), (1569, 937), (1569, 938), (1570, 936), (1570, 937), (1571, 935), (1571, 936), (1572, 934), (1572, 935), (1573, 933), (1573, 934), (1574, 932), (1574, 933), (1575, 931), (1575, 932), (1576, 930), (1576, 931), (1635, 1318), (1635, 1319), (1810, 1807), (1811, 1807)]
# for x in range(0, 2000):
#     xsq = x * 2000
#     print(x)
#     for y in range(0, 2000):
#         ysq = y * 2000
#         covered = False
#         for sensor in sensors:
#             xs, ys, srange = sensor
#             if max((abs(xsq - xs) + abs(ysq - ys),
#                     abs(xsq +2000 - xs) + abs(ysq - ys),
#                     abs(xsq - xs) + abs(ysq +2000 - ys),
#                     abs(xsq +2000 - xs) + abs(ysq + 2000 - ys))) <= srange:
#                 covered = True
#                 break
#         else:
#             squares_to_search.append((x, y))

for square in squares_to_search:
    print(square)
    xsq, ysq = square
    for x in range(xsq*2000, xsq*2000 + 2000):
        for y in range(ysq*2000, ysq*2000 + 2000):
            for sensor in sensors:
                xs, ys, srange = sensor
                if abs(xs-x) + abs(ys-y) <= srange:
                    break
            else:
                print(x, y)
                print(x*4000000+y)
                input()

print(squares_to_search)
