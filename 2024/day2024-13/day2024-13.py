import re

TEST = False
filename = 'test-2024-13.txt' if TEST else 'input-2024-13.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

machines = []

i = 0
while True:
    but_a = tuple([int(x) for x in re.findall(r'\d+', lines[i])])
    but_b = tuple([int(x) for x in re.findall(r'\d+', lines[i+1])])
    prize = tuple([int(x) for x in re.findall(r'\d+', lines[i+2])])
    machines.append((but_a, but_b, prize))
    if i+3 < len(lines):
        i += 4
    else:
        break

def solve(machine, limit=False):
    but_a, but_b, prize = machine
    a_dx, a_dy = but_a
    b_dx, b_dy = but_b
    prize_x, prize_y = prize
    n_b = (prize_y - prize_x*a_dy/a_dx) / (b_dy - b_dx*a_dy/a_dx)
    n_a = (prize_x - b_dx*n_b) / a_dx
    n_a = round(n_a)
    n_b = round(n_b)
    if (a_dx * n_a + b_dx * n_b == prize_x) and (a_dy * n_a + b_dy * n_b == prize_y):
        if limit:
            if n_a <= limit and n_b <= limit:
                return (n_a, n_b)
            return False
        return (n_a, n_b)
    return False


tokens = 0
for machine in machines:
    solution = solve(machine, limit=100)
    if solution:
        n_a, n_b = solution
        tokens += n_a * 3 + n_b * 1

print(tokens)


machines = []
ADD = 10000000000000
i = 0
while True:
    but_a = tuple([int(x) for x in re.findall(r'\d+', lines[i])])
    but_b = tuple([int(x) for x in re.findall(r'\d+', lines[i+1])])
    prize = tuple([int(x) + ADD for x in re.findall(r'\d+', lines[i+2])])
    machines.append((but_a, but_b, prize))
    if i+3 < len(lines):
        i += 4
    else:
        break

tokens = 0
for machine in machines:
    solution = solve(machine)
    if solution:
        n_a, n_b = solution
        tokens += n_a * 3 + n_b * 1

print(tokens)
