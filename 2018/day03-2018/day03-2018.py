with open('input_day03-2018.txt', 'r') as f:
    lines = f.readlines()

fabric = [[[] for _ in range(1001)] for _ in range(1001)]
claims = [True] * (len(lines)+1)

for line in lines:
    line = line.strip()
    claim = line.split()
    n = int(claim[0].strip('#'))
    x, y = [int(z) for z in claim[2].strip(':').split(',')]
    dx, dy = [int(z) for z in claim[3].split('x')]
    for i in range(x, x+dx):
        for j in range(y, y+dy):
            if fabric[i][j]:
                for c in fabric[i][j]:
                    claims[c] = False
                claims[n] = False
            fabric[i][j].append(n)

# part 1
count = 0
for i in range(1000):
    for j in range(1000):
        if len(fabric[i][j]) > 1:
            count += 1
print(count)

# part 2
for i in range(1, len(claims)):
    if claims[i]:
        print(i)
