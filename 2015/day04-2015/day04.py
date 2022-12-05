import hashlib

my_key = 'iwrupvqb'

i = 1
while True:
    m = hashlib.md5()
    m.update(b'iwrupvqb')
    m.update(str(i).encode())
    hexstring = m.hexdigest()
    if i % 1000000 == 0:
        print('i =', i)
    if hexstring[0:6] == '000000':
        print('the answer is', i)
        print('hexstring is', hexstring)
        input()
        break
    i = i+1
