with open('input_day03.txt', 'r') as f:
    lines = f.readlines()


def get_priority(char):
    if ord('a') <= ord(char) <= ord('z'):
        return ord(char) - ord('a') + 1
    elif ord('A') <= ord(char) <= ord('Z'):
        return ord(char) - ord('A') + 27


sump = 0

for line in lines:
    line = line.strip()
    length = len(line)
    first = line[:(length // 2)]
    second = line[(length // 2):]
    for char in first:
        if char in second:
            sump += get_priority(char)
            break

print(sump)

sump = 0

for i in range(0, len(lines), 3):
    first = set(list(lines[i].strip()))
    second = set(list(lines[i+1].strip()))
    third = set(list(lines[i+2].strip()))
    for char in third:
        if char in first and char in second:
            sump += get_priority(char)
            break

print(sump)
