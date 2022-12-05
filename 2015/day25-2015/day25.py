#"Enter the code at row 2978, column 3083"     
seed = 20151125
r_code = 2978
c_code = 3083

r = 1
c = 1
N = 1    
while not ((r == r_code) and (c == c_code)):
    N = N + 1
    if r == 1:
        r, c = c+1, 1
    else:
        r, c = r - 1, c + 1
        
print('at row', r_code, ', column', c_code, 'is code number', N)


code = seed 
for i in range(2, N+1):
    code = (code*252533) % 33554393
    if i % 100000 == 0:
        print(i, 'codes generated')
        
print(N, 'code is', code)
input()

