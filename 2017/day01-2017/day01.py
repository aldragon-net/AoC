with open('day01input.txt', 'r') as inpfile:
    line = inpfile.readline().strip()

digits = [int(char) for char in line]

N = len(digits)
halfN = N //2

sum1 = 0
sum2 = 0

for i in range(N-1):
    if digits[i] == digits[i+1]:
        sum1 = sum1 + digits[i]
if digits[-1] == digits[0]:
        sum1 = sum1 + digits[-1]      
print('Sum 1 is', sum1)


for i in range(halfN):
    if digits[i] == digits[i+halfN]:
        sum2 = sum2 + 2*digits[i]
print('Sum 2 is', sum2)       
