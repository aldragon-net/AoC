with open('input_day07.txt', 'r') as f:
    lines = f.readlines()


def splitter(s):
    outside_pos = True
    inside = []
    outside = []
    for char in s:
        if char == '[':
            outside_pos = False
            outside.append('####')
            continue
        if char == ']':
            outside_pos = True
            inside.append('####')
            continue
        if outside_pos:
            outside.append(char)
        else:
            inside.append(char)
    inside = ''.join(inside)
    outside = ''.join(outside)
    return inside, outside


def has_pair(s):
    for i in range(len(s)-3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    return False


def get_triplets(s):
    triplets = []
    for i in range(len(s)-2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            triplets.append(s[i:i+3])
    return triplets


count_1 = 0
count_2 = 0

for line in lines:
    inside, outside = splitter(line.strip())
    if has_pair(outside) and not has_pair(inside):
        count_1 += 1
    triplets_outside = get_triplets(outside)
    triplets_inside = get_triplets(inside)
    if triplets_inside and triplets_outside:
        supports = False
        for triplet_inside in triplets_inside:
            for triplet_outside in triplets_outside:
                if (triplet_inside[0] == triplet_outside[1] and
                        triplet_inside[1] == triplet_outside[0]):
                    count_2 += 1
                    supports = True
                    break
            if supports:
                break

print(count_1)
print(count_2)
