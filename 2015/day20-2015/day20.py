import math as m

NN = 34000000

n = 0
while True:
    n = n+1
    N = 0
    for i in range (1, round(m.sqrt(n))+1):
        if n % i == 0:
            if (n // i) <= 50:
                N = N + i*11
            if not (n // i) == i and (i<=50):
                N = N + (n // i)*11
    if n % 10000 == 0:
        print(N, 'presents for house number', n)
    if N > NN:
        print(N, 'presents for house number', n)
        input()    

        
    
        

   
    
