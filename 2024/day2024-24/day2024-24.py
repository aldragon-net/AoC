filename = 'input-2024-24.txt'
with open(filename, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

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


def operator(x1, x2, op):
    if op == 'AND':
        return x1 and x2
    if op == 'OR':
        return x1 or x2
    if op == 'XOR':
        return x1 != x2


def get_result():
    '''Эволюция системы и вывод результата из z00, ... , z45'''
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


def find_gate_with_wires(x, y, type):
    '''Поиск вентиля с заданными входами'''
    for label, gate_info in gates.items():
        wire_1, wire_2, op = gate_info
        if x in [wire_1, wire_2] and y in [wire_1, wire_2] and op == type:
            return label
    return None  # не найдено соответствия по двум входам


def find_gate_with_wire(x, type):
    '''Поиск однозначно определенного вентиля с заданным входом'''
    labels = []
    for label, gate_info in gates.items():
        wire_1, wire_2, op = gate_info
        if x in [wire_1, wire_2] and op == type:
            labels.append(label)
    if len(labels) == 1:
        return labels.pop()  # однозначное соответствие
    else:
        return None  # нет однозначного соответствия


def check_cascade():
    '''Проверка каскада суммирования от младшего к старшим разрядам'''
    wrongs = set()
    prev = 'nvv'  # передано из разряда 0 (особый случай)
    for i in range(1, 45):
        label_x = f'x{i}' if i >= 10 else f'x0{i}'
        label_y = f'y{i}' if i >= 10 else f'y0{i}'
        label_z = f'z{i}' if i >= 10 else f'z0{i}'
        # всегда существующие вентили входа
        input_XOR = find_gate_with_wires(label_x, label_y, 'XOR')
        input_AND = find_gate_with_wires(label_x, label_y, 'AND')
        # поиск кросс-вентиля
        cross_AND = find_gate_with_wires(input_XOR, prev, 'AND')
        if not cross_AND:
            cross_AND = find_gate_with_wire(input_XOR, 'AND')
            if cross_AND:
                wrongs.add(prev)
            if not cross_AND:
                cross_AND = find_gate_with_wire(prev, 'AND')
                wrongs.add(input_XOR)
        # поиск вентиля-переноса на следующий разряд
        next = find_gate_with_wires(input_AND, cross_AND, 'OR')
        if not next:
            next = find_gate_with_wire(input_AND, 'OR')
            if next:
                wrongs.add(cross_AND)
            if not next:
                next = find_gate_with_wire(cross_AND, 'OR')
                wrongs.add(input_AND)
        # поиск вентиля-выхода данного разряда
        output = find_gate_with_wires(input_XOR, prev, 'XOR')
        if not output:
            output = find_gate_with_wire(input_XOR, 'XOR')
            if output:
                wrongs.add(prev)
            if not output:
                output = find_gate_with_wire(prev, 'XOR')
                wrongs.add(input_XOR)
        # проверка, соответствует ли найденный выход разряду
        if output != label_z:
            wrongs.add(output)
            wrongs.add(label_z)
        # передача в следующий разряд
        prev = next

    # подготовка вывода
    wrongs = list(wrongs)
    wrongs.sort()
    return ','.join(wrongs)


print(get_result())
print(check_cascade())
