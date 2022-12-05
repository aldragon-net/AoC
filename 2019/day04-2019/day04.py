# range: 240920-789857

def is_pass(number):
    is_pass = False
    digits = [int(char) for char in str(number)]
    is_pair = False
    for i in range(5):
        if digits[i+1] == digits[i]:
            if (i == 0 and not digits[i+2] == digits[i]) or\
               (i == 4 and not digits[i-1] == digits[i]) or\
               ((i > 0 and i < 4) and not
                    (digits[i-1] == digits[i] or digits[i+2] == digits[i])):
                is_pair = True
                break
    increasing = True
    for i in range(5):
        if digits[i+1] < digits[i]:
            increasing = False
            break
    if is_pair and increasing:
        is_pass = True
    return is_pass


pass_counter = 0
for number in range(240920, 789857+1):
    if is_pass(number):
        pass_counter = pass_counter + 1

print('There are', pass_counter, 'passwords')
input()
