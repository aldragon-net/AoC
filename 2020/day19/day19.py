import re

part2 = False

rules = {}
msgs = []

with open('day19input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        key, rule = line.split(':', 1)
        rule = rule.strip().split('|')
        for i in range(len(rule)):
            rule[i] = [n for n in rule[i].strip().strip('\"').split()]
        rules[key] = rule
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        msgs.append(line)

def genreg(n):
    rule = rules[n]

    def onlyopt(ruleblock):
        if len(ruleblock) == 1:
            if ruleblock[0] in ["a", "b"]:
                return ruleblock[0]
            else:
                return genreg(ruleblock[0])
        elif len(rule[0]) == 2:
            return genreg(ruleblock[0]) + genreg(ruleblock[1])
        else:
            print('WTF?')

    if part2:
        if n == '8':
            return '('+genreg('42')+'){1,}'
        if n == '11':
            return '(' + genreg('42') + '){1}(' +genreg('31') + '){1}' #TODO

    if len(rule) == 1:
        return onlyopt(rule[0])
    elif len(rule) == 2:
        return '(' + onlyopt(rule[0]) + '|' + onlyopt(rule[1]) + ')'
    else:
        print('WTF?')

pattern = genreg('0')

matches = 0
for msg in msgs:
    if re.fullmatch(pattern, msg):
        matches +=1
print('There are {} matches'.format(matches))
