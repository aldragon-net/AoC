with open('day13input.txt', 'r') as inpfile:
    curt = int(inpfile.readline().strip())
    buses = inpfile.readline().strip().split(',')

avbuses = []
for i in range(len(buses)):
    try:
        n = int(buses[i])
        avbuses.append([n, i, 0])
    except:
        pass

# part 1
firstbus = maxwaitt = min([bus[0] for bus in avbuses])
for bus in avbuses:
    waitt = bus[0] - curt % bus[0]
    if waitt <= maxwaitt:
        maxwaitt = waitt
        firstbus = bus[0]
print('part 1: Bus {} arrives in {} minutes, answer is is {}'.format(firstbus,
                                                                     maxwaitt,
                                                                     firstbus*maxwaitt))

# part 2
def vbus(avbuses):
    step1, dt1, shift1 = avbuses[0][0], avbuses[0][1], avbuses[0][2]
    step2, dt2, _ = avbuses[1][0], avbuses[1][1], avbuses[1][2]
    i = 0
    off2 = step2 - shift1 % step2
    doff2 = - step1 % step2
    dt2 = dt2 % step2
    while True:
        i += 1
        off2 = (off2 + doff2) % step2
        curt = i*step1 + shift1
        if off2 == dt2:
            vir_n = step1*step2
            vir_shift = curt
            virtual_bus = [vir_n, 0, curt]
            # editing list
            new_avbuses = []
            new_avbuses.append(virtual_bus)
            if len(avbuses)>2:
                new_avbuses.extend(avbuses[2:])
            break
    return new_avbuses

while True:
    avbuses = vbus(avbuses)
    if len(avbuses) == 1:
        break

print('part 2: timestamp is {}'.format(avbuses[0][2]))
