seed = '3113322113'

def nextstring(seed):
    nextstring = [] 
    i = 0
    while i<len(seed):
        j = 1
        while True:
            if i+j>=len(seed):
                break
            if seed[i+j] == seed[i]:
                j = j+1
            else:
                break
        nextstring.append(str(j)+seed[i])
        i = i+j
    nextstring = ''.join(nextstring)
    return nextstring
    
for i in range(51):
    seed = nextstring(seed)
    #print('String is', seed, 'on', i, 'iteration')
    print('Length of string is', len(seed), 'on', i, 'iteration')
    input()

input()


