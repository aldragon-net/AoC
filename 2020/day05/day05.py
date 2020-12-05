with open('day05input.txt') as inpfile:
    ticketbase = inpfile.readlines()
    inpfile.close()

numlist = []
for line in ticketbase:
    number = 0
    for i in range(10):
        number = number * 2
        if line[i] in ['B', 'R']:
            number += 1
    numlist.append(number)

numlist.sort()

# part 1
print('Max number is {}'.format(numlist[-1]))

# part 2
delta = numlist[0]
for i in range(1, len(numlist)):
    if numlist[i]>i+delta:
        print('Missing place is {}'.format(i+delta))
        break