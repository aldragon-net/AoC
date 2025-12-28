TEST = False
filename = 'test-2016-12.txt' if TEST else 'input-2016-12.txt'
with open(filename, 'r') as f:
    lines = f.readlines()


def run_program(lines, registers):
    i = 0
    while i < len(lines):
        command = lines[i].strip().split()
        operator, operand_1 = command[0], command[1]
        if operator == 'inc':
            registers[operand_1] += 1
        if operator == 'dec':
            registers[operand_1] -= 1
        try:
            value = int(operand_1)
        except ValueError:
            value = registers[operand_1]
        if operator == 'cpy':
            operand_2 = command[2]
            registers[operand_2] = value
        if operator == 'jnz':
            if value != 0:
                operand_2 = command[2]
                i += int(operand_2)
                continue
        i += 1
    print(registers['a'])


registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
run_program(lines, registers)
registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
run_program(lines, registers)
