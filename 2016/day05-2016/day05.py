import hashlib

my_key = 'ugkcyxxp'

i = 1
passsym = 0
passsymbols = []
while not passsym == 8:
    m = hashlib.md5()
    m.update(b'ugkcyxxp')
    m.update(str(i).encode())
    hexstring = m.hexdigest()
    if i % 1000000 == 0:
        print ('i =', i)
    if hexstring[0:5] == '00000':
        passsym = passsym + 1
        print('the answer is', i)
        print('hexstring is', hexstring)
        passsymbols.append(hexstring[5])
    i = i+1

password = ''.join(passsymbols)
print('password is:', password)
input()
