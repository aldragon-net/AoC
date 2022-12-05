import hashlib

my_key = 'ugkcyxxp'

i = 1
passsym = 0
passsymbols = ['' for i in range(8)]
while not passsym == 8:
    m = hashlib.md5()
    m.update(b'ugkcyxxp')
    m.update(str(i).encode())
    hexstring = m.hexdigest()
    if i % 1000000 == 0:
        print ('i =', i)
    if hexstring[0:5] == '00000':
        print('the answer is', i)
        print('hexstring is', hexstring)
        if not hexstring[5] in ['0', '1', '2', '3', '4', '5', '6', '7']:
            print('Invalid, passed')
            pass
        else:
            if passsymbols[int(hexstring[5])] == '':
                passsym = passsym + 1
                passsymbols[int(hexstring[5])] = hexstring[6]
                print('found symbol', hexstring[6], 'in position', int(hexstring[5]))
            else:
                print('Repeated position', int(hexstring[5]), ', passed')
    i = i+1

password = ''.join(passsymbols)
print('password is:', password)
input()
