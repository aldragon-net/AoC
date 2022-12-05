seed = 'hepxxyzz'

abc = 'abcdefghijklmnopqrstuvwxyz'

triplets = []

for i in range(24):
    triplet = abc[i]+abc[i+1]+abc[i+2]
    triplets.append(triplet)
    
pairs = []

for i in range(26):
    pair = 2 * abc[i]
    pairs.append(pair)
    
stops = ['i', 'o', 'l']

print(triplets)
print(pairs)

def incstring(text):
    symbols = list(text)
    def nextpass(symbols, pos):
        n = abc.find(symbols[pos])
        if n < 25:
            symbols[pos] = abc[n+1]
        elif n == 25:
            symbols[pos] = 'a'
            if pos > 0:
                symbols = nextpass(symbols, pos-1)   
        return symbols
    symbols = nextpass(symbols, 7)
    symbols = ''.join(symbols)
    return symbols

def checktriplet(seed):
    is_triplet = False
    for i in range(24):
        k = seed.find(triplets[i])
        if not k == -1:
            is_triplet = True
            break
    return is_triplet

def checkpairs(seed):
    is_pairs = False
    for i in range(25):
        for j in range(26):
            k = seed.find(pairs[i])
            r = seed.rfind(pairs[j])
            if (not k == -1) and (not r == -1) and (abs(k-r)>1):
                is_pairs = True
                break
        if is_pairs:
            break
    return is_pairs

def checkstops(seed):
    is_stops = False
    for stop in stops:
        i = seed.find(stop)
        if not i == -1:
            is_stops = True
            break
    return is_stops
       

while True:
    seed = incstring(seed)
    is_stops = checkstops(seed)
    if not is_stops:
        is_triplet = checktriplet(seed)
        if is_triplet:
            print(seed, 'triplet')
            is_pairs = checkpairs(seed)
            if is_pairs:
                is_pass = True
        else:
            is_pass = False
    else:
        is_pass = False 
    if is_pass:    
        print('Password found!', seed)
        input()
