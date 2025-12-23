TEST = False
filename = 'test-2018-08.txt' if TEST else 'input-2018-08.txt'
with open(filename, 'r') as f:
    line = f.readline()

inpseq = [int(x) for x in line.strip().split(' ')]

metadata_sum = 0


def parse_node(i):
    nodes = inpseq[i]
    metadata_entries = inpseq[i+1]
    shift = 2
    node_values = []
    for n in range(nodes):
        node_length, node_metadata, value = parse_node(i+shift)
        node_values.append(value)
        shift += node_length
    metadata = []
    for n in range(metadata_entries):
        metadata.append(inpseq[i+shift])
        shift += 1
    if nodes == 0:
        value = sum(metadata)
    else:
        value = 0
        for n in metadata:
            if n <= nodes:
                value += node_values[n-1]
    global metadata_sum
    metadata_sum += sum(metadata)
    return shift, metadata, value


print('part_2:', parse_node(0)[2])
print('part_1:', metadata_sum)
