import collections

p1 = collections.deque()
p2 = collections.deque()

def cards_from_file():
    with open('day22input.txt', 'r') as inpfile:
        inpfile.readline()
        while True:
            line = inpfile.readline().strip()
            if line == '':
                break
            p1.append(int(line))
        inpfile.readline()
        while True:
            line = inpfile.readline().strip()
            if line == '':
                break
            p2.append(int(line))
    return p1, p2


p1, p2 = cards_from_file()
# part 1
n = 0
while True:
    n += 1
    card1 = p1.popleft()
    card2 = p2.popleft()
    if card1 > card2:
        p1.append(card1)
        p1.append(card2)
    else:
        p2.append(card2)
        p2.append(card1)
    if len(p1) == 0 or len(p2) == 0:
        break

print('after move', n)

if len(p1) == 0:
    winner = p2
else:
    winner = p1

n = 0
sum = 0
while True:
    n += 1
    sum += n * winner.pop()
    if len(winner) == 0:
        break
print(sum)

# part 2
p1, p2 = cards_from_file()
print(p1)
print(p2)
def game(p1,p2):
    archive = set()
    while True:
        # print('Current desks:')
        # print(p1)
        # print(p2)
        l1 = tuple(p1)
        l2 = tuple(p2)
        if (l1,l2) in archive:
            winp1 = True
            return winp1
        archive.add((l1,l2))
        card1 = p1.popleft()
        card2 = p2.popleft()
        if card1 <= len(p1) and card2 <= len(p2):
            rec1 = collections.deque()
            for i in range(card1):
                rec1.append(p1[i])
            rec2 = collections.deque()
            for i in range(card2):
                rec2.append(p2[i])
            # print('Recursive with:')
            # print(rec1)
            # print(rec2)
            winp1 = game(rec1,rec2)
        else:
            if card1>card2:
                winp1 = True
            else:
                winp1 = False
        if winp1:
            p1.append(card1)
            p1.append(card2)
        else:
            p2.append(card2)
            p2.append(card1)
        if len(p1) == 0 or len(p2) == 0:
            break
    if len(p1) == 0:
        winp1 = False
    else:
        winp1 = True
    return winp1

print(game(p1, p2))


print(p1)

winner = p1
n = 0
sum = 0
print(winner)
while True:
    n += 1
    sum += n * winner.pop()
    if len(winner) == 0:
        break
print(sum)