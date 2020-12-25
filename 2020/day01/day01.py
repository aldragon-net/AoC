numbers = []
with open('day01input.txt') as inpfile:
    while True:
        st = inpfile.readline()
        if st == '':
            break
        number = int(st.strip())
        numbers.append(number)
n = len(numbers)
found = False
for i in range(n):
    for j in range(i, n):
        if numbers[i]+numbers[j] == 2020:
            print('Pair founded! {} at pos. {} and {} at pos {}'.format(
                numbers[i], i, numbers[j], j
            ))
            print('Multiplication result: {}'.format(numbers[i]*numbers[j]))
            found = True
            break
    if found:
        break
# part two
found = False
for i in range(n):
    for j in range(n):
        if j == i:
            continue
        third = 2020 - numbers[i] - numbers[j]
        for k in range(n):
            if k == i or k == j:
                continue
            if numbers[k] == third:
                print('Trinity founded! {} at pos. {}, {} at pos {} and {} at pos {}'.format(
                    numbers[i], i, numbers[j], j, numbers[k], k
                ))
                print('Multiplication result: {}'.format(numbers[i] * numbers[j] * numbers[k]))
                found = True
                break
        if found:
            break
    if found:
        break
