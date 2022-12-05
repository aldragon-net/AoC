

lines = []            
with open('day15input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline()
        if line == '':
            break
        line = line.split(':')[1].strip()
        lines.append(line)


ingrs = []

for i in range(len(lines)):
    cap, dur, fla, tex, cal = int(lines[i].split(',')[0].split()[1]),\
                              int(lines[i].split(',')[1].split()[1]),\
                              int(lines[i].split(',')[2].split()[1]),\
                              int(lines[i].split(',')[3].split()[1]),\
                              int(lines[i].split(',')[4].split()[1])
    ingrs.append([cap, dur, fla, tex, cal])

print(ingrs)

mixes = []
for i in range(0, 101):
    for j in range(0, 101-i):
        for k in range(0, 101-i-j):
             mixes.append([i, j, k, 100-i-j-k])
print(len(mixes),' recipes total')  

cal500mixes = []

for i in range(len(mixes)):
    cal = 0
    for j in range(len(ingrs)):
        cal = cal + mixes[i][j]*ingrs[j][4]
    if cal == 500:
        cal500mixes.append(mixes[i])

print(len(cal500mixes), 'recipes with 500 cal')

  
max_score = 0

for i in range(len(mixes)):
    cap, dur, fla, tex = 0, 0, 0, 0
    for j in range(len(ingrs)):
        cap = cap + mixes[i][j]*ingrs[j][0]
        dur = dur + mixes[i][j]*ingrs[j][1]
        fla = fla + mixes[i][j]*ingrs[j][2]
        tex = tex + mixes[i][j]*ingrs[j][3]
    if cap <= 0:
        cap = 0
    if dur <= 0:
        dur = 0
    if fla <= 0:
        fla = 0
    if tex <= 0:
        tex = 0
    score = cap*dur*fla*tex
    if score > max_score:
        max_score = score

print('Best score is', max_score)
        
mixes = cal500mixes
max_score = 0

for i in range(len(mixes)):
    cap, dur, fla, tex = 0, 0, 0, 0
    for j in range(len(ingrs)):
        cap = cap + mixes[i][j]*ingrs[j][0]
        dur = dur + mixes[i][j]*ingrs[j][1]
        fla = fla + mixes[i][j]*ingrs[j][2]
        tex = tex + mixes[i][j]*ingrs[j][3]
    if cap <= 0:
        cap = 0
    if dur <= 0:
        dur = 0
    if fla <= 0:
        fla = 0
    if tex <= 0:
        tex = 0
    score = cap*dur*fla*tex
    if score > max_score:
        max_score = score

print('Best score with 500 cal is', max_score)

print('Best score is', max_score)
input()



