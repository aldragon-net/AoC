import numpy as np

TEST = False
filename = 'test-2025-12.txt' if TEST else 'input-2025-12.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

p_0 = np.array([[1, 1, 1],
                [0, 0, 1],
                [1, 1, 1]])
p_1 = np.array([[0, 1, 1],
                [1, 1, 0],
                [1, 0, 0]])
p_2 = np.array([[1, 1, 1],
                [0, 1, 1],
                [0, 1, 1]])
p_3 = np.array([[1, 0, 1],
                [1, 1, 1],
                [1, 0, 1]])
p_4 = np.array([[1, 0, 0],
                [1, 1, 0],
                [1, 1, 1]])
p_5 = np.array([[1, 1, 0],
                [1, 1, 1],
                [1, 1, 1]])

presents = [p_0, p_1, p_2, p_3, p_4, p_5]
weights = [int(p.sum()) for p in presents]

places = []
for line in lines[30:]:
    dimensions, presents = line.strip().split(':')
    dimensions = tuple([int(x) for x in dimensions.split('x')])
    presents = [int(x) for x in presents.strip().split(' ')]
    places.append((dimensions, presents))

fit = 0
for place in places:
    dimensions, n_presents = place
    surface = dimensions[0]*dimensions[1]
    total = 0
    for i in range(6):
        total += n_presents[i] * weights[i]
    if total < surface:
        fit += 1

print(fit)
