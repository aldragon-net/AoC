lines = []            
with open('day08input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)

sumlit = 0
summem = 0
sumcode = 0    
    
for line in lines:
    sumlit = sumlit + len(line)
    truncline = line[1:-1]
    
    i = 0
    j = 0
    k = 6
    while i < len(truncline):
        j = j + 1
        k = k + 1
        if truncline[i] == '\\':
            k = k + 1
            if truncline[i+1] == '\\' or truncline[i+1] == '"':
                k = k + 2
                i = i + 2
                continue
        if truncline[i] == '\\' and truncline[i+1] == 'x' \
           and truncline[i+2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'] \
           and truncline[i+3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
            k = k + 3
            i = i+4
            continue
        i = i + 1
    summem = summem + j
    sumcode = sumcode + k
    print (line, truncline, len(line), j, k)
diff1 = sumlit - summem
diff2 = sumcode - sumlit
print('differences is', diff1, diff2)
input()

