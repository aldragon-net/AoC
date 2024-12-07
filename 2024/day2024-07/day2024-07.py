TEST = False
filename = 'test-2024-07.txt' if TEST else 'input-2024-07.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

equations = []
for line in lines:
    result, numbers = [[int(x) for x in s.split()] for s in line.strip().split(':')]
    equations.append((result[0], numbers))


def solvable_p1(equation):
    if not equation:
        return False
    result, numbers = equation
    if len(numbers) == 1:
        return result == numbers[0]
    last = numbers[-1]
    rest = numbers[:-1]
    if last > result:
        return False
    subtracted = (result - last, rest)
    divided = (result // last, rest) if result % last == 0 else False
    return solvable_p1(subtracted) or solvable_p1(divided)


def solvable_p2(equation):
    if not equation:
        return False
    result, numbers = equation
    if len(numbers) == 1:
        return result == numbers[0]
    last = numbers[-1]
    rest = numbers[:-1]
    if last > result:
        return False
    subtracted = (result - last, rest)
    divided = (result // last, rest) if result % last == 0 else False
    if len(str(result)) > len(str(last)) and str(result)[-len(str(last)):] == str(last):
        concatenated = (int(str(result)[:-len(str(last))]), rest)
    else:
        concatenated = False
    return solvable_p2(subtracted) or solvable_p2(divided) or solvable_p2(concatenated)


eqsum_1 = 0
for equation in equations:
    if solvable_p1(equation):
        eqsum_1 += equation[0]
print('part 1:', eqsum_1)

eqsum_2 = 0
for equation in equations:
    if solvable_p2(equation):
        eqsum_2 += equation[0]
print('part 2:', eqsum_2)
