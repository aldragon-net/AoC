TEST = False
filename = 'test-2025-01.txt' if TEST else 'input-2025-01.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

pos = 50
password_p1 = 0
password_p2 = 0

for line in lines:
    direction, num = line[0], int(line[1:])
    if direction == 'L':
        num = -num
    clicks = (pos + num) // 100
    if pos == 0 and num < 0:
        clicks += 1
    pos = (pos + num) % 100
    if pos == 0 and num < 0:
        clicks -= 1
    password_p1 += int(pos == 0)
    password_p2 += abs(clicks)

print(password_p1)
print(password_p2)
