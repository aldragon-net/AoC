with open('input_day12.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    f.close()


def fill_caves(cave1, cave2):
    if cave1 not in caves.keys():
        caves[cave1] = [cave2]
    else:
        lst = caves[cave1]
        if cave2 not in lst:
            lst.append(cave2)
            caves[cave1] = lst


caves = {}
for line in lines:
    cave1, cave2 = line.split('-')
    fill_caves(cave1, cave2)
    fill_caves(cave2, cave1)


def paths_to_end_1(cave, vis_list):
    new_list = vis_list.copy()
    if cave.islower():
        new_list.append(cave)
    if cave == 'end':
        return 1
    else:
        sumpaths = 0
        for next in caves[cave]:
            if next not in vis_list:
                sumpaths += paths_to_end_1(next, new_list)
        return sumpaths


def paths_to_end_2(cave, vis_list, chosen):
    new_list = vis_list.copy()
    if cave.islower():
        new_list.append(cave)
    if cave == 'end':
        return 1
    else:
        sumpaths = 0
        for next in caves[cave]:
            if next not in vis_list:
                sumpaths += paths_to_end_2(next, new_list, chosen)
            else:
                if chosen == '' and next not in ['start', 'end']:
                    sumpaths += paths_to_end_2(next, new_list, next)
        return sumpaths


print(paths_to_end_1('start', []))
print(paths_to_end_2('start', [], ''))
