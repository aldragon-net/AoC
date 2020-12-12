class Ferry:
    def __init__(self, x, y, nose):
        self.x = x
        self.y = y
        self.nose = nose
        self.wpx = 0
        self.wpy = 0

    def setwp(self, x, y):
        self.wpx = x
        self.wpy = y

    def move(self, command):
        direction = command[0]
        shift = int(command[1:])
        if direction == 'N':
            self.y += shift
        elif direction == 'S':
            self.y -= shift
        elif direction == 'W':
            self.x -= shift
        elif direction == 'E':
            self.x += shift
        elif direction == 'F':
            vcomm = self.nose + command[1:]
            self.move(vcomm)

    def movewp(self, command):
        direction = command[0]
        shift = int(command[1:])
        if direction == 'N':
            self.wpy += shift
        elif direction == 'S':
            self.wpy -= shift
        elif direction == 'W':
            self.wpx -= shift
        elif direction == 'E':
            self.wpx += shift

    def move2wp(self, command):
        shift = int(command[1:])
        self.x += self.wpx * shift
        self.y += self.wpy * shift

    def rotate(self, command):
        rose = {'N': 0, 'E': 90, 'S': 180, 'W':270,
                0: 'N', 90: 'E', 180: 'S', 270: 'W'}
        az = rose[self.nose]
        dangle = int(command[1:])
        if command[0] == 'R':
            dsign = 1
        else:
            dsign = -1
        az += dsign * dangle
        az = (az % 360)
        self.nose = rose[az]

    def rotatewp(self, command):
        nrot = int(command[1:]) // 90
        for i in range(nrot):
            if command[0] == 'R':
                self.wpx, self.wpy = self.wpy, -self.wpx
            else:
                self.wpx, self.wpy = -self.wpy, self.wpx

    def step1(self, command):
        if command[0] in ['L', 'R']:
            self.rotate(command)
        elif command[0] in ['N', 'S', 'W', 'E', 'F']:
            self.move(command)
        else:
            print('Wrong command ', command)

    def step2(self, command):
        if command[0] in ['L', 'R']:
            self.rotatewp(command)
        elif command[0] in ['N', 'S', 'W', 'E']:
            self.movewp(command)
        elif command[0] == 'F':
            self.move2wp(command)
        else:
            print('Wrong command ', command)

with open('day12input.txt', 'r') as inpfile:
    commands = [s.strip() for s in inpfile.readlines()]

# part 1
ferry = Ferry(0, 0, 'E')
for command in commands:
    ferry.step1(command)
print('part 1: Manhattan distance is {}'.format(abs(ferry.x)+abs(ferry.y)))

# part 2
ferry = Ferry(0, 0, 'E')
ferry.setwp(10, 1)
for command in commands:
    ferry.step2(command)
print('part 2: Manhattan distance is {}'.format(abs(ferry.x)+abs(ferry.y)))
