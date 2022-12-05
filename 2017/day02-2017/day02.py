lines = []
with open('day02input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)

checksum = 0
ressum = 0
for line in lines:
    numbers = [int(num) for num in line.split()]
    numbers.sort()
    checkadd = numbers[-1] - numbers[0]
    checksum += checkadd
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (not i == j) and (numbers[j] % numbers[i] == 0):
                ressum += numbers[j] // numbers[i]              
print('Checksum is:', checksum)
print('Results sum is:', ressum)
input()
