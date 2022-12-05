lines = []
with open('day07input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)

holded = set()
programs = {}
for line in lines:
    hld_by = []
    if not line.find('->') == -1:
        hld_by = [name.strip() for name in line.split('->')[1].split(',')]
        for hld in hld_by:
            holded.add(hld)
    name = line.split()[0].strip()
    weight = int(line[line.find('(')+1:line.find(')')])
    programs[name] = [weight, hld_by]
    
for name in programs.keys():
    if not name in holded:
        print('Bottom program is', name)
        bottom = name

def checkbalance(name):
    def tweight(name):
        weight = programs[name][0]
        subtowers = programs[name][1]
        for subtower in subtowers:
            weight += tweight(subtower)
        return weight
    subtowers = programs[name][1]
    upweights = []
    for subtower in subtowers:
        upweights.append(tweight(subtower))
    max_w = max(upweights)
    min_w = min(upweights)
    if not max_w == min_w:
        for i in range(len(upweights)):
            if upweights.count(upweights[i]) == 1:
                diff = max_w - min_w
                print(name, 'is unbalanced, subtower', subtowers[i], 'of', subtowers, 'out of weight:', upweights[i], 'among', upweights)
                isitup = not checkbalance(subtowers[i])
                if isitup == False:
                    print('Wrong program is', subtowers[i], 'weight is',  upweights[i], 'among', upweights)
                    print('selfweight of', subtowers[i], 'is', programs[subtowers[i]][0] )
                    input()
        return False
    else:
        print(name, 'is balanced')
        return True

checkbalance(bottom)            
