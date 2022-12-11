with open('input_day10-2022.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

x = 1
cycle = 1
summ = 0
screen = [' '] * 240


def draw_screen(x, step):
    if abs((step-1) % 40 - x) <= 1:
        screen[step-1] = '#'


def check(summ, x, step):
    draw_screen(x, step)
    if (step+20) % 40 == 0:
        summ += x * step
    step += 1
    return summ, step


for line in lines:
    summ, cycle = check(summ, x, cycle)
    if line.split()[0] == 'addx':
        summ, cycle = check(summ, x, cycle)
        x += int(line.split()[1])


print(summ)
for i, char in enumerate(screen):
    if i % 40 == 0:
        print()
    print(char, end='')
