with open('day14input.txt', 'r') as inpfile:
    code = [line.strip() for line in inpfile.readlines()]

def setmask(mask):
    mask1 = []
    mask0 = []
    maskX = []
    for i in range(0, 36):
        if mask[-i-1] == '0':
            mask0.append(i)
        elif mask[-i-1] == '1':
            mask1.append(i)
        elif mask[-i-1] == 'X':
            maskX.append(i)
    return mask0, mask1, maskX

def appmask1(value, mask0, mask1):
    for bit in mask0:
        if (value >> bit) % 2 == 1:
            value = value - (1 << bit)
    for bit in mask1:
        if (value >> bit) % 2 == 0:
            value = value + (1 << bit)
    return value

def appmask2(value, mask0, mask1, maskX):
    value = appmask1(value, mask0, mask1)
    values = [value]
    for bit in maskX:
        newvalues = []
        for value in values:
            if (value >> bit) % 2 == 0:
                newvalues.extend([value, value + (1<<bit)])
            else:
                newvalues.extend([value, value - (1<<bit)])
        values = newvalues
    return values

# part 1
memory = {}
for line in code:
    if line[:4] == 'mask':
        mask0, mask1, _ = setmask(line[-36:])
    elif line[:3] == 'mem':
        reg = int(line.rsplit('[', 1)[1].split(']')[0])
        value = int(line.split('=')[1].strip())
        value = appmask1(value, mask0, mask1)
        memory[reg] = value

memsum = 0
for reg in memory.keys():
    memsum += memory[reg]

print('part 1: memory sum is:', memsum)

# part 2
memory = {}
for line in code:
    if line[:4] == 'mask':
        mask0, mask1, maskX = setmask(line[-36:])
    elif line[:3] == 'mem':
        reg = int(line.rsplit('[', 1)[1].split(']')[0])
        value = int(line.split('=')[1].strip())
        regs = appmask2(reg, [], mask1, maskX)
        for reg in regs:
            memory[reg] = value

memsum = 0
for reg in memory.keys():
    memsum += memory[reg]

print('part 2: memory sum is:', memsum)
