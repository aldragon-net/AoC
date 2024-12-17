TEST = False
filename = 'test-2024-17.txt' if TEST else 'input-2024-17.txt'

with open(filename, 'r') as f:
    init_A = int(f.readline().strip().split(':')[1])
    init_B = int(f.readline().strip().split(':')[1])
    init_C = int(f.readline().strip().split(':')[1])
    _ = f.readline()
    program = [int(x) for x in f.readline().strip().split(':')[1].split(',')]
    position = 0

output = []

def to_output(value):
    output.append(value)

def literal(operand):
    return operand

def combo(operand):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return reg_A
    if operand == 5:
        return reg_B
    if operand == 6:
        return reg_C
    
def operator(opcode, operand):
    global reg_A
    global reg_B
    global reg_C
    global position
    if opcode == 0:  # adv
        reg_A = reg_A // (2 ** combo(operand))
    if opcode == 1:  # bxl
        reg_B = reg_B ^ literal(operand)
    if opcode == 2:  # bst
        reg_B = combo(operand) % 8
    if opcode == 3:  # jnz
        if reg_A != 0:
            position = literal(operand)
            return
    if opcode == 4:  # bxc
        reg_B = reg_B ^ reg_C
    if opcode == 5:  # out
        to_output(combo(operand) % 8)
    if opcode == 6:  # cdv
        reg_B = reg_A // (2 ** combo(operand))
    if opcode == 7:  # cdv
        reg_C = reg_A // (2 ** combo(operand))
    position += 2    

# while True:
#     if position > len(program) - 1:
#         break
#     opcode = program[position]
#     operand = program[position+1]
#     operator(opcode, operand)

# print(f'A = {reg_A} | B = {reg_B} | C = {reg_C}')
# print(','.join([str(x) for x in output]))

def compare(output, program):
    return ''.join([str(x) for x in output]) == ''.join([str(x) for x in program])

init_A = 0
while True:
    position = 0
    reg_A, reg_B, reg_C = init_A, init_B, init_C
    output = []
    while True:
        if position > len(program) - 1:
            break
        opcode = program[position]
        operand = program[position+1]
        operator(opcode, operand)
        if output:
            if output[0] != program[0]:
                break
    if compare(output, program) == True:
        break
    init_A += 1

print(f'repoduced at init_A = {init_A}')

# reverse:
   reg_b = output
   reg_b = reg_b ^ 7

   reg_b = reg_b ^ reg_c

   reg_a = reg_c * 32 + reg_b