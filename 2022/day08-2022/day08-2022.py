with open('input_day08-2022.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

trees = [[None] * len(lines[0]) for _ in range(len(lines))]
visible = [[False] * len(lines[0]) for _ in range(len(lines))]
visible_t = [[False] * len(lines[0]) for _ in range(len(lines))]
visible_b = [[False] * len(lines[0]) for _ in range(len(lines))]
visible_r = [[False] * len(lines[0]) for _ in range(len(lines))]
visible_l = [[False] * len(lines[0]) for _ in range(len(lines))]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        trees[i][j] = int(lines[i][j])


for i in range(len(trees)):
    visible_l[i][0] = True
    top_tree = trees[i][0]
    for j in range(1, len(trees[i])):
        if trees[i][j] > top_tree:
            visible_l[i][j] = True
        top_tree = max(top_tree, trees[i][j])

for i in range(len(trees)):
    visible_l[i][-1] = True
    top_tree = trees[i][-1]
    for j in range(len(trees[i])-2, -1, -1):
        if trees[i][j] > top_tree:
            visible_r[i][j] = True
        top_tree = max(top_tree, trees[i][j])

for j in range(len(trees[0])):
    visible_t[0][j] = True
    top_tree = trees[0][j]
    for i in range(1, len(lines)):
        if trees[i][j] > top_tree:
            visible_t[i][j] = True
        top_tree = max(top_tree, trees[i][j])

for j in range(len(trees[0])):
    visible_t[-1][j] = True
    top_tree = trees[-1][j]
    for i in range(len(trees)-2, -1, -1):
        if trees[i][j] > top_tree:
            visible_b[i][j] = True
        top_tree = max(top_tree, trees[i][j])

for i in range(len(trees)):
    for j in range(len(trees[i])):
        if any((visible_r[i][j], visible_l[i][j],
                visible_t[i][j], visible_b[i][j])):
            visible[i][j] = True
count = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if visible[i][j]:
            count += 1

print(count)


def get_score(x, y):
    score_l = 1
    while y-score_l > 0 and trees[x][y-score_l] < trees[x][y]:
        score_l += 1
    score_r = 1
    while y+score_r < (len(trees[x])-1) and trees[x][y+score_r] < trees[x][y]:
        score_r += 1
    score_t = 1
    while x-score_t > 0 and trees[x-score_t][y] < trees[x][y]:
        score_t += 1
    score_b = 1
    while x+score_b < (len(trees)-1) and trees[x+score_b][y] < trees[x][y]:
        score_b += 1
    return score_l * score_r * score_t * score_b


max_score = 0
for i in range(1, len(trees)-1):
    for j in range(1, len(trees[i])-1):
        max_score = max(max_score, get_score(i, j))

print(max_score)
