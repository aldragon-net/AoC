with open('day07input.txt') as inpfile:
    rules = inpfile.readlines()
    inpfile.close()

ruledict = {}

for rule in rules:
    key, cdr = rule.split('bags contain')[0].strip(), \
               rule.split('bags contain')[1].strip().strip('.')
    baglist = []
    for item in cdr.split(','):
        description = item.strip().split(' ')
        quantity = description[0]
        qualia = description[1] + ' ' + description[2]
        if quantity == 'no':
            baglist.append(None)
        else:
            quantity = int(quantity)
            baglist.append((qualia, quantity))
    ruledict[key] = baglist

# part 1
has_gold = ['shiny gold']
while True:
    edited = False
    for key in ruledict.keys():
        if key in has_gold:
            continue
        bags_in = ruledict[key]
        for bag in bags_in:
            if not bag:
                continue
            if bag[0] in has_gold:
                has_gold.append(key)
                edited = True
                break
    if not edited:
        break
print('There are {} colors of bags with shiny gold bag'.format(len(has_gold)-1))

# part 2
def bag_count(key):
    bags_in = ruledict[key]
    if bags_in[0] is None:
        return 0
    else:
        counter = 0
        for bag in bags_in:
            counter += bag[1] * (bag_count(bag[0]) + 1)
        return counter

n = bag_count('shiny gold')
print('There are {} bags inside shiny gold bag'.format(n))
