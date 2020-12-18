with open('day18input.txt', 'r') as inpfile:
    lines = [line.strip() for line in inpfile.readlines()]


def eval(line):
    def binsplitter(line):
        if line.find(' ') == -1:
            return line, None, None
        if line[0] == '(':
            i = 0
            parcount = 1
            while True:
                i += 1
                if line[i] == '(':
                    parcount += 1
                elif line[i] == ')':
                    parcount -= 1
                if parcount == 0:
                    break
            car = line[1:i]
            if i == len(line)-1:
                op = None
                cdr = None
            else:
                op, cdr = line[i+1:].strip().split(' ', 1)
        else:
            car, op, cdr = line.split(' ', 2)
        return car, op, cdr

    def splitter(line):
        vals = []
        ops = ['+']
        cdr = line
        while True:
            car, op, cdr = binsplitter(cdr)
            vals.append(car)
            if op is None:
                break
            else:
                ops.append(op)
        return vals, ops

    if line.find(' ') == -1:
        value1 = value2 = int(line)
    else:
        vals, ops = splitter(line)
        # part 1
        value1 = 0
        for i in range((len(ops))):
            if ops[i] == '+':
                value1 += eval(vals[i])[1]
            else:
                value1 = value1 * eval(vals[i])[1]
        # part 2
        value2 = 0
        while True:
            i = len(ops)-1
            while True:
                if ops[i] == '+':
                    break
                i -= 1
            if i == 0:
                break
            else:
                vals[i-1] = str(eval(vals[i-1])[2]+eval(vals[i])[2])
                vals.pop(i)
                ops.pop(i)
        for i in range((len(ops))):
            if ops[i] == '+':
                value2 += eval(vals[i])[2]
            else:
                value2 = value2 * eval(vals[i])[2]
    return None, value1, value2


linesum1 = 0
linesum2 = 0
for line in lines:
    value = eval(line)
    linesum1 += value[1]
    linesum2 += value[2]

print('part 1: {}\npart 2: {}'.format(linesum1, linesum2))
