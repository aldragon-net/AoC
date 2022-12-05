lines = []
with open('day04input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)

phrases = [sorted(line.split()) for line in lines]
#addition for part 2
for i in range(len(phrases)):
    for j in range(len(phrases[i])):
        phrases[i][j]= ''.join(sorted(list(phrases[i][j])))
#end of addition for part 2
valid_counter = 0
for phrase in phrases:
    is_valid = True
    for i in range(1,len(phrase)):
        if phrase[i] == phrase[i-1]:
            is_valid = False
            break
    if is_valid:
        valid_counter += 1
print('There are', valid_counter, 'valid phrases')
input()
