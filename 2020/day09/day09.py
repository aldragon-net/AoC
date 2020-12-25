import collections

PRE = 25

with open('day09input.txt') as inpfile:
    numbers = [int(x.strip()) for x in inpfile.readlines()]

print('There are {} numbers'.format(len(numbers)))

# part 1
pool = collections.deque()
pool.extend(numbers[:PRE])

for i in range(PRE, len(numbers)):
    number = numbers[i]
    valid = False
    for j in range(PRE):
        diff = number - pool[j]
        for k in range(PRE):
            if diff == pool[k] and not k == j:
                valid = True
                break
        if valid:
            break
    if valid:
        pool.popleft()
        pool.append(numbers[i])
    else:
        print('Number {} at position {} is not valid'.format(number, i))
        keynum = number
        break

# part 2
for i in range(len(numbers)):
    summ = 0
    j = 0
    while summ < keynum:
        summ += numbers[i+j]
        if summ == keynum and j > 0:
            keyset = list(numbers[i:i+j+1])
            break
        j += 1

keyset.sort()
print('Answer is {}'.format(keyset[0]+keyset[-1]))
