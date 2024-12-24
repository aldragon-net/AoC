TEST = False
filename = 'test-2024-24.txt' if TEST else 'input-2024-24.txt'
with open(filename, 'r') as f:
    lines = [line.strip() for line in f.readlines()]


def operator(x1, x2, op):
    if op == 'AND':
        return (x1 and x2)
    if op == 'OR':
        return (x1 or x2)
    if op == 'XOR':
        return (x1 != x2)

initial_info = []
gates_info = []
for line in lines:
    if ':' in line:
        initial_info.append(line)
    if '->' in line:
        gates_info.append(line)


wires = {}
for line in initial_info:
    wire, value = line.split(': ')[0], bool(int(line.split(':')[1]))
    wires[wire] = value

gates = {}
for line in gates_info:
    info = line.split()
    wire_1, op, wire_2, out = info[0], info[1], info[2], info[4]
    gates[out] = (wire_1, wire_2, op)


def get_result(wires):
    evolving = True
    while evolving:
        evolving = False
        for gate, gate_info in gates.items():
            wire_1, wire_2, op = gate_info
            if gate not in wires:
                if (wire_1 in wires) and (wire_2 in wires):
                    evolving = True
                    result = operator(wires[wire_1], wires[wire_2], op)
                    wires[gate] = result

    output = 0
    for wire, value in wires.items():
        if wire[0] == 'z':
            num = int(wire[1:])
            if value:
                output += 2 ** num

    return output

print(get_result(wires))


def set_initial(x, y):
    wires = {}
    x = bin(x)[2:].zfill(45)
    y = bin(y)[2:].zfill(45)
    for i in range(45):
        label_x = f'x{i}' if i >= 10 else f'x0{i}'
        label_y = f'y{i}' if i >= 10 else f'y0{i}'
        wires[label_x] = bool(int(x[-(i+1)]))
        wires[label_y] = bool(int(y[-(i+1)]))
    return wires

for x in range(16):
    for y in range(16):
        wires = set_initial(x, y)
        result = get_result(wires)
        if x + y != result:
            print('АГА!', x, y, result)
