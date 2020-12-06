with open('day06input.txt') as inpfile:
    base = inpfile.readlines()
    inpfile.close()

sum1 = 0
sum2 = 0
answer1 = set()
answer2 = set()
first = True
for line in base:
    strline = line.strip()
    if strline == '':
        sum1 += len(answer1)
        sum2 += len(answer2)
        answer1 = set()
        answer2 = set()
        first = True
        continue
    memanswer = set()
    for ch in strline:
        memanswer.add(ch)
    answer1 = answer1.union(memanswer)
    if first:
        answer2 = memanswer
        first = False
    else:
        answer2 = answer2.intersection(memanswer)
sum1 += len(answer1)
sum2 += len(answer2)
print('part 1: Sum is {}'.format(sum1))
print('part 2: Sum is {}'.format(sum2))