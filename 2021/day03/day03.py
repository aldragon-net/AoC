with open('input_day03.txt', 'r') as f:
    lines = f.readlines()
    f.close()

summ = [0 for x in range(12)]

for line in lines:
    line = line.strip()
    for i in range(len(line)):
        summ[i] += int(line[i])

for i in range(len(summ)):
    summ[i] = summ[i] // 500

summ.reverse()


p = 1
x = 0
for i in range(len(summ)):
    x += summ[i]*p
    p = p*2

p = 1
y = 0
for i in range(len(summ)):
    y += ((1+summ[i]) % 2) * p
    p = p*2

print(x*y)

# part 2

oldset = lines
for j in range(12):
    summ = [0 for x in range(12)]
    for line in oldset:
        line = line.strip()
        for i in range(len(line)):
            summ[i] += int(line[i])
    for i in range(len(summ)):
        if summ[i] >= len(oldset)/2:
            summ[i] = 1
        else:
            summ[i] = 0
    newset = []
    for line in oldset:
        if int(line[j]) == summ[j]:
            newset.append(line)
    if len(newset) == 1:
        break
    oldset = newset

x = newset[0].strip()

oldset = lines
for j in range(12):
    summ = [0 for x in range(12)]
    for line in oldset:
        line = line.strip()
        for i in range(len(line)):
            summ[i] += int(line[i])
    for i in range(len(summ)):
        if summ[i] >= len(oldset)/2:
            summ[i] = 1
        else:
            summ[i] = 0
    newset = []
    for line in oldset:
        if int(line[j]) != summ[j]:
            newset.append(line)
    if len(newset) == 1:
        break
    oldset = newset

y = newset[0].strip()
print(int(x, 2) * int(y, 2))
