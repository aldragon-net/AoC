def get_calibration_value(line):
    digits = []
    for symbol in line:
        if symbol.isdigit():
            digits.append(symbol)
    return int(digits[0] + digits[-1])


def get_calibration_value2(line):
    line = line.replace('one', 'one1one') \
               .replace('two', 'two2two') \
               .replace('three', 'three3three') \
               .replace('four', 'four4four') \
               .replace('five', 'five5five') \
               .replace('six', 'six6six') \
               .replace('seven', 'seven7seven') \
               .replace('eight', 'eight8eight') \
               .replace('nine', 'nine9nine')
    return get_calibration_value(line)


with open('input-2023-01.txt', 'r') as f:
    lines = f.readlines()

calibration_value_sum = 0
for line in lines:
    calibration_value_sum += get_calibration_value(line)
print(calibration_value_sum)

calibration_value_sum = 0
for line in lines:
    calibration_value_sum += get_calibration_value2(line)
print(calibration_value_sum)
