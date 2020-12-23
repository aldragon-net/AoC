import collections as coll

cups = coll.deque()

# part 1

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

print('After 100th move:', end = '')
for char in cups:
    print(char, end='')

# part 2
cups = coll.deque()
with open('day23input.txt', 'r') as inpfile:
    line = inpfile.readline().strip()
for char in line:
    cups.append(int(char))

for i in range(10,1000001):
    cups.append(i)

n_moves = 0
while True:
    for i in range(20):
        print(cups[i],',', end='')
    print('...', end='')
    for i in range(20):
        print(cups[999980+i],',', end='')
    input()
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
            dest = 1000000
    dest_i = cups.index(dest) + 1
    for i in range(3):
        cups.insert(dest_i, taken.pop())
    n_moves += 1
    if n_moves == 1000:
        break

print('Done')
