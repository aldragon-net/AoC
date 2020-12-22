foods = []
all_ings = set()
all_allergens = set()

with open('day21input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line.strip() == '':
            break
        ings = line.split('(contains')[0].split()
        for ing in ings:
            all_ings.add(ing)
        allergens = line.split('(contains')[1].strip().strip(')').split(', ')
        for allergen in allergens:
            all_allergens.add(allergen)
        foods.append((ings, allergens))

all_allergens = list(all_allergens)
all_allergens.sort()

print(len(all_allergens), 'allergens:',  all_allergens)
print(len(all_ings),'ingredients in', len(foods), 'foods')

clean_ings = []
aller_ings = []
for ing in all_ings:
    can_contain = [True for allergen in all_allergens]
    for food in foods:
        receipt, aller_list = food
        if ing not in receipt:
            for i in range(len(all_allergens)):
                if all_allergens[i] in aller_list:
                    can_contain[i] = False
    if sum(can_contain) == 0:
        clean_ings.append(ing)
    else:
        aller_ings.append((ing, can_contain))

# part 1
counter = 0
for ing in clean_ings:
    for food in foods:
        receipt, _ = food
        if ing in receipt:
            counter += 1
print('part 1: safe ingredients appear', counter, 'times')

# part 2
answer = ['n/a' for allergen in all_allergens]
while True:
    for i in range(len(aller_ings)):
        name, can_contain = aller_ings[i]
        if sum(can_contain) == 1:
            k = can_contain.index(True)
            answer[k] = name
            for j in range(len(aller_ings)):
                if not i == j:
                    aller_ings[j][1][k] = False
    try:
        answer.index('n/a')
    except:
        break

print('part 2 answer is:')
for i in range(len(answer)):
    if i>0:
        print(',', end ='')
    print(answer[i], end='')
