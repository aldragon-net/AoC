with open('day06input.txt', 'r') as inpfile:
    line = inpfile.readline().strip()
    banks = [int(i) for i in line.split()]

states = set()
states.add(tuple(banks))    

part2 = False
step = 0
start_banks = []
while True:
    step += 1
    N = max(banks)
    i = banks.index(N)
    banks[i] = 0
    for j in range(16):
        banks[j] += N // 16
    M = N % 16
    for j in range(M):
        i += 1
        if i>15:
            i = 0
        banks[i] +=1
    if part2 and banks == start_banks:
        print('Loop size is:', step - start_loop)
        input()
    if (not part2) and (tuple(banks) in states):
        print('Repetition happened at step', step)
        input()
        start_loop = step
        start_banks = banks.copy()
        part2 = True
    else:
        states.add(tuple(banks))
