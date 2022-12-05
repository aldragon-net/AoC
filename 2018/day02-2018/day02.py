
ABC = 'abcdefghijklmnopqrstuvwxyz'

ids = []
with open('day02input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        ids.append(line)

count2 = 0
count3 = 0

for id in ids:
    is2 = False
    is3 = False
    symbols = [char for char in id]
    for letter in ABC:
        n = symbols.count(letter)
        if n == 2:
            is2 = True
        if n == 3:
            is3 = True
        if is2 and is3:
            break
    if is2:
        count2 += 1
    if is3:
        count3 += 1

checksum = count2 * count3
print('Checksum is', checksum)
input()

for id1 in ids:
    for id2 in ids:
        count = 0
        for i in range(len(id1)):
            if id1[i] != id2[i]:
                count += 1
        if count == 1:
            print(id1, id2)
