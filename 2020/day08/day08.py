class AoCVM:

    def reset(self):
        self.pos = 0
        self.accumulator = 0
        self.counter = 0
        self.execlines = set()

    def __init__(self):
        self.reset()

    def fromtxt(self, filepath):
        self.code = []
        with open('day08input.txt') as inpfile:
            while True:
                line = inpfile.readline()
                if line.strip() == '':
                    break
                operation = line.strip().split()[0]
                argument = int(line.strip().split()[1])
                self.code.append([operation, argument])
            inpfile.close()
        self.maxpos = len(self.code)-1

    def step(self):
        op, arg = self.code[self.pos][0], self.code[self.pos][1]
        self.execlines.add(self.pos)
        if op == 'nop':
            self.pos += 1
        elif op == 'acc':
            self.accumulator += arg
            self.pos += 1
        elif op == 'jmp':
            self.pos += arg

    def loopcheck(self, report=False):
        if self.pos in self.execlines:
            if report:
                print('Loop start at line {}'.format(self.pos))
            return True
        else:
            return False

    def outcheck(self):
        return (self.pos < 0) or (self.pos > self.maxpos)

    def endofcode(self):
        return self.pos == self.maxpos


vm = AoCVM()
vm.fromtxt('day08input.txt')

# part 1
while True:
    if vm.loopcheck(report=True):
        print('Accumulator value before loop is {}'.format(vm.accumulator))
        break
    vm.step()
    if vm.outcheck():
        print('Out of code!')
        break

vm.reset()

# part 2
maybugs = []
for i in range(len(vm.code)):
    if vm.code[i][0] in ['nop', 'jmp']:
        maybugs.append(i)
for i in maybugs:
    # flip
    if vm.code[i][0] == 'nop':
        vm.code[i][0] = 'jmp'
    else:
        vm.code[i][0] = 'nop'
    # trying
    vm.reset()
    while True:
        if vm.loopcheck():
            break
        vm.step()
        if vm.outcheck():
            print('Out of code!')
            break
        if vm.endofcode():
            break
    if vm.endofcode():
        vm.step()
        print('Accumulator value at end of code is {}'.format(vm.accumulator))
        break
    # reverse flip
    if vm.code[i][0] == 'nop':
        vm.code[i][0] = 'jmp'
    else:
        vm.code[i][0] = 'nop'
