with open('day05input.txt', 'r') as inpfile:
    lines = []
    while True:
        line = inpfile.readline()
        if line == '':
            break
        lines.append(line.strip())

print('Number of lines:', len(lines))

count = 0
for line in lines:

    three_vowels = False
    vnum = 0
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        vcount = 0
        i = 0
        templine = line
        while not i == -1:          
            i = templine.find(vowel)
            if not i == -1:
                templine = templine[i+1:]
                vcount = vcount + 1     
        vnum = vnum + vcount
        if vnum >= 3:
            three_vowels = True
            break
    
    twice_in_row = False
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        for i in range(0, len(line)-1):
            if line[i] == line [i+1]:
                twice_in_row = True
                break   
    
    fwords = False
    for fword in ['ab', 'cd', 'pq', 'xy']:
        i = line.find(fword)
        if not i == -1:
            fwords = True
            break
    
    double_pair = False
    for letter1 in 'abcdefghijklmnopqrstuvwxyz':
        for letter2 in 'abcdefghijklmnopqrstuvwxyz':
            pair = letter1+letter2
            i1 = line.find(pair)
            i2 = line.rfind(pair)
            if not (i1 == -1 or i2 == -1):
                if abs(i1-i2)>1:
                    double_pair = True
                    break
        if double_pair:
            break
    
    twice_with_gap = False
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        for i in range(0, len(line)-2):
            if line[i] == line [i+2]:
                twice_with_gap = True
                break       
            
            
    # if (three_vowels and twice_in_row) and (not fwords):
        # count = count + 1
        
    if (twice_with_gap) and (double_pair):
        count = count + 1

print('Number of nice lines:', count)
