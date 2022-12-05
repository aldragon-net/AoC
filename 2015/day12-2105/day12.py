digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open('day12input.txt', 'r') as inpfile:
    line = inpfile.readline().strip()

def count_object(line):
    N = len(line)
    sum = 0
    i = 1
    while i<len(line):
        number = []
        if line[i] == '{':
            k = 0
            counter = 1
            while counter > 0:
                k = k + 1
                if line [i+k] == '{':
                    counter = counter + 1
                if line [i+k] == '}':
                    counter = counter - 1
            sum = sum + count_object(line[i+1:i+k])
            i = i + k
        
        if i<len(line)-5 and line[i:i+5] == ':"red':
            print ('Ignored', line)
            return 0
        
        if line[i] in digits:
            if line[i-1] == '-':
                number.append(line[i-1])
            number.append(line[i])
            j = 1
            while i+j<N and (line[i+j] in digits):
                number.append(line[i+j])
                j = j + 1
            i = i + j
            num = ''.join(number)
            print(num)
            sum = sum + int(num)
        i = i + 1   
    return sum    

sum = count_object(line)

print('Sum of numbers is:', sum)    
input()            
