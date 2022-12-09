with open('input_day05-2018.txt', 'r') as f:
    input_polymer =  f.readline().strip()

polymer = list(input_polymer)


def make_pass(polymer, exclude=''):
    next = []
    reduced = False
    for char in polymer:
        if char.lower() == exclude.lower():
            continue
        if next and next[-1] != char and next[-1].upper() == char.upper():
            next.pop()
            reduced = True
        else:
            next.append(char)
    return reduced, next

while True:
    reduced, polymer = make_pass(polymer)
    if not reduced:
        break

print(len(polymer))

min_length = len(input_polymer)
for exclude in 'abcdefghijklmnopqrstuvwxyz':
    polymer = list(input_polymer)
    while True:
        reduced, polymer = make_pass(polymer, exclude)
        if not reduced:
            break
    if len(polymer) < min_length:
        min_length = len(polymer)

print(min_length)

    