with open('day10input.txt') as inpfile:
    ratings = [int(x.strip()) for x in inpfile.readlines()]

ratings.sort()
ratings.insert(0, 0)
ratings.append(ratings[-1]+3)

# part 1

count1 = 0
count3 = 0

for i in range(1, len(ratings)):
    diff = ratings[i]-ratings[i-1]
    if diff == 1:
        count1 += 1
    elif diff == 3:
        count3 += 1

print('Multiplication of 1- and 3-jolts connections numbers is', count1*count3)

# part 2

isfixed = []
for i in range(len(ratings)):
    if i in [0, len(ratings)]:
        isfixed.append(True)
        continue
    if ratings[i]-ratings[i-1] == 1 and ratings[i+1]-ratings[i] == 1:
        isfixed.append(False)
    else:
        isfixed.append(True)

count_free = 0
free_groups = []
for i in range(1, len(isfixed)):
    if not isfixed[i]:
        count_free += 1
    else:
        if count_free > 0:
            free_groups.append(count_free)
        count_free = 0

n = 1
for k in free_groups:
    if k == 1:
        n = n*2
    elif k == 2:
        n = n*4
    elif k == 3:
        n = n*7
print('There are {} distinct ways of connection'.format(n))
