
with open('day02input.txt', 'r') as inpfile:
    line = inpfile.readline().strip()    

sourcecode = [int(char) for char in line.split(',')]

def runcode(code):
    i = 0
    while True:
        if code[i] == 1:
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
        elif code[i] == 2:
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
        elif code[i] == 99:
            #print('99 code: Program halt')
            break
        else:
            print('Error! Unknown code')
            input()
            break
        i = i + 4
        if i > len(code)-1:
            print('Error! Out of code')
            input()
            break
    return code[0]

code = sourcecode.copy()
#input
code[1] = 12
code[2] = 2  
print('Value at [0] after run:', runcode(code))
input('Press any key to continue')

#restoring


for noun in range(100):
    for verb in range(100):
        code = sourcecode.copy()
        code[1] = noun
        code[2] = verb
        result = runcode(code)
        if result == 19690720:
            print('noun and verb found:', noun, verb)
            print('answer is', 100 * noun + verb)
            break
print('Press any key to quit')
input()
