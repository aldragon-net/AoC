with open('input_day04.txt', 'r') as f:
    lines = f.readlines()


count_1 = 0
count_2 = 0

for line in lines:
    first, second = line.strip().split(',')
    first = [int(x) for x in first.split('-')]
    second = [int(x) for x in second.split('-')]
    if ((first[0] <= second[0] and first[1] >= second[1]) or
            (second[0] <= first[0] and second[1] >= first[1])):
        count_1 += 1
    if ((first[0] <= second[1] and first[1] >= second[0]) or
            (second[0] <= first[1] and second[1] >= first[0])):
        count_2 += 1


print(count_1)
print(count_2)
