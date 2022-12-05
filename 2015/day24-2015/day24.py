boxes = []            
with open('day24input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        boxes.append(int(line))
        
N_box = len(boxes)
print(N_box, 'boxes in file:')
print(boxes)

tot_W = sum(boxes)
print('Total_weight is', tot_W)

tot_W3 = tot_W // 3

N1 = 1

#while True:


groups1 = []


def gen_groups(N_box, n):
    def addbox(group, i_start, N_box, rest):
        if rest == 0:
            addon = group.copy()
            groups.append(addon)
            group.pop()
            return
        else:
            for i in range(i_start+1, N_box):
                group.append(i)
                addbox(group, i, N_box, rest-1)
            try:
                group.pop()
            except:
                return
    groups = []
    addbox([], -1, N_box, n)
    return groups
            
groups1 = gen_groups(N_box, 6)

QE_min = 100000000000
for group1 in groups1:
    weight = 0
    for i in range(len(group1)):
        weight = weight + boxes[group1[i]]
    #print('Weight is', weight, 'for group', group1)
    if weight == tot_W3:
            print('Good weight:', group1)
            twogroups = [i for i in range(N_box)]
            for i in range(len(group1)):
                k = twogroups.index(group1[i])
                del twogroups[k]
            restweights = [boxes[i] for i in twogroups]
            N_rest = len(restweights)
            good_group1 = False
            for k in range(1, N_rest // 2):
                groups2 = gen_groups(N_rest, k)
                for group2 in groups2:
                    weight = 0
                    for i in range(len(group2)):
                        weight = weight + restweights[group2[i]]
                    if  weight == tot_W3:
                        good_group1 = True
                        break
                if good_group1:
                    break
            if good_group1:
                QE = 1
                for k in range(len(group1)):
                    QE = QE*boxes[group1[k]]
                print('QE for good group', group1, 'is', QE)
                if QE < QE_min:
                    QE_min = QE
print('min QE is', QE_min)       
input()                 
                
                



