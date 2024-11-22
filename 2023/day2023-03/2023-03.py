with open('input-2023-03.txt', 'r') as f:
    raw_lines = f.readlines()

extended_lines = ['.' + line.strip() + '.' for line in raw_lines]

empty_line = '.' * len(extended_lines[0])

lines = [empty_line]
lines.extend(extended_lines)
lines.append(empty_line)

numbers = []
details = []
for i, line in enumerate(lines):
    digits = []
    for j, symbol in enumerate(line):
        if symbol != '.' and not symbol.isdigit():
            details.append(([i, j], symbol))
        if symbol.isdigit():
            digits.append(symbol)
        if not symbol.isdigit() and digits:
            numbers.append(((i, j-len(digits), j-1), int(''.join(digits))))
            digits = []

numbers_sum = 0

for number in numbers:
    value = number[1]
    x, y_min, y_max = number[0]
    for detail in details:
        x_det, y_det = detail[0]
        if x_det - 1 <= x <= x_det + 1 and (y_det >= y_min-1 and y_det <= y_max+1):
            numbers_sum += value
            break
print(numbers_sum)

gears = []
for detail in details:
    if detail[1] == '*':
        connected_numbers = []
        x_det, y_det = detail[0]
        for number in numbers:
            value = number[1]
            x, y_min, y_max = number[0]
            if x_det - 1 <= x <= x_det + 1 and (y_det >= y_min-1 and y_det <= y_max+1):
                connected_numbers.append(value)
        if len(connected_numbers) == 2:
            gears.append(connected_numbers[0]*connected_numbers[1])

print(sum(gears))


