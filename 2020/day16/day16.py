import numpy as np

with open('day16input.txt', 'r') as inpfile:
    inforanges = []
    while True:
        line = inpfile.readline()
        if line.strip() == '':
            break
        infoname, infovalues = line.split(':')[0], line.split(':')[1].strip()
        range1, range2 = infovalues.split(' or ')[0],  infovalues.split(' or ')[1]
        l1, h1 = int(range1.split('-')[0]), int(range1.split('-')[1])
        l2, h2 = int(range2.split('-')[0]), int(range2.split('-')[1])
        inforanges.append((infoname, (l1, h1), (l2, h2)))
    while True:
        if inpfile.readline().strip() == 'your ticket:':
            myticket = [int(x) for x in inpfile.readline().strip().split(',')]
            break
    while True:
        if inpfile.readline().strip() == 'nearby tickets:':
            break
    tickets = []
    while True:
        line = inpfile.readline()
        if line == '':
            break
        tickets.append([int(x) for x in line.strip().split(',')])

shape = (len(inforanges), 1000)
ar = np.full(shape, False, dtype=bool)

for i in range(len(inforanges)):
    l1, h1, l2, h2 = inforanges[i][1][0], inforanges[i][1][1], \
                     inforanges[i][2][0], inforanges[i][2][1]
    for j in range(l1, h1+1):
        ar[i, j] = True
    for j in range(l2, h2+1):
        ar[i, j] = True

# part 1
errrate = 0
validtickets = []
for ticket in tickets:
    isvalid = True
    for value in ticket:
        if not any(ar[:, value]):
            errrate += value
            isvalid = False
    if isvalid:
        validtickets.append(ticket)

print('part 1: ticket scanning error rate is', errrate)

# print('There are {} valid tickets of {}'.format(len(validtickets), len(tickets)))
tickets = validtickets

# part 2
fitting = []
for i in range(len(myticket)):
    fit = []
    for j in range(len(inforanges)):
        isfit = True
        for k in range(len(tickets)):
            if not ar[j, tickets[k][i]]:
                isfit = False
                break
        if isfit:
            fit.append(j)
    fitting.append(fit)

finalfit = [-1 for i in range(20)]
while True:
    foundunique = False
    for i in range(len(fitting)):
        if len(fitting[i]) == 1:
            foundunique = True
            # print('Field {} fit only for "{}"'.format(i, inforanges[fitting[i][0]][0]))
            finalfit[i] = fitting[i][0]
            for j in range(len(fitting)):
                try:
                    fitting[j].remove(finalfit[i])
                except ValueError:
                    pass
            break
    if len(fitting) == 0 or not foundunique:
        break

answ2 = 1
for i in range(len(myticket)):
    if inforanges[finalfit[i]][0].split()[0] == 'departure':
        answ2 = answ2 * myticket[i]
print('part 2: answer is', answ2)
