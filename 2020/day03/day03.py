with open('day03input.txt') as inpfile:
    terrain = inpfile.readlines()
    for i in range(len(terrain)):
        terrain[i] = terrain[i].strip()
    inpfile.close()

height = len(terrain)
width = len(terrain[0])


def count_trees(slope_h, slope_v):
    pos_x = 0
    pos_y = 0
    tree_count = 0
    while True:
        if pos_y >= height:
            break
        if terrain[pos_y][pos_x] == '#':
            tree_count += 1
        pos_x += slope_h
        pos_x = pos_x % width
        pos_y += slope_v
    return tree_count


# part 1
n1 = count_trees(3, 1)
print("There were {} trees!".format(n1))

# part 2
n = count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) \
    * count_trees(7, 1) * count_trees(1, 2)
print("Answer is ", n)
