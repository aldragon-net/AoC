TEST = False
filename = 'test-2025-08.txt' if TEST else 'input-2025-08.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

boxes = []
for line in lines:
    line = line.strip()
    x, y, z = [int(v) for v in line.split(',')]
    boxes.append((x, y, z))


def distance(box_1, box_2):
    x1, y1, z1 = box_1
    x2, y2, z2 = box_2
    return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2


lengths = []
for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        lengths.append((distance(boxes[i], boxes[j]), (i, j)))

lengths.sort(key=lambda x: x[0])

circuits = []
for i in range(len(boxes)):
    circuits.append({i})

i = 0
while True:
    length, boxes_pair = lengths[i]
    box_1, box_2 = boxes_pair
    for j in range(len(circuits)):
        if box_1 in circuits[j]:
            box_1_in = j
        if box_2 in circuits[j]:
            box_2_in = j
    if box_1_in != box_2_in:
        box_1_in, box_2_in = sorted([box_1_in, box_2_in])
        circuit_2 = circuits.pop(box_2_in)
        circuit_1 = circuits.pop(box_1_in)
        new_circuit = circuit_1 | circuit_2
        circuits.append(new_circuit)
    print(len(circuits))
    if len(circuits) == 1:
        print('just added:', boxes[box_1], boxes[box_2])
        print('part 2 answer:', boxes[box_1][0]*boxes[box_2][0])
        break
    i += 1


# circuits.sort(key = lambda x: len(x), reverse=True)


# print(len(circuits[0])*len(circuits[1])*len(circuits[2]))
