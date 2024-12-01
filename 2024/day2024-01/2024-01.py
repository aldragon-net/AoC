with open('input-2024-01.txt', 'r') as f:
    lines = f.readlines()

list_1 = []
list_2 = []

for line in lines:
    n1, n2 = line.strip().split()
    list_1.append(int(n1))
    list_2.append(int(n2))

list_1.sort()
list_2.sort()

difsum = 0
for i in range(len(list_1)):
    difsum += abs(list_1[i] - list_2[i])

print(difsum)


simsum = 0
for i in range(len(list_1)):
    for j in range(len(list_2)):
        if list_2[j] == list_1[i]:
            simsum += list_1[i]
        if list_2[j] > list_1[i]:
            break
print(simsum)