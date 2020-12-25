import collections as coll
import numpy as np

cups = coll.deque()

# part 1 naive

with open('day23input.txt', 'r') as inpfile:
    line = inpfile.readline().strip()

for char in line:
    cups.append(int(char))

n_moves = 0

while True:
    dest = cups[0] - 1
    if dest == 0:
        dest = 9
    cups.rotate(-1)
    taken = []
    for i in range(3):
        taken.append(cups.popleft())
    while dest in taken:
        dest -= 1
        if dest == 0:
            dest = 9
    dest_i = cups.index(dest) + 1
    for i in range(3):
        cups.insert(dest_i, taken.pop())
    n_moves += 1
    if n_moves == 100:
        break

while cups[0] != 1:
    cups.rotate(-1)
print('part 1: cups after cup 1 after 100th move: ', end = '')
for i in range(1, len(cups)):
    print(cups[i], end='')
print()


# part 2
inpcups = []
with open('day23input.txt', 'r') as inpfile:
    line = inpfile.readline().strip()
for char in line:
    inpcups.append(int(char))

cups = np.empty((1000001, 5), dtype=np.int32)

for i in range(1,1000001):
    for j in range(3):
        if 10 <= i <= 999997:
            cups[i,j] = i+j+1
        elif i>999997:
            if i+j+1 <= 1000000:
                cups[i,j] = i+j+1
            else:
                cups[i,j] = inpcups[(i+j) % 1000000]
        elif i<10:
            if inpcups.index(i)+j+1 <= 8:
                cups[i,j] = inpcups[inpcups.index(i)+j+1]
            else:
                cups[i,j] = inpcups.index(i)+j+2

for i in range(1,1000001):
    if i>10:
        cups[i,4] = i-1
    elif i == 10:
        cups[i,4] = inpcups[-1]
    elif inpcups.index(i) == 0:
        cups[i,4] = 1000000
    else:
        cups[i,4] = inpcups[inpcups.index(i)-1]

for i in range(1,1000001):
    cups[i,3] = cups[cups[i,4], 4]

n_moves = 0
pointer = inpcups[0]
while True:
    dest = pointer - 1
    next3 = cups[pointer,:3]
    if dest == 0:
        dest = 1000000
    while any(next3 == dest):
        dest -= 1
        if dest == 0:
            dest = 1000000
    n1, n2, n3, pr2, pr1 = cups[pointer, 0], cups[pointer, 1], cups[pointer, 2],\
                           cups[pointer, 3], cups[pointer, 4]
    n4 = cups[n3,0]
    n5 = cups[n4,0]
    # extract
    cups[pr1, 1] = n4
    cups[pr1, 2] = cups[n4,0]
    cups[pr2, 2] = n4
    cups[pointer, 0] = n4
    cups[pointer, 1] = cups[n4,0]
    cups[pointer, 2] = cups[cups[n4,0],0]
    cups[n5, 3] = pointer
    cups[n4, 3] = pr1
    cups[n4, 4] = pointer
    # insertion
    t1, t2, t3, pr2, pr1 = cups[dest,0], cups[dest,1], cups[dest,2], \
                           cups[dest, 3], cups[dest, 4]

    cups[dest, 0] = n1
    cups[dest, 1] = n2
    cups[dest, 2] = n3
    cups[n1, 2] = t1
    cups[n1, 3] = pr1
    cups[n1, 4] = dest
    cups[n2, 1] = t1
    cups[n2, 3] = dest
    cups[n2, 2] = t2
    cups[n3, 0] = t1
    cups[n3, 1] = t2
    cups[n3, 2] = t3
    cups[t2, 3] = n3
    cups[t1, 3] = n2
    cups[t1, 4] = n3
    cups[pr1, 1] = n1
    cups[pr1, 2] = n2
    cups[pr2, 2] = n1
    n_moves += 1
    pointer = cups[pointer,0]
    if n_moves == 10000000:
        break

n1, n2 = int(cups[1,0]), int(cups[1,1])

print('part 2: answer is:', n1 * n2)
