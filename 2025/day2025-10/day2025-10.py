import numpy as np
import scipy as sp

TEST = False
filename = 'test-2025-10.txt' if TEST else 'input-2025-10.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

machines = []


# part 1
# def lights2bin(lights):
#     value = 0
#     for i in range(len(lights)):
#         j = len(lights) - i - 1
#         if lights[j] == '#':
#             value += 2**i
#     return value

# def buttons2bin(buttons, length):
#     byte_buttons = []
#     for button in buttons:
#         value = 0
#         positions = [int(x) for x in button[1:-1].split(',')]
#         for i in range(length):
#             j = length - i - 1
#             if j in positions:
#                 value += 2**i
#         byte_buttons.append(value)
#     return byte_buttons

# for line in lines:
#     config = line.strip().split(' ')
#     lights = lights2bin(config[0][1:-1])
#     buttons = buttons2bin(config[1:-1], len(config[0][1:-1]))
#     jolting = config[-1][1:-1]
#     machines.append((lights, buttons, jolting))

# total_presses = 0
# for machine in machines:
#     target = machine[0]
#     buttons = machine[1]
#     presses = 0
#     values = set()
#     values.add(0)
#     while target not in values:
#         prevs = list(values)
#         for button in buttons:
#             for prev in prevs:
#                 values.add(prev ^ button)
#         presses += 1
#     total_presses += presses

# print(total_presses)

# part 2
for line in lines:
    config = line.strip().split(' ')
    buttons = config[1:-1]
    arrbuttons = []
    jolting = np.array([int(x) for x in config[-1][1:-1].split(',')])
    for button in buttons:
        pos = [int(x) for x in button[1:-1].split(',')]
        arrbutton = np.array([int(x in pos) for x in range(len(jolting))])
        arrbuttons.append(arrbutton)
    jolting = np.array([int(x) for x in config[-1][1:-1].split(',')])
    machines.append((arrbuttons, jolting))


def min_press(machine):   
    buttons, jolting = machine
    buttons = np.array(buttons)
    result = sp.optimize.linprog([1]*len(buttons),
                                 A_eq=buttons.T,
                                 b_eq=jolting,
                                 bounds=(0, None),
                                 method="highs",
                                 integrality=1)
    return round(result.fun)


total = 0
for i, machine in enumerate(machines):
    value = min_press(machine)
    print(i, value)
    total += value


print('total:', total)
